from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Conversation
from .forms import ConversationMessageForm
from hmk.accounts.models import Profile


@login_required
def new_conversation(request, user_pk):
    user_is_staff = request.user.is_staff
    user = get_object_or_404(User, pk=user_pk)


    conversations = Conversation.objects.filter(member2=request.user, member1=user).first()
    if not conversations:
        conversations = Conversation.objects.filter(member1=request.user, member2=user).first()

    if conversations:
        return redirect(f'/embracewellness/conversation/{user_pk}')

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(member1=request.user, member2=user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect(f'/embracewellness/conversation/{user_pk}')

    else:
        form= ConversationMessageForm()

    return render( request, 'conversation/new.html', {
        'form': form,
        'user_is_staff': user_is_staff
    })

@login_required
def inbox(request):
    user_is_staff = request.user.is_staff
    conversations1 = Conversation.objects.filter(member1 = request.user.id).all()
    conversations2 = Conversation.objects.filter(member2 = request.user.id).all()

    return render(request, 'conversation/inbox.html', {
        'conversations1': conversations1,
        'conversations2': conversations2,
        'user_is_staff': user_is_staff
    })

@login_required
def detail(request, user_pk):
    user_is_staff = request.user.is_staff
    user = get_object_or_404(User, pk=user_pk)
    profile = get_object_or_404(Profile, user=user)
    conversation = Conversation.objects.filter(member2=request.user, member1=user).first()
    if not conversation:
        conversation = Conversation.objects.filter(member1=request.user, member2=user).first()


    form = ConversationMessageForm()

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect(f'/embracewellness/conversation/{user_pk}')
    else:
        form = ConversationMessageForm( )

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
        'profile':profile,
        'user_is_staff': user_is_staff
    })

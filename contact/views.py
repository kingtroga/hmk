from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import AttendToForm
from django.contrib.auth.decorators import user_passes_test

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def index(request):
    user_is_staff = request.user.is_staff
    direct_messages = Contact.objects.filter(attended_to=False).all()


    for direct_message in direct_messages:
        direct_message.subject = direct_message.subject[0:50] + "..."

    return render(request, 'contact/contact_index.html', {
        'user_is_staff': user_is_staff,
        'direct_messages': direct_messages,
    })

@user_passes_test(is_staff)
def detail(request, pk):
    message = get_object_or_404(Contact, pk=pk)
    user_is_staff = request.user.is_staff

    if request.method == 'POST':
        form = AttendToForm(request.POST, instance=message)
        if form.is_valid():
            form.save(commit=True)
            return redirect('contact:index')
    else:
        form = AttendToForm(instance=message)

    return render(request, 'contact/detail.html', {
        'user_is_staff': user_is_staff,
        'message': message,
        'form': form
    })


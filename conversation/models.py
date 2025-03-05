from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    member1 = models.ForeignKey(User, related_name=f'member1_conversations', on_delete=models.DO_NOTHING)
    member2 = models.ForeignKey(User, related_name=f'member2_conversations', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-modified_at',)

    def __str__(self):
        return str(self.created_at)


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User

class Forum(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name="forums", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.TimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    forum = models.ForeignKey(Forum, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.TimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.comment


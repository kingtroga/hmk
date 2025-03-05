from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=300, default="Anonymous")
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=300, default="No subject")
    message = models.TextField(null=False, blank=False)
    attended_to = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    


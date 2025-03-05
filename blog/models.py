from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images")

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

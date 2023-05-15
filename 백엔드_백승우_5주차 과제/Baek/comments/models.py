from django.db import models

class Comment(models.Model):
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)

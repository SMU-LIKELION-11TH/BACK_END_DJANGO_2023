from django.db import models

class Recomment(models.Model):
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey("comments.Comment", on_delete=models.CASCADE, null=True)

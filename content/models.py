from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

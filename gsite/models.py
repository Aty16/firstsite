from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=10)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.email


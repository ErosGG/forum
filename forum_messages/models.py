from django.contrib.auth.models import User
from django.db import models


# class User(models.Model):
#     name = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     is_admin = models.BooleanField(default=False)


class Publication(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_at = models.DateTimeField()

    class Meta:
        abstract = True


class Message(Publication):
    title = models.CharField(max_length=50)
    pass

    def __str__(self):
        return f'id: {self.id} >>> title: {self.title}'


class Reply(Publication):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    pass

    def __str__(self):
        return f'id: {self.id} >>> content: {self.content}'

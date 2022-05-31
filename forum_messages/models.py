from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    id_admin = models.BooleanField(default=False)


class Publication(models.Model):
    content = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publicated_at = models.DateTimeField()

    class Meta:
        abstract = True


class Message(Publication):
    title = models.CharField(max_length=50)
    pass


class Reply(Publication):
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)
    pass
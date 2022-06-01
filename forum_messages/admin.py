from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.decorators import register

from forum_messages.models import Message, Reply


# class ForumMessagesAdmin(ModelAdmin):
#     pass


# admin.site.register(Message, ForumMessagesAdmin)
# admin.site.register(Reply, ForumMessagesAdmin)


@register(Message)
class MessageAdmin(ModelAdmin):
    pass


@register(Reply)
class ReplyAdmin(ModelAdmin):
    pass

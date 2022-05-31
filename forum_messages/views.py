from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from forum_messages.models import Message, Reply
import datetime


class MessageView(View):

    def get(self, request):
        Message.objects.create(title='test01', content='contingut de prova', published_at=datetime.datetime.now())
        context = {
            'messages': list(Message.objects.annotate(replies_count=Count('reply'))),
        }
        return render(request, 'messages.html', context=context)


class ReplyView(View):
    def get(self, request, message_id: int):
        Reply.objects.create(content='contingut de prova', published_at=datetime.datetime.now(), message_id=message_id)
        context = {
            'replies': list(Reply.objects.filter(message_id=message_id)),
        }
        print(context['replies'])
        return render(request, 'replies.html', context=context)

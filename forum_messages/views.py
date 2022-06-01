from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView

from forum_messages.models import Message, Reply
import datetime


class MessageView(View):

    def get(self, request):
        # Message.objects.create(title='test01', content='contingut de prova', published_at=datetime.datetime.now())
        context = {
            'username': 'Anonymous' if request.user.is_anonymous else request.user.username,
            'messages': list(Message.objects.annotate(replies_count=Count('reply'))),
        }
        return render(request, 'messages.html', context=context)


class CreateMessageView(View):

    def get(self, request):
        if request.user.is_anonymous:
            return redirect('/login/', request)
        else:
            return render(request, 'message_create.html')

    def post(self, request):
        Message.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            user_id=request.user.id,
            published_at=datetime.datetime.now()
        )
        return redirect('/messages/', request)


class DeleteMessageView(DeleteView):
    model = Message
    success_url = '/messages/'


class ReplyView(View):
    def get(self, request, message_id: int):
        # Reply.objects.create(content='contingut de prova', published_at=datetime.datetime.now(), message_id=message_id)
        context = {
            'username': 'Anonymous' if request.user.is_anonymous else request.user.username,
            'message': Message.objects.filter(id=message_id).first(),
            'replies': list(Reply.objects.filter(message_id=message_id)),
        }
        return render(request, 'replies.html', context=context)


class CreateReplyView(View):

    def get(self, request, message_id: int):
        if request.user.is_anonymous:
            return redirect('/login/', request)
        else:
            context = {
                'message': Message.objects.filter(id=message_id).first(),
            }
            return render(request, 'reply_create.html', context)

    def post(self, request, message_id: int):
        Reply.objects.create(
            content=request.POST['content'],
            user_id=request.user.id,
            message_id=message_id,
            published_at=datetime.datetime.now()
        )
        return redirect(f'/messages/{message_id}', request)


class DeleteReplyView(DeleteView):
    model = Reply
    success_url = f'/messages/{1}'

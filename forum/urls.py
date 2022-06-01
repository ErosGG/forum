"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forum_messages.views import MessageView, ReplyView, CreateMessageView, CreateReplyView
from users.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MessageView.as_view()),
    path('messages/', MessageView.as_view(), name='messages'),
    path('messages/<int:message_id>/', ReplyView.as_view(), name='replies'),
    path('messages/create/', CreateMessageView.as_view(), name='message.create'),
    path('messages/create/', CreateMessageView.as_view(), name='message.store'),
    path('messages/<int:message_id>/replies/create/', CreateReplyView.as_view(), name='reply.create'),
    path('messages/<int:message_id>/replies/create/', CreateReplyView.as_view(), name='reply.store'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

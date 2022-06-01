from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/messages/', request)
        else:
            return self.get(request)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/messages/', request)


class RegisterView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return render(request, 'register.html')
        else:
            return redirect('/messages/', request)

    def post(self, request):
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
        return redirect('/messages/', request)

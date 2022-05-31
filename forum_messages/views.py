from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class MessageView(View):

    def get(self, request):
        context = {
            'items': list(range(10)),
        }
        return render(request, 'index.html', context=context)

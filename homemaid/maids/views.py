from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import MaidForm
from .models import Maid


class MaidListView(View):
    template_name = 'maid_list.html'

    def get(self, request):
        context = {
            'maid_list': Maid.objects.all()
        }
        return render(request, self.template_name, context)


class MaidAddView(View):
    template_name = 'maid_add.html'

    def get(self, request):
        form = MaidForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = MaidForm(request.POST)
        if form.is_valid():
            form.save()
        
        # print(form.errors)

        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        return HttpResponse()


def maid_another_list_view(request):
    template_name = 'maid_list.html'
    
    if request.method == 'GET':
        context = {
            'maid_list': Maid.objects.all()
        }
        return render(request, template_name, context)


class MaidListAPIView(APIView):
    def get(self, request):
        return Response()
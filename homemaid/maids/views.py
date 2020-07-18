# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Maid


class MaidListView(View):
    def get(self, request):
        # Maid.objects.all()
        # m.name
        # for m in Maid.objects.all():
        # เราจะสามารถใช้ m.name ได้

        # my_list = [1, 2, 3, 4, 5]
        # for item in my_list:
        #     print(item)

        html = ''
        maids = Maid.objects.all()
        for maid in maids:
            html += f'<li>{maid.name}</li>'

        return HttpResponse(html)
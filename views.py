# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View


class ExampleAppThreeView(View):

    def get(self, request):
        return render(request, 'example_app_three/example_app_three.html', {"data": "Example App Three"})
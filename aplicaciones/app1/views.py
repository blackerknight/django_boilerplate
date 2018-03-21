# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
     context={'test':[]}
     return render(request,'app1/index.html',context)

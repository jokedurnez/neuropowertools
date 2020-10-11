from __future__ import unicode_literals
import sys
sys.path = sys.path[1:]
from django.shortcuts import render

### MAIN TEMPLATE PAGES ################################################

def home(request):
    return render(request,"main/home.html",{})
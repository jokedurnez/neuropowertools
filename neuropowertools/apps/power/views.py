from .utils import sessions
from django.shortcuts import render

def npFAQ(request):
    return render(request,"power/neuropowerFAQ.html",{})

def tutorial(request):
    return render(request,"power/tutorial.html",{})

def methods(request):
    return render(request,"power/methods.html",{})

def neuropowerstart(request):
    '''step 1: start'''

    # Get the template/step status
    sid = sessions.get_session_id(request)
    template = "power/neuropowerstart.html"
    # steps = get_neuropower_steps(template,sid)

    context = {"steps": 0}

    return render(request,template,context)

from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import HOD,Question
from django.utils import timezone
import base64
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def on_submit(request):
    choice=request.GET.get('choice')
    query=request.GET.get('query-textarea')
    mail=request.GET.get('mail_id')
    if(choice == 'cse'):
        branch =1
    elif(choice =='ce'):
        branch = 2
    elif(choice=='public'):
        branch = 3
    elif(choice=='eee'):
        branch = 4
    elif(choice=='ec'):
        branch = 5
    elif(choice=='eie'):
        branch = 6
    else:
        branch= 7  
    hod_object = HOD.objects.get(pk=branch)
    print("branch:{},query:{},time:{},mail{}".format(hod_object.name,query,timezone.now(),mail))
    q = Question(branch_id=hod_object,query=query,query_date=timezone.now(),mail_id=mail)
    q.save()
    return HttpResponseRedirect('/')

def hod_view(request,hod_id):
    query_hod=Question.objects.filter(branch_id=HOD.objects.get(branch_id=hod_id))
    print(query_hod)
    return render(request,'hod.html',{"queries":query_hod})

def login_success(request):
    b_id=HOD.objects.get(name=request.user).branch_id
    return HttpResponseRedirect('/hod/{}'.format(b_id))
def logout(request):
    return render(request,'registration/logout.html')
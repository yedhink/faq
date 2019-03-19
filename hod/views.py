from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import HOD,Question
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index.html')

def on_submit(request):
    choice=request.GET.get('choice')
    query=request.GET.get('query-textarea')
    if(choice == 'cse'):
        branch =1
    elif(choice == 'ce'):
        branch = 2
    else:
        branch = 0  
    hod_object = HOD.objects.get(pk=branch)
    print("branch:{},query:{},time:{}".format(hod_object.name,query,timezone.now()))
    q = Question(branch_id=hod_object,query=query,query_date=timezone.now())
    q.save()
    return HttpResponseRedirect('/')

def hod_view(request,hod_id):
    query_hod=Question.objects.filter(branch_id=HOD.objects.get(pk=hod_id))
    print(query_hod)
    return render(request,'hod.html',{"queries":query_hod})
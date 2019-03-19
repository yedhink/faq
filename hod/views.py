from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(content=template.render())

def on_submit(request):
    query_obj={"choice":"","query":""}
    query_obj["choice"]=request.GET.get('choice')
    query_obj["query"]=request.GET.get('query-textarea')
    print(query_obj)
    return HttpResponseRedirect('/')
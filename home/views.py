from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse   # our backend server will return a http respnse

def home(request):
    return render(request , "index.html")

#when some1 will call main route then our home func shoul be triggered


#another func for another route/ page 

def suceess_call(request):
    return HttpResponse("<h1> This is the result from the other pg</h1>")

# to return actual html templates from backend django server 


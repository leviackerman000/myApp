from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse   # our backend server will return a http respnse

def home(request):

    people_data = [
        {'name : leonardo' ,'age: 55'},
        {'name : Robert' ,'age: 45'},
        {'name : Qasim' ,'age: 20'},
        {'name : Ali' , 'age: 21'}
    #we can pass data from backend to HTML file through context
    ]
    for people in people_data:
        print(people)
    return render(request , "index.html" , context ={'people_data':people_data})

#when some1 will call main route then our home func shoul be triggered


#another func for another route/ page 

def suceess_call(request):
    return HttpResponse("<h1> This is the result from the other pg</h1>")

# to return actual html templates from backend django server 


from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

# def index(request):
#     response = "hello liseth"
#     return HttpResponse(response)

def index(request):
    context = {
    "name": "liseth"
    }
    return render(request, "teamUp/index.html", context)
def loginUser(request):
    response = "hello liseth"
    return HttpResponse(response)

def logOutUser(request):
    response = "hello liseth"
    return HttpResponse(response)

def registerUser(request):
    response = "hello liseth"
    return HttpResponse(response)

def projects(request):
    response = "hello liseth"
    return HttpResponse(response)

from django.shortcuts import render,redirect
from .models import CounterModel

# Create your views here.
def helloworld(request):
    name = "apurva"
    obj = CounterModel.objects.filter(id = 1)[0]
    ournumber = obj.number
    context = {'na' : name, 'num' : ournumber}                                       #creating dictionary to pass the variable
    return render(request, "helloworld/helloworld.html" , context)
# def hellostudent(request):
    return render(request, "helloworld/hellostudent.html")

def increment(request):
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = int(obj.number) + 1 
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def reset(request):
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])


def decrement(request):
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = int(obj.number) - 1 
    obj.save()
    return redirect(request.META['HTTP_REFERER'])
from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,'sample.html')

def button(request):
    return render(request,'button.html')

def bardges(request):
    return render(request,'bardges.html')
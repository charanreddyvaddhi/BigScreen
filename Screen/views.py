from django.shortcuts import render, HttpResponse


# Create your views here.
def page1(request):
    return render(request,'home_page.html')
def page2(request):
    return render(request,'world.html')
def page3(request):
    return render(request,'india.html')
def page4(request):
    return render(request,'media.html')
def page5(request):
    return render(request,'worldnews.html')
def page6(request):
    return render(request,'worldmovies.html')
def page7(request):
    return render(request,'worldbusiness.html')
def page8(request):
    return render(request,'indianews.html')
def page9(request):
    return render(request,'indiamovies.html')
def page10(request):
    return render(request,'indiabusiness.html')

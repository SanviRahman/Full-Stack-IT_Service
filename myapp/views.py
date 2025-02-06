from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm


# Create your views here.
def landing(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "index.html", {"form": form})

def contact(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    else:
        form = CustomUserCreationForm()
    return render(request, "contact.html", {"form": form})

def service(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service")
    else:
        form = CustomUserCreationForm()
    return render(request, "service.html", {"form": form})


def serviceDetails(request):
    if request.method =='POST':
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serviceDetails')
    else:
        form= CustomUserCreationForm()
    return render(request, "serviceDetails.html", {"form": form})

def about(request):
    if request.method == "POST":
        form=CustomUserCreationForm(request.data)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form=CustomUserCreationForm()
    return render(request, 'about.html',{'form':form})   



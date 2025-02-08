from django.shortcuts import render,redirect
from .forms import CustomModelForm
from .models import Services


# Create your views here.
# def landing(request):
#     if request.method == "POST":
#         form = CustomModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     else:
#         form =CustomModelForm()
#     return render(request, "index.html", {"form": form})

# def contact(request):
#     if request.method == "POST":
#         form = CustomModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("contact")
#     else:
#         form = CustomModelForm()
#     return render(request, "contact.html", {"form": form})


def service(request):
    if request.method == 'GET':
        form=Services.objects.all()
    return render(request,'service.html',{'form': form})

def serviceDetails(request,pk):
    if request.method == 'GET':
        form=Services.objects.get(pk=pk)
    return render(request,'serviceDetails.html',{'form': form})

 

    






def about(request):
    if request.method == "POST":
        form=(request.data)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form=CustomModelForm()
    return render(request, 'about.html',{'form':form})  





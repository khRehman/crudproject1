from django.shortcuts import render, HttpResponseRedirect
from .forms import StuentRegistration
from .models import User

# Create your views here.
# this function will add item and show all items 
def add_show(request):
    if request.method == 'POST':
        fm = StuentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StuentRegistration()
    else:
        fm = StuentRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})


# this function will update/edit data
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StuentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StuentRegistration(instance=pi)

    return render (request, 'enroll/updatestudent.html', {'form':fm})




# this function will delete the item
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



# this is a small project only for testing
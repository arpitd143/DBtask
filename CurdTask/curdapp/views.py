from django.shortcuts import render
from .forms import UploadForm
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employe
import pandas as pd
import os
from django.contrib import messages
# Create your views here.


def upload(request):
    # os.save("uploads/")
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.FILES)
        file = request.FILES["file"]
        # print(file)

        data = pd.read_csv(file)
        df = pd.DataFrame(data)
        df.dropna(inplace=True)
        print(df)

        for r in df.itertuples():
            employe = Employe()
            employe.name = r.Name
            employe.contact = r.Contact
            employe.leave = r.Leave
            employe.salary = r.Salary
            employe.designation = r.Designation
            employe.department = r.Department
            employe.save()
        messages.success(request, 'Data Uploaded Successfully')
        return HttpResponseRedirect(request.path_info)
    return render(request, 'index.html',{'form': form})


def showdata(request):
    data = Employe.objects.all()
    return render(request,'table.html', {"data":data})

@csrf_exempt
def update_data(request):
    id = request.POST.get('id')
    type = request.POST.get('type')
    value = request.POST.get('value')
    employe = Employe.objects.get(id=id)
    if type ==  "name":
        employe.name = value
    if type ==  "department":
        employe.department = value
    if type ==  "salary":
        employe.salary = value
    if type ==  "leave":
        employe.leave = value
    if type ==  "contact":
        employe.contact = value
    if type ==  "designation":
        employe.designation = value

    employe.save()

    return JsonResponse({"success":"updated"})


@csrf_exempt
def delete_data(request):
    id = request.POST.get('id')
    Employe.objects.filter(id=id).delete()
    return  JsonResponse({"success":"deleted"})

@csrf_exempt
def add_data(request):
    name = request.POST.get('name')
    department = request.POST.get('department')
    salary = request.POST.get('salary')
    designation = request.POST.get('designation')
    leave = request.POST.get('leave')
    contact = request.POST.get('contact')
    if name=='':
        msg="enter name"
    elif salary=='':
        msg="enter salary"

    elif leave=='':
        msg="enter leave"

    elif contact=='':
        msg="enter contact"

    elif department=='':
        msg="enter department"

    elif designation=='':
        msg="enter designation"
    else:
        employe = Employe(name=name,salary=salary,designation=designation,contact=contact,leave=leave,department=department)
        employe.save()
    return  JsonResponse({"success":msg})
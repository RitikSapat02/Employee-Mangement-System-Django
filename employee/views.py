from django.shortcuts import render,HttpResponse
from .models import Department,Role,Employee
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):

    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context ={
        'emps':emps
    }
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        bonus = int(request.POST['bonus'])

        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,joined_date=datetime.now(),role_id=role, dept_id=dept)

        new_emp.save()

    return render(request,'add_emp.html')


def remove_emp(request,emp_id = 0):
    if emp_id:
        emp_to_be_remove = Employee.objects.get(id=emp_id)
        emp_to_be_remove.delete()
        return HttpResponse("Employee has been deleted successfully! <a href='/remove_emp'><button class='btn btn-primary'>back</button></a>")
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    
    return render(request,'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        dept = request.POST['dept']

        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains =dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
       
        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
                      
    elif request.method == 'GET':
        return render(request,'filter_employee.html')
    
    else:
        return HttpResponse('AN Exception occured')
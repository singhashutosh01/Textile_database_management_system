from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
from .filters import *
from .filters import SalaryReportFilter, MachineReportFilter, MachineReportFilter
from django.http import HttpResponse
from .models import *
from .forms import party_bill_delivery_order_form, CreateUserForm, create_employee_form,create_party_form, create_monthly_wage_form
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required(login_url='login')
def home(request):
    employees = employee.objects.all()
    wages_reports = wages_report.objects.all()
    total_employees = employees.count()
    parties = party.objects.all()
    total_parties = parties.count()
    total_wage_money=0
    for i in wages_reports:
        total_wage_money = total_wage_money+i.salary
    context ={ 'employees': employees, 'total_employees': total_employees, 'total_parties':total_parties, 'total_wage_money':total_wage_money }
    return render(request, 'textmanage/home_page.html', context )

def register_page(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created for '+ user + '!!!')
            return redirect('login')


    context ={'form': form}
    return render( request, 'textmanage/register.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password= password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            messages.info(request, 'Username and Password is incorrect!!!')
          
    context = {}
    return render(request, 'textmanage/login.html', context)


def index(request):
    return HttpResponse("Akanksha Textile Management System!")


def employees(request, pk):
    employees = employee.objects.get(employee_id=pk)
    
    context= { 'employees': employees}
    return render(request, 'textmanage/1employee_show.html', context)

def employee_search(request):
    employee_lists = employee.objects.all()
   
    myFilter =EmployeeFilter(request.GET, queryset=employee_lists)
    employee_lists = myFilter.qs

    context ={'myFilter':myFilter , 'employee_lists':employee_lists}
    return render( request, 'textmanage/employee_search.html', context)


def employee_lists(request):
    employee_lists = employee.objects.all()
   
    myFilter =EmployeeFilter(request.GET, queryset=employee_lists)
    employee_lists = myFilter.qs

    context ={'myFilter':myFilter , 'employee_lists':employee_lists}
    return render( request, 'textmanage/dashboard.html', context)

def parties(request):
    parties = party.objects.all()
    total_parties = parties.count()


    myFilter = PartyFilter(request.GET, queryset=parties)
    parties = myFilter.qs
    
    context= { 'parties': parties, 'myFilter': myFilter}
    return render(request, 'textmanage/parties.html', context)

def parties_search(request):
    parties = party.objects.all()
    total_parties = parties.count()


    myFilter = PartyFilter(request.GET, queryset=parties)
    parties = myFilter.qs
    
    context= { 'parties': parties, 'myFilter': myFilter}
    return render(request, 'textmanage/parties_search.html', context)



def search(request):
    parties = party.objects.all()

    myFilter = PartyFilter(request.GET, queryset=parties)
    parties = myFilter.qs
    
    context= { 'parties': parties, 'myFilter': myFilter}
    return render(request, 'textmanage/search.html', context)

def statistics(request):
    return render(request, 'textmanage/statistics.html')

def party_bill_delivery_order(request):
    form = party_bill_delivery_order_form()
    if request.method == 'POST':
        #print('Printing party bill delivery order POST', request.POST)
        form = party_bill_delivery_order_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form}
    return render(request, 'textmanage/party_bill_delivery_order.html', context)

def create_employee(request):
    form = create_employee_form()
    if request.method == 'POST':
        #print('Printing party bill delivery order POST', request.POST)
        form = create_employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form}
    return render(request, 'textmanage/create_employee.html', context)

def create_party(request):
    form = create_party_form()
    if request.method == 'POST':
        #print('Printing party bill delivery order POST', request.POST)
        form = create_party_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form}
    return render(request, 'textmanage/create_party.html', context)


def employee_monthly_wage_report(request):
   wages_reports = wages_report.objects.all()
   total_wage_money = wages_report.objects.aggregate(Sum('salary'))
   context ={'total_wage_money':total_wage_money}
   return render(request, 'textmanage/employee_monthly_wage_report.html', context)

def salary_report(request):
   
    salary_reports=wages_report.objects.all()
    total_salary_report = salary_reports.count()

    myFilter = SalaryReportFilter(request.GET, queryset=salary_reports)
    salary_reports = myFilter.qs
    
    context= { 'salary_reports': salary_reports, 'myFilter': myFilter}
    return render(request, 'textmanage/salary_reports.html', context)

def machine_reports(request):
       
    machine_reports=maintenance_inventory.objects.all()
    total_machine_report = machine_reports.count()

    myFilter = MachineReportFilter(request.GET, queryset=machine_reports)
    machine_reports = myFilter.qs
    
    context= { 'machine_reports': machine_reports, 'myFilter': myFilter}
    return render(request, 'textmanage/machine_reports.html', context)

def orders(request):
    orders = party_bill_delivery.objects.all()
    total_orders = orders.count()


    myFilter = OrdersFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    context= { 'orders': orders, 'myFilter': myFilter}
    return render(request, 'textmanage/orders.html', context)

def orders_search(request):
    orders = party_bill_delivery.objects.all()
    total_orders = orders.count()


    myFilter = OrdersFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    context= { 'orders': orders, 'myFilter': myFilter}
    return render(request, 'textmanage/orders_search.html', context)


def earnings(request):
    
    return render(request, 'textmanage/status.html', context)

class HomeView(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'textmanage/index.html') 

class ChartData(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None): 
        labels = [ 
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            ] 
        chartLabel = "my data"
        machine_reports=maintenance_inventory.objects.all()
        val1=0
        val2=0
        val3=0
        val4=0
        val5=0
        val6=0
        for machine_report in machine_reports:
            if machine_report.machine_id_id==1:
                val1+=1
            if machine_report.machine_id_id==2:
                val2+=1
            if machine_report.machine_id==3:
                    val3+=1
            if machine_report.machine_id_id==4:
                val4+=1
            if machine_report.machine_id_id==5:
                val5+=1
            if machine_report.machine_id_id==6:
                val6+=1

        chartdata = [val1, val2,val3, val4, val5, val6] 
        data ={ 
                        "labels":labels, 
                        "chartLabel":chartLabel, 
                        "chartdata":chartdata, 
                } 
        return Response(data) 



class HomeView_part(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'textmanage/index_part_name.html') 
        
class ChartData_part(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None): 
        labels = [ 
            'Gripper Tep Patti',
            'Arm Bushing',
            'Under Osom Rashi',
            'Under Mosom Rashi',
            'Under Nusum Rashi',
            'Tape',
            'Dropin Patti',
            'Palish Paper',
            'Gripper-Set',
            'Cutter Bolt',
            'Bes Patti',
            'Bearing',
            '10N Bolt',
            ] 
        chartLabel = "my data"
        machine_reports=maintenance_inventory.objects.all()
        val1=0
        val2=1
        val3=5
        val4=0
        val5=0
        val6=0
        val7=0
        val8=1
        val9=5
        val10=0
        val11=0
        val12=0
        val13=0
        for machine_report in machine_reports:
            if machine_report.part_name=='gripper tep patti' :
                val1+=machine_report.quantity
            if machine_report.part_name=='arm bushing':
                val2+=machine_report.quantity
            if machine_report.part_name=='under osom rashi':
                val3+=machine_report.quantity
            if machine_report.part_name=='under mosom rashi':
                val4+=machine_report.quantity
            if  machine_report.part_name=='under nusum rashi':
                val5+=machine_report.quantity
            if  machine_report.part_name=='tape':
                val6+=machine_report.quantity
            if  machine_report.part_name=='dropin patti':
                val7+=machine_report.quantity
            if  machine_report.part_name=='palish paper':
                val8+=machine_report.quantity
            if  machine_report.part_name=='grperset'or machine_report.part_name=='gripperset':
                val9+=machine_report.quantity
            if  machine_report.part_name=='cutter bolt'or machine_report.part_name=='cuttur bolt':
                val10+=machine_report.quantity
            if  machine_report.part_name=='bes patti':
                val11+=machine_report.quantity
            if  machine_report.part_name=='beering' or  machine_report.part_name=='bering':
                val12+=machine_report.quantity
            if  machine_report.part_name=='10N bolt':
                val13+=machine_report.quantity
                   
        chartdata = [val1, 5,val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13] 
        data ={ 
                        "labels":labels, 
                        "chartLabel":chartLabel, 
                        "chartdata":chartdata, 
                } 
        return Response(data) 


class HomeView_orders(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'textmanage/index_orders.html') 

class ChartData_orders(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None): 
        labels = [ 
            'Vedh Textiles',
            'Mahalakshmi Textile',
            'Lakshmi Textiles',
            'Sanketh Textiles',
            'Shaswath Textiles',
            'Viraj Textiles',
            'Suraj Textiles',
            'Ashlesh Textiles',
            'nipani Textiles',
            'Shri Textiles',
            ] 
        chartLabel = "my data"
        party_bills=party_bill_delivery.objects.all()
        val1=0
        val2=0
        val3=0
        val4=0
        val5=0
        val6=0
        val7=0
        val8=0
        val9=0
        val10=0
        for party_bill in party_bills:
            if party_bill.party_id_id==1:
                val1+=1
            if party_bill.party_id_id==2:
                val2+=1
            if party_bill.party_id_id==3:
                val3+=1
            if party_bill.party_id_id==4:
                val4+=1
            if party_bill.party_id_id==5:
                val5+=1
            if party_bill.party_id_id==6:
                val6+=1
            if party_bill.party_id_id==7:
                val7+=1
            if party_bill.party_id_id==8:
                val8+=1
            if party_bill.party_id_id==9:
                val9+=1
            if party_bill.party_id_id==10:
                val10+=1
    
        chartdata = [val1, val2,val3, val4, val5, val6, val7, val8, val9, val10] 
        data ={ 
                        "labels":labels, 
                        "chartLabel":chartLabel, 
                        "chartdata":chartdata, 
                } 
        return Response(data) 


class HomeView_employee_info(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'textmanage/index_employee_info.html') 

class ChartData_employee_info(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None): 
        labels = [ 
            'Driver',
            'Weaver',
            'Manager',
            
            ] 
        chartLabel = "my data"
        employees=employee.objects.all()
        max=0
        val1=0
        val2=0
        val3=0
        for employee1 in employees:
            if employee1.designation=='driver':
                val1+=1
            if employee1.designation=='weaver'or employee1.designation=='Weaver':
                val2+=1
            if employee1.designation=='manager':
                val3+=1

        chartdata = [val1, val2,val3] 
        data ={ 
                        "labels":labels, 
                        "chartLabel":chartLabel, 
                        "chartdata":chartdata, 
                } 
        return Response(data) 



from django.urls import path, include
from . import views
from .views import ChartData, HomeView, ChartData_part, HomeView_part, HomeView_orders, ChartData_orders, HomeView_employee_info, ChartData_employee_info

urlpatterns = [
    path('', views.home, name="home"),
    path('logout', views.logout_page, name="logout"),
    path('login', views.login_page, name="login"),
    path('register', views.register_page, name="register"),
    path('employees/<str:pk>', views.employees, name="employee"),
    path('employee_lists', views.employee_lists, name="employee_lists"), 
    path('parties', views.parties, name="parties"),
    path('parties_search', views.parties_search, name="parties_search"),
    path('salary_report', views.salary_report, name="salary_report"), 
    path('machine_reports', views.machine_reports, name="machine_reports"), 
    path('party_bill_delivery_order', views.party_bill_delivery_order, name ="party_bill_delivery_order"),
    path('create_employee', views.create_employee, name ="create_employee") ,
    path('create_party', views.create_party, name ="create_party") ,
    path('employee_monthly_wage_report', views.employee_monthly_wage_report, name ="employee_monthly_wage_report") ,
    path('api', ChartData.as_view(), name= "api"), 
    path('api_chart', HomeView.as_view(), name="api_chart"),
    path('api_part', ChartData_part.as_view(), name= "api_part"), 
    path('api_part_chart', HomeView_part.as_view(), name="api_part_chart"), 
    path('api_orders', ChartData_orders.as_view(), name= "api_orders"), 
    path('api_orders_chart', HomeView_orders.as_view(), name="api_orders_chart"), 
    path('api_employee_info', ChartData_employee_info.as_view(), name= "api_employee_info"), 
    path('api_employee_info_chart', HomeView_employee_info.as_view(), name="api_employee_info_chart"), 
    path('orders', views.orders, name="orders"),
    path('orders_search', views.orders_search, name="orders_search"),
    path('search', views.search, name="search"),
    path('employee_search', views.employee_search, name="employee_search"),
    path('statistics', views.statistics, name="statistics"),
]

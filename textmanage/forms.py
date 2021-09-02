from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class party_bill_delivery_order_form(ModelForm):
    class Meta:
        model = party_bill_delivery
        fields = '__all__'

class create_employee_form(ModelForm):
    class Meta:
        model = employee
        fields = '__all__'

class create_party_form(ModelForm):
    class Meta:
        model = party
        fields = '__all__'

class create_monthly_wage_form(ModelForm):
    class Meta:
        model = wages_report
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

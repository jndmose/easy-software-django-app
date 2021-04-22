from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from webapp.models import Building, Tenant, TenantBuilding


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta():
        model = User
        fields = ('username','email','password1','password2')

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ('name','location','owner','units_count')

class TenantForm(forms.ModelForm):
    class Meta:
        model= Tenant
        fields = ('name','email','phone','next_of_kin')
        

class BuildingTenantForm(forms.ModelForm):
    class Meta:
        model= TenantBuilding
        fields = ('building','tenant','checkin_date','contract_amount','status')

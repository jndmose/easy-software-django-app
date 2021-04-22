from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from webapp.forms import UserForm, BuildingForm, TenantForm, BuildingTenantForm
from webapp.models import Building, Tenant, TenantBuilding
from django.urls import reverse

# Create your views here.


@transaction.atomic
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
     
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            registered = True
            return redirect('webapp:allgood')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        
    return render(request,'signup.html',
                          {'user_form':user_form,
                           'registered':registered})


def allgood(request):
    return render(request,'allgood.html')



def building(request):
    if request.method == 'POST':
        buildingform= BuildingForm(request.POST)
        if buildingform.is_valid():
            buildingform.save()
            return redirect('webapp:allgood')

    else:
        buildingform= BuildingForm()

    context= {'buildingform':buildingform}
    return render (request,'create_building.html', context)

def tenant(request):
    if request.method == 'POST':
        tenantform= TenantForm(request.POST)
        if tenantform.is_valid():
            tenantform.save()
            return redirect('webapp:allgood')

    else:
        tenantform= TenantForm()

    context= {'tenantform':tenantform}
    return render (request,'create_tenant.html', context)

def list_tenant(request):
    tenant_list= Tenant.objects.all()
    if tenant_list.exists():
        context={
            'tenant_list': tenant_list
        }
    return render(request,'tenant_list.html',context)


def list_building(request):
    building_list= Building.objects.all()
    if building_list.exists():
        context={
            'building_list': building_list
        }
    return render(request,'building_list.html',context)

def update_building_number(request, **kwargs):
    item_id = kwargs.get('item_id', "10")
    item_number = kwargs.get('item_number', "10")
    item_to_update = get_object_or_404(Building, pk=item_id)
    item_to_update.units_count= item_number
    item_to_update.save(update_fields=["units_count"])
    return redirect(reverse('webapp:listBuilding')) 

def delete_building(request, **kwargs):
    item_id = kwargs.get('item_id', "10")
    print(item_id)
    Building.objects.filter(pk=item_id).delete()
    return redirect(reverse('webapp:listBuilding')) 

def building_tenant(request):
    if request.method == 'POST':
        buildingTenantForm= BuildingTenantForm(request.POST)
        if buildingTenantForm.is_valid():
            buildingTenantForm.save()
            return redirect('webapp:allgood')

    else:
        buildingTenantForm= BuildingTenantForm()

    context= {'buildingTenantForm':buildingTenantForm}
    return render (request,'building_tenant.html', context)


def list_tenant_building(request):
    tenant_building_list= TenantBuilding.objects.all()
    if tenant_building_list.exists():
        context={
            'tenant_building_list': tenant_building_list
        }
    return render(request,'tenant_bulding_list.html',context)

    


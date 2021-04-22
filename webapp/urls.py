from django.urls import path
from django.conf.urls import url
from webapp import views

# SET THE NAMESPACE!
app_name = 'webapp'

urlpatterns = [
    path('',views.allgood,name='allgood'),
    path('register/',views.register,name='register'),
    path('allgood/',views.allgood,name='allgood'),
    path('createBuilding/',views.building,name='building'),
    path('listBuilding/',views.list_building,name='listBuilding'),
    url(r'^service/update/(?P<item_id>[-\w]+)/(?P<item_number>[-\w]+)/$', views.update_building_number, name='update_building'),
    url(r'^service/delete/(?P<item_id>[-\w]+)/$', views.delete_building, name='delete_building'),
    path('createTenant/',views.tenant,name='tenant'),
    path('listTenant/',views.list_tenant,name='listTenant'),
    path('createBuildingTenant/',views.building_tenant,name='buildingTenant'),
     path('listBuildingTenant/',views.list_tenant_building,name='listBuildingTenant'),

]
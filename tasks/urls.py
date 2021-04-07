from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name="index"),
    path('AllTaskview/', views.AllTaskview , name="AllTaskview"),
    path('updatetask/<int:id>/', views.Edittask , name="updatetask"),
    path('<int:id>/', views.Deletetask , name="deletetask"), 
    path('try/',views.Try,name='try')   
]

from django.contrib import admin
from .models import AddtaskForm
# Register your models here.

@admin.register(AddtaskForm)
class AddtaskAdmin(admin.ModelAdmin):
    list_display=['id','Project','Task','Status']

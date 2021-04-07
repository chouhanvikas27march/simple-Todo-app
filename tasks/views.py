from django.shortcuts import render
from .forms import AddTaskForms
from .models import AddtaskForm
from django.http import HttpResponseRedirect
from django.views import View


# Create your views here.


#add new task
def home(request):
    if request.method == 'POST' :     
      fm = AddTaskForms(request.POST) 
      if fm.is_valid():
            # Pj  = fm.cleaned_data['Project']
            # Tk = fm.cleaned_data['Task']
            # Sd = fm.cleaned_data['Start_Date']
            # Dl = fm.cleaned_data['Deadline']
            # Des = fm.cleaned_data['Description']
            # St = fm.cleaned_data['Status']
            # data = AddtaskForm(Project = Pj , Task =Tk , Start_Date =Sd , Deadline = Dl , Description= Des ,Status= St)
            # data.save()
            fm.save()
    else:
      fm = AddTaskForms() 
    return render(request,"tasks/index.html" , {'form':fm}) 



#try
def Try(request):
  return render(request , 'tasks/try.html')  

#dashboard / view all tasks
def AllTaskview(request):
  data = AddtaskForm.objects.all().order_by('Deadline')
  return render(request , 'tasks/viewalltask.html', {'data':data})   
    
#edit/update
def Edittask(request,id):
  pk = AddtaskForm.objects.get(pk=id)
  if request.method == 'POST':  
    fm = AddTaskForms(request.POST , instance=pk) 
    if fm.is_valid():
      fm.save()
  else:
     fm = AddTaskForms(instance=pk)         
  return render(request , 'tasks/updatetask.html', {'form':fm})   

#delete
def Deletetask(request,id):
  pk = AddtaskForm.objects.get(pk=id)
  if request.method == 'POST':  
     pk.delete()
  return HttpResponseRedirect('/AllTaskview/')
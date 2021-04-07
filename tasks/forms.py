from django import forms
from .models import AddtaskForm

class AddTaskForms(forms.ModelForm):
    class Meta :
        model = AddtaskForm
        fields = '__all__'
        widgets = {
            'Project' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project'}, ),
            'Task' : forms.TextInput(attrs={'class':'form-control','placeholder':'Task'}),
            'Start_Date' : forms.DateInput(attrs={'class':'form-control','placeholder':'Start Date'}),
            'Deadline' : forms.DateInput(attrs={'class':'form-control','placeholder':'Deadline'}),
            'Description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'Status' : forms.Select(attrs={'class':'form-control','placeholder':'Status'}),
        }



from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__' # que django considere todos los campos

class CreateTaskForm(forms.Form):

    title = forms.CharField(
        label = "Titulo de la tarea",
        max_length = 200
    )
    description = forms.CharField(
        label = "Descripcion",
        widget = forms.Textarea()
    )

class UpdateTaskForm(forms.Form):

    title = forms.CharField(
        label = "Titulo de la tarea",
        max_length = 200
    )
    description = forms.CharField(
        label = "Descripcion",
        widget = forms.Textarea()
    )
    completed = forms.BooleanField(
        label = "Completado",
        required = False
    )
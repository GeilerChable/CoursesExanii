from tkinter.tix import Form
from django import forms
from exani.models import Student

class InscriptionStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ "student", "school"]
    
        labels = {
        'student' : "Nombre Completo",
        'school' : "Escuela Procediente", 
        }

        widgets = {
        'student': forms.TextInput(attrs={'class': 'form-control'}),
        'school': forms.TextInput(attrs={'class': 'form-control'})
        }

    #student: forms.CharField(label="Nombre Completo", max_length=200)
    #school: forms.CharField(label="Escuela Procediente", widget=forms.Textarea)

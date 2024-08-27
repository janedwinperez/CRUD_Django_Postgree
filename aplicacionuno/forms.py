from django import forms

class FormularioRegistro(forms.Form):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    casa = forms.CharField()
    celular = forms.CharField()

from django.shortcuts import render
from . forms import FormularioRegistro 
from . models import Propietarios


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def showformdata(request):
    if (request.method == "GET"):
        fm = FormularioRegistro()
    if (request.method == "POST"):
        fm = FormularioRegistro(request.POST)
        if (fm.is_valid()):
            propietarios = Propietarios(nombres = request.POST['nombres'], apellidos=request.POST['apellidos'], casa=request.POST['casa'], 
                           celular=request.POST['celular'])
            propietarios.save()
    return render(request, 'registro.html', {'form': fm})


def viewdata(request):
    propietarios = Propietarios.objects.all()
    return render(request, 'viewdata.html', {'propietarios' : propietarios})

#def Editpropietario(request):
    #if (request.method == "GET"):
    #    fm = FormularioRegistro()
    #if (request.method == "POST"):
    #    fm = FormularioRegistro(request.POST)
    #    if (fm.is_valid()):
    #        propietarios = Propietarios(nombres = request.POST['nombres'], apellidos=request.POST['apellidos'], casa=request.POST['casa'], 
    #                       celular=request.POST['celular'])
    #        propietarios.save()
    #return render(request, 'edit.html', {'form': fm})

def Editpropietario(request, id):
    editprop = Propietarios.objects.get(id = id)
    return render(request, 'editpropietario.html', {'propietarios' : editprop})

def updateprop(request, id):
    actprop = Propietarios.objects.get(id = id)
    form = FormularioRegistro(request.POST)
    if (form.is_valid()):
        propietarios = Propietarios(id = request.POST['id'], nombres = request.POST['nombres'], apellidos=request.POST['apellidos'], casa=request.POST['casa'], 
                           celular=request.POST['celular'])
        propietarios.save()
        actprop = Propietarios.objects.get(id = id)
        return render(request, 'editpropietario.html', {'propietarios' : actprop})


def deletepropietario(request, id):
    delprop = Propietarios.objects.get(id = id)   #Se carga el numero id
    delprop.delete()
    propietarios = Propietarios.objects.all()
    return render(request, 'viewdata.html', {'propietarios' : propietarios})
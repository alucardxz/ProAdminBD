from django.shortcuts import render,redirect,get_object_or_404,render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import csv,io
from django.contrib import messages 
from django.contrib.auth.decorators import permission_required
from django.http import  HttpResponseNotFound
from django.http import HttpResponse, request
from django.urls import reverse_lazy 

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import Clienteform,Paiform,Estadoform,Ciudadeform
from .forms import Recepcionistaform,Habitacioneform,Reservacioneform , Registroform
from .models import Cliente,Ciudade,Estado,Pai,Recepcionista,Reservacione,Habitacione

import subprocess, gzip
from django.contrib.auth.models import Permission
from subprocess import Popen
from  PracticaHotel.settings import DATABASES
from django.core.files.storage import FileSystemStorage
from django.db import transaction
import json
# Create your views here.

###############################################################################################
###############################################################################################
###############################################################################################
############################## VISTAS  CRUD ###################################################

#Cliente
class ClienteList(ListView):
    model = Cliente
    template_name = 'HotelSayula/consultar_cliente.html'

class ClienteCreate(CreateView):
    model =Cliente
    form_class = Clienteform
    template_name = 'HotelSayula/añadir_cliente.html'
    success_url = reverse_lazy('ver_cliente')

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = Clienteform
    template_name = 'HotelSayula/añadir_cliente.html'
    success_url = reverse_lazy('ver_cliente')

class ClienteDelete(DeleteView):
    model = Cliente
    form_class = Clienteform
    template_name = 'HotelSayula/eliminar_cliente.html'
    success_url = reverse_lazy('ver_cliente')

#Ciudades
class CiudadeList(ListView):
    model = Ciudade
    template_name = 'HotelSayula/consultar_ciudade.html'

class CiudadeCreate(CreateView):
    model = Ciudade
    form_class = Ciudadeform
    template_name = 'HotelSayula/añadir_ciudade.html'
    success_url = reverse_lazy('ver_ciudade')

class CiudadeUpdate(UpdateView):
    model =  Ciudade
    form_class = Ciudadeform
    template_name = 'HotelSayula/añadir_ciudade.html'
    success_url = reverse_lazy('ver_ciudade')

class CiudadeDelete(DeleteView):
    model =  Ciudade
    form_class = Ciudadeform
    template_name = 'HotelSayula/eliminar_ciudade.html'
    success_url = reverse_lazy('ver_ciudade')

#Estado
class EstadoList(ListView):
    model = Estado
    template_name = 'HotelSayula/consultar_estado.html'

class EstadoCreate(CreateView):
    model = Estado
    form_class = Estadoform
    template_name = 'HotelSayula/añadir_estado.html'
    success_url = reverse_lazy('ver_estado')

class EstadoUpdate(UpdateView):
    model =  Estado
    form_class = Estadoform
    template_name = 'HotelSayula/añadir_estado.html'
    success_url = reverse_lazy('ver_estado')

class EstadoDelete(DeleteView):
    model =  Estado
    form_class = Estadoform
    template_name = 'HotelSayula/eliminar_estado.html'
    success_url = reverse_lazy('ver_estado')

#Pais
class PaiList(ListView):
    model = Pai
    template_name = 'HotelSayula/consultar_pai.html'

class PaiCreate(CreateView):
    model = Pai
    form_class = Paiform
    template_name = 'HotelSayula/añadir_pai.html'
    success_url = reverse_lazy('ver_pai')

class PaiUpdate(UpdateView):
    model =  Pai
    form_class = Paiform
    template_name = 'HotelSayula/añadir_pai.html'
    success_url = reverse_lazy('ver_pai')

class PaiDelete(DeleteView):
    model =  Pai
    form_class = Paiform
    template_name = 'HotelSayula/eliminar_pai.html'
    success_url = reverse_lazy('ver_pai')
#Recepcionista
class RecepcionistaList(ListView):
    model = Recepcionista
    template_name = 'HotelSayula/consultar_recepcionista.html'

class RecepcionistaCreate(CreateView):
    model = Recepcionista
    form_class = Recepcionistaform
    template_name = 'HotelSayula/añadir_recepcionista.html'
    success_url = reverse_lazy('ver_recepcionista')

class RecepcionistaUpdate(UpdateView):
    model =  Recepcionista
    form_class = Recepcionistaform
    template_name = 'HotelSayula/añadir_recepcionista.html'
    success_url = reverse_lazy('ver_recepcionista')

class RecepcionistaDelete(DeleteView):
    model =  Recepcionista
    form_class = Recepcionistaform
    template_name = 'HotelSayula/eliminar_recepcionista.html'
    success_url = reverse_lazy('ver_recepcionista')

#Reservacione
class ReservacioneList(ListView):
    model = Reservacione
    template_name = 'HotelSayula/consultar_reservacione.html'

class ReservacioneCreate(CreateView):
    model = Reservacione
    form_class = Reservacioneform
    template_name = 'HotelSayula/añadir_recervacione.html'
    success_url = reverse_lazy('ver_reservacione')

class ReservacioneUpdate(UpdateView):
    model =  Reservacione
    form_class = Reservacioneform
    template_name = 'HotelSayula/añadir_reservacione.html'
    success_url = reverse_lazy('ver_reservacione')

class ReservacioneDelete(DeleteView):
    model =  Reservacione
    form_class = Reservacioneform
    template_name = 'HotelSayula/eliminar_reservacione.html'
    success_url = reverse_lazy('ver_reservacione')
#Habitacione
class HabitacioneList(ListView):
    model = Habitacione
    template_name = 'HotelSayula/consultar_habitacione.html'

class HabitacioneCreate(CreateView):
    model = Habitacione
    form_class = Habitacioneform
    template_name = 'HotelSayula/añadir_habitacione.html'
    success_url = reverse_lazy('ver_habitacione')

class HabitacioneUpdate(UpdateView):
    model =  Habitacione
    form_class = Habitacioneform
    template_name = 'HotelSayula/añadir_habitacione.html'
    success_url = reverse_lazy('ver_habitacione')

class HabitacioneDelete(DeleteView):
    model =  Habitacione
    form_class = Habitacioneform
    template_name = 'HotelSayula/eliminar_habitacione.html'
    success_url = reverse_lazy('ver_habitacione')

###############################################################################################
###############################################################################################
###############################################################################################
############################## Acciones extras ################################################
#respalda base de datos
def backup(request):
    name = DATABASES['default']['NAME']
    passwd = DATABASES['default']['PASSWORD']
    user = DATABASES['default']['USER']
    #mysqldump -u root -p agenda > C:/respaldos/PracticaHotel.sql
    proc = subprocess.Popen("C:/xampp/mysql/bin/mysqldump -u "+user+" -p"+passwd+" "+name+" > "+ "D:/respaldos/backup.sql", shell=True)
    proc.wait()
    procs = subprocess.Popen("tar -czvf "+ "D:/respaldos/backup.tar.tgz "+ "C:/respaldos/backup.sql", shell=True, )
    procs.wait()
    fs = FileSystemStorage("D:/respaldos/")
    with fs.open('backup.tar.tgz') as tar:
        response = HttpResponse(tar, content_type='application/x-gzip')
        response['Content-Disposition'] = 'filename="backup.tar.tgz"'
        return response
#Permisos en mysql
def check(request):
        try:
            passwd = DATABASES['default']['PASSWORD']#pasword
            user = DATABASES['default']['USER']#nombre Superuser
            use= request.Get.get("username") #usuario q se esta creando aqui meter nombre caja de text ("ct")
            pasw= request.Get.get("password") #usuario q se esta creando aqui meter el nombre de las cajadetex
            ######## de aqui 
            permisos= request.POST.getlist('perm[]')
            i=len('perm[]')
            if i==0:
                privileges=" "
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
            if i==1:
                privileges=" "+permisos[0]
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
            if i==2:  
                privileges=" "+permisos[0]+","+permisos[1]
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
            if i==3:
                privileges=" "+permisos[0]+","+permisos[1]+","+permisos[2]
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
            if i==4:
                privileges=" "+permisos[0]+","+permisos[1]+","+permisos[2]+","+permisos[3]
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
        except :
             print()

        return render(request,"HotelSayula/permisos.html")
#permisos en django
def index(request):
    if request.method=='GET':
        return render(request,'HotelSayula/index.html')
    else:
        username=request.POST['username']
        if username=="":
            return render(request,'HotelSayula/index.html')
        else:
            permisos1= request.POST.get('perm1')
            if permisos1=="add":
                u=User.objects.get(username=username)
                a=Permission.objects.get(codename='add_reservacione')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='add_cliente')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='add_ciudade')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='add_estado')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='add_pai')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='add_habitacione')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='add_recepcionista')  
                u.user_permissions.add(a.id)# Añadir el permiso
             
            permisos2= request.POST.get('perm2')
            if permisos2=="view":
                u=User.objects.get(username=username)
                a=Permission.objects.get(codename='view_cliente')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='view_habitacione')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='view_ciudade')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='view_pai')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='view_estado')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='view_recepcionista')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='view_reservacione')  
                u.user_permissions.add(a.id)# Añadir el permiso
                
            permisos3= request.POST.get('perm3')
            if permisos3=="change":
                u=User.objects.get(username=username)
                a=Permission.objects.get(codename='change_cliente')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='change_pai')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='change_estado')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='change_ciudade')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='change_habitacione')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='change_reservacione')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='change_recepcionista')  
                u.user_permissions.add(a.id)# Añadir el permiso
             
            permisos4= request.POST.get('perm4')
            if permisos4=="delete":
                u=User.objects.get(username=username)
                a=Permission.objects.get(codename='delete_cliente')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='delete_pai')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='delete_estado')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='delete_ciudade')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='delete_habitacione')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='delete_recepcionista')  
                u.user_permissions.add(a.id)# Añadir el permiso
                a=Permission.objects.get(codename='delete_reservacion')  
                u.user_permissions.add(a.id)# Añadir el permiso
            return render(request, 'HotelSayula/index.html')      
#respaldo
def respaldo(request):
    return render(request, 'HotelSayula/respaldo.html')
class RegistrarUsuario(CreateView):
    model = User
    template_name = 'HotelSayula/crear_usuario.html'
    form_class = Registroform
    success_url = reverse_lazy('login')
#Respaldar cada tabla

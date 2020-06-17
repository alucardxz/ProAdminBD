from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente,Pai,Estado,Ciudade,Reservacione,Recepcionista,Habitacione

class Registroform(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre de pila',
            'last_name' : 'Apellidos',
            'email' : 'Correo electronico',
        }

class Ciudadeform(forms.ModelForm):
    class Meta:
        model = Ciudade
        fields = [
            'Id_Ciudad',
            'Nombre_C',
        ]
        labels = {
            'Id_Ciudad' : 'Id_Ciudad',
            'Nombre_C' : 'Nombre_C',
        }
        widgets = {
            'Id_Ciudad' : forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_C' : forms.TextInput(attrs={'class':'form-control'}),
        
        }
class Paiform(forms.ModelForm):
    class Meta:
        model = Pai
        fields = [
            'Id_Pais',
            'Nombre_P',
        ]
        labels = {
            'Id_Pais' : 'Id_Pais',
            'Nombre_P' : 'Nombre_P',
        }
        widgets = {
            'Id_Pais' : forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_P' :forms.TextInput(attrs={'class':'form-control'}),
        }

class Habitacioneform(forms.ModelForm):
    class Meta:
        model = Habitacione
        fields = [
            'Numero_Habitaciones',
            'Precio',
            'Disponibilidad',
            'Tipo',
            'Descripcion',
        ]
        labels = {
            'Numero_Habitaciones' : 'Numero_Habitaciones',
            'Precio' : 'Precio',
            'Disponibilidad' : 'Disponibilidad',
            'Tipo' : 'Tipo',
            'Descripcion' : 'Descripcion',
        }
        widgets = {
            'Numero_Habitaciones' : forms.TextInput(attrs={'class':'form-control'}),
            'Precio' : forms.TextInput(attrs={'class':'form-control'}),
            'Disponibilidad' : forms.TextInput(attrs={'class':'form-control'}),
            'Tipo' : forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion' : forms.TextInput(attrs={'class':'form-control'}),
        }

class Recepcionistaform(forms.ModelForm):
    class Meta:
        model = Recepcionista
        fields = [
            'Id_Empleado',
            'Nombre_R',
            'AP_R',
            'AM_R',
            'Turno',
        ]
        labels = {
            'Id_Empleado' : 'Id_Empleado',
            'Nombre_R' : 'Nombre_R',
            'AP_R' : 'AP_R',
            'AM_R' : 'AM_R',
            'Turno' : 'Turno',


        }
        widgets = {
            'Id_Empleado': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_R' : forms.TextInput(attrs={'class':'form-control'}),
            'AP_R' : forms.TextInput(attrs={'class':'form-control'}),
            'AM_R' : forms.TextInput(attrs={'class':'form-control'}),
            'Turno': forms.TextInput(attrs={'class':'form-control'}),

        }

class Reservacioneform(forms.ModelForm):
    class Meta:
        model = Reservacione
        fields = [
            'Id_Reservacion',
            'Fecha_Reservacion',
            'Fecha_Entrada',
            'Fecha_Salida',
            'Total',
            'Subtotal',

        ]
        labels = {
            'Id_Reservacion' : 'Id_Reservacion',
            'Fecha_Reservacion' : 'Fecha_Reservacion',
            'Fecha_Entrada' : 'Fecha_Entrada',
            'Fecha_Salida' : 'Fecha_Salida',
            'Total' : 'Total',
            'Subtotal' : 'Subtotal',
        }
        widgets = {
            'Id_Reservacion' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Reservacion' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Entrada' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Salida' : forms.TextInput(attrs={'class':'form-control'}),
            'Total' : forms.TextInput(attrs={'class':'form-control'}),
            'Subtotal':forms.TextInput(attrs={'class':'form-control'}), 
        }
class Estadoform(forms.ModelForm):
    class Meta:
        model = Estado
        fields = [
            'Id_Estado',
            'Nombre_E',
        ]
        labels = {
            'Id_Estado' : 'Id_Estado',
            'Nombre_E' : 'Nombre_E',
        }
        widgets = {
            'Id_Estado' : forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_E' : forms.TextInput(attrs={'class':'form-control'}),

        }
class Clienteform(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'Id_Cliente',
            'NombreC',
            'AP_C',
            'AM_M',
            'TCel_C',
            'TCasa_C',
            'Cantidad_Personas',
            'Ciudad',
            'Estado',
            'Pais',
            'Numero_Habitaciones',
        ]
        labels = {
            'Id_Cliente' : 'Id_Cliente',
            'NombreC'    : 'NombreC',
            'AP_C'       : 'AP_C',
            'AM_M'       : 'AM_M',
            'TCel_C'     :'TCel_C',
            'TCasa_C'    : 'TCasa_C',
            'Cantidad_Personas' : 'Cantidad_Personas',
            'Ciudad'     : 'Ciudad',
            'Estado'     : 'Estado',
            'Pais'       : 'Pais',
            'Numero_Habitaciones' : 'Numero_Habitaciones',
        }
        widgets = {
            'Id_Cliente' : forms.TextInput(attrs={'class':'form-control'}),
            'NombreC' : forms.TextInput(attrs={'class':'form-control'}),
            'AP_C' : forms.TextInput(attrs={'class':'form-control'}),
            'AM_M' : forms.TextInput(attrs={'class':'form-control'}),
            'TCel_C' : forms.TextInput(attrs={'class':'form-control'}),
            'TCasa_C' : forms.TextInput(attrs={'class':'form-control'}),
            'Cantidad_Personas' : forms.TextInput(attrs={'class':'form-control'}),
            'Ciudad' : forms.TextInput(attrs={'class':'form-control'}),
            'Estado' : forms.TextInput(attrs={'class':'form-control'}),
             'Pais' : forms.TextInput(attrs={'class':'form-control'}),
            'Numero_Habitaciones' : forms.TextInput(attrs={'class':'form-control'}),
        }
        
class Registroform(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre de pila',
            'last_name' : 'Apellidos',
            'email' : 'Correo electronico',
        }
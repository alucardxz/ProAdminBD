from django.urls import path
from django.conf.urls import url, handler404, handler500
from django.contrib.auth.decorators import login_required
from .views import index,check,respaldo,backup
from .views import ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete
from .views import PaiList, PaiCreate, PaiUpdate, PaiDelete
from .views import CiudadeList, CiudadeCreate, CiudadeUpdate, CiudadeDelete
from .views import EstadoList, EstadoCreate, EstadoUpdate, EstadoDelete
from .views import ReservacioneList, ReservacioneCreate, ReservacioneUpdate, ReservacioneDelete
from .views import HabitacioneList, HabitacioneCreate, HabitacioneUpdate, HabitacioneDelete
from .views import RecepcionistaList, RecepcionistaCreate, RecepcionistaUpdate, RecepcionistaDelete


urlpatterns = [
    path('',login_required(index)),
    path('respalda', backup, name='backup'),
    path('check', check, name='check'),
    path('respaldo',login_required(respaldo)),
    path('añadir_cliente',login_required(ClienteCreate.as_view())),
    path('consultar_cliente',login_required(ClienteList.as_view()),name='ver_cliente'),
    url(r'^modificar_cliente/(?P<pk>\d+)/$',login_required(ClienteUpdate.as_view()), name= 'modi_cliente'),
    url(r'^eliminar_cliente/(?P<pk>\d+)/$',login_required(ClienteDelete.as_view()), name= 'eli_cliente'),
    path('consultar_pai',login_required(PaiList.as_view()),name='ver_pai'),
    path('añadir_pai',login_required(PaiCreate.as_view())),
    url(r'^modificar_pai/(?P<pk>\d+)/$',login_required(PaiUpdate.as_view()), name= 'modi_pai'),
    url(r'^eliminar_pai/(?P<pk>\d+)/$',login_required(PaiDelete.as_view()), name= 'eli_pai'),
    path('consultar_estado',login_required(EstadoList.as_view()),name='ver_estado'),
    path('añadir_estado',login_required(EstadoCreate.as_view())),
    url(r'^modificar_estado/(?P<pk>\d+)/$',login_required(EstadoUpdate.as_view()), name= 'modi_estado'),
    url(r'^eliminar_estado/(?P<pk>\d+)/$',login_required(EstadoDelete.as_view()), name= 'eli_estado'),
    path('consultar_ciudade',login_required(CiudadeList.as_view()),name='ver_ciudade'),
    path('añadir_ciudade',login_required(CiudadeCreate.as_view())),
    url(r'^modificar_ciudade/(?P<pk>\d+)/$',login_required(CiudadeUpdate.as_view()), name= 'modi_ciudade'),
    url(r'^eliminar_ciudade/(?P<pk>\d+)/$',login_required(CiudadeDelete.as_view()), name= 'eli_ciudade'),
    path('consultar_recepcionista',login_required(RecepcionistaList.as_view()),name='ver_recepcionista'),
    path('añadir_recepcionista',login_required(RecepcionistaCreate.as_view())),
    url(r'^modificar_recepcionista/(?P<pk>\d+)/$',login_required(RecepcionistaUpdate.as_view()), name= 'modi_recepcionista'),
    url(r'^eliminar_recepcionista/(?P<pk>\d+)/$',login_required(RecepcionistaDelete.as_view()), name= 'eli_recepcionista'),
    path('consultar_reservacione',login_required(ReservacioneList.as_view()),name='ver_reservacione'),
    path('añadir_reservacione',login_required(ReservacioneCreate.as_view())),
    url(r'^modificar_reservacione/(?P<pk>\d+)/$',login_required(ReservacioneUpdate.as_view()), name= 'modi_reservacione'),
    url(r'^eliminar_reservacione/(?P<pk>\d+)/$',login_required(ReservacioneDelete.as_view()), name= 'eli_reservacione'),
    path('consultar_habitacione',login_required(HabitacioneList.as_view()),name='ver_habitacione'),
    path('añadir_habitacione',login_required(HabitacioneCreate.as_view())),
    url(r'^modificar_habitacione/(?P<pk>\d+)/$',login_required(HabitacioneUpdate.as_view()), name= 'modi_habitacione'),
    url(r'^eliminar_habitacione/(?P<pk>\d+)/$',login_required(HabitacioneDelete.as_view()), name= 'eli_habitacione'),

]
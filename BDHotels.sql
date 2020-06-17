create database HotelS
use HotelS
create table pais(
     Id_Pais int ,
     Nombre_P varchar(20),
     primary key(Id_Pais)
)

create table estado(
     Id_Estado int not null,
     Nombre_E varchar(20),
     Id_Pais int not null,
     primary key(Id_Estado),
     FOREIGN KEY (Id_Pais) references pais(Id_Pais)
)


--
create table ciudad(
  Id_Ciudad int not null,
  Nombre_C varchar(20),
  Id_Estado int not null,
  primary key(Id_Ciudad),
  FOREIGN KEY (Id_Estado) references estado(Id_Estado) 
)

create table habitaciones(
     Numero_Habitaciones int not null,
     Precio float,
     Disponibilidad bit,
     Tipo varchar(15),
    primary key(Numero_Habitaciones)
)

create table recepcionista(
    Id_Empleado int not null,
    Nombre_R varchar(30),
    AP_R varchar(30),
    AM_R varchar(30),
    Turno varchar(30),
    primary key(Id_Empleado)
)



create table cliente(
	Id_Cliente int not null,
    NombreC varchar(30),
    AP_C varchar (30),
    AM_M varchar(30),
    TCel_C int,
    TCasa_C int,
    Cantidad_Personas int,
    Id_Ciudad int,
    Id_Estado int,
    Id_Pais int,
    Numero_Habitaciones int,
	primary key(Id_Cliente),
    FOREIGN KEY(Numero_Habitaciones) references habitaciones(Numero_Habitaciones),
	Foreign key(Id_Pais) references pais (Id_Pais),
	Foreign key(Id_Estado) references estado(Id_Estado),
    Foreign key (Id_Ciudad) references ciudad(Id_Ciudad)
)


create table reservaciones(
    Id_Reservacion int not null,
    Fecha_Reservacion date,
    Fecha_Entrada date,
    Fecha_Salida date,
    Total float,
    Subtotal float,
    Id_Cliente int not null,
    Id_Empleado int not null,
    primary key(Id_Reservacion),
    FOREIGN KEY (Id_Empleado)references recepcionista (Id_Empleado),
    FOREIGN KEY (Id_Cliente) references cliente (Id_Cliente)
)

--insert normal
insert into recepcionista(Id_Empleado,Nombre_R,AP_R,AM_R,Turno)values (1,'sara','sanchez','perez','matutino')
insert into recepcionista(Id_Empleado,Nombre_R,AP_R,AM_R,Turno)values (2,'Juliana','Montes','Gonzalez','Matutino')
insert into recepcionista(Id_Empleado,Nombre_R,AP_R,AM_R,Turno)values (5,'Daniel','Morales','Gomez','Vespertino')
insert into recepcionista(Id_Empleado,Nombre_R,AP_R,AM_R,Turno)values (6,'Juan','De Corona','Montes','Vespertino')

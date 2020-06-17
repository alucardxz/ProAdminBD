use HotelS
----------------------------***********************++PAIS++**************--------------------------------------
CREATE PROCEDURE PAISN @Id_Pais int ,
     @Nombre_P varchar(20),
	@msg AS VARCHAR(100) OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	Begin Tran Tad
	  Begin Try
        INSERT INTO dbo.pais(Id_Pais,Nombre_P) VALUES (@Id_Pais,@Nombre_P)
        SET @msg = ' se registro correctamente.'
		print @msg
        COMMIT TRAN Tad

    End try
    Begin Catch
        SET @msg = 'Ocurrio un Error: ' + ERROR_MESSAGE() + ' en la línea ' + CONVERT(NVARCHAR(255), ERROR_LINE() ) + '.'
		print @msg
        Rollback TRAN Tad

    End Catch

END
GO
create procedure ConsultarPai @Id_Pais int
as
	begin
		select * from pais where 
		Id_Pais= @Id_Pais
	end
go
--fin 
---
-------------------------------**********************+ESTADO+*---------------------------
CREATE PROCEDURE EstadoN @Id_Estado int ,
     @Nombre_E varchar(20),
     @Id_Pais int ,
	@msg AS VARCHAR(100) OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	Begin Tran Tad
	  Begin Try
        INSERT INTO dbo.estado(Id_Estado,Nombre_E,Id_Pais) VALUES (@Id_Estado,@Nombre_E,@Id_Pais)
        SET @msg = ' se registro correctamente.'
		print @msg
        COMMIT TRAN Tad

    End try
    Begin Catch
        SET @msg = 'Ocurrio un Error: ' + ERROR_MESSAGE() + ' en la línea ' + CONVERT(NVARCHAR(255), ERROR_LINE() ) + '.'
		print @msg
        Rollback TRAN Tad

    End Catch

END
GO
create procedure ConsultarEstado @Id_Estado int
as
	begin
		select * from estado where 
		Id_Estado= @Id_Estado
	end
go
------------------------***********************+CIUDAD+******************************-------------------
CREATE PROCEDURE CiudadN @Id_Ciudad int ,
  @Nombre_C varchar(20),
  @Id_Estado int,
	@msg AS VARCHAR(100) OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	Begin Tran Tad
	  Begin Try
        INSERT INTO dbo.ciudad(Id_Ciudad ,Nombre_C,Id_Estado) VALUES (@Id_Ciudad,@Nombre_C,@Id_Estado)
        SET @msg = ' se registro correctamente.'
		print @msg
        COMMIT TRAN Tad

    End try
    Begin Catch
        SET @msg = 'Ocurrio un Error: ' + ERROR_MESSAGE() + ' en la línea ' + CONVERT(NVARCHAR(255), ERROR_LINE() ) + '.'
		print @msg
        Rollback TRAN Tad

    End Catch

END
GO
create procedure ConsultarCiudad @Id_Ciudad int
as
	begin
		select * from ciudad where 
		Id_Ciudad= @Id_Ciudad
	end
go
--------------------------------*****************Habitacion***************-------------------------------------
CREATE PROCEDURE habitacionN @Numero_Habitaciones int,
     @Precio float,
     @Disponibilidad bit,
     @Tipo varchar(15),
	@msg AS VARCHAR(100) OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	Begin Tran Tad
	  Begin Try
        INSERT INTO dbo.habitaciones(Numero_Habitaciones,Precio,Disponibilidad,Tipo) VALUES (@Numero_Habitaciones,@Precio,@Disponibilidad,@Tipo)
        SET @msg = ' se registro correctamente.'
		print @msg
        COMMIT TRAN Tad

    End try
    Begin Catch
        SET @msg = 'Ocurrio un Error: ' + ERROR_MESSAGE() + ' en la línea ' + CONVERT(NVARCHAR(255), ERROR_LINE() ) + '.'
		print @msg
        Rollback TRAN Tad

    End Catch

END
GO
create procedure ConsultarHabitaciones @Id_Habitacione int
as
	begin
		select * from habitaciones where 
		Numero_Habitaciones= @Id_Habitacione
	end
go
---------------------------------------------------------*******recepcionista**************-----------------------
CREATE PROCEDURE recepcionistaN @Id_Empleado int,
    @Nombre_R varchar(30),
    @AP_R varchar(30),
    @AM_R varchar(30),
    @Turno varchar(30),
	@msg AS VARCHAR(100) OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	Begin Tran Tad
	  Begin Try
        INSERT INTO dbo.recepcionista(Id_Empleado,Nombre_R,AP_R,AM_R,Turno) VALUES (@Id_Empleado,@Nombre_R,@AP_R,@AM_R,@Turno)
        SET @msg = ' se registro correctamente.'
		print @msg
        COMMIT TRAN Tad

    End try
    Begin Catch
        SET @msg = 'Ocurrio un Error: ' + ERROR_MESSAGE() + ' en la línea ' + CONVERT(NVARCHAR(255), ERROR_LINE() ) + '.'
		print @msg
        Rollback TRAN Tad

    End Catch

END
GO
create procedure ConsultarRecepcionista @Id_Recepcionista int
as
	begin
		select * from recepcionista where 
		Id_Empleado=@Id_Recepcionista
	end
go
--------------------------------------********************cliente******************--------------------------------------------
CREATE PROCEDURE clienteN @Id_Cliente int,
    @NombreC varchar(30),
    @AP_C varchar (30),
    @AM_M varchar(30),
    @TCel_C int,
    @TCasa_C int,
    @Cantidad_Personas int,
    @Id_Ciudad int,
    @Id_Estado int,
    @Id_Pais int,
    @Numero_Habitaciones int,
	@msg AS VARCHAR(100) OUTPUT
AS

BEGIN
	SET NOCOUNT ON;
	Begin Tran Tad
	  Begin Try
        INSERT INTO dbo.cliente(Id_Cliente,NombreC,AP_C,AM_M,TCel_C,TCasa_C,Cantidad_Personas,Id_Ciudad,Id_Estado,Id_Pais,Numero_Habitaciones ) VALUES (@Id_Cliente,@NombreC,@AP_C,@AM_M,@TCel_C,@TCasa_C,@Cantidad_Personas,@Id_Ciudad,@Id_Estado,@Id_Pais,@Numero_Habitaciones)
        SET @msg = ' se registro correctamente.'
		print @msg
        COMMIT TRAN Tad

    End try
    Begin Catch
        SET @msg = 'Ocurrio un Error: ' + ERROR_MESSAGE() + ' en la línea ' + CONVERT(NVARCHAR(255), ERROR_LINE() ) + '.'
		print @msg
        Rollback TRAN Tad

    End Catch

END
GO
create procedure ConsultarCliente @Id_Cliente int
as
	begin
		select Id_Cliente,NombreC from cliente where 
		Id_Cliente=@Id_Cliente
	end
go
-----------------------------------------*****************reservacion***********************---------------------------------
CREATE PROCEDURE recervacioneN @Id_Reservacion int,
    @Fecha_Reservacion date,
    @Fecha_Entrada date,
    @Fecha_Salida date,
    @Total float,
    @Subtotal float,
    @Id_Cliente int,
    @Id_Empleado int,
	@msg AS VARCHAR(100) OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	Begin Tran Tad
	  Begin Try
        INSERT INTO dbo.reservaciones(Id_Reservacion,Fecha_Reservacion,Fecha_Entrada,Fecha_Salida,Total,Subtotal,Id_Cliente,Id_Empleado) VALUES (@Id_Reservacion,@Fecha_Reservacion,@Fecha_Entrada,@Fecha_Salida,@Total,@Subtotal,@Id_Cliente,@Id_Empleado)
        SET @msg = ' se registro correctamente.'
		print @msg
        COMMIT TRAN Tad

    End try
    Begin Catch
        SET @msg = 'Ocurrio un Error: ' + ERROR_MESSAGE() + ' en la línea ' + CONVERT(NVARCHAR(255), ERROR_LINE() ) + '.'
		print @msg
        Rollback TRAN Tad

    End Catch

END
GO
create procedure ConsultarReservacione @Id_Reservacion int
as
	begin
		select * from reservaciones where 
		Id_Reservacion=@Id_Reservacion
	end
go
--procedimiento que haga un insert,select, update,delete.
create PROCEDURE Paisinsertupdatedelete  @Id_Pais int ,
										@Nombre_P varchar(20),
                                          @StatementType NVARCHAR(20) 
AS  
  BEGIN  
      IF @StatementType = 'Insert'  
        BEGIN  
             INSERT INTO dbo.pais(Id_Pais,Nombre_P) VALUES (@Id_Pais,@Nombre_P) 
        END  
  
      IF @StatementType = 'Select'  
        BEGIN  
            SELECT * FROM   pais
        END  
  
      IF @StatementType = 'Update'  
        BEGIN  
            UPDATE pais
            SET    Nombre_P=@Nombre_P
            WHERE  Id_Pais = @Id_Pais 
        END  
      ELSE IF @StatementType = 'Delete'  
        BEGIN  
            DELETE FROM pais
            WHERE  Id_Pais = @Id_Pais 
        END  
  END   
create PROCEDURE Estadoinsertupdatedelete @Id_Estado int ,
										  @Nombre_E varchar(20),
										  @Id_Pais int,
                                          @StatementType NVARCHAR(20) 
AS  
  BEGIN  
      IF @StatementType = 'Insert'  
        BEGIN  
             INSERT INTO dbo.estado(Id_Estado,Nombre_E,Id_Pais) VALUES (@Id_Estado,@Nombre_E,@Id_Pais)
        END  
  
      IF @StatementType = 'Select'  
        BEGIN  
            SELECT * FROM  estado
        END  
  
      IF @StatementType = 'Update'  
        BEGIN  
            UPDATE estado
            SET    Nombre_E=@Nombre_E,
				   Id_Pais = @Id_Pais
            WHERE  Id_Estado = @Id_Estado 
        END  
      ELSE IF @StatementType = 'Delete'  
        BEGIN  
            DELETE FROM estado
            WHERE  Id_Estado = @Id_Estado
        END  
  END   
go

create PROCEDURE CDinsertupdatedelete @Id_Ciudad int ,
										  @Nombre_C varchar(20),
										  @Id_Estado int,
                                          @StatementType NVARCHAR(20) 
AS  
  BEGIN  
      IF @StatementType = 'Insert'  
        BEGIN  
             INSERT INTO dbo.ciudad(Id_Ciudad,Nombre_C,Id_Estado) VALUES (@Id_Ciudad,@Nombre_C,@Id_Estado)
        END  
  
      IF @StatementType = 'Select'  
        BEGIN  
            SELECT * FROM ciudad
        END  
  
      IF @StatementType = 'Update'  
        BEGIN  
            UPDATE ciudad
            SET    Nombre_C =@Nombre_C,
				   Id_Estado = @Id_Estado
            WHERE  Id_Estado = @Id_Estado 
        END  
      ELSE IF @StatementType = 'Delete'  
        BEGIN  
            DELETE FROM ciudad
            WHERE  Id_Ciudad = @Id_Ciudad
        END  
  END   
  go
  
create PROCEDURE Habitacioninsertupdatedelete  @Numero_Habitaciones int,
     @Precio float,
     @Disponibilidad bit,
     @Tipo varchar(15),
	 @StatementType NVARCHAR(20) 

AS  
  BEGIN  
      IF @StatementType = 'Insert'  
        BEGIN  
            INSERT INTO dbo.habitaciones(Numero_Habitaciones,Precio,Disponibilidad,Tipo) VALUES (@Numero_Habitaciones,@Precio,@Disponibilidad,@Tipo)
        END  
  
      IF @StatementType = 'Select'  
        BEGIN  
            SELECT * FROM habitaciones
        END  
  
      IF @StatementType = 'Update'  
        BEGIN  
            UPDATE habitaciones
            SET    Precio=@Precio,
				   Disponibilidad=@Disponibilidad,
				   Tipo=@Tipo
            WHERE  Numero_Habitaciones = @Numero_Habitaciones
        END  
      ELSE IF @StatementType = 'Delete'  
        BEGIN  
            DELETE FROM habitaciones
            WHERE  Numero_Habitaciones = @Numero_Habitaciones
        END  
  END   
  go
  create PROCEDURE Recepcionistainsertupdatedelete  @Id_Empleado int,
    @Nombre_R varchar(30),
    @AP_R varchar(30),
    @AM_R varchar(30),
    @Turno varchar(30),
	 @StatementType NVARCHAR(20) 

AS  
  BEGIN  
      IF @StatementType = 'Insert'  
        BEGIN  
		INSERT INTO dbo.recepcionista(Id_Empleado,Nombre_R,AP_R,AM_R,Turno) VALUES (@Id_Empleado,@Nombre_R,@AP_R,@AM_R,@Turno)
           END  
  
      IF @StatementType = 'Select'  
        BEGIN  
            SELECT * FROM recepcionista
        END  
  
      IF @StatementType = 'Update'  
        BEGIN  
            UPDATE recepcionista
            SET    Nombre_R=@Nombre_R,
					AP_R=@AP_R,
					AM_R=@AM_R,
					Turno=@Turno
            WHERE  Id_Empleado = @Id_Empleado
        END  
      ELSE IF @StatementType = 'Delete'  
        BEGIN  
            DELETE FROM recepcionista
            WHERE  Id_Empleado = @Id_Empleado
        END  
  END   
  go
  create PROCEDURE Clienteinsertupdatedelete   @Id_Cliente int,
    @NombreC varchar(30),
    @AP_C varchar (30),
    @AM_M varchar(30),
    @TCel_C int,
    @TCasa_C int,
    @Cantidad_Personas int,
    @Id_Ciudad int,
    @Id_Estado int,
    @Id_Pais int,
    @Numero_Habitaciones int,
	 @StatementType NVARCHAR(20) 

AS  
  BEGIN  
      IF @StatementType = 'Insert'  
        BEGIN  
		  INSERT INTO dbo.cliente(Id_Cliente,NombreC,AP_C,AM_M,TCel_C,TCasa_C,Cantidad_Personas,Id_Ciudad,Id_Estado,Id_Pais,Numero_Habitaciones ) VALUES (@Id_Cliente,@NombreC,@AP_C,@AM_M,@TCel_C,@TCasa_C,@Cantidad_Personas,@Id_Ciudad,@Id_Estado,@Id_Pais,@Numero_Habitaciones)
           END  
  
      IF @StatementType = 'Select'  
        BEGIN  
            SELECT * FROM cliente
        END  
  
      IF @StatementType = 'Update'  
        BEGIN  
            UPDATE cliente
            SET    NombreC=@NombreC,
					AP_C=@AP_C,
					AM_M=@AM_M,
					TCel_C=@TCel_C,
					TCasa_C=@TCasa_C,
					Cantidad_Personas=@Cantidad_Personas,
					Id_Ciudad=@Id_Ciudad,
					Id_Estado=@Id_Estado,
					Id_Pais=@Id_Pais,
					Numero_Habitaciones=@Numero_Habitaciones
            WHERE  Id_Cliente = @Id_Cliente
        END  
      ELSE IF @StatementType = 'Delete'  
        BEGIN  
            DELETE FROM cliente
            WHERE  Id_Cliente = @Id_Cliente
        END  
  END   
  go
  create PROCEDURE reservainsertupdatedelete  @Id_Reservacion int,
    @Fecha_Reservacion date,
    @Fecha_Entrada date,
    @Fecha_Salida date,
    @Total float,
    @Subtotal float,
    @Id_Cliente int,
    @Id_Empleado int,
	 @StatementType NVARCHAR(20) 

AS  
  BEGIN  
      IF @StatementType = 'Insert'  
        BEGIN  
		   INSERT INTO dbo.reservaciones(Id_Reservacion,Fecha_Reservacion,Fecha_Entrada,Fecha_Salida,Total,Subtotal,Id_Cliente,Id_Empleado) VALUES (@Id_Reservacion,@Fecha_Reservacion,@Fecha_Entrada,@Fecha_Salida,@Total,@Subtotal,@Id_Cliente,@Id_Empleado)
        END  
  
      IF @StatementType = 'Select'  
        BEGIN  
            SELECT * FROM reservaciones
        END  
  
      IF @StatementType = 'Update'  
        BEGIN  
            UPDATE reservaciones
            SET    Fecha_Reservacion=@Fecha_Reservacion,
				Fecha_Entrada=@Fecha_Entrada,
				Fecha_Salida=@Fecha_Salida,
				Total=@Total,
				Subtotal=@Subtotal,
				Id_Cliente=@Id_Cliente,
				Id_Empleado=@Id_Empleado
            WHERE  Id_Reservacion= @Id_Reservacion
        END  
      ELSE IF @StatementType = 'Delete'  
        BEGIN  
            DELETE FROM reservaciones
            WHERE Id_Reservacion= @Id_Reservacion
        END  
  END   
  go

  --vista que solo muestre los nombres de los clientes con fecha de ingreso de hoy
  create view clienteFentraH
  as
    select c.NombreC, c.AP_C, c.AM_M 
	from cliente c ,reservaciones r where r.Id_Cliente=c.Id_Cliente and r.Fecha_Entrada=getdate();
  go
select * from clienteFentraH
--vista que solo muestre los nombres de los clientes con fecha de salida de hoy
create view clienteFsaleH
  as
    select c.NombreC, c.AP_C, c.AM_M 
	from cliente c ,reservaciones r where r.Id_Cliente=c.Id_Cliente and r.Fecha_Salida=getdate();
  go

--vista q muestre los nombres de las recepcionistas con turno matutino
create view Re_TM
  as
    select Nombre_R
	from recepcionista where Turno like '%[Mm]atutino%' 
  go
--vista q muestre los nombres de las recepcionistas con turno vespertino
create view Re_TV
  as
    select Nombre_R
	from recepcionista where Turno like '%[Vv]espertino%' 
  go

-----ejemplos exec ejecutar proc
-- Id_Pais int,varchar,msg
exec PAISN 1,Mexico,hola 
------Id_Estado int,nombre varchar,Id_Pais int
exec EstadoN 1,Jalisco,1,holis
exec EstadoN 2,CaliforniaNorte,1,holis
------Id_Ciudad int,nombre varchar,Id_Estado int
exec CiudadN 1,Zapotiltic,1,hola
exec CiudadN 2,Guzman,1,hola
---numero_habitacion int,precio float,disponibilidad (1,0),tipo varchar,msg
exec habitacionN 1,299.99,1,suite,hola
exec habitacionN 2,399.99,1,imperial,hola
--- id_empleado int,nombre varchar,apellido varchar, apellido varchar,turno,@msg
exec recepcionistaN 7,Maria,Gutierrez,Sanchez,Matutino,hola 
---Id_cliente int,nombre varchar,apellido varchar, apellido varchar,telcel_c,tcasa_c,cantidad_personas int,Id_Ciudad int,Id_Estado,Id_Pais,numero_habitacion int,@msg
exec clienteN 1,juan,lares,montes,341,410,4,1,2,1,2,hola
exec clienteN 2,Martina,gomez,deReal,341,410,4,1,2,1,2,hola
---reservacion
exec recervacioneN 1,'05/09/20','05/09/20','06/05/20',90000.99,10000.0,1,1,hola 
exec recervacioneN 2,'07/06/20','06/06/20','07/06/20',90000.99,10000.0,2,5,hola 
select * from clienteFsaleH
select * from clienteFentraH
select * from Re_TM
select * from Re_TV
 --------------------------------------
 
use master
  backup database [HotelS]
  to disk ='D\respaldps'
  with checksum;


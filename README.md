# Integrantes del Grupo: 

-De Rivas Pablo

-Lombardi Simon

# Uso de la aplicacion

Debe crearse un archivo .env basado en .env.sample

Utilizamos el comando:

`cp .env.sample .env`

Y ponemos nuestras variables

# Creacion de la imagen

`sudo docker-compose build`

# Corriendo el contenedor

`sudo docker-compose up`

# Una vez corriendo:

La aplicacion funciona con el puerto 5005, para entrar a la pagina entraremos a localhost:5005 desde nuestro navegador para poder ver templates o usando thunder client para trabajar con metodos get, put, delete o post.

La aplicacion fue creada en un principio con templates, pero debido a la nueva consigna de solo trabajar con los Methodviews de las operaciones nombradas recientemente. Puede que los templates en las desde navegador fallen.

# Descripcion de aplicacion
Aplicacion destinada a funcionar de blog basado en el framework flask, actualizada para utilizar Marshmallow y MethodView.

Hemos recreado la aplicacion utilizando una arquitectura mas ordenada, utilizando modelos, esquemas y views.

Se crearon 4 modelos, esquemas y rutas principales de la aplicacion.

# Login:

  -Los usuarios deben ingresar un bearer token para demostrar que estan logeados.
  
  -Este se consigue en la ruta 'login' en la cual usamos autenticación básica para ingresar nuestro usuario y contraseña y recibir el dicho token.


Para ver, crear, modificar y borrar la informacion de los esquemas usaremos los metodos get, post, put y delete respectivamente.


# Usuario:

  -Lo veremos en la ruta '/usuario' o '/usuario/id' para ver a un usuario en especifico y es manejado por UsuarioAPI. Para ver y crear usuarios no necesitaremos estar logeados, pero si para modificar y borrar (es necesario estar logeado como el usuario o como administrador para estos dos casos).

# Post:

  -Ruta 'post' o 'post/id' y es manejado por PostAPI. Para crear, modificar y borrar posts deberemos estar logeados. Un administrador puede borrar pero no modificar posts de otros usuarios.

# Comentario

  -Ruta 'comentario' o 'comentario/id' y es manejado por ComentarioAPI. Para crear, modificar y borrar comentarios deberemos estar logeados. Un administrador puede borrar pero no modificar comentarios de otros usuarios.
  
# Categoria:

  -Ruta 'categoria' o 'categoria/id' y es manejado por CategoriaAPI. Para crear, modificar y borrar categorias deberemos estar logeados y ser administradores, los usuarios comunes no pueden hacer nada de esto.


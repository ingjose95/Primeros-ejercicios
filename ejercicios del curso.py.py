# for i in range(1,100,2):
#     print(i, end=',')







# contador=0

# clave=input('Por favor, ingrese su contraseña: ')

# for i in range(len(clave)):

#     if clave[i]==' ':

#         contador=contador+1

# if contador==1 or len(clave)<8:

#     print('La contraseña ingresada es incorrecta')

# else:

#     print('La contraseña es correcta')




# contadorArroba=0
# contadorPunto=0

# correo=input('Ingrese su correo electrónico: ')

# for x in range(len(correo)):

#     if correo[x]=='@':

#         contadorArroba=contadorArroba+1

#     if correo[x]=='.':

#         contadorPunto=1

# if contadorArroba!=1 or contadorPunto==0:

#     print('El correo ingresado es incorrecto')

# else:

#     print('El correo ingresado es correcto')




contadorClave=0
contadorArroba=0
contadorPunto=0

correo=input('Ingrese su correo eletrónico: ')
clave=input('Ingrese su contraseña: ')

for i in range(len(correo)):

    if correo[i]=='@':

        contadorArroba=contadorArroba+1

    if correo[i]=='.':

        contadorPunto=1

for y in range(len(clave)):

    if clave[y]==' ':

        contadorClave=contadorClave+1

if contadorArroba!=1 or contadorPunto==0 or contadorClave==1 or len(clave)<8:
    
    print('Los datos ingresados son incorrectos')

else:

    print('Los datos ingresados son correctos')

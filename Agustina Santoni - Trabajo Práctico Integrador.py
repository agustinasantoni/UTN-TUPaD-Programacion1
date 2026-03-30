#Ejercicio 1

total_sin_descuentos = 0
total_con_descuentos = 0
total_ahorrado = 0
descuento = 0 #creé las variables a utilizar con igualdad a 0 para poder realizar el conteo al finalizar el código.

while True:
    nombre_cliente = input("Por favor, ingrese su nombre: ").strip() #se utiliza strip para eliminar espacios o caracteres al principio y al final del string.
    if (nombre_cliente.replace(" ", "").isalpha() and nombre_cliente != ""): #se utiliza replace para remplazar una parte del texto con otra, e isalpha para comprobar que el texto solo tiene letras.
         print(f"Bienvenido/a {nombre_cliente}! ")
         break
    else:
         print("Error, por favor ingrese su nombre nuevamente sin números o campos vacíos. ")
while True:
     cant_productos_str = input("¿Cuantos productos desea comprar? ").strip()
     if(cant_productos_str.isdigit() and cant_productos_str != "" and int(cant_productos_str) > 0): #utilizé isdigit para condicionar que si el usuario ingreso correctamente un número realice el print utilizado y luego el break.
          cant_productos_int = int(cant_productos_str) #diferencié las variables en string y las variables en int para utilizarlas correctamente.
          print(f"Cantidad de productos ({cant_productos_int}) cargados con éxito. ")
          break
     else:
          print("Por favor, ingrese la cantidad de productos en números. ")
for i in range(cant_productos_int):
     while True: #utilizé el "while True" dentro del ciclo for para validar los productos dentro del bucle.
          precio_prod_str = input(f"Por favor, ingrese el precio del producto {i + 1}: ").strip()
          if(precio_prod_str.replace(".", "").isdigit() and precio_prod_str != "" and float(precio_prod_str) > 0): #utilizé el replace para validar que el dato sea un número con el isdigit para luego usar el valor original de la variables con el float.
               precio_prod_fl =  float(precio_prod_str)
               total_sin_descuentos += precio_prod_fl # += acumula la variable
               print("Precio ingresado con éxito. ")
               break
          else:
               print("Por favor, ingrese el precio en números. ")     
     while True:
          desc_producto = input("¿Su producto tiene descuento?: S/N ").upper().strip() #valido con el upper que sin importar el formato que ingrese el usuario me lo va a tomar correctamente.
          if (desc_producto in "SN"): #utilizo el if para colocar el break una sola vez y no en cada case.
               match desc_producto:
                    case "S":
                         print("¡Se aplicó el %10 de descuento a su producto!")
                    case "N":
                         print("Su producto no tiene descuento. ")
               break
          else:
               print("Por favor, ingrese una opción correcta. ")
     if desc_producto == "S":
          descuento = precio_prod_fl * 0.10 #ejecuté los descuentos dentro del for para sumarlos en cada producto y que no se haga una sola vez.
     else:
          descuento = 0
     total_con_descuentos += precio_prod_fl - descuento
     total_ahorrado += descuento

print(f"Total sin descuentos: ${total_sin_descuentos} ")
print(f"Total con descuentos ${total_con_descuentos:.2f} ")
print(f"Ahorro: ${total_ahorrado:.2f} ")

promedio_productos = total_con_descuentos / cant_productos_int #promedio de los productos lo agregúe al final para hacer las cuentas ya con los descuentos aplicados.

print(f"Promedio por producto: ${promedio_productos:.2f} ")

#Ejercicio 2

usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 3
opcion_str = "0"
while(intentos):
     usuario = input("Por favor, ingrese el usuario: ").strip()
     clave = input("Por favor, ingrese la clave: ").strip()
     if(usuario == usuario_correcto and clave == clave_correcta): #condicioné con el and para que se ejecute solo si las dos condiciones son verdaderas.
          print("Ha iniciado sesión. ")
          break
     else:
          intentos -= 1
          print("Usuario y/o clave incorrecto. ")
          if(intentos == 0):
               print("Cuenta bloqueada. ")
          else:
               print(f"Le quedan {intentos} intentos. ")
while(opcion_str != 4 and intentos != 0):
     print("\n" + "=" * 50)
     print('''1. Ver estado de inscripción. 
2. Cambiar clave.
3. Mostrar mensaje motivacional.
4. Salir''')
     print("=" * 50)
     opcion_str = input("Por favor, ingrese una opción: ").strip()
     if opcion_str.isdigit():
          opcion = int(opcion_str) #convierto la variables para poder compararlas en formato int.
     else:
          print("Por favor, ingrese una opción correcta. ")
          continue
     if opcion < 1 or opcion > 4:
          print("Opción fuera de rango. ")
          continue
     match opcion:
          case 1:
               print("Inscripto. ")
          case 2:
               while True:
                    nueva_clave = input("Ingrese su nueva clave (debe contener como mínimo 6 caracteres): ").strip()
                    if len(nueva_clave) < 6: #corroboré con len que solo contenga más de 6 caracteres para que ejecute.
                         print("Su clave ha sido rechazada, contiene menos de 6 caracteres. ")
                         continue
                    conf_clave = input("Ingrese nuevamente la clave para confirmar (las claves deben coincidir): ").strip()
                    if nueva_clave != conf_clave:
                         print("Error las contraseñas no coinciden, intente nuevamente. ")
                    else:
                         clave_correcta = nueva_clave
                         print("¡Su clave ha sido cambiada con éxito!")
                         break
          case 3:
               print("Elige un trabajo que ames, y no tendrás que trabajar un solo día de tu vida. ")
          case 4:
               print("Usted a salido del menú. ")
               break
          case _:
               print("Opción inválida, intente nuevamente. ")

#Ejercicio 3         

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while True:
     nombre_operador = input("Por favor, ingrese su nombre completo: ").strip()
     if nombre_operador.replace(" ", "").isalpha() and nombre_operador != "":
          break
     else:
          print("Error, por favor ingrese solo letras. ")
opcion = 0
while(opcion != 5):
     print("\n" + "=" * 50)
     print('''1. Reservar turno. 
2. Cancelar turno (por nombre).
3. Ver agenda del día.
4. Ver resumen general.
5. Cerrar sistema.''')
     print("=" * 50)
     opcion_str = input("Por favor, ingrese una opción: ").strip()
     if opcion_str.isdigit():
          opcion = int(opcion_str)
     else:
          print("Por favor, ingrese una opción correcta. ")
          continue
     if opcion < 1 or opcion > 5: #utilizé or para corroborar que se encuentre dentro del rango.
          print("Opción fuera de rango. ")
          continue
     match opcion:
          case 1:
               dia = input("Por favor, elija un día: (1. Lunes / 2. Martes). ")
               if not dia.isdigit():
                    print("Por favor, ingrese un número válido. ")
                    continue
               dia = int(dia)
               if dia not in (1, 2):
                    print("Día inválido")
                    continue
               nombre = input("Por favor, ingrese el numbre del paciente: ").strip()
               if not nombre.replace(" ", "").isalpha() or nombre == "":
                    print("Error, ingrese el nombre solo con letras. ")
                    continue
               if dia == 1:
                    if nombre in (lunes1, lunes2, lunes3, lunes4):
                         print("Paciente ya registrado. ")
                         continue
               if dia == 2:
                    if nombre in (martes1, martes2, martes3):
                         print("Paciente ya registrado. ")
                         continue
               if dia == 1:
                    if lunes1 == "":
                              lunes1 = nombre
                    elif lunes2 == "":
                              lunes2 = nombre
                    elif lunes3 == "":
                              lunes3 = nombre
                    elif lunes4 == "":
                              lunes4 = nombre
                    else:
                         print("¡Todos los turnos del día Lunes se encuentran ocupados, por favor elija otro día! ")
                         continue
               if dia == 2:
                    if martes1 == "":
                              martes1 = nombre
                    elif martes2 == "":
                              martes2 = nombre
                    elif martes3 == "":
                              martes3 = nombre
                    else:
                         print("¡Todos los turnos del día Martes se encuentran ocupados, por favor elija otro día! ")
                         continue
               print("Su turno ha sido reservado con éxito. ")
          case 2:
               dia = input("Por favor, elija el día: (1. Lunes / 2. Martes) ")
               if not dia.isdigit():
                       print("Por favor, ingrese un número válido. ")
                       continue
               dia = int(dia)
               if dia not in (1, 2):
                    print("Día inválido")
                    continue
               nombre = input("Ingrese el nombre del paciente que desea cancelar: ").strip()
               if dia == 1:
                    if not nombre in (lunes1, lunes2, lunes3, lunes4):
                         print("Paciente no registrado. ")
                         continue
                    if nombre == lunes1:
                         lunes1 = ""
                    elif nombre == lunes2:
                         lunes2 = ""
                    elif nombre == lunes3:
                         lunes3 = ""
                    elif nombre == lunes4:
                         lunes4 = ""
               if dia == 2:
                    if not nombre in (martes1, martes2, martes3):
                         print("Paciente no registrado. ")
                         continue
                    if nombre == martes1:
                         martes1 = ""
                    elif nombre == martes2:
                         martes2 = ""
                    elif nombre == martes3:
                         martes3 = ""
               print("Su turno a sido cancelado con éxito. ")
          case 3:
               dia = input("Por favor, elija el día que desea ver la agenda: (1. Lunes / 2. Martes) ")
               if not dia.isdigit():
                       print("Por favor, ingrese un número válido. ")
                       continue
               dia = int(dia)
               if dia not in (1, 2):
                    print("Día inválido")
                    continue
               if dia == 1:
                    print("Lunes: ")
                    print("1: ", lunes1 if lunes1 != "" else "(Libre)")
                    print("2: ", lunes2 if lunes2 != "" else "(Libre)")
                    print("3: ", lunes3 if lunes3 != "" else "(Libre)")
                    print("4: ", lunes4 if lunes4 != "" else "(Libre)")
                    continue
               if dia == 2:
                    print("Martes: ")
                    print("1: ", martes1 if martes1 != "" else "(Libre)")
                    print("2: ", martes2 if martes2 != "" else "(Libre)")
                    print("3: ", martes3 if martes3 != "" else "(Libre)")
          case 4:
               ocup_lunes = 0
               ocup_martes = 0
               if lunes1 != "": ocup_lunes += 1
               if lunes2 != "": ocup_lunes += 1
               if lunes3 != "": ocup_lunes += 1
               if lunes4 != "": ocup_lunes += 1

               if martes1 != "": ocup_martes += 1
               if martes2 != "": ocup_martes += 1
               if martes3 != "": ocup_martes += 1

               print("Lunes:", ocup_lunes, "ocupados,", 4 - ocup_lunes, "libres")
               print("Martes:", ocup_martes, "ocupados,", 3 - ocup_martes, "libres")

               if ocup_lunes > ocup_martes:
                    print("Día con más turnos: Lunes")
               elif ocup_martes > ocup_lunes:
                    print("Día con más turnos: Martes")
               else:
                    print("Empate")
          case 5:
               print("Cerrando sistema... ")

#Ejercicio 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_cerradura = 0
while True:
     nombre_agente = input("Por favor, ingrese su nombre: ").strip()
     if nombre_agente.replace(" ", "").isalpha() and nombre_agente != "":
          print(f"¡Bienvenido/a agente {nombre_agente}! ")
          break
     else:
          print("Error, por favor ingrese solo letras. ")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print("-ESTADO ACTUAL-")
    print(f"Energía: {energia}. ")
    print(f"Tiempo: {tiempo}. ")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}. ")
    print(f"Alarma: {alarma}. ")

    print("\n" + "=" * 50)
    print('''1. Forzar cerradura (costo: -20 energía, -2 tiempo). 
2. Hackear panel (costo -10 energía, -3 tiempo).
3. Descansar (+15 energía, -1 tiempo).''')
    print("=" * 50)
    while True:
        opcion_str = input("Ingrese una opción (1 - 3): ").strip()
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            if 1 <= opcion <= 3:
                break
            else:
                print("Opción fuera de rango. ")
        else:
            print("Por favor, ingrese un número válido. ")
    match opcion:
        case 1:
            alarma_activada = False
            energia -= 20
            tiempo -= 2
            forzar_cerradura += 1
            if forzar_cerradura >= 3:
                alarma = True
                alarma_activada = True
                print("La cerradura ha sido trabada. Alarma activada. ")
            else:
                if energia < 40:
                    numero = input("Por favor, ingrese un número del 1 al 3: ")
                    while not numero.isdigit() or int(numero) not in (1, 2, 3):
                        numero = input("Error, ingrese un número del 1 al 3. ")
                    numero = int(numero)
                    if numero == 3: 
                        alarma = True
                        alarma_activada = True
                        print("La alarma ha sido activada. ")
            if not alarma_activada:
                cerraduras_abiertas += 1
                print("La cerradura ha sido abierta con éxito. ")
        case 2:
            energia -= 10
            tiempo -= 3
            forzar_cerradura = 0
            print("Hackeando panel... ")
            for i in range(4):
                print(f"Paso {i + 1}. ")
                codigo_parcial += "A"
            print(f"Código parcial: {codigo_parcial}. ")
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Cerradura abierta automáticamente. ")
        case 3:
            tiempo -= 1
            forzar_cerradura = 0
            if alarma:
                energia -= 10
                print("La alarma consume energía extra. ")
            energia += 15
            if energia > 100:
                energia = 100
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("El sistema se ha bloqueado por la activación de la alarma. ")
        break
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Has conseguido abrir la bóveda. ")
elif energia <= 0 or tiempo <= 0:
    print("¡DERROTA! Has agotado todos tus recursos. ")
else: 
    print("¡DERROTA! Se ha bloqueado el sistema. ") 

#Ejercicio 5

print("--- BIENVENIDO A LA ARENA DEL GLADIADOR --- ")

while True:
    nombre_gladiador = input("Por favor, ingrese su nombre: ").strip()
    if nombre_gladiador.replace(" ", "").isalpha() and nombre_gladiador != "":
        print(f"¡Bienvenido/a gladiador {nombre_gladiador}! ")
        break
    else:
        print("Error: Solo se permiten letras. ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
daño_pesado = 15
daño_enemigo = 12
turno_jugador = True 

print("=== INICIO DEL COMBATE === ")
while vida_jugador > 0 and vida_enemigo > 0:
    print("=== NUEVO TURNO ===  ")
    print(f"{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}. ") #HP: health points
    if turno_jugador:
        while True:
            print("Elija su acción: ")
            print("1. Ataque Pesado ")
            print("2. Ráfaga Veloz ")
            print("3. Curar ")
            opcion = input("Opción: ")
            if not opcion.isdigit():
                print("Error: Ingrese un número válido. ")
            elif int(opcion) < 1 or int(opcion) > 3:
                print("Error: Opción fuera de rango. ")
            else:
                opcion = int(opcion)
                break
        if opcion == 1:
            daño = daño_pesado
            if vida_enemigo < 20:
                daño = daño_pesado * 1.5  
                print("¡Golpe Crítico! ")
            vida_enemigo -= daño
            print(f"¡Atacaste al enemigo por {daño} puntos de daño! ")
        elif opcion == 2:
            print("¡Iniciaste una ráfaga de golpes! ")
            for i in range(3):
                vida_enemigo -= 5
                print("¡Golpe conectado por 5 de daño! ")
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Te curaste 30 puntos de vida! ")
            else:
                print("¡No quedan pociones! ")
        turno_jugador = False  
    else:
        vida_jugador -= daño_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño! ")
        turno_jugador = True  
print("=== FIN DEL COMBATE === ")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla. ")
else:
    print("DERROTA. Has caído en combate. ")
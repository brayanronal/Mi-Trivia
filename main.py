import random  # Importamos la librería random
import time # Importamos la librería 

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("\033[35m Bienvenido a mi trivia sobre Cultura General \033[39m" )
print ("\033[35m Pondremos a prueba tus conocimientos \033[39m")
print (MAGENTA+"Obtuviste", puntaje, "puntos"+RESET)

while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")

  nombre = input(WHITE+"Ingresa tu nombre: "+RESET)
  
  # Es importante dar instrucciones sobre cómo jugar:
  # Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
  print(MAGENTA+"\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
  
  # OJO, el \n al final de la línea 6 es para dar un "salto de línea"
  
  # Pregunta 1
  print (GREEN+"1) ¿En que año acabo la segunda guerra mundial ?"+RESET)
  print (YELLOW+"a) 1956"+RESET)
  print (YELLOW+"b) 1942"+RESET)
  print (YELLOW+"c) 1945"+RESET)
  print (YELLOW+"d) 1950"+RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input(RED+"\nTu respuesta: "+RESET)
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_1 == "c":
    puntaje += 10
    print (RED+"Muy bien", nombre, "!.", "La Segunda Guerra Mundial fue el conflicto bélico más importante del siglo XX. Entre 1939 y 1945"+RESET)
  else:
    puntaje -= 2
    print (YELLOW+"Incorrecto", nombre, "!","se te resto 2 puntos"+RESET)
  print(RED+nombre, "llevas", puntaje, "puntos"+RESET)
  
  time.sleep(3) # Espera 3 segundos antes de continuar.
    
  # Pregunta 2
  print(BLUE+"2) ¿Cuál es el país más grande del mundo?"+RESET)
  print(CYAN+"a) Mexico"+RESET)
  print(CYAN+"b) Estados Unidos"+RESET)
  print(CYAN+"c) China"+RESET)
  print(CYAN+"d) Rusia"+RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input(RED+"\nTu respuesta: "+RESET)
  
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_2 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
  elif respuesta_2 == "b":
    print ("Intentalo nuevamente! ...")
    puntaje = puntaje + 5
  elif respuesta_2 == "c":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
  else:
    print (RED+"Correcto!. Rusia es el país más grande del mundo con una superficie de 17 098 246 km²."+RESET)
    puntaje = puntaje * 2
  print(RED+nombre,"llevas", puntaje, "puntos"+RESET)
  
  time.sleep(3) # Espera 3 segundos antes de continuar.
  
  # Pregunta 3
  print(WHITE+"3) ¿Cuál es el río más largo del planeta?"+RESET)
  print(MAGENTA+"a) El Amazonas"+RESET)
  print(MAGENTA+"b) El Nilo"+RESET)
  print(MAGENTA+"c) El Yangtsé"+RESET)
  print(MAGENTA+"d) El Misisip"+RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input(RED+"\nTu respuesta: "+RESET)
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_3 == "b":
    print("Incorrecto!", nombre, "El Nilo es el segundo río más largo del planeta")
    puntaje = puntaje - 8
  elif respuesta_3 == "c":
    print("Incorrecto!", nombre, "El Yangtsé es el tercer río más largo del planeta")
    puntaje = puntaje * 3
  elif respuesta_3 == "d":
    print("Incorrecto!", nombre, "El Misisip es el cuarto río más largo del planeta")
    puntaje = puntaje / 3
  else:
    puntaje += 15
    print(RED+"Muy bien", nombre, "!","El Amazonas es el río más largo del planeta con 7.062 km². "+RESET)
  print(RED+nombre,"llevas", puntaje, "puntos"+RESET)
  time.sleep(3) # Espera 3 segundos antes de continuar.
  
 # Pregunta 4
  print(MAGENTA+"4) ¿Cuál es el continente más extenso del planeta?"+RESET)
  print(CYAN+"a) Asia"+RESET)
  print(CYAN+"b) America"+RESET)
  print(CYAN+"c) Europa"+RESET)
  print(CYAN+"d) África"+RESET)
  
 # Almacenamos la respuesta del usuario en la variable "respuesta_4"
  respuesta_4 = input(RED+"\nTu respuesta: "+RESET)
  
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
 # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_4 == "b":
    print("Incorrecto!", nombre, "America es el segundo más grandes con una extensión de 42 330 000 km²")
    puntaje = puntaje - 8
  elif respuesta_4 == "c":
    print("Incorrecto!", nombre, "Europa es el cuarto con una superficie de 10 180 000 km²")
    puntaje = puntaje * 3
  elif respuesta_4 == "d":
    print("Incorrecto!", nombre, "África es el tercer continente más grande de la tierra. Ocupa una extensión de 30 370 000 km²")
    puntaje = puntaje / 3
  else:
    puntaje += 20
    print(RED+"Muy bien", nombre, "!","Asia es el continente más grande de la tierra con 43 810 000 km². "+RESET)
  
  time.sleep(3) # Espera 3 segundos antes de continuar.
  
  print(YELLOW+"Gracias", nombre, "por jugar mi trivial, alcanzaste", puntaje, "puntos"+RESET)
  
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero", nombre,"que lo hayas disfrutado, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.

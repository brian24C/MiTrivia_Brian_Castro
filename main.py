import random, time


BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

for numero_carga in range(2,0,-1):

  if numero_carga==2:
  
    print (GREEN+"Bienvenido a mi trivia sobre programación"+RESET)
    tiempo=time.sleep(2)
    
  elif numero_carga==1:
    print ("\nVeremos cuánto sabes! vamos allá!")
    puntaje=random.randint(1,10)
    print(GREEN+"Comienzas con", puntaje, "puntos!!!\n"+RESET)
  
    tiempo=time.sleep(2)



nombre = input("Ingresa tu nombre: ")
print("\nHola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

iniciar_trivia = True
intentos=0

while iniciar_trivia == True:

  intentos+=1

  if intentos==1:
    print(CYAN+"\nIntento número:", intentos,RESET)
    input("Presiona Enter para continuar")
  else:
    puntaje=0
    print("\nIntento número:", intentos)
    print(GREEN+"Comienzas con", puntaje, "puntos\n"+RESET)
    input("Presiona Enter para continuar")
    
  print("\n-----------------------1ERA PREGUNTA-----------------------\n")
  print (RED+"1) Cuando nos referimos a la brecha digital estamos considerando:\n"+RESET)
  print (BLUE+"a) La dependencia de las nuevas tecnologías, que provocan aislamiento, soledad y pérdidas de tiempo")
  print ("b) La situación de desigualdad que se produce entre quienes tienen acceso a las TIC y quienes no lo tienen.")
  print ("c) Las dos opciones anteriores son correctas.")
  print ("d) Ninguna de las opciones anteriores es correcta."+RESET)
  
  
  print("\npiensa en tu respuesta, solo tienes 5 segundos\n")
  tiempo=time.sleep(5)
  respuesta_1 = input("Ingresa tu respuesta : ").lower()
  
  
  
  
  while respuesta_1 not in ("a", "b", "c", "d", "z",""):
    respuesta_1 = input(RED+"!!! Debes responder a, b, c o d !!! Ingresa nuevamente tu respuesta : "+RESET).lower()
    
  
  
  
  if respuesta_1 == "a":
    print ("Totalmente incorrecto!")
    puntaje = puntaje - 5
  elif respuesta_1 == "d":
    print ("muy cerca pero incorrecto")
    puntaje = puntaje + 2
  elif respuesta_1 == "c":
    print ("Incorrecto! ")
    puntaje = puntaje - 3
    
  elif respuesta_1 == "z":
    print ("Incorrecto! la respuesta es la ´b´\n"+GREEN+
           "PERO HAZ ESCRITO ´Z´ ENCONTRASTE LA LETRA SECRETA!"
           "por eso se te sumarán la cantidad de tu quieras" )
    puntaje=int(input("ingresa la cantidad de puntos que quieras: "))
    puntaje = puntaje
  
  else:
    print ("Correcto!")
    puntaje = puntaje + 10
  
  print(GREEN+"Tu puntaje hasta ahora es:", puntaje,RESET)
  
  
  
  print("\n-----------------------2DA PREGUNTA-----------------------\n")
  
  
  print (RED+"2) La fase donde se realiza un algoritmo se le conoce como diseño\n"+RESET)
  print (BLUE+"VERDADERO")
  print ("FALSO"+RESET)
  
  print("\npiensa en tu respuesta, solo tienes 5 segundos\n")
  tiempo=time.sleep(5)
  respuesta_2 = input("Ingresa 'V' para verdadero, o 'F' para falso: ").lower()
 
  
  
  while respuesta_2 not in ("v", "f"):
    respuesta_2 = input(RED+"!!! Debes responder 'v' o 'f' !!! Ingresa nuevamente tu respuesta : "+RESET).lower()
    
  
  if respuesta_2 == "v":
    print ("Correcto!")
    puntaje = puntaje + 10

  else:
    print ("INCORRECTO!")
    puntaje = puntaje -5
  
  print(GREEN+"Tu puntaje hasta ahora es:", puntaje,RESET)




  print("\n-----------------------3ERA PREGUNTA-----------------------\n")

  
  print (RED+"3) Es la fase en la cual se revisan los resultados arrojados por un algoritmo:\n"+RESET)
  print (BLUE+"a) Análisis")
  print ("b) Prueba")
  print ("c) Diseño")
  print ("d) Planteamiento del problema"+RESET)
  
  
  print("\npiensa en tu respuesta, solo tienes 5 segundos\n")
  tiempo=time.sleep(5)
  respuesta_3 = input("Ingresa tu respuesta : ").lower()

  
  
  
  while respuesta_3 not in ("a", "b", "c", "d","p"):
    respuesta_3 = input(RED+"!!! Debes responder a, b, c o d !!! Ingresa nuevamente tu respuesta : "+RESET).lower()
    
  
  
  
  if respuesta_3 == "a":
    print ("Totalmente incorrecto!")
    puntaje = puntaje - 5
  elif respuesta_3 == "d":
    print ("muy cerca pero incorrecto")
    puntaje = puntaje + 2
  elif respuesta_3 == "c":
    print ("Incorrecto! ")
    puntaje = puntaje - 3
    
  elif respuesta_3 == "p":
    print ("Incorrecto! la respuesta es la ´b´\n"+GREEN+
           "PERO HAZ ESCRITO ´p´, ENTONCES ENCONTRASTE LA LETRA SECRETA!"
           "por eso se te sumarán la cantidad que tu quieras" )
    puntaje=int(input("ingresa la cantidad de puntos que quieras: "))
    puntaje = puntaje
  
  else:
    print ("Correcto!")
    puntaje = puntaje + 10
  
  print(GREEN+"Tu puntaje hasta ahora es:", puntaje,RESET)
  









  print("\n-----------------------SE TERMINARON LAS PREGUNTAS-----------------------\n")
  
  
  print(YELLOW+"Gracias",nombre,"por jugar mi trivia\n"+RESET+
       GREEN+"Tu puntaje es:", puntaje,RESET)
  
  
  print("\nAHORA JUGAREMOS A LA RULETA PARA SUMARTE PUNTOS")
  
  pregunta=input("quieres jugar? (escribe 'y' para continuar  o cualquier tecla para finalizar) : ")
  pregunta=pregunta.lower()
  if pregunta=="y":
  
    print("\nGIRANDO LA RULETA\n")
    tiempo=time.sleep(2)
    
    aleatorio=random.randint(1,10)
    print("se te sumaran",aleatorio,"puntos")
    print(GREEN+"tu puntaje total es: ", puntaje + aleatorio,RESET)
  
  else:
    print("Se terminó el juego")

  
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'y' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "y":  
     print("\nEspero {nombre} que te hayas divetido mucho!!!")
     iniciar_trivia = False 
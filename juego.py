#Juego del Ahorcado
# @JoseAguirre
'''
Explicacion del juego
1. Elegir aleatoreamente una palabra de una lista de palabras.
2. Mostrar el dibujo de una horca.
3. Mostrar un guion bajo por cada letra de la palabra.
4. Pedir al usuario que introduzca una letra: si no es una unica 
   letra indicarlo. Si ya se ha dicho indicarlo.
5. Comprobar si esa letra esta en la palabra elegida.
6. Si esta, volver a mostrar el dibujo de la horca como la ultima 
   vez. sustituir el guien correspondiente por la letra dicha.
7. Si la palabra no esta, mostrar el dibujo de la horca al que se 
   añade una nueva parte.
8. Si se falla 6 veces, se completa el dibujo del ahorcado.
9. Si se aciertan todas las letras de la palabra, mostrar mensaje de Ganador.
'''

import random #libreria aleatoria
import os     #libreria que borra la pantalla

palabras = ["SAITAMA", "NARUTO","HINUYACHA","BLEACH","L","LIGTH","GOKU","BROLY","BORUTO","ASH","BROKE","RIUK"]
palabra = random.choice(palabras)

fallo0 = '''
          !===N
          |   N
              N
              N
              N
      =========
'''
fallo1 = '''
          !===N
          |   N
          O   N
              N
              N
      =========
'''
fallo2 = '''
          !===N
          |   N
         \O   N
              N
              N
      =========
'''
fallo3 = '''
          !===N
          |   N
         \O/  N
              N
              N
      =========
'''
fallo4 = '''
          !===N
          |   N
         \O/  N
          |   N
              N
      =========
'''
fallo5 = '''
          !===N
          |   N
         \O/  N
          |   N
           \  N
      =========
'''
fallo6 = '''
          !===N
 GAME     |   N
 OVER!   \O/  N
          |   N
         / \  N
      =========
'''
letras_correctas = "" #Letras correctas dichas por el usuario
letras_todas = "" #todas las letras dichas por el usuario
fallos = 0

while True:
  os.system("cls")   #Borrar pantalla cada vez que se juega
  print("**********************")
  print("**PERSONAJE DE ANIME**")
  print("**********************")
  if fallos == 0:
    print(fallo0)
  elif fallos == 1:
    print(fallo1)
  elif fallos == 2:
    print(fallo2)
  elif fallos == 3:
    print(fallo3)
  elif fallos == 4:
    print(fallo4)
  elif fallos == 5:
    print(fallo5)
  elif fallos == 6:
    print(fallo6)

  print()
  
  #Se muestran las letras acertadas y guines bajos en las no acertadas
  resultado =""

  for letra in palabra:
    if letra in letras_correctas:
      resultado += letra
    else:
      resultado += "_"
  print("      {}".format(resultado))
  print()
  print()
  #Comprobamos si se ha acertado la palabra o se han terminado los intentos

  if resultado == palabra:
    print("**** Has Ganado ****")
    break
  if fallos > 5:
    print("La palabra es: ",palabra)
    print("**** Has Perdido ****")
    break
# Bucle para que el usuario teclee una letra que cumpla los requisitos
  while True:
    letra_usuario_sin_formato = input("Dime una letra: ")
    letra_usuario = letra_usuario_sin_formato.upper()
    if len(letra_usuario) < 1 or len(letra_usuario) > 1:
      print("Introduce una letra")
    elif letra_usuario in letras_todas:
      print("Esa letra ya la has dicho!")
    elif not letra_usuario.isalpha():
      print("Eso no es una letra (-_-)")
    else:
      letras_todas += letra_usuario
      break
#Comprobamos si la letra dicha por el usuario esta en la palabra 
  if letra_usuario not in palabra:
    fallos +=1
  else:
    letras_correctas += letra_usuario
      
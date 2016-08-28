#!/usr/bin/python3
from random import *

class InputError(Exception):
  pass

def zufallSSP():
  zufall = random()
  if zufall < 0.33333334:
    return "stein"
  if zufall < 0.66666667:
    return "schere"
  else:
    return "papier"

COMPUTER_HAT_GEWONNEN = -1
SPIELER_HAT_GEWONNEN = 1
UNENTSCHIEDEN = 0

def gewonnenOderNicht(antwort,eigenes):
  if antwort==eigenes:
    return UNENTSCHIEDEN
  else:
    if antwort=="stein":
      if eigenes=="schere":
        return SPIELER_HAT_GEWONNEN
      else:
        return COMPUTER_HAT_GEWONNEN
    if antwort=="schere":
      if eigenes=="papier":
        return SPIELER_HAT_GEWONNEN
      else:
        return COMPUTER_HAT_GEWONNEN
    if antwort=="papier":
      if eigenes=="stein":
        return SPIELER_HAT_GEWONNEN
      else:
        return COMPUTER_HAT_GEWONNEN
    else:
      raise InputError(antwort) 

def spiel():
  punkte = 0
  while 1:
    eigenes = zufallSSP()
    print("schere,stein,papier")
    antwort = input()
    print("Ich habe", eigenes)
    try:
      ergebnis = gewonnenOderNicht(antwort,eigenes)
      punkte = punkte + ergebnis
      if ergebnis==COMPUTER_HAT_GEWONNEN:
        print("Ich habe gewonnen!")
      if ergebnis==SPIELER_HAT_GEWONNEN:
        print("Du hast gewonnen!")
      if ergebnis==UNENTSCHIEDEN:
        print("Unentschieden.")
      if punkte==1 | punkte==-1:
        print("Du hast", punkte, "Punkt.")  
      else:  
        print("Du hast", punkte, "Punkte.")  
    except InputError:
      print("Du mußt schere oder stein oder papier eingeben!")


#spiel()

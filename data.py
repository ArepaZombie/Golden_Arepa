import functions

#Valores son: Nombre, HP, AP, DP, SP, Money

#Funcion para crear un monstruo desde una plantilla
def born(data: tuple):
  name = data[0]
  hp = data[1]
  ap = data[2]
  dp = data[3]
  sp = data[4]
  money = data[5]
  return functions.creature(name,hp,ap,dp,sp,money)


#Valores iniciales para el jugador:

PlayerData = ("Ramon", 10,2,1,1,1,0,[1,1,1])

#Valores iniciales del Slime
Slime = ("Slime", 5,1,0,0,0,0)


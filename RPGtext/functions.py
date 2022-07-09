import random

#Así serán definidas las criaturas del juego
class creature():
  def __init__(self,name: str, hp: int, a: int, d: int, s: int, money: int):
    self.name=name
    self.hp=hp
    self.ap=a
    self.dp=d
    self.sp=s
    self.money=money

  def __str__(self):
    return f'''{self.name}: HP {self.hp} 
      DP: {self.dp}
      AP: {self.ap}
      SP: {self.sp}
      GLD: {self.money}'''

#El jugador, a parte de tener todo lo de arriba, tendrá un equipo y un inventario (a agregar luego)
class player(creature):
  def __init__(self, name, hp, a, d, s, money, equip: list):
    super().__init__(name, hp, a, d, s, money)
    self.equip=equip

  def equip(self):
    return self.equip

#Esta es la funcion para cuando hay pelea... hay que agregar cosas
def fight(player: player, enemy: creature):
  print("Empieza la pelea")

  #Escoje que harás
  while player.hp>0 and enemy.hp>0:
    option = input("Ataca webon!")
    if option == "":
      print(attack(player, enemy))

    #El turno del enemigo
    print("Turno de ", enemy.name)
    print(attack(enemy, player))

  #Si no estas muerto... ganaste! 
  if player.hp>0:
    player.money += enemy.money
    print(f"Haz ganado! Obtuviste {enemy.money} G")
  #Si estas muerto... perdiste
  else:
    print("Perdiste pendejo :c")


#Así es como ocurren los ataques

  #Si el defensor es mas rapido, puede que esquive el golpe
  if defen.sp >= atac.sp:
    dif = defen.sp - atac.sp
    #ESto hay que mejorarlo, pero basicamente si la diferencia es de 4 eres intocable... no se que pase si el rango sea mayor a 4
    if random.randrange(dif, 4) == 4:
      return "Se esquivó el ataque"
    #Si el defensor es igual o mas rapido, la defensa quita medio punto per punto
    shield = defen.dp/2
  #Si  es mas lento, solo quita .25 puntos
  else:
    shield = defen.dp/4

  #Aca se almacena el golpe
  sword = atac.ap - shield
  #Se reduce la vida
  defen.hp -= sword
  #Y se entrega el resultado
  return f"Ataque efectivo! {atac.name} gastó {sword} a {defen.name}"
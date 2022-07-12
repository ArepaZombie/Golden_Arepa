import random

line="-"*30

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
    return f'''-------------
***{self.name}***
HP {self.hp} 
DP: {self.dp}
AP: {self.ap}
SP: {self.sp}
GLD: {self.money}'''

  #Así es como ocurren los ataques
  def attack(self, defen):
  #Si el defensor es mas rapido, puede que esquive el golpe
    if defen.sp >= self.sp:
      #Si el defensor es igual o mas rapido, la defensa quita medio punto per punto
      shield = defen.dp/2
      dif = defen.sp - self.sp
    #ESto hay que mejorarlo, pero basicamente si la diferencia es de 4 eres intocable... no se que pase si el rango sea mayor a 4
      if random.randrange(dif, 5) == 4:
        return input("Se esquivó el ataque")

  #Si  es mas lento, solo quita .25 puntos
    else:
      shield = defen.dp/4

    #Aca se almacena el golpe
    sword = self.ap - shield
    #Se reduce la vida
    defen.hp -= sword
    #Y se entrega el resultado
    return input(f"Ataque efectivo! {self.name} gastó {sword} a {defen.name}")

  #Esta es la funcion para huir del enemigo
  def run(self, enemy):
    if self.sp <= enemy.sp:
      input(f'''{enemy.name} es muy rapido.
            No se pudo huir.''')
      return False
    else:
      if self.sp>enemy.sp:
        dif = self.sp - enemy.sp
    #ESto hay que mejorarlo, pero basicamente si la diferencia es de 4 eres intocable... no se que pase si el rango sea mayor a 4
        if random.randrange(dif, 5) == 4:
          input(f'{self.name} huyó de {enemy.name}')
          return True
        else:
          input(f'{self.name} no pudo huir de {enemy.name}')
          return False

  
#El jugador, a parte de tener todo lo de arriba, tendrá un equipo y un inventario (a agregar luego)
class player(creature):
  def __init__(self, name, hp, a, d, s, money, equip: list):
    super().__init__(name, hp, a, d, s, money)
    self.equip=equip

  def equip(self):
    return self.equip

###########################################

#SISTEMA DE PELEA
    
#Esta es la funcion para cuando hay pelea... hay que agregar cosas
def fight(player: player, enemy: creature):
  print(line)
  print("Empieza la pelea")

  while player.hp>0 and enemy.hp>0:
    run = False
    while True:
      print(line)
      try:
        #Escoje que harás
        option = int(fight_menu())
      except:
        print("Opcion incorrecta. Intente de nuevo.")
      else:
        if option > 0 and option < 4:
          #Atacar a un enemigo
          if option==1:
            player.attack(enemy)
          #Usar objetos
          elif option==3:
            input("Aún no hago esto jeje. Pierdes turno por pendejo")
          elif option==2:
            run = player.run(enemy)
            if run:
             #Que termine la pelea si se huyó
              return input("Pelea terminada")
          break
        else:
          print(option,"is not an option. Try again.")
    
    #El turno del enemigo
    print(line)
    print("Turno de ", enemy.name)
    print(enemy.attack(player))

  #Si no estas muerto... ganaste! 
  if player.hp>0:
    print(line)
    player.money += enemy.money
    print(f"Haz ganado! Obtuviste {enemy.money} G")
  #Si estas muerto... perdiste
  else:
    print(line)
    print("Perdiste pendejo :c")


#Para que funcione el ataque tengo estas dos funciones
def fight_menu():
  print('''Es tu turno. ¿Que deseas hacer?
        1. Atacar
        2. Correr
        3. Usar objeto''')
  o = input("")
  return o






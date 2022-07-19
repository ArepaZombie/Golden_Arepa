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
  def __init__(self, name, hp, a, d, s, money):
    super().__init__(name, hp, a, d, s, money)
    self.equip= [0,0,0]
    self.inventory = list()

  def see_equip(self):
    print("Sword Lvl.",self.equip[0])
    print("Armor Lvl.",self.equip[1])
    print("Boots Lvl.",self.equip[2])
    return self.equip

  def see_inventory(self):
    for x in self.inventory:
      print(x)
    return None

  def grab_item(self, item):
    self.inventory.append(item)
    return input(f'Has obtenido {item.name}')

  def use_item(self, item):
    item.use(self)

#Funcion para crear un monstruo desde una plantilla
def born(data: tuple):
  return creature(data[0],data[1],data[2],data[3],data[4],data[5])


###########################################

#####SISTEMA DE PELEA#####
    
#Esta es la funcion para cuando hay pelea... hay que agregar cosas
def fight(player: player, enemy: creature):
  print(line)
  print("Empieza la pelea")
  turn = 0 #Contador de turnos
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
          
          #Huir
          elif option==2:
            run = player.run(enemy)

          #Ver estado
          elif option==4:
            print(player)
            continue
          
            if run:
             #Que termine la pelea si se huyó
              return input("Pelea terminada")
          
          break
          
        else:
          print(option,"is not an option. Try again.")
    
    #El turno del enemigo
    print(line)
    print("Turno de ", enemy.name)
    print(enemy.attack(player)) #Tendre que agregar unas funciones de "comportamiento"
    turn += 1 #contador de turnos aumenta
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
        3. Usar item
        4. Ver estado''')
  o = input("")
  return o


###########################################

#Sistema de objetos
def create_item(data: tuple):
  return item(data[0], data[1], data[2])


class item():
  def  __init__(self, name: str, action: tuple, price: int):
    self.name=name
    self.action=action
    self.price=price

  def use(self, player: player):
    if self.action[0] == "LifeUp":
      player.hp =+ self.action[1]
      print(f"Estaba buena. +{self.action[1]} de HP")
    elif self.action[0] == "SpeedUp":
      player.sp =+ self.action[1]
      print(f"Uy, calientito. +{self.action[1]} de velocidad por 3 turnos")
    elif self.action[0] == "DefenseUp":
      player.dp =+ self.action[1]
      print(f"Erga, esta potente. +{self.action[1]} de defensa por 3 turnos")
import functions
import data

equip = [0,0,0]
player = functions.player("Ramon", 10,2,1,1,0)
monster = functions.born(data.Slime)

print(player)
print(player.equip)

print(monster)
functions.fight(player, monster)
from stellarwars import *

sides = ["F", "FR", "RR", "R", "RL", "FL"]

# start off with a name
name = input("Choose a name for your ship: ")

# now the type
print("\n")
print("Ship Types (build points):")
print("1 - Dreadnought (125)")
print("2 - Battleship (110)")
print("3 - Cruiser (100)")
print("4 - Destroyer (90)")
print("5 - Escort (80)")
print("6 - Scout (70)")
print("7 - Freighter (45)")
type = input("Choose a type (1-7) [default 3]: ")
if type == "":
    type = Ship.TYPE_CRUISER
shiptype = int(type)
# set initial build points
if shiptype == Ship.TYPE_DREADNOUGHT:
    build_points = 125
    hull = 5
    reactor = 3
    speed_cost = [1,2,5,8,11,14]
elif shiptype == Ship.TYPE_BATTLESHIP:
    build_points = 110
    hull = 4
    reactor = 3
    speed_cost = [1,2,4,6,9,12]
elif shiptype == Ship.TYPE_CRUISER:
    build_points = 100
    hull = 4
    reactor = 3
    speed_cost = [1,2,3,6,8,11]
elif shiptype == Ship.TYPE_DESTROYER:
    build_points = 90
    hull = 3
    reactor = 2
    speed_cost = [1,2,3,5,7,9]
elif shiptype == Ship.TYPE_ESCORT:
    build_points = 80
    hull = 2
    reactor = 2
    speed_cost = [1,2,3,4,6,8]
elif shiptype == Ship.TYPE_SCOUT:
    build_points = 70
    hull = 1
    reactor = 1
    speed_cost = [1,2,3,4,5,6]
else: #FR
    build_points = 45
    hull = 3
    reactor = 2
    speed_cost = [1,2,3,5,7,9]
build_points -= (hull + reactor)
print("*** You have {0} build points remaining after buying hull ({1}) and reactor ({2}) points.".format(build_points, hull, reactor))

# pick speed
print("\n")
print("Speed costs:")
for i in range(len(speed_cost)):
    print("Speed of {0} costs {1}.".format(i+1, speed_cost[i]))
speed = input("What speed do you want to buy (1-6) [default 3]: ")
if speed == "":
    speed = 3
build_points -= speed_cost[int(speed)-1]
print("*** You have {0} build points remaining.".format(build_points))

# pick shields
shields = []
print("\n")
print("For each of the six sides (F, FR, RR, R, RL, FL), choose how many points you want to spend on shields (1-6) [default 3]: ")
for s in sides:
    shield = input("{0}: ".format(s))
    if shield == "":
        shield = 3
    shields.append(int(shield))
    build_points -= int(shield)
print("*** You have {0} build points remaining.".format(build_points))

# pick armor
armor = []
print("\n")
print("For each of the six sides (F, FR, RR, R, RL, FL), choose how many points you want to spend on armor (1-6) [default 3]: ")
for s in sides:
    arm = input("{0}: ".format(s))
    if arm == "":
        arm = 3
    armor.append(int(arm))
    build_points -= int(arm)
print("*** You have {0} build points remaining.".format(build_points))

# pick weapons
weapons = []
missile_count = 0
while True:
    print("\n")
    print("Pick a weapon (build points):")
    print("1 - Laser (2)")
    print("2 - Force Beam (3)")
    print("3 - One Missile (3)")
    print("4 - Beam (4)")
    print("5 - Gun (5)")
    print("6 - Plasma Cannon (15)")
    print("0 - Quit")
    wep = input("Weapon (0-6) [default 1]: ")
    if wep == "":
        wep = 1
    wepnum = int(wep)
    if (wepnum == Weapon.TYPE_MISSILE) and (missile_count == 20):
        print("You can't have more than twenty missiles!")
    else:
        if wepnum == 0:
            break
        else:
            side = input("Side (1. F, 2. FR, 3. RR, 4. R, 5. RL, 6.FL) (1-6): ")
            w = Weapon(wepnum, int(side))
            weapons.append(w)
            if wepnum == Weapon.TYPE_LASER:
                build_points -= 2
            elif wepnum == Weapon.TYPE_FORCEBEAM:
                build_points -= 3
            elif wepnum == Weapon.TYPE_MISSILE:
                missile_count += 1
                build_points -= 3
            elif wepnum == Weapon.TYPE_BEAM:
                build_points -= 4
            elif wepnum == Weapon.TYPE_GUN:
                build_points -= 5
            else: # PLASMACANNON
                build_points -= 15
            print("*** You have {0} build points remaining.".format(build_points))

# pick systems
systems = []
mine_count = 0
while True:
    print("\n")
    print("Pick a system (build points):")
    print("1 - Missile Rack (4)")
    print("2 - Missile Defence (4)")
    print("3 - Multi-Tracking  (5)")
    print("4 - Sensors (7)")
    print("5 - Cloaking (10)")
    print("6 - One Mine (2)")
    print("7 - Self Destruct (8)")
    print("0 - Quit")
    sys = input("System (0-7) [default 1]: ")
    if sys == "":
        sys = 1
    sysnum = int(sys)
    if (sysnum == System.TYPE_MINE) and (mine_count == 10):
        print("You can't have more than ten mines!")
    else:
        if sysnum == 0:
            break
        else:
            s = System(sysnum)
            systems.append(s)
            if sysnum == System.TYPE_MISSILERACK:
                build_points -= 4
            elif sysnum == System.TYPE_MISSILEDEFENSE:
                build_points -= 4
            elif sysnum == System.TYPE_MULTITRACK:
                build_points -= 5
            elif sysnum == System.TYPE_SENSORS:
                build_points -= 7
            elif sysnum == System.TYPE_CLOAKING:
                build_points -= 10
            elif sysnum == System.TYPE_MINE:
                mine_count += 1
                build_points -= 2
            else: # SELFDESTRUCT
                build_points -= 8
            print("*** You have {0} build points remaining.".format(build_points))

# finalize
print("\n")
print("{0} has been completed and is ready for battle!".format(name))
myship = Ship(name, shiptype, speed, hull, reactor, shields, armor, weapons, systems)




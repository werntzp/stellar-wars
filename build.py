from stellarwars import *

sides = ["F", "FR", "RR", "R", "RL", "FL"]

# start off with a name
name = input("Choose a name for your ship: ")

# now the type
print("\n")
print("Ship Types (build points):")
print("DN - Dreadnought (125)")
print("BB - Battleship (110)")
print("CA - Cruiser (100)")
print("DD - Destroyer (90)")
print("ES - Escort (80)")
print("SC - Scout (70)")
print("FR - Freighter (45)")
type = input("Choose a type (DN, BB, CA, DD, ES, SC or FR): ")

# set initial build points
if type == "DN":
    build_points = 125
    hull = 5
    reactor = 3
    speed_cost = [1,2,5,8,11,14]
elif type == "BB":
    build_points = 110
    hull = 4
    reactor = 3
    speed_cost = [1,2,4,6,9,12]
elif type == "CA":
    build_points = 100
    hull = 4
    reactor = 3
    speed_cost = [1,2,3,6,8,11]
elif type == "DD":
    build_points = 90
    hull = 3
    reactor = 2
    speed_cost = [1,2,3,5,7,9]
elif type == "ES":
    build_points = 80
    hull = 2
    reactor = 2
    speed_cost = [1,2,3,4,6,8]
elif type == "SC":
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
while True:
    print("\n")
    print("Pick a weapon (build points):")
    print("1 - Laser (2)")
    print("2 - Force Beam (3)")
    print("3 - Missile(1) (3)")
    print("4 - Beam (4)")
    print("5 - Gun (5)")
    print("6 - Plasma Cannon (15)")
    print("Q - Quit")
    wep = input("Weapon (1-6, Q) [default 1]: ")
    if wep == "":
        wep = 1
    if wep == "Q":
        break
    else:
        side = input("Side (1. F, 2. FR, 3. RR, 4. R, 5. RL, 6.FL) (1-6): ")
        wepnum = int(wep)
        w = Weapon(wepnum, int(side))
        weapons.append(w)
        if wepnum == Weapon.TYPE_LASER:
            build_points -= 2
        elif wepnum == Weapon.TYPE_FORCEBEAM:
            build_points -= 3
        elif wepnum == Weapon.TYPE_MISSILE:
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
while True:
    print("\n")
    print("Pick a system (build points):")
    print("1. Missile Rack (4)")
    print("2. Missile Defence (4)")
    print("3. Multi-Tracking  (5)")
    print("4. Sensors (7)")
    print("5. Cloaking (10)")
    print("6. Mine(1) (2)")
    print("7. Self Destruct (8)")
    print("Q - Quit")
    sys = input("System (1-7, Q) [default 1]: ")
    if sys == "":
        sys = 1
    else:
        sysnum = int(sys)
        s = System(sysnum)
        systems.append(s)
        if wepnum == System.TYPE_MISSILERACK:
            build_points -= 4
        elif wepnum == System.TYPE_MISSILEDEFENSE:
            build_points -= 4
        elif wepnum == System.TYPE_MULTITRACK:
            build_points -= 5
        elif wepnum == System.TYPE_SENSORS:
            build_points -= 7
        elif wepnum == System.TYPE_CLOAKING:
            build_points -= 10
        elif wepnum == System.TYPE_MINE:
            build_points -= 2
        else: # SELFDESTRUCT
            build_points -= 8
    print("*** You have {0} build points remaining.".format(build_points))


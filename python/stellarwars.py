class System():

    TYPE_MISSILERACK = 1
    TYPE_MISSILEDEFENSE = 2
    TYPE_MULTITRACK = 3
    TYPE_SENSORS = 4
    TYPE_CLOAKING = 5
    TYPE_MINE = 6
    TYPE_SELFDESTRUCT = 7

    def __init__(self, type):
        self._type = type
        self._damage = 0

    @property
    def damage(self):
        return self._damage

class Weapon():

    TYPE_LASER = 1
    TYPE_FORCEBEAM = 2
    TYPE_MISSILE = 3
    TYPE_BEAM = 4
    TYPE_GUN = 5
    TYPE_PLASMACANNON = 6

    def __init__(self, type, side):
        self._type = type
        self._side = side
        self._damage = 0

    @property
    def damage(self):
        return self._damage


class Ship():

    TYPE_DREADNOUGHT = 7
    TYPE_BATTLESHIP = 6
    TYPE_CRUISER = 5
    TYPE_DESTROYER = 4
    TYPE_ESCORT = 3
    TYPE_SCOUT = 2
    TYPE_FREIGHTER = 1

    SIDE_FORWARD = 1
    SIDE_FORWARDRIGHT = 2
    SIDE_REARRIGHT = 3
    SIDE_REAR = 4
    SIDE_REARLEFT = 5
    SIDE_FORWARDLEFT = 6

    def __init__(self, name, type, engine, hull, reactor, shields, armor, weapons, systems):
        self._name = name
        self._type = type
        self._engine = engine
        self._hull = hull
        self._reactor = reactor
        self._shields = shields
        self._armor = armor
        self._weapons = weapons
        self._systems = systems

    @property
    def name(self):
        return _name

    @property
    def type(self):
        return self._type

    @property
    def engine(self):
        return self._engine

    @property
    def hull(self):
        return self._hull

    @property
    def reactor(self):
        return self._reactor

    @property
    def shields(self):
        return self._shields

    @property
    def armor(self):
        return self._armor

    @property
    def weapons(self):
        return self._weapons

    @property
    def systems(self):
        return self._systems



class StellarWars():

    pass



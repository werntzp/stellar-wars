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



class Ship():

    TYPE_DREADNOUGHT = 7
    TYPE_BATTLESHIT = 6
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

    def __init__(self, name, type):
        self._name = name
        self._type = type
        self._engine = 0
        self._hull = 0
        self._reactor = 0
        self._shield = {}
        self._armor = {}
        self._missles = 0
        self._mines = 0
        self._weapons = []
        self._systems = []

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
    def shield(self, side):
        return self._shield[side]

    @property
    def armor(self, side):
        return self._armor[side]

    @property
    def missles(self):
        return self._missles

    @property
    def mines(self):
        return self._mines



class StellarWars():

    pass



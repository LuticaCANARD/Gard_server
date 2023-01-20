from atom.unit import Lation_unit
#override 할 것이므로 

class GroundUnit(Lation_unit) :
    #Lation_unit 을 상속하여 Ground용 unit을 구축함.
    pass

class SeaUnit(Lation_unit) :
    #Lation_unit 을 상속하여 Sea or Space용 unit을 구축함.
    pass

class AirUnit(Lation_unit) :
    #Lation_unit 을 상속하여 Air 용 unit을 구축함.
    pass

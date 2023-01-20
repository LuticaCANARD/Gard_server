from atom.unit import Lation_unit
# override 할 것이므로 새로 생성.
# DB는 분리한다. 이때, Ground냐 SEA냐 Air이냐를 구분한다.
# Ground vs Sea같은 상호작용은 공격측에서 공격data를 생성하면... 피격측에서 그 data를 수신하여 상성에 따라서 처리한다.
# 이때, 데미지는 battle class의 inter_action 객체를 생성하여 피격측에 수신하게 한다.


class GroundUnit(Lation_unit) :
    #Lation_unit 을 상속하여 Ground용 unit을 구축함.

    pass

class SeaUnit(Lation_unit) :
    #Lation_unit 을 상속하여 Sea or Space용 unit을 구축함.
    pass

class AirUnit(Lation_unit) :
    #Lation_unit 을 상속하여 Air 용 unit을 구축함.
    pass

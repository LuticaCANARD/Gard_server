from DB import DB
# 이 class는 유닛과 유닛간의 상호작용을 규정하는 class이다.
# 이 class로 유닛에게 데미지를 제공하며, 필요하다면, 이 상호작용을 수정 하여 데미지의 강화, 혹은 상성의 작용을 진행 활 수 있다.

class UnitInteraction :
    _data = {
        "from_unitno"       : None,        #interaction의 출발유닛 번호
        "inter_action_type" : None,        #interaction의 종류
        "scala"             : None,        #interaction의 스칼라값 ... > 전투시의 '데미지', 회복시의 '힐값'
        "modifi"            : [],          #interaction에 적용되는 모디파이어의 id
    }
    def __init__ (self,data:dict) :
        return
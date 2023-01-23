import Process
from lib.molcule.latioin_unit import Lation_unit
from lib.molcule.atom.battle import UnitInteraction
from lib.molcule.province import Province
class ProcessBattle(Process) : 
    # 유저의 전투를 처리한다.
    _battledata = {
        "province" :  None ,  
        "defence_unit" : [],  
        "attack_unit" :  [] 
    }
    def __init__(self,data:dict) :
        self._battledata = data

    def load_location(self) :
        # 위치 정보 조회 -> 제약 사항 검색
        location = Province(self._battledata["province"])
        self._battledata["defence_unit"].extend( location.load_arms())
        pass


    def execute_battle(self) :
        # 전투 실시
        pass



    pass

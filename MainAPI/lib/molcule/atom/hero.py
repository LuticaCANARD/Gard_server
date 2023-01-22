import DB

class Hero :
    _info = {         # 영웅의 정보
        "name"     : None, #영웅의 이름
        "class"    : None, #영웅의 등급
        "location" : None, #영웅의 위치
        "desc"     : None, #영웅이 지휘중인 부대
        "skillids" : [],   #영웅의 skill id
        "modi"     : []    #영웅의 현 상황
    }

    def retrn_skill (self) :
        return self._info["skillids"]
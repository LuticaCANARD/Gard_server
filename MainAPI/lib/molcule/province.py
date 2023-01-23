from DB import DB

class Province :
    _info = {
        "id"       : None,
        "type"     : None,
        "userno"   : None,
        "building" : [],
        "army"     : [],
        "modi"     : []
    }
    def __init__(self,province_no) -> None:
        #비종기식 처리를 염두에 두어 단 하나의 변수만 수여
        db = DB()
        svl=db.execute_query('SELECT * FROM tb_province WHERE id = %s',(province_no,))[0]
        for key in self._info.keys() :
            self._info[key] = svl[key]
        return
    def load_arms(self) :
        return self._info["army"]
    def load_modifi (self) :
        return self._info["modi"]
    def extend_arms(self,arms:list) :
        self._info["army"].extend(arms)

    def update_db(self) :
        # 변경된 지역 상태를 업데이트 한다.
        db = DB()
        ret = db.update_object('tb_province','id',self._info)
        return
    
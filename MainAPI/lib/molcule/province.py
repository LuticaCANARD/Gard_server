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
    
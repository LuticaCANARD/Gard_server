from DB import DB


class Lation_unit:
    #  모든 유닛의 기본이 되는 class
    db = DB()
    _info = {             # 유닛의 기본 정보. tb_user_divion에 정의 예정.
        "type": None,   # 병종
        "name": None,   # 유닛 이름
        "group": None,   # 상위조직
        "contry": None,   # 국적및 소속
        "unitno": None,   # 내부 처리용 유닛용 no
    }
    _stat = {             # 유닛의 현재 상태. update마다 사용하며, 이 역시 tb_user_divion에 규정한다. (미정)
        "hp": None,     # 체력
        "atk": None,     # 공격력
        "def": None,     # 방어력
        "modi": [],       # 모디파이어, 상황
        "action": None,     # 현재 남은 행동력
        "costs": None      # 유닛의 상황만을 고려한 현 유지비
    }
    _spec = {                # 유닛의 original spec. reference value로 사용된다.tb_divion_ref에 저장한다. 사용용도는 caching
        "hp": None,      # 체력
        "atk": None,      # 공격력
        "def": None,      # 방어력
        "modi": [],        # 모디파이어, 상황
        "action": None,    # 초기 행동력
        "costs": None     # 병종 자체의 유지비
    }

    def __init__(self, data) -> None:
        # 유닛을 생성 할 때 사용하는 설정이다.
        # 유닛을 생성 할 때, data는 tb_user_divion에서 뽑아온 하나의 데이터로, 뽑을 때 *를 사용하는 것을 원칙으로 한다.
        for d in self._info.keys():
            self._info[d] = data[d]
        for key in self._stat.keys():
            self._stat[key] = data[key]
        _ref = self.db.execute_query(
            'SELECT * FROM tb_divion_ref WHERE type=%s', (self._info["type"],))[0]
        for k in _ref.keys():
            self._spec[k] = _ref[k]
        return

    def save_unit_stat_db(self) -> None:
        # DB에 unitinfo를 update하여 반영한다. 전투 종결등에 사용한다.
        if self._stat["hp"] == 0:
            self.db.execute_query(
                'DELETE FROM tb_user_divion WHERE unitno = %s', (self._info["unitno"],))
        else:
            self.db.execute_query('UPDATE tb_user_divion SET hp = %s, atk = %s, def = %s, modi = %s WHERE unitno = %s', (
                self._info["hp"], self._info["atk"], self._info["def"], self._info["modi"], self._info["unitno"],))
        return

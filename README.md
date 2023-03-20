# Notices
- This repo is no use now.
(duplicated)
# 대전제
* 이 프로그램은 게임 가르드의 server를 목표로 한다.
* 이 프로그램는 웹 뿐만아니라 게임등 각종 형태의 client programs의 수요에 맞춰 밀표한 데이터를 전달하는 API의 형식을 띤다.
* 따라서, 통신에 필요한 데이터는 최소한으로 진행하며 최대한 다양한 기능의 제공을 목표로 한다.
* 이 API는 '로직의 구현'만을 중심으로 한다. 인증등의 기능은 별도의 API나 확장된 API로 구현한다.

# 고려되는 환경
* 언어는 초보자의 접근이 쉽고, 데이터의 가공이 간편한 python을 기반으로 한다.
* DB는 간단한 Postgres를 기반으로 접근한다. 만약 필요하다면 RDBMS외 다른 DB를 구축할 수 있다. postgres를 제외하고는 최대한 local 에서 굴리는 것을 원칙으로 한다.
* 성능은 python 특성상 떨어 질 수는 있으나, 가르드 게임의 특성상 그렇게까지 빠를 필요는 없고, 핵심로직 구축이 목표임으로 신경쓰지 않음.
* 인증 기능은 naver API와 연계할 예정. 그러나 이 프로그램에서는 다루지 않고, WEB project에서 다룬다. 

# 고려되는 FrameWorks
* FastApi : Flask및 Django와 달리, 필요한 기능만 지원하여 성능상 이점이 있음.
* Poatgres SQL : PGSQL의 퍼포먼스나 다양한 기능을 사용
* Docker? : 서버및 환경구축시 도움됨.

# 역할분담계획
* CANA: 개발 계획 전임, Infra, DB Functions, DB 관리 등
* Marint? : (참가 의사가 있는 경우) 기본 Logics, 통신 입출력

# DB 구축 방안
* 현재 CANA Discord Bot의 이용률이 저조한 바를 확인하였고, 이 server를 전용하여 가르드 서버 구축에 활용함.
* 혹은 라즈베이파이의 활용도 가능함.


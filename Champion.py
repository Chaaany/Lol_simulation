# 과제 2
# 전역변수 안 쓰기
#
# class를 이용해서 lol simulation을 만들어보자
#
# 1. requests를 사용해 champion정보를 가져온다.
#     1. http://ddragon.leagueoflegends.com/cdn/11.17.1/data/ko_KR/champion.json
# 2. red, blue팀에 랜덤으로 다섯개 챔피언을 생성한다(중복 허용 안됨)
# 3. 게임을 시작한다.
# 4. 챔피언은 상대팀의 다른 챔피언을 공격할 수 있고, hp가 0 이하로 떨어지면 사망처리되며, 사망처리되면 더이상 공격을 할 수 없다.
# 5. 게임이 시작되면 스피드가 높은 챔피언부터 순서대로 공격을 하며, 각 챔피언의 데미지는 챔피언의 타입에 따라 (attack * attackdamage) 혹은 (magic * attackdamage)가 될 수 있다(분류기준은 자유), 각 action을 print하자(ex: Azir가 Brand에게 123의 데미지를 주었다. Brand는 사망했다!)
# 6. 한 팀의 챔피언이 모두 사망할때까지 반복한다.
# 7. 게임이 종료되면 이긴 팀을 출력하자.
# 8. 완성된 코드는 github에 업로드할 것.
import json
import requests

class Champion:
# 챔피언 생성자
    def __init__(self, champion_name):
        champion_info = json.loads(requests.get("http://ddragon.leagueoflegends.com/cdn/11.17.1/data/ko_KR/champion.json").text)["data"]
        self.name = champion_name
        self.hp = champion_info[champion_name]["stats"]["hp"]
        self.attack = champion_info[champion_name]["info"]["attack"]
        self.magic = champion_info[champion_name]["info"]["magic"]
        self.movespeed = champion_info[champion_name]["stats"]["movespeed"]
        self.damage = champion_info[champion_name]["stats"]["attackdamage"]
        self.dead = False

#각 속성 값 getter
    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_movespeed(self):
        return self.movespeed

#ad인지 ap인지 주문력이 다르게 처리해야 함(ad : attack > magic / ap : attack < magic)
    def get_hitdamage(self):
        if self.attack > self.magic:
            return self.attack + self.damage
        else:
            return self.magic + self.damage

    def get_is_dead(self):
        return self.dead

# hp 변화량 적용, hp 변화량에 따른 사망여부 처리
    def set_hp(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.is_dead = True
# 행위 정의
    def doattack(self, foename):
        print(f"{self.name}님께서 {foename}님에게 {self.get_hitdamage()}만큼 피해를 입혔습니다.")
        return self.get_hitdamage()



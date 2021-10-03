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
from Champion import *

class Team:
#팀 생성자 생성
    def __init__(self, member):
        self.team = []
        if len(member) == 5:
            for champ in member:
                self.team.append(Champion(champ))
        else:
            Print("팀 내의 챔피언의 수가 5명이어야 합니다.")
        self.team_all_dead = False

#Team 클래스 getter
    def get_member(self):
        return self.team

    def get_member_name(self):
        member_name = []
        for champion in self.team:
            member_name.append(champion.get_name())
        return member_name

    def get_member_hp(self):
        member_hp = []
        for champion in self.team:
            member_hp.append([champion.get_name(), champion.get_hp()])
        return member_hp

    def get_member_movespeed(self):
        member_movespeed = []
        for champion in self.team:
            member_hp.append([champion.get_name(), champion.get_movespeed()])
        return member_hp

    def are_team_all_dead(self):
        for champion in self.get_member():
            if champion.get_is_dead() == True:
                return champion.get_is_dead()

        return False

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

import random
import requests
import json
from Team import *
from Champion import *

class Game:
    #게임 생성자
    def __init__(self):
        champion_info = json.loads(requests.get("http://ddragon.leagueoflegends.com/cdn/11.17.1/data/ko_KR/champion.json").text)["data"]
        # 무작위로 챔피언 10개 생성 및 5개씩 redteam, blueteam 생성
        data = random.sample(list(champion_info), 10)
        self.redteam = Team(data[:5])
        self.blueteam = Team(data[5:])

    # 게임 시작
    def game_start(self):
        print("게임이 시작되었습니다.")
        print("redteam : ", self.redteam.get_member_name(), "/ blueteam : ", self.blueteam.get_member_name())
        fight_count = 1
        while not(self.redteam.are_team_all_dead() or self.blueteam.are_team_all_dead()):
            print(fight_count, "번째 싸움 시작\n")
            for champion in self.set_attack_sq(self.redteam.get_member(), self.blueteam.get_member()):
                if champion in self.redteam.get_member():
                    foe = random.choice(self.blueteam.get_member())
                    foe.set_hp(champion.doattack(foe))
                else:
                    foe = random.choice(self.redteam.get_member())
                    foe.set_hp(champion.doattack(foe))
            fight_count += 1

        if self.redteam.are_team_all_dead() == True:
            print("게임이 종료 되었습니다. blueteam이 승리하였습니다.")
        else:
            print("게임이 종료 되었습니다. redteam이 승리하였습니다.")


    # 공격 순서 정의
    def set_attack_sq(self, team1, team2):
        all_champion = team1 + team2
        champion_and_speed = []
        attack_order = []
        attack_order_name = []
        for champion in all_champion:
            champion_and_speed.append([champion, champion.get_movespeed()])
        sorted(champion_and_speed, key=lambda x: x[1], reverse=True)
        i = 0
        while i < len(champion_and_speed):
            attack_order_name.append(champion_and_speed[i][0].get_name())
            i += 1

        i = 0
        while i < len(champion_and_speed):
            attack_order.append(champion_and_speed[i][0])
            i += 1

        print(f"공격순서는 {attack_order_name}입니다.")
        return attack_order



# Luke Strassburg
        
class Player:
    def __init__(self, nflid, birthDate, officialPosition, name, height, weight, college):
        self.id = nflid
        self.birthday = birthDate
        self.position = officialPosition
        self.name = name
        self.week1 = []
        self.week2 = []
        self.week3 = []
        self.week4 = []
        self.week5 = []
        self.week6 = []
        self.week7 = []
        self.week8 = []
        self.height = height
        self.weight = weight
        self.college = college

    def get_name(self):
        return self.name[1:-2]
    
    def get_position(self):
        return self.position[1:-1]

    def get_birthDate(self):
        return self.birthday

    def get_age(self):   
        if str(self.birthday) == 'NA':
            return 22

        birthyear = self.birthday [1:5]
        
        if birthyear[2] == '/':
            birthyear = self.birthday[-5:-1]
            
        else:
            birthyear = birthyear
            
        difference = 2021 - int(birthyear)

        return difference

    def get_id(self):
        return self.id

    def set_week1(self, play_output):
        self.week1.append(play_output)

    def set_week2(self, play_output):
        self.week2.append(play_output)

    def set_week3(self, play_output):
        self.week3.append(play_output)

    def set_week4(self, play_output):
        self.week4.append(play_output)

    def set_week5(self, play_output):
        self.week5.append(play_output)

    def set_week6(self, play_output):
        self.week6.append(play_output)

    def set_week7(self, play_output):
        self.week7.append(play_output)

    def set_week8(self, play_output):
        self.week8.append(play_output)
        
    def get_week1(self):
        return self.week1

    def get_week2(self):
        return self.week2
    
    def get_week3(self):
        return self.week3

    def get_week4(self):
        return self.week4    

    def get_week5(self):
        return self.week5

    def get_week6(self):
        return self.week6
    
    def get_week7(self):
        return self.week7

    def get_week8(self):
        return self.week8

    def get_height(self):
        feet = int(self.height[1:2])
        if self.height[-3:-2] == '-':
            tee = int(self.height[3:4])
        else:
            tee = int(self.height[3:5])

        total = feet*12 + tee

        return total

    def get_weight(self):
        return self.weight

    def get_college(self):
        if self.college == 'na':
            return self.college
        else:
            return self.college[1:-1]


class Play():
    def __init__(self, playid, playerid, beaten, hit, hurried, sacked, gameid, weeknum):
        self.playid = playid
        self.player = playerid
        self.beaten = beaten
        self.hit = hit
        self.hurried = hurried
        self.sacked = sacked
        self.gameid = gameid
        self.weeknum = weeknum

    def play_outcome(self):
        if self.beaten == str(1) or self.hit == str(1) or self.hurried == str(1) or self.sacked == str(1):
            return 1
        elif self.beaten == str(0) and self.hit == str(0) and self.hurried == str(0) and self.sacked == str(0):
            return 0
        else:
            return 'NA'

    def get_info(self):
        return [self.playid, self.player, self.beaten, self.hit, self.hurried, self.sacked]

    def get_gameid(self):
        return self.gameid

    def set_weeknum(self, weeknum):
        self.weeknum = int(weeknum)

    def get_weeknum(self):
        return int(self.weeknum)

    def get_playerid(self):
        return self.player


# Places game codes to their corresponding weeks
def game_dictionary():
    fp = open('games.csv', 'r')
    lines = fp.readlines()
    fp.close()

    game_list = []
    x = 0
    game_dict = {}
    for i in lines:
        i.strip()
        game_list.append(i.split(','))
        game_list = game_list[0]
        game_dict[game_list[0]] = game_list[2]
        
        game_list = []
        x = 0
    return game_dict


def player_dictionary():
    fp = open('players.csv', 'r')
    lines = fp.readlines()
    fp.close()

    data_list = []
    tree = 0
    player_dict = {}
    for i in lines:
        i.strip()
        data_list.append(i.split(','))
        data_list = data_list[0]
        tree = Player(data_list[0], data_list[3], data_list[5], data_list[6], data_list[1], data_list[2], data_list[4])
        player_dict[data_list[0]] = tree
        
        data_list = []
        tree = 0
    return player_dict


def play_dictionary():
    fg = open('pffScoutingData.csv', 'r')
    line = fg.readlines()
    fg.close()

    play_list = []
    pig = 0
    play_dict = {}
    for j in line:
        j.strip()
        play_list.append(j.split(','))
        play_list = play_list[0]
        
        pig = Play(play_list[1], play_list[2], play_list[8], play_list[9], play_list[10], play_list[11], play_list[0], weeknum = 0)
        play_dict[int(play_list[0]), int(play_list[2]), int(play_list[1])] = pig

        play_list = []
        pig = 0

    return play_dict





def main():
    game_dict = game_dictionary()
    player_dict = player_dictionary()
    play_dict = play_dictionary()

    for key in play_dict:
        gameid = play_dict[key].get_gameid()
        weeknum = game_dict[gameid]
        play_dict[key].set_weeknum(weeknum)
        weeknum = 0
        gameid = 0

    for ke in play_dict:
        weeknum = int(play_dict[ke].get_weeknum())
        player_id = play_dict[ke].get_playerid()
        player_ob = player_dict[player_id]

        if weeknum == 1:
            player_ob.set_week1(play_dict[ke].play_outcome())

        elif weeknum == 2:
            player_ob.set_week2(play_dict[ke].play_outcome())
    
        elif weeknum == 3:
            player_ob.set_week3(play_dict[ke].play_outcome())

        elif weeknum == 4:
            player_ob.set_week4(play_dict[ke].play_outcome())
    
        elif weeknum == 5:
            player_ob.set_week5(play_dict[ke].play_outcome())

        elif weeknum == 6:
            player_ob.set_week6(play_dict[ke].play_outcome())

        elif weeknum == 7:
            player_ob.set_week7(play_dict[ke].play_outcome())
    
        elif weeknum == 8:
            player_ob.set_week8(play_dict[ke].play_outcome())

    nyc = open("bdb-fatigue.csv" , 'w')
    nyc.write('name,age,position,height,weight,college,week,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80')
    nyc.write('\n')
    
# Not sure how to use a for loop to call all eight weeks automatically, so I will
# manually do each one
    
    string = ''
    for keys in player_dict:
        week = 1
        play_list = []
        play_list = player_dict[keys].get_week1()
        if len(play_list) != 0:
            if player_dict[keys].get_position() == 'T' or player_dict[keys].get_position() == 'G' or player_dict[keys].get_position() == 'C':
                for i in range(len(play_list)):
                    string += str(play_list[i])
                    string += ','
                string = string[:-1]
                nyc.write(f'{player_dict[keys].get_name()},{player_dict[keys].get_age()},{player_dict[keys].get_position()},{player_dict[keys].get_height()},{player_dict[keys].get_weight()},{player_dict[keys].get_college()},{week},{string}')
                string2 = ''
                blanks = 80 - len(play_list)
                for j in range(blanks):
                    string2 += ','
                    string2 += 'NA'
                nyc.write(string2)
                nyc.write('\n')
                string = ''
                string2 = ''
    string = ''
    for keys in player_dict:
        week = 2
        play_list = []
        play_list = player_dict[keys].get_week2()
        if len(play_list) != 0:
            if player_dict[keys].get_position() == 'T' or player_dict[keys].get_position() == 'G' or player_dict[keys].get_position() == 'C':
                for i in range(len(play_list)):
                    string += str(play_list[i])
                    string += ','
                string = string[:-1]
                nyc.write(f'{player_dict[keys].get_name()},{player_dict[keys].get_age()},{player_dict[keys].get_position()},{player_dict[keys].get_height()},{player_dict[keys].get_weight()},{player_dict[keys].get_college()},2,{string}')
                string2 = ''
                blanks = 82 - len(play_list)
                for j in range(blanks):
                    string2 += ','
                    string2 += 'NA'
                nyc.write(string2)
                nyc.write('\n')
                string = ''
                string2 = ''
    string = ''
    for keys in player_dict:
        week = 3
        play_list = []
        play_list = player_dict[keys].get_week3()
        if len(play_list) != 0:
            if player_dict[keys].get_position() == 'T' or player_dict[keys].get_position() == 'G' or player_dict[keys].get_position() == 'C':
                for i in range(len(play_list)):
                    string += str(play_list[i])
                    string += ','
                string = string[:-1]
                nyc.write(f'{player_dict[keys].get_name()},{player_dict[keys].get_age()},{player_dict[keys].get_position()},{player_dict[keys].get_height()},{player_dict[keys].get_weight()},{player_dict[keys].get_college()},3,{string}')
                string2 = ''
                blanks = 82 - len(play_list)
                for j in range(blanks):
                    string2 += ','
                    string2 += 'NA'
                nyc.write(string2)
                nyc.write('\n')
                string = ''
                string2 = ''
    string = ''
    for keys in player_dict:
        week = 4
        play_list = []
        play_list = player_dict[keys].get_week4()
        if len(play_list) != 0:
            if player_dict[keys].get_position() == 'T' or player_dict[keys].get_position() == 'G' or player_dict[keys].get_position() == 'C':
                for i in range(len(play_list)):
                    string += str(play_list[i])
                    string += ','
                string = string[:-1]
                nyc.write(f'{player_dict[keys].get_name()},{player_dict[keys].get_age()},{player_dict[keys].get_position()},{player_dict[keys].get_height()},{player_dict[keys].get_weight()},{player_dict[keys].get_college()},4,{string}')
                string2 = ''
                blanks = 82 - len(play_list)
                for j in range(blanks):
                    string2 += ','
                    string2 += 'NA'
                nyc.write(string2)
                nyc.write('\n')
                string = ''
                string2 = ''
    string = ''
    for keys in player_dict:
        week = 5
        play_list = []
        play_list = player_dict[keys].get_week5()
        if len(play_list) != 0:
            if player_dict[keys].get_position() == 'T' or player_dict[keys].get_position() == 'G' or player_dict[keys].get_position() == 'C':
                for i in range(len(play_list)):
                    string += str(play_list[i])
                    string += ','
                string = string[:-1]
                nyc.write(f'{player_dict[keys].get_name()},{player_dict[keys].get_age()},{player_dict[keys].get_position()},{player_dict[keys].get_height()},{player_dict[keys].get_weight()},{player_dict[keys].get_college()},5,{string}')
                string2 = ''
                blanks = 82 - len(play_list)
                for j in range(blanks):
                    string2 += ','
                    string2 += 'NA'
                nyc.write(string2)
                nyc.write('\n')
                string = ''
                string2 = ''

    string = ''
    for keys in player_dict:
        week = 6
        play_list = []
        play_list = player_dict[keys].get_week6()
        if len(play_list) != 0:
            if player_dict[keys].get_position() == 'T' or player_dict[keys].get_position() == 'G' or player_dict[keys].get_position() == 'C':
                for i in range(len(play_list)):
                    string += str(play_list[i])
                    string += ','
                string = string[:-1]
                nyc.write(f'{player_dict[keys].get_name()},{player_dict[keys].get_age()},{player_dict[keys].get_position()},{player_dict[keys].get_height()},{player_dict[keys].get_weight()},{player_dict[keys].get_college()},6,{string}')
                string2 = ''
                blanks = 82 - len(play_list)
                for j in range(blanks):
                    string2 += ','
                    string2 += 'NA'
                nyc.write(string2)
                nyc.write('\n')
                string = ''
                string2 = ''
    string = ''
    for keys in player_dict:
        week = 7
        play_list = []
        play_list = player_dict[keys].get_week7()
        if len(play_list) != 0:
            if player_dict[keys].get_position() == 'T' or player_dict[keys].get_position() == 'G' or player_dict[keys].get_position() == 'C':
                for i in range(len(play_list)):
                    string += str(play_list[i])
                    string += ','
                string = string[:-1]
                nyc.write(f'{player_dict[keys].get_name()},{player_dict[keys].get_age()},{player_dict[keys].get_position()},{player_dict[keys].get_height()},{player_dict[keys].get_weight()},{player_dict[keys].get_college()},7,{string}')
                string2 = ''
                blanks = 82 - len(play_list)
                for j in range(blanks):
                    string2 += ','
                    string2 += 'NA'
                nyc.write(string2)
                nyc.write('\n')
                string = ''
                string2 = ''
    string = ''
    for keys in player_dict:
        week = 8
        play_list = []
        play_list = player_dict[keys].get_week8()
        if len(play_list) != 0:
            if player_dict[keys].get_position() == 'T' or player_dict[keys].get_position() == 'G' or player_dict[keys].get_position() == 'C':
                for i in range(len(play_list)):
                    string += str(play_list[i])
                    string += ','
                string = string[:-1]
                nyc.write(f'{player_dict[keys].get_name()},{player_dict[keys].get_age()},{player_dict[keys].get_position()},{player_dict[keys].get_height()},{player_dict[keys].get_weight()},{player_dict[keys].get_college()},8,{string}')
                string2 = ''
                blanks = 82 - len(play_list)
                for j in range(blanks):
                    string2 += ','
                    string2 += 'NA'
                nyc.write(string2)
                nyc.write('\n')
                string = ''
                string2 = ''

    nyc.close()

if __name__ == '__main__':
    main()

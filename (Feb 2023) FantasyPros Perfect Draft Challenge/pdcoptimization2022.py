# Optimization model for Perfect Draft Challenge Fantasy Football 2022
import random

class playerOptimization:
    def __init__(self):
        # Best available players dictionary
        self.playerDicti = {"mccaffrey": ('rb'),
                    "ekeler": ('rb'),
                    "jefferson": ('wr'),
                    "adams": ('wr'),
                    "kelce": ('te'),
                    "diggs": ('wr'),
                    "lamb": ('wr'),
                    "barkley": ('rb'),
                    "chubb": ('rb'),
                    "hill": ('wr'),
                    "allen": ('qb'),
                    "Abrown": ('wr'),
                    "higgins": ('wr'),
                    "mahomes": ('qb'),
                    "kittle": ('te'),
                    "waddle": ('wr'),
                    "jacobs": ('rb'),
                    "hurts": ('qb'),
                    "amonra": ('wr'),
                    "Gdavis": ('wr'),
                    "hockenson": ('te'),
                    "pollard": ('rb'),
                    "Acooper": ('wr'),
                    "sanders": ('rb'),
                    "stevenson": ('rb'),
                    "aiyuk": ('wr'),
                    "devonta": ('wr'),
                    "walker": ('rb'),
                    "kirk": ('wr'),
                    "lockett": ('wr'),
                    "Jwilliams": ('rb'),
                    "Gwilson": ('wr'),
                    "mostert": ('rb'),
                    "boyd": ('wr'),
                    "allgeier": ('rb'),
                    "pacheco": ('rb'),
                    "palmer": ('wr'),
                    "watson": ('wr'),
                    "taysom": ('te'),
                    "meyers": ('wr'),
                    "engram": ('te'),
                    "Zjones": ('wr'),
                    "mckinnon": ('rb'),
                    "hollins": ('wr'),
                    "samuel": ('wr'),
                    "Gsmith": ('qb'),
                    "Djones": ('qb'),
                    "olave": ('wr'),
                    "wilson": ('rb')
                       }
        self.flexTE = 0
        self.flexWR = 0
        self.flexRB = 0

        # Potential Picks at each of the first 10 rounds of the simulator
        self.rd1 = ["mccaffrey", "ekeler", "jefferson"]
        self.rd2 = ["adams", "diggs", "kelce", "lamb", "barkley", "hill"]
        self.rd3 = ["allen", "Abrown", "higgins", "mahomes", "kittle"]
        self.rd4 = ["mahomes", "kittle", "waddle", "jacobs"]
        self.rd5 = ["hurts", "amonra", "Gdavis", "hockenson", "pollard", "lockett"]
        self.rd6 = ["Gdavis", "hockenson", "Acooper", "sanders", "pollard","stevenson", "lockett"]
        self.rd7 = ["hockenson","pollard","stevenson","aiyuk", "devonta","walker", "kirk", "lockett", "sanders"]
        self.rd8 = ["olave", "Jwilliams","Gwilson","stevenson","aiyuk", "devonta","walker", "kirk"]
        self.rd9 = ["olave", "Jwilliams","Gwilson","walker", "kirk"]
        self.rd10 = ["Jwilliams","mostert", "boyd","allgeier","pacheco","palmer", "watson", "taysom","meyers", "engram","Zjones","mckinnon","hollins", "samuel","Gsmith", "Djones","wilson"]
    
    # Initialize dictionary of all available players
    def initialDict(self):
        fp = open("realPerfectLineupData.csv", 'r')
        line = fp.readlines()
        fp.close()
        new_list = []

        for i in line:
            i.strip()
            new_list.append(i.split(','))

        for j in range(len(new_list)):
            player_list = new_list[j]
            sub_player_list = player_list[1:19]
            for i in range(0, len(sub_player_list)):
                sub_player_list[i] = float(sub_player_list[i])
            self.playerDicti[player_list[0]] = (self.playerDicti[player_list[0]], sub_player_list)

    # Randomize Selections in each round
    def generateIndices(self):
        rd1index = random.randint(0,len(self.rd1) - 1)
        rd2index = random.randint(0,len(self.rd2) - 1)
        rd3index = random.randint(0,len(self.rd3) - 1)
        rd4index = random.randint(0,len(self.rd4) - 1)
        rd5index = random.randint(0,len(self.rd5) - 1)
        rd6index = random.randint(0,len(self.rd6) - 1)
        rd7index = random.randint(0,len(self.rd7) - 1)
        rd8index = random.randint(0,len(self.rd8) - 1)
        rd9index = random.randint(0,len(self.rd9) - 1)
        rd10index = random.randint(0,len(self.rd10) - 1)
        rd11index = random.randint(0,len(self.rd10) - 1)
        rd12index = random.randint(0,len(self.rd10) - 1)
        rd13index = random.randint(0,len(self.rd10) - 1)
        rd14index = random.randint(0,len(self.rd10) - 1)
        
        return (rd1index, rd2index, rd3index, rd4index, rd5index, rd6index, rd7index, rd8index, rd9index, rd10index, rd11index, rd12index, rd13index, rd14index)
    
    # Create 1 sim of a draft round
    def draft(self, indices):
        draftList = []
        overallList = []
        #draft 1 person from each round
        overallList.append(self.rd1)
        overallList.append(self.rd2)
        overallList.append(self.rd3)
        overallList.append(self.rd4)
        overallList.append(self.rd5)
        overallList.append(self.rd6)
        overallList.append(self.rd7)
        overallList.append(self.rd8)
        overallList.append(self.rd9)
        overallList.append(self.rd10)
        overallList.append(self.rd10)
        overallList.append(self.rd10)
        overallList.append(self.rd10)
        overallList.append(self.rd10)
        overallList.append(self.rd10)
     
        for i in range(len(indices)):
            draftList.append(overallList[i][indices[i]])

        return draftList

    # Make sure you have proper positions to field a lineup
    def positionCompile(self, playerList):
        for i in range(len(playerList)):
            if playerList.count(playerList[i]) > 1:
                return "invalid"

        positionList = []
        for i in range(len(playerList)):
            positionList.append(self.playerDicti[playerList[i]])

        return positionList

    # Determine total points of this simulation
    def pointsSummation(self, positionList):
        qbList = []
        rbList = []
        wrList = []
        teList = []
        totalPoints = 0
        weekList = []
        
        for i in range(len(positionList)):
            if positionList[i][0] == "rb":
                rbList.append(positionList[i][1])
            elif positionList[i][0] == "wr":
                wrList.append(positionList[i][1])
            elif positionList[i][0] == "qb":
                qbList.append(positionList[i][1])
            elif positionList[i][0] == "te":
                teList.append(positionList[i][1])

        # Best Ball scoring so take best by week
        for i in range(18):
            for j in range(len(rbList)):
                weekList.append(rbList[j][i])
            totalPoints += self.positionCalc(weekList, 'rb')
            weekList = []

            for j in range(len(wrList)):
                weekList.append(wrList[j][i])
            totalPoints += self.positionCalc(weekList, 'wr')
            weekList = []

            for j in range(len(teList)):
                weekList.append(teList[j][i])
            totalPoints += self.positionCalc(weekList, 'te')
            weekList = []

            for j in range(len(qbList)):
                weekList.append(qbList[j][i])
            totalPoints += self.positionCalc(weekList, 'qb')
            weekList = []

            totalPoints += self.flexCalc(self.flexTE, self.flexWR, self.flexRB)

            self.flexTE = 0
            self.flexWR = 0
            self.flexRB = 0

        return totalPoints
    
    def positionCalc(self, weekScores, position):
        weekScores.sort(reverse = True)
        if len(weekScores) == 0:
            return 0

        elif(position == 'qb'):
             return weekScores[0]

        elif(position == 'def'):
            return weekScores[0]

        elif(position == 'te'):
            if(len(weekScores) > 1):
                self.flexTE = weekScores[1]
            return weekScores[0]

        elif(position == "rb"):
            if(len(weekScores) > 1):
                if(len(weekScores) > 2):
                    self.flexRB = weekScores[2]
                return weekScores[0] + weekScores[1]
            else:
                return weekScores[0]

        elif(position == "wr"):
            if(len(weekScores) > 3):
                self.flexWR = weekScores[3]
                return weekScores[0] + weekScores[1] + weekScores[2]
            elif(len(weekScores) > 2):
                return weekScores[0] + weekScores[1] + weekScores[2]
            elif(len(weekScores) > 1):
                return weekScores[0] + weekScores[1]
            else:
                return weekScores[0]

    # Determine who starts at flex each week
    def flexCalc(self, teValue, wrValue, rbValue):
        if ((rbValue > wrValue) and (rbValue > teValue)):
            return rbValue
        elif (wrValue > teValue):
            return wrValue
        else:
            return teValue

    def getInitialDict(self, player):
        return self.playerDicti[player]
    
def main():
    # Run a bunch of simulation and print the best sims
    # Analyze which players are targets in each round
    for i in range(1000000):

        test1 = playerOptimization()
        test1.initialDict()
        indices = test1.generateIndices()
        playerList = test1.draft(indices)
        positionPointList = test1.positionCompile(playerList)
        if (positionPointList == "invalid") == False: 
            if((test1.pointsSummation(positionPointList) + 158) > 2778):
                print(test1.pointsSummation(positionPointList) + 142)
                print(playerList)


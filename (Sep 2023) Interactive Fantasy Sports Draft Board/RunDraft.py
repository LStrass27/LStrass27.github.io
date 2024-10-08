import pandas as pd

# Set up positional arrays
overall = []
qbs = []
rbs = []
wrs = []
tes = []
defs = []
ks = []

df = pd.read_csv('UnivDynasty2023.csv', encoding='unicode_escape')

'''
Player Rater (PR) is the metric used to determine how good of a value a 
player is at the current moment in time. It is based upon a variety of factors:
overall rankings, positional rankings, and the player's performance against the 
remaining players available in each category.
'''

# This function resets PR after a player is removed
def resetPR(overall, qbs, rbs, wrs, tes, defs, ks, user_picks):
    # Constants for roster alignment
    # For flex add 40% to rbs and 60% to WRS
    num_teams = 12
    start_qb = 1
    start_rb = 2.4
    start_wr = 2.6
    start_te = 1
    start_def = 1
    start_k = 1

    for pick in user_picks:
        if((pick == "qb") and (start_qb > .2)):
            start_qb -= 0.8
        elif((pick == "rb") and (start_rb > .2)):
            start_rb -= 0.8
        elif((pick == "wr") and (start_wr > .2)):
            start_wr -= 0.8
        elif((pick == "te") and (start_te > .2)):
            start_te -= 0.8
        elif((pick == "def") and (start_def > .2)):
            start_def -= 0.8
        elif((pick == "k") and (start_k > .2)):
            start_k -= 0.8

        if(start_qb < .2):
            start_qb = .2
        if(start_rb < .2):
            start_rb = .2
        if(start_wr < .2):
            start_wr = .2
        if(start_te < .2):
            start_te = .2
        if(start_def < .2):
            start_def = .2
        if(start_k < .2):
            start_k = .2
            
    # Generate Average Values
    val = 0
    for i in range(5):
        val += overall[i][2]
    overall5 = val / 5

    val = 0
    for i in range(10):
        val += overall[i][2]
    overall10 = val/10

    val = 0
    for i in range(int(round(5 * start_qb))):
        val += qbs[i][1]
    qb5 = val / int(round((5 * start_qb)))

    val = 0
    for i in range(int(round(10 * start_qb))):
        val += qbs[i][1]
    qb10 = val/ int(round((10 * start_qb)))
    qbStart = qbs[int(round(num_teams * start_qb))][1]

    
    val = 0
    for i in range(int(round(5 * start_rb))):
        val += rbs[i][1]
    rb5 = val / int(round((5 * start_rb)))

    val = 0
    for i in range(int(round(10 * start_rb))):
        val += rbs[i][1]
    rb10 = val/int(round((10 * start_rb)))
    rbStart = rbs[int(round(num_teams * start_rb))][1]

    val = 0
    for i in range(int(round(5 * start_wr))):
        val += wrs[i][1]
    wr5 = val / int(round((5 * start_wr)))

    val = 0
    for i in range(int(round(10 * start_wr))):
        val += wrs[i][1]
    wr10 = val/int(round((10 * start_wr)))
    wrStart = wrs[int(round(num_teams * start_wr))][1]

    val = 0
    for i in range(int(round(5 * start_te))):
        val += tes[i][1]
    te5 = val / (int(round(5 * start_te)))

    val = 0
    for i in range(int(round(10 * start_te))):
        val += tes[i][1]
    te10 = val/ int(round((10 * start_te)))
    teStart = tes[int(round(num_teams * start_te))][1]

    val = 0
    for i in range(int(round(5 * start_def))):
        val += defs[i][1]
    def5 = val / int(round((5 * start_def)))

    val = 0
    for i in range(int(round(10 * start_def))):
        val += defs[i][1]
    def10 = val/ int((10 * start_def))
    defStart = defs[int(round(num_teams * start_def))][1]

    val = 0
    for i in range(int(round(5 * start_k))):
        val += ks[i][1]
    k5 = val / int(round((5 * start_k)))

    val = 0
    for i in range(int(round(10 * start_k))):
        val += ks[i][1]
    k10 = val/ int(round((10 * start_k)))
    kStart = ks[int(round(num_teams * start_k))][1]

# Update Ratings
    for i in range(len(qbs)):
        playerPoints = qbs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ qb5) + .15 * (playerPoints / qb10) + .4 * (playerPoints/qbStart))
        qbs[i][2] = calc
        
    for i in range(len(rbs)):
        playerPoints = rbs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ rb5) + .15 * (playerPoints / rb10) + .4 * (playerPoints/rbStart))
        rbs[i][2] = calc

    for i in range(len(wrs)):
        playerPoints = wrs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ wr5) + .15 * (playerPoints / wr10) + .4 * (playerPoints/wrStart))
        wrs[i][2] = calc

    for i in range(len(tes)):
        playerPoints = tes[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ te5) + .15 * (playerPoints / te10) + .4 * (playerPoints/teStart))
        tes[i][2] = calc

    for i in range(len(defs)):
        playerPoints = defs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ def5) + .15 * (playerPoints / def10) + .4 * (playerPoints/defStart))
        defs[i][2] = calc

    for i in range(len(ks)):
        playerPoints = ks[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ k5) + .15 * (playerPoints / k10) + .4 * (playerPoints/kStart))
        ks[i][2] = calc


    return overall, qbs, rbs, wrs, tes, defs, ks

# Start Function for the Interactive Interface
def runDraft(overall, qbs, rbs, wrs, tes, defs, ks):
    user_picks = []
    userPos = 'Luke' # Temp initialization value
    total_picks = 0
    printNew(overall, qbs, rbs, wrs, tes, defs, ks)
    found = False
    first = True
    while(userPos != "End"):
        if(found):
            printNew(overall, qbs, rbs, wrs, tes, defs, ks)
        elif(first == False):
            print("Player Not Found, Please Try Again")
            
        print('\n')
        userPos = input("Enter Position: ")
        userPlayer = input("Enter Player: ")
        userPick = input("Is this a User Pick (T or F): ")
        match userPick.lower():
            case "t":
                userPick = True
            case "f":
                userPick = False

        print(userPick)
        found = False
        count = 0

        # Search through each of the positional arrays for selected player
        if(userPos.lower() == 'qb'):
            while found != True and count < 100:
                if(qbs[count][0] == userPlayer):
                    last_player = qbs[count][0]
                    last_position = "qb"
                    last_points = qbs[count][1]
                    last_posInd = count
                    qbs.pop(count)
                    found = True
                    print(userPlayer, "has been removed")
                    print("\n")
                    total_picks += 1

                    if(userPick):
                        user_picks.append("qb")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                else:
                    count += 1

        elif(userPos.lower() == 'rb'):
            while found != True and count < 100:
                if(rbs[count][0] == userPlayer):
                    last_player = rbs[count][0]
                    last_position = "rb"
                    last_points = rbs[count][1]
                    last_posInd = count
                    rbs.pop(count)
                    found = True
                    print(userPlayer, "has been removed")
                    print("\n")
                    total_picks += 1

                    if(userPick):
                        user_picks.append("rb")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                else:
                    count += 1

        elif(userPos.lower() == 'wr'):
            while found != True and count < 100:
                if(wrs[count][0] == userPlayer):
                    last_player = wrs[count][0]
                    last_position = "wr"
                    last_points = wrs[count][1]
                    last_posInd = count
                    wrs.pop(count)
                    found = True
                    print(userPlayer, "has been removed")
                    print("\n")
                    total_picks += 1

                    if(userPick):
                        user_picks.append("wr")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                else:
                    count += 1

        elif(userPos.lower() == 'te'):
            while found != True and count < 100:
                if(tes[count][0] == userPlayer):
                    last_player = tes[count][0]
                    last_position = "te"
                    last_points = tes[count][1]
                    last_posInd = count
                    tes.pop(count)
                    found = True
                    print(userPlayer, "has been removed")
                    print("\n")
                    total_picks += 1

                    if(userPick):
                        user_picks.append("te")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                else:
                    count += 1

        elif(userPos.lower() == 'def'):
            while found != True and count < 100:
                if(defs[count][0] == userPlayer):
                    last_player = defs[count][0]
                    last_position = "def"
                    last_points = defs[count][1]
                    last_posInd = count
                    defs.pop(count)
                    found = True
                    print(userPlayer, "has been removed")
                    print("\n")
                    total_picks += 1

                    if(userPick):
                        user_picks.append("def")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                else:
                    count += 1

        elif(userPos.lower() == 'k'):
            while found != True and count < 100:
                if(ks[count][0] == userPlayer):
                    last_player = ks[count][0]
                    last_position = "k"
                    last_points = ks[count][1]
                    last_posInd = count
                    ks.pop(count)
                    found = True
                    print(userPlayer, "has been removed")
                    print("\n")
                    total_picks += 1

                    if(userPick):
                        user_picks.append("k")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                else:
                    count += 1

        # Undo the last player selection
        elif(userPos.lower() == 'undo'):
            overall.insert(lastOverallInd, [last_player, last_position, last_points, 0])
            found = True
            total_picks -= 1
            user_picks.pop()
            if(last_position.lower() == 'qb'):
                qbs.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'rb'):
                rbs.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'wr'):
                wrs.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'te'):
                tes.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'def'):
                defs.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'k'):
                ks.insert(last_posInd, [last_player, last_points, 0])

        elif(userPos.lower() == 'search'):
            for i in range(len(qbs)):
                if(userPlayer.lower() in qbs[i][0].lower()):
                    print("qb " + qbs[i][0] + " " + str(qbs[i][1]) + "\n")
            for i in range(len(rbs)):
                if(userPlayer.lower() in rbs[i][0].lower()):
                    print("rb " + rbs[i][0] + " " + str(rbs[i][1]) + "\n")
            for i in range(len(wrs)):
                if(userPlayer.lower() in wrs[i][0].lower()):
                    print("wr " + wrs[i][0] + " " + str(wrs[i][1]) + "\n")
            for i in range(len(tes)):
                if(userPlayer.lower() in tes[i][0].lower()):
                    print("te " + tes[i][0] + " " + str(tes[i][1]) + "\n")
            for i in range(len(defs)):
                if(userPlayer.lower() in defs[i][0].lower()):
                    print("def " + defs[i][0] + " " + str(defs[i][1]) + "\n")
            for i in range(len(ks)):
                if(userPlayer.lower() in ks[i][0].lower()):
                    print("k " + ks[i][0] + " " + str(ks[i][1]) + "\n")
            

        elif(userPos.lower() == 'count'):
            print("Pick total: ", total_picks)

        else:
            print("Position Not Found")

        first = False

        overall, qbs, rbs, wrs, tes, defs, ks = resetPR(overall, qbs, rbs, wrs, tes, defs, ks, user_picks)

# Print function to see leading players available by PR
def printNew(overall, qbs, rbs, wrs, tes, defs, ks):
    print ("{:<36} {:<36} {:<36} {:<36}".format('QBS','RBS','WRS','TES'))
    for i in range(20): # USUALLY 20
        PR = qbs[i][2]
        PR = "{:.3f}".format(PR)
        qb = str(PR) + " " +  qbs[i][0] + " " + str(qbs[i][1])
        PR = rbs[i][2]
        PR = "{:.3f}".format(PR)
        rb = str(PR)+ " " + rbs[i][0] + " " + str(rbs[i][1])
        PR = wrs[i][2]
        PR = "{:.3f}".format(PR)
        wr = str(PR)+ " "  + wrs[i][0] + " "  + str(wrs[i][1])
        PR = tes[i][2]
        PR = "{:.3f}".format(PR)
        te = str(PR) + " " + tes[i][0] + " " + str(tes[i][1])
   
        print ("{:<36} {:<36} {:<36} {:<36}".format(qb, rb, wr, te))

    print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

    print ("{:<36} {:<36} {:<36} {:<36}".format('DEFS','KS','Overall 1-10','Overall 11-20'))
    for i in range(10):
        PR = defs[i][2]
        PR = "{:.3f}".format(PR)
        defi = str(PR) + " " +  defs[i][0] + " " + str(defs[i][1])
        PR = ks[i][2]
        PR = "{:.3f}".format(PR)
        k = str(PR)+ " " + ks[i][0] + " " + str(ks[i][1])
        PR = overall[i][2]
        PR = "{:.3f}".format(PR)
        overall1 = str(PR)+ " "  + overall[i][0] + " "  + str(overall[i][1])
        PR = overall[i + 10][2]
        PR = "{:.3f}".format(PR)
        overall2 = str(PR) + " " + overall[i + 10][0] + " " + str(overall[i + 10][1])
   
        print ("{:<36} {:<36} {:<36} {:<36}".format(defi, k, overall1, overall2))

# Go through data and populate positional arrays
for index, row in df.iterrows():
    overall.append([row['Player'], row['Position'], row['Points'], 0])

    if(row['Position'] == 'QB'):
        qbs.append([row['Player'], row['Points'], 0])
    
    elif(row['Position'] == 'RB'):
        rbs.append([row['Player'], row['Points'], 0])

    elif(row['Position'] == 'WR'):
        wrs.append([row['Player'], row['Points'], 0])

    elif(row['Position'] == 'DEF'):
        defs.append([row['Player'], row['Points'], 0])

    elif(row['Position'] == 'K'):
        ks.append([row['Player'], row['Points'], 0])

    else:
        tes.append([row['Player'], row['Points'], 0])

# Append null values to end of positional arrays
# Ensures PR calculation doesn't fail
for i in range(100):
    overall.append(('N/A', 'QB', 1, 1))
    qbs.append(['N/A', 1, 1])
    rbs.append(['N/A', 1, 1])
    wrs.append(['N/A', 1, 1])
    tes.append(['N/A', 1, 1])
    defs.append(['N/A', 1, 1])
    ks.append(['N/A', 1, 1])

# Defense contains weird formatting
for j in range(len(defs)):
    defense = defs[j][0]
    defense = defense.replace(u'\xa0', u' ')
    defense = defense.strip()
    defs[j][0] = defense

BLANK_LIST = []
# Intialize PR for all players
overall, qbs, rbs, wrs, tes, defs, ks = resetPR(overall, qbs, rbs, wrs, tes, defs, ks, BLANK_LIST)

# Call the main interaction function
runDraft(overall, qbs, rbs, wrs, tes, defs, ks)

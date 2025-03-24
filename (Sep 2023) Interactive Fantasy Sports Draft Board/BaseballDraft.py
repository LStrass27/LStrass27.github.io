import pandas as pd

# Initialize positional arrays
overall = []
obs = []
sbs = []
sss = []
tbs = []
ofs = []
sps = []
rps = []
cs = []

df = pd.read_csv('FantasyBaseball.csv', encoding='utf-8-sig')

'''
Player Rater (PR) is the metric used to determine how good of a value a 
player is at the current moment in time. It is based upon a variety of factors:
overall rankings, positional rankings, and the player's performance against the 
remaining players available in each category.
'''

# This function resets PR after a player is removed
def resetPR(overall, obs, sbs, sss, tbs, ofs, sps, rps, cs):
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
    for i in range(5):
        val += obs[i][1]
    ob5 = val / 5

    val = 0
    for i in range(10):
        val += obs[i][1]
    ob10 = val/10
    obstart = obs[12][1]

    
    val = 0
    for i in range(5):
        val += sbs[i][1]
    sb5 = val / 5

    val = 0
    for i in range(10):
        val += sbs[i][1]
    sb10 = val/10
    sbstart = sbs[12][1]

    val = 0
    for i in range(5):
        val += sss[i][1]
    ss5 = val / 5

    val = 0
    for i in range(10):
        val += sss[i][1]
    ss10 = val/10
    ssstart = sss[12][1]

    val = 0
    for i in range(5):
        val += tbs[i][1]
    tb5 = val / 5

    val = 0
    for i in range(10):
        val += tbs[i][1]
    tb10 = val/ 10
    tbstart = tbs[12][1]

    val = 0
    for i in range(15):
        val += ofs[i][1]
    of5 = val / 15

    val = 0
    for i in range(30):
        val += ofs[i][1]
    of10 = val/30
    ofstart = ofs[36][1]

    val = 0
    for i in range(25):
        val += sps[i][1]
    sp5 = val / 25

    val = 0
    for i in range(50):
        val += sps[i][1]
    sp10 = val/ 50
    spstart = sps[60][1]

    val = 0
    for i in range(15):
        val += rps[i][1]
    rp5 = val / 15

    val = 0
    for i in range(30):
        val += rps[i][1]
    rp10 = val/ 30
    rpstart = rps[36][1]

    val = 0
    for i in range(5):
        val += cs[i][1]
    c5 = val / 5

    val = 0
    for i in range(10):
        val += cs[i][1]
    c10 = val/ 10
    cstart = cs[12][1]

# Update Ratings
    for i in range(len(obs)):
        playerPoints = obs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ ob5) + .15 * (playerPoints / ob10) + .4 * (playerPoints/obstart))
        obs[i][2] = calc
        
    for i in range(len(sbs)):
        playerPoints = sbs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ sb5) + .15 * (playerPoints / sb10) + .4 * (playerPoints/sbstart))
        sbs[i][2] = calc

    for i in range(len(sss)):
        playerPoints = sss[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ ss5) + .15 * (playerPoints / ss10) + .4 * (playerPoints/ssstart))
        sss[i][2] = calc

    for i in range(len(tbs)):
        playerPoints = tbs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ tb5) + .15 * (playerPoints / tb10) + .4 * (playerPoints/tbstart))
        tbs[i][2] = calc

    for i in range(len(ofs)):
        playerPoints = ofs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ of5) + .15 * (playerPoints / of10) + .4 * (playerPoints/ofstart))
        ofs[i][2] = calc

    for i in range(len(sps)):
        playerPoints = sps[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ sp5) + .15 * (playerPoints / sp10) + .4 * (playerPoints/spstart))
        sps[i][2] = calc

    for i in range(len(rps)):
        playerPoints = rps[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ rp5) + .15 * (playerPoints / rp10) + .4 * (playerPoints/rpstart))
        rps[i][2] = calc

    for i in range(len(cs)):
        playerPoints = cs[i][1]
        calc = (.15 * (playerPoints / overall5) + .1 * (playerPoints / overall10) + .2 * (playerPoints/ c5) + .15 * (playerPoints / c10) + .4 * (playerPoints/cstart))
        cs[i][2] = calc


    return overall, obs, sbs, sss, tbs, ofs, sps, rps, cs

# Main interactive function for the draft
def runDraft(overall, obs, sbs, sss, tbs, ofs, sps, rps, cs):
    total_picks = 0
    userPos = 'Luke' # Temporary initialization value
    printNew(overall, obs, sbs, sss, tbs, ofs, sps, rps, cs)
    found = False
    first = True
    while(userPos != "End"):
        if(found):
            printNew(overall, obs, sbs, sss, tbs, ofs, sps, rps, cs)
        elif(first == False):
            print("Player Not Found, Please Try Again")
            
        userPos = input("Enter Position: ")
        userPlayer = input("Enter Player: ")
        found = False
        count = 0
        if(userPos.lower() == '1b'):
            while found != True and count < 100:
                if(obs[count][0] == userPlayer):
                    last_player = obs[count][0]
                    last_position = "1b"
                    last_points = obs[count][1]
                    last_posInd = count
                    obs.pop(count)
                    found = True
                    total_picks += 1
                    print(userPlayer, "has been removed")
                    print("\n")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                            break;
                else:
                    count += 1

        elif(userPos.lower() == '2b'):
            while found != True and count < 100:
                if(sbs[count][0] == userPlayer):
                    last_player = sbs[count][0]
                    last_position = "2b"
                    last_points = sbs[count][1]
                    last_posInd = count
                    sbs.pop(count)
                    found = True
                    total_picks += 1
                    print(userPlayer, "has been removed")
                    print("\n")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                            break;
                else:
                    count += 1

        elif(userPos.lower() == 'ss'):
            while found != True and count < 100:
                if(sss[count][0] == userPlayer):
                    last_player = sss[count][0]
                    last_position = "ss"
                    last_points = sss[count][1]
                    last_posInd = count
                    sss.pop(count)
                    found = True
                    total_picks += 1
                    print(userPlayer, "has been removed")
                    print("\n")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                            break;
                else:
                    count += 1

        elif(userPos.lower() == '3b'):
            while found != True and count < 100:
                if(tbs[count][0] == userPlayer):
                    last_player = tbs[count][0]
                    last_position = "3b"
                    last_points = tbs[count][1]
                    last_posInd = count
                    tbs.pop(count)
                    found = True
                    total_picks += 1
                    print(userPlayer, "has been removed")
                    print("\n")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                            break;
                else:
                    count += 1

        elif(userPos.lower() == 'of'):
            while found != True and count < 100:
                if(ofs[count][0] == userPlayer):
                    last_player = ofs[count][0]
                    last_position = "of"
                    last_points = ofs[count][1]
                    last_posInd = count
                    ofs.pop(count)
                    found = True
                    total_picks += 1
                    print(userPlayer, "has been removed")
                    print("\n")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                            break;
                else:
                    count += 1

        elif(userPos.lower() == 'sp'):
            while found != True and count < 100:
                if(sps[count][0] == userPlayer):
                    last_player = sps[count][0]
                    last_position = "sp"
                    last_points = sps[count][1]
                    last_posInd = count
                    sps.pop(count)
                    found = True
                    total_picks += 1
                    print(userPlayer, "has been removed")
                    print("\n")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                            break;
                else:
                    count += 1
                    
        elif(userPos.lower() == 'rp'):
            while found != True and count < 100:
                if(rps[count][0] == userPlayer):
                    last_player = rps[count][0]
                    last_position = "rp"
                    last_points = rps[count][1]
                    last_posInd = count
                    rps.pop(count)
                    found = True
                    total_picks += 1
                    print(userPlayer, "has been removed")
                    print("\n")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                            break;
                else:
                    count += 1

        elif(userPos.lower() == 'c'):
            while found != True and count < 100:
                if(cs[count][0] == userPlayer):
                    last_player = cs[count][0]
                    last_position = "c"
                    last_points = cs[count][1]
                    last_posInd = count
                    cs.pop(count)
                    found = True
                    total_picks += 1
                    print(userPlayer, "has been removed")
                    print("\n")

                    for i in range(len(overall) - 1):
                        if(overall[i][0] == userPlayer):
                            lastOverallInd = i
                            overall.pop(i)
                            break;
                else:
                    count += 1

        # Function to undo the last pick
        elif(userPos.lower() == 'undo'):
            overall.insert(lastOverallInd, [last_player, last_position, last_points, 0])
            found = True
            if(last_position.lower() == '1b'):
                obs.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == '2b'):
                sbs.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'ss'):
                sss.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == '3b'):
                tbs.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'of'):
                ofs.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'sp'):
                sps.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'rp'):
                rps.insert(last_posInd, [last_player, last_points, 0])
            elif(last_position.lower() == 'c'):
                cs.insert(last_posInd, [last_player, last_points, 0])

        elif(userPos.lower() == 'search'):
            for i in range(len(obs)):
                if(userPlayer.lower() in obs[i][0].lower()):
                    print("1b " + obs[i][0] + " " + str(obs[i][1]) + "\n")
            for i in range(len(sbs)):
                if(userPlayer.lower() in sbs[i][0].lower()):
                    print("2b " + sbs[i][0] + " " + str(sbs[i][1]) + "\n")
            for i in range(len(sss)):
                if(userPlayer.lower() in sss[i][0].lower()):
                    print("ss " + sss[i][0] + " " + str(sss[i][1]) + "\n")
            for i in range(len(tbs)):
                if(userPlayer.lower() in tbs[i][0].lower()):
                    print("3b " + tbs[i][0] + " " + str(tbs[i][1]) + "\n")
            for i in range(len(ofs)):
                if(userPlayer.lower() in ofs[i][0].lower()):
                    print("of " + ofs[i][0] + " " + str(ofs[i][1]) + "\n")
            for i in range(len(sps)):
                if(userPlayer.lower() in sps[i][0].lower()):
                    print("sp " + sps[i][0] + " " + str(sps[i][1]) + "\n")
            for i in range(len(rps)):
                if(userPlayer.lower() in rps[i][0].lower()):
                    print("rp " + rps[i][0] + " " + str(rps[i][1]) + "\n")
            for i in range(len(cs)):
                if(userPlayer.lower() in cs[i][0].lower()):
                    print("c " + cs[i][0] + " " + str(cs[i][1]) + "\n")
            

        elif(userPos.lower() == 'count'):
            print("Pick total: ", total_picks) 
        
        else:
            print("Position Not Found")

        first = False

        overall, obs, sbs, sss, tbs, ofs, sps, rps, cs = resetPR(overall, obs, sbs, sss, tbs, ofs, sps, rps, cs)

# Prints out leading remaining PR data
def printNew(overall, obs, sbs, sss, tbs, ofs, sps, rps, cs):
    print ("{:<36} {:<36} {:<36} {:<36}".format('1b','2b','ss','3b'))
    for i in range(15):
        PR = obs[i][2]
        pts = obs[i][1]
        pts = "{:.3f}".format(pts)
        PR = "{:.3f}".format(PR)
        ob = str(PR) + " " +  obs[i][0] + " " + str(pts)
        PR = sbs[i][2]
        PR = "{:.3f}".format(PR)
        pts = sbs[i][1]
        pts = "{:.3f}".format(pts)
        sB = str(PR)+ " " + sbs[i][0] + " " + str(pts)
        PR = sss[i][2]
        PR = "{:.3f}".format(PR)
        pts = sss[i][1]
        pts = "{:.3f}".format(pts)
        ss = str(PR)+ " "  + sss[i][0] + " "  + str(pts)
        PR = tbs[i][2]
        pts = tbs[i][1]
        pts = "{:.3f}".format(pts)
        PR = "{:.3f}".format(PR)
        tb = str(PR) + " " + tbs[i][0] + " " + str(pts)
   
        print ("{:<36} {:<36} {:<36} {:<36}".format(ob, sB, ss, tb))

    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

    print ("{:<36} {:<36} {:<36} {:<36}".format('of','sp','rp','c'))
    for i in range(27):
        PR = ofs[i][2]
        PR = "{:.3f}".format(PR)
        pts = ofs[i][1]
        pts = "{:.3f}".format(pts)
        ofi = str(PR) + " " +  ofs[i][0] + " " + str(pts)
        PR = sps[i][2]
        pts = sps[i][1]
        pts = "{:.3f}".format(pts)
        PR = "{:.3f}".format(PR)
        sp = str(PR)+ " " + sps[i][0] + " " + str(pts)
        PR = rps[i][2]
        PR = "{:.3f}".format(PR)
        pts = rps[i][1]
        pts = "{:.3f}".format(pts)
        rp = str(PR) + " " +  rps[i][0] + " " + str(pts)
        PR = cs[i][2]
        PR = "{:.3f}".format(PR)
        pts = cs[i][1]
        pts = "{:.3f}".format(pts)
        c = str(PR)+ " " + cs[i][0] + " " + str(pts)
   
        print ("{:<36} {:<36} {:<36} {:<36}".format(ofi, sp, rp, c))

# Populate positional arrays
for index, row in df.iterrows():
    overall.append([row['Player'], row['Position'], row['Points'], 0])


    if(row['Position'] == '1B'):
        obs.append([row['Player'], row['Points'], 0])
    
    elif(row['Position'] == '2B'):
        sbs.append([row['Player'], row['Points'], 0])

    elif(row['Position'] == 'SS'):
        sss.append([row['Player'], row['Points'], 0])

    elif(row['Position'] == 'OF'):
        ofs.append([row['Player'], row['Points'], 0])

    elif(row['Position'] == 'SP'):
        sps.append([row['Player'], row['Points'], 0])

    elif(row['Position'] == 'RP'):
        rps.append([row['Player'], row['Points'], 0])

    elif(row['Position'] == 'C'):
        cs.append([row['Player'], row['Points'], 0])

    else:
        tbs.append([row['Player'], row['Points'], 0])

# Add null values to end of positional arrays to ensure the PR function doesn't fail
for i in range(100):
    overall.append(('N/A', '1b', 1, 1))
    obs.append(['N/A', 1, 1])
    sbs.append(['N/A', 1, 1])
    sss.append(['N/A', 1, 1])
    tbs.append(['N/A', 1, 1])
    ofs.append(['N/A', 1, 1])
    sps.append(['N/A', 1, 1])
    rps.append(['N/A', 1, 1])
    cs.append(['N/A', 1, 1])

overall, obs, sbs, sss, tbs, ofs, sps, rps, cs = resetPR(overall, obs, sbs, sss, tbs, ofs, sps, rps, cs)

# Call main function
runDraft(overall, obs, sbs, sss, tbs, ofs, sps, rps, cs)

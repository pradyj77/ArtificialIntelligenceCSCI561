import math

fin = open("input.txt", "r")
fout = open("output.txt", "w")

method = fin.readline()
color = fin.readline()
timeLeft = fin.readline()

boardConfig = []
temp = []
que = []
campGoingOutMoves = []
campGoingAwayMoves = []
outOfCampMoves = []
dirRow = [-1, +1, 0, 0, -1, -1, +1, +1]
dirCol = [0, 0, -1, +1, -1, +1, -1, +1]
myOwnList = []
bestMove = []
startingMoves = []

trial = ""
sampleList = []
for i in range(0, 16):
    trial = fin.readline().strip()
    sampleList = list(trial)
    boardConfig.append(sampleList)

campPosBlack = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1],
                [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1]]

campPosWhite = [[15, 15], [15, 14], [15, 13], [15, 12], [15, 11], [14, 15], [14, 14], [14, 13], [14, 12], [14, 11],
                [13, 15], [13, 14], [13, 13], [13, 12], [12, 15], [12, 14], [12, 13], [11, 15], [11, 14]]

def displayOut(arr, startX, startY):
    outputStr = ""
    if [startX, startY] in campPos:
        for i in range(0, len(arr)):
            currentMove = arr[i]
            length = len(currentMove)
            if length == 2:
                if [currentMove[0], currentMove[1]] not in campPos:
                    outputStr = outputStr + "E "
                    outputStr = outputStr + str(startY)
                    outputStr = outputStr + ","
                    outputStr = outputStr + str(startX)
                    outputStr = outputStr + " "
                    outputStr = outputStr + str(currentMove[1])
                    outputStr = outputStr + ","
                    outputStr = outputStr + str(currentMove[0])
                    fout.write(outputStr)
                    fout.write("\n")
                    exit(0)
            else:
                if [currentMove[length - 2], currentMove[length - 3]] not in campPos:
                    stars = 0
                    stars = currentMove.count('*')
                    i = 0
                    x = 0
                    y = 1
                    t = 1
                    for j in range(0, stars):
                        outputStr = outputStr + "J "
                        outputStr = outputStr + str(startY)
                        outputStr = outputStr + ","
                        outputStr = outputStr + str(startX)
                        outputStr = outputStr + " "
                        startX = currentMove[i]
                        startY = currentMove[i + 1]
                        while currentMove[i] != '*':
                            outputStr = outputStr + str(currentMove[t])
                            if currentMove[i + 1] != "*":
                                outputStr = outputStr + ","
                            t = t - 1
                            i += 1
                        t = t + 5
                        i += 1
                        outputStr = outputStr + " "

                        fout.write(outputStr)
                        fout.write("\n")
                        outputStr = ""
                    exit(0)

        currentMove = arr[0]
        if len(currentMove) == 2:
            outputStr = outputStr + "E "
            outputStr = outputStr + str(startY)
            outputStr = outputStr + ","
            outputStr = outputStr + str(startX)
            outputStr = outputStr + " "
            outputStr = outputStr + str(currentMove[1])
            outputStr = outputStr + ","
            outputStr = outputStr + str(currentMove[0])
            fout.write(outputStr)
            fout.write("\n")

        if len(currentMove) > 2:
            stars = 0
            stars = currentMove.count('*')
            i = 0
            x = 0
            y = 1
            t = 1
            for j in range(0, stars):
                outputStr = outputStr + "J "
                outputStr = outputStr + str(startY)
                outputStr = outputStr + ","
                outputStr = outputStr + str(startX)
                outputStr = outputStr + " "
                startX = currentMove[i]
                startY = currentMove[i + 1]
                while currentMove[i] != '*':
                    outputStr = outputStr + str(currentMove[t])
                    if currentMove[i + 1] != "*":
                        outputStr = outputStr + ","
                    t = t - 1
                    i += 1
                t = t + 5
                i += 1
                outputStr = outputStr + " "

                fout.write(outputStr)
                fout.write("\n")
                outputStr = ""
            exit(0)

    else:

        currentMove = arr[0]
        if len(currentMove) == 2:
            outputStr = outputStr + "E "
            outputStr = outputStr + str(startY)
            outputStr = outputStr + ","
            outputStr = outputStr + str(startX)
            outputStr = outputStr + " "
            outputStr = outputStr + str(currentMove[1])
            outputStr = outputStr + ","
            outputStr = outputStr + str(currentMove[0])
            fout.write(outputStr)
            fout.write("\n")

        if len(currentMove) > 2:
            stars = 0
            stars = currentMove.count('*')
            i = 0
            x = 0
            y = 1
            t = 1
            for j in range(0, stars):
                outputStr = outputStr + "J "
                outputStr = outputStr + str(startY)
                outputStr = outputStr + ","
                outputStr = outputStr + str(startX)
                outputStr = outputStr + " "
                startX = currentMove[i]
                startY = currentMove[i + 1]
                while currentMove[i] != '*':
                    outputStr = outputStr + str(currentMove[t])
                    if currentMove[i + 1] != "*":
                        outputStr = outputStr + ","
                    t = t - 1
                    i += 1
                t = t + 5
                i += 1
                outputStr = outputStr + " "

                fout.write(outputStr)
                fout.write("\n")
                outputStr = ""

def getMoves(rowPawn, colPawn):
    que = []
    for i in range(0, 8):
        myOwnList.clear()
        safe = []
        r1 = rowPawn + dirRow[i]
        c1 = colPawn + dirCol[i]
        if r1 < 0 or c1 < 0:
            continue
        if r1 > 15 or c1 > 15:
            continue

        if boardConfig[r1][c1] == '.':

            if [r1, c1] not in campPos:
                if pawnInOppCamp is False:
                    safe.append(r1)
                    safe.append(c1)
                    que.append(safe)
                else:
                    if [r1, c1] in oppCamp:
                        safe.append(r1)
                        safe.append(c1)
                        que.append(safe)
            else:
                if color.strip() == "BLACK":
                    if r1 >= rowPawn and c1 >= colPawn:
                        safe.append(r1)
                        safe.append(c1)
                        que.append(safe)
                if color.strip() == "WHITE":
                    if r1 <= rowPawn and c1 <= colPawn:
                        safe.append(r1)
                        safe.append(c1)
                        que.append(safe)

        else:
            if i == 0:
                if r1 - 1 > -1 and boardConfig[r1 - 1][c1] == '.':
                    if [r1 - 1, c1] not in campPos:
                        if pawnInOppCamp is False:
                            safe = [r1 - 1, c1, '*']
                            quick = jumpMoves(r1 - 1, c1)
                            if len(quick) != 0:
                                for i in range(0, len(quick)):
                                    safe.extend(quick[i])
                                    que.append(safe)
                                    safe = [r1 - 1, c1, '*']
                            else:
                                que.append(safe)
                        else:
                            if [r1 - 1, c1] in oppCamp:
                                safe = [r1 - 1, c1, '*']
                                quick = jumpMoves(r1 - 1, c1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1, '*']
                                else:
                                    que.append(safe)
                    else:
                        if color.strip() == "BLACK":
                            if r1 - 1 >= rowPawn and c1 >= colPawn:
                                safe = [r1 - 1, c1, '*']
                                quick = jumpMoves(r1 - 1, c1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1, '*']
                                else:
                                    que.append(safe)
                        if color.strip() == "WHITE":
                            if r1 - 1 <= rowPawn and c1 <= colPawn:
                                safe = [r1 - 1, c1, '*']
                                quick = jumpMoves(r1 - 1, c1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1, '*']
                                else:
                                    que.append(safe)
            if i == 1:
                if r1 + 1 < 16 and boardConfig[r1 + 1][c1] == '.':
                    if [r1 + 1, c1] not in campPos:
                        if pawnInOppCamp is False:
                            safe = [r1 + 1, c1, '*']
                            quick = jumpMoves(r1 + 1, c1)
                            if len(quick) != 0:
                                for i in range(0, len(quick)):
                                    safe.extend(quick[i])
                                    que.append(safe)
                                    safe = [r1 + 1, c1, '*']
                            else:
                                que.append(safe)
                        else:
                            if [r1 + 1, c1] in oppCamp:
                                safe = [r1 + 1, c1, '*']
                                quick = jumpMoves(r1 + 1, c1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1, '*']
                                else:
                                    que.append(safe)
                    else:
                        if color.strip() == "BLACK":
                            if r1 + 1 >= rowPawn and c1 >= colPawn:
                                safe = [r1 + 1, c1, '*']
                                quick = jumpMoves(r1 + 1, c1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1, '*']
                                else:
                                    que.append(safe)
                        if color.strip() == "WHITE":
                            if r1 + 1 <= rowPawn and c1 <= colPawn:
                                safe = [r1 + 1, c1, '*']
                                quick = jumpMoves(r1 + 1, c1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1, '*']
                                else:
                                    que.append(safe)
            if i == 2:
                if c1 - 1 > -1 and boardConfig[r1][c1 - 1] == '.':
                    if [r1, c1 - 1] not in campPos:
                        if pawnInOppCamp is False:
                            safe = [r1, c1 - 1, '*']
                            quick = jumpMoves(r1, c1 - 1)
                            if len(quick) != 0:
                                for i in range(0, len(quick)):
                                    safe.extend(quick[i])
                                    que.append(safe)
                                    safe = [r1, c1 - 1, '*']
                            else:
                                que.append(safe)
                        else:
                            if [r1, c1 - 1] in oppCamp:
                                safe = [r1, c1 - 1, '*']
                                quick = jumpMoves(r1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1, c1 - 1, '*']
                                else:
                                    que.append(safe)
                    else:
                        if color.strip() == "BLACK":
                            if r1 >= rowPawn and c1 - 1 >= colPawn:
                                safe = [r1, c1 - 1, '*']
                                quick = jumpMoves(r1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1, c1 - 1, '*']
                                else:
                                    que.append(safe)
                        if color.strip() == "WHITE":
                            if r1 <= rowPawn and c1 - 1 <= colPawn:
                                safe = [r1, c1 - 1, '*']
                                quick = jumpMoves(r1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1, c1 - 1, '*']
                                else:
                                    que.append(safe)
            if i == 3:
                if c1 + 1 < 16 and boardConfig[r1][c1 + 1] == '.':
                    if [r1, c1 + 1] not in campPos:
                        if pawnInOppCamp is False:
                            safe = [r1, c1 + 1, '*']
                            quick = jumpMoves(r1, c1 + 1)
                            if len(quick) != 0:
                                for i in range(0, len(quick)):
                                    safe.extend(quick[i])
                                    que.append(safe)
                                    safe = [r1, c1 + 1, '*']
                            else:
                                que.append(safe)
                        else:
                            if [r1, c1 + 1] in oppCamp:
                                safe = [r1, c1 + 1, '*']
                                quick = jumpMoves(r1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                    else:
                        if color.strip() == "BLACK":
                            if r1 >= rowPawn and c1 + 1 >= colPawn:
                                safe = [r1, c1 + 1, '*']
                                quick = jumpMoves(r1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                        if color.strip() == "WHITE":
                            if r1 <= rowPawn and c1 + 1 <= colPawn:
                                safe = [r1, c1 + 1, '*']
                                quick = jumpMoves(r1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1, c1 + 1, '*']
                                else:
                                    que.append(safe)
            if i == 4:
                if r1 - 1 > -1 and c1 - 1 > -1 and boardConfig[r1 - 1][c1 - 1] == '.':
                    if [r1 - 1, c1 - 1] not in campPos:
                        if pawnInOppCamp is False:
                            safe = [r1 - 1, c1 - 1, '*']
                            quick = jumpMoves(r1 - 1, c1 - 1)
                            if len(quick) != 0:
                                for i in range(0, len(quick)):
                                    safe.extend(quick[i])
                                    que.append(safe)
                                    safe = [r1 - 1, c1 - 1, '*']
                            else:
                                que.append(safe)
                        else:
                            if [r1 - 1, c1 - 1] in oppCamp:
                                safe = [r1 - 1, c1 - 1, '*']
                                quick = jumpMoves(r1 - 1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1 - 1, '*']
                                else:
                                    que.append(safe)
                    else:
                        if color.strip() == "BLACK":
                            if r1 - 1 >= rowPawn and c1 - 1 >= colPawn:
                                safe = [r1 - 1, c1 - 1, '*']
                                quick = jumpMoves(r1 - 1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1 - 1, '*']
                                else:
                                    que.append(safe)
                        if color.strip() == "WHITE":
                            if r1 - 1 <= rowPawn and c1 - 1 <= colPawn:
                                safe = [r1 - 1, c1 - 1, '*']
                                quick = jumpMoves(r1 - 1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1 - 1, '*']
                                else:
                                    que.append(safe)
            if i == 5:

                if r1 - 1 > -1 and c1 + 1 < 16 and boardConfig[r1 - 1][c1 + 1] == '.':
                    if [r1 - 1, c1 + 1] not in campPos:
                        if pawnInOppCamp is False:
                            safe = [r1 - 1, c1 + 1, '*']
                            quick = jumpMoves(r1 - 1, c1 + 1)
                            if len(quick) != 0:
                                for i in range(0, len(quick)):
                                    safe.extend(quick[i])
                                    que.append(safe)
                                    safe = [r1 - 1, c1 + 1, '*']
                            else:
                                que.append(safe)
                        else:
                            if [r1 - 1, c1 + 1] in oppCamp:
                                safe = [r1 - 1, c1 + 1, '*']
                                quick = jumpMoves(r1 - 1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                    else:
                        if color.strip() == "BLACK":
                            if r1 - 1 >= rowPawn and c1 + 1 >= colPawn:
                                safe = [r1 - 1, c1 + 1, '*']
                                quick = jumpMoves(r1 - 1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                        if color.strip() == "WHITE":
                            if r1 - 1 <= rowPawn and c1 + 1 <= colPawn:
                                safe = [r1 - 1, c1 + 1, '*']
                                quick = jumpMoves(r1 - 1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1 + 1, '*']
                                else:
                                    que.append(safe)
            if i == 6:
                if r1 + 1 < 16 and c1 - 1 > -1 and boardConfig[r1 + 1][c1 - 1] == '.':
                    if [r1 + 1, c1 - 1] not in campPos:
                        if pawnInOppCamp is False:
                            safe = [r1 + 1, c1 - 1, '*']
                            quick = jumpMoves(r1 + 1, c1 - 1)
                            if len(quick) != 0:
                                for i in range(0, len(quick)):
                                    safe.extend(quick[i])
                                    que.append(safe)
                                    safe = [r1 + 1, c1 - 1, '*']
                            else:
                                que.append(safe)
                        else:
                            if [r1 + 1, c1 - 1] in oppCamp:
                                safe = [r1 + 1, c1 - 1, '*']
                                quick = jumpMoves(r1 + 1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1 - 1, '*']
                                else:
                                    que.append(safe)
                    else:
                        if color.strip() == "BLACK":
                            if r1 + 1 >= rowPawn and c1 - 1 >= colPawn:
                                safe = [r1 + 1, c1 - 1, '*']
                                quick = jumpMoves(r1 + 1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1 - 1, '*']
                                else:
                                    que.append(safe)
                        if color.strip() == "WHITE":
                            if r1 + 1 <= rowPawn and c1 - 1 <= colPawn:
                                safe = [r1 + 1, c1 - 1, '*']
                                quick = jumpMoves(r1 + 1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1 - 1, '*']
                                else:
                                    que.append(safe)
            if i == 7:
                if r1 + 1 < 16 and c1 + 1 < 16 and boardConfig[r1 + 1][c1 + 1] == '.':
                    if [r1 + 1, c1 + 1] not in campPos:
                        if pawnInOppCamp is False:
                            safe = [r1 + 1, c1 + 1, '*']
                            quick = jumpMoves(r1 + 1, c1 + 1)
                            if len(quick) != 0:
                                for i in range(0, len(quick)):
                                    safe.extend(quick[i])
                                    que.append(safe)
                                    safe = [r1 + 1, c1 + 1, '*']
                            else:
                                que.append(safe)
                        else:
                            if [r1 + 1, c1 + 1] in oppCamp:
                                safe = [r1 + 1, c1 + 1, '*']
                                quick = jumpMoves(r1 + 1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                    else:
                        if color.strip() == "BLACK":
                            if r1 + 1 >= rowPawn and c1 + 1 >= colPawn:
                                safe = [r1 + 1, c1 + 1, '*']
                                quick = jumpMoves(r1 + 1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                        if color.strip() == "WHITE":
                            if r1 + 1 <= rowPawn and c1 + 1 <= colPawn:
                                safe = [r1 + 1, c1 + 1, '*']
                                quick = jumpMoves(r1 + 1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1 + 1, '*']
                                else:
                                    que.append(safe)

    return que

def jumpMoves(rowNum, colNum):
    que = []
    myOwnList.append([rowNum, colNum])
    for i in range(0, 8):

        r1 = rowNum + dirRow[i]
        c1 = colNum + dirCol[i]

        if r1 < 0 or c1 < 0:
            continue
        if r1 > 15 or c1 > 15:
            continue

        if boardConfig[r1][c1] != '.':
            if i == 0:
                if r1 - 1 > -1 and boardConfig[r1 - 1][c1] == '.':
                    temp = [r1 - 1, c1]
                    if temp not in myOwnList:
                        if temp not in campPos:
                            if [rowNum, colNum] not in oppCamp:
                                safe = [r1 - 1, c1, '*']
                                quick = jumpMoves(r1 - 1, c1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1, '*']
                                else:
                                    que.append(safe)
                            else:
                                if [r1 - 1, c1] in oppCamp:
                                    safe = [r1 - 1, c1, '*']
                                    quick = jumpMoves(r1 - 1, c1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1, '*']
                                    else:
                                        que.append(safe)
                        else:
                            if color.strip() == "BLACK":
                                if r1 - 1 >= rowNum and c1 >= colNum:
                                    safe = [r1 - 1, c1, '*']
                                    quick = jumpMoves(r1 - 1, c1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1, '*']
                                    else:
                                        que.append(safe)
                            if color.strip() == "WHITE":
                                if r1 - 1 <= rowNum and c1 <= colNum:
                                    safe = [r1 - 1, c1, '*']
                                    quick = jumpMoves(r1 - 1, c1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1, '*']
                                    else:
                                        que.append(safe)
            if i == 1:
                if r1 + 1 < 16 and boardConfig[r1 + 1][c1] == '.':
                    temp = [r1 + 1, c1]
                    if temp not in myOwnList:
                        if temp not in campPos:
                            if [rowNum, colNum] not in oppCamp:
                                safe = [r1 + 1, c1, '*']
                                quick = jumpMoves(r1 + 1, c1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1, '*']
                                else:
                                    que.append(safe)
                            else:
                                if [r1 + 1, c1] in oppCamp:
                                    safe = [r1 + 1, c1, '*']
                                    quick = jumpMoves(r1 + 1, c1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1, '*']
                                    else:
                                        que.append(safe)
                        else:
                            if color.strip() == "BLACK":
                                if r1 + 1 >= rowNum and c1 >= colNum:
                                    safe = [r1 + 1, c1, '*']
                                    quick = jumpMoves(r1 + 1, c1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1, '*']
                                    else:
                                        que.append(safe)
                            if color.strip() == "WHITE":
                                if r1 + 1 <= rowNum and c1 <= colNum:
                                    safe = [r1 + 1, c1, '*']
                                    quick = jumpMoves(r1 + 1, c1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1, '*']
                                    else:
                                        que.append(safe)
            if i == 2:
                if c1 - 1 > -1 and boardConfig[r1][c1 - 1] == '.':
                    temp = [r1, c1 - 1]
                    if temp not in myOwnList:
                        if temp not in campPos:
                            if [rowNum, colNum] not in oppCamp:
                                safe = [r1, c1 - 1, '*']
                                quick = jumpMoves(r1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1, c1 - 1, '*']
                                else:
                                    que.append(safe)
                            else:
                                if [r1, c1 - 1] in oppCamp:
                                    safe = [r1, c1 - 1, '*']
                                    quick = jumpMoves(r1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1, c1 - 1, '*']
                                    else:
                                        que.append(safe)
                        else:
                            if color.strip() == "BLACK":
                                if r1 >= rowNum and c1 - 1 >= colNum:
                                    safe = [r1, c1 - 1, '*']
                                    quick = jumpMoves(r1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1, c1 - 1, '*']
                                    else:
                                        que.append(safe)
                            if color.strip() == "WHITE":
                                if r1 <= rowNum and c1 - 1 <= colNum:
                                    safe = [r1, c1 - 1, '*']
                                    quick = jumpMoves(r1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1, c1 - 1, '*']
                                    else:
                                        que.append(safe)
            if i == 3:
                if c1 + 1 < 16 and boardConfig[r1][c1 + 1] == '.':
                    temp = [r1, c1 + 1]
                    if temp not in myOwnList:
                        if temp not in campPos:
                            if [rowNum, colNum] not in oppCamp:
                                safe = [r1, c1 + 1, '*']
                                quick = jumpMoves(r1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                            else:
                                if [r1, c1 + 1] in oppCamp:
                                    safe = [r1, c1 + 1, '*']
                                    quick = jumpMoves(r1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1, c1 + 1, '*']
                                    else:
                                        que.append(safe)
                        else:
                            if color.strip() == "BLACK":
                                if r1 >= rowNum and c1 + 1 >= colNum:
                                    safe = [r1, c1 + 1, '*']
                                    quick = jumpMoves(r1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1, c1 + 1, '*']
                                    else:
                                        que.append(safe)
                            if color.strip() == "WHITE":
                                if r1 <= rowNum and c1 + 1 <= colNum:
                                    safe = [r1, c1 + 1, '*']
                                    quick = jumpMoves(r1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1, c1 + 1, '*']
                                    else:
                                        que.append(safe)

            if i == 4:
                if r1 - 1 > -1 and c1 - 1 > -1 and boardConfig[r1 - 1][c1 - 1] == '.':
                    temp = [r1 - 1, c1 - 1]
                    if temp not in myOwnList:
                        if temp not in campPos:
                            if [rowNum, colNum] not in oppCamp:
                                safe = [r1 - 1, c1 - 1, '*']
                                quick = jumpMoves(r1 - 1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1, '*']
                                else:
                                    que.append(safe)
                            else:
                                if [r1 - 1, c1 - 1] in oppCamp:
                                    safe = [r1 - 1, c1 - 1, '*']
                                    quick = jumpMoves(r1 - 1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1, '*']
                                    else:
                                        que.append(safe)
                        else:
                            if color.strip() == "BLACK":
                                if r1 - 1 >= rowNum and c1 - 1 >= colNum:
                                    safe = [r1 - 1, c1 - 1, '*']
                                    quick = jumpMoves(r1 - 1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1, '*']
                                    else:
                                        que.append(safe)
                            if color.strip() == "WHITE":
                                if r1 - 1 <= rowNum and c1 - 1 <= colNum:
                                    safe = [r1 - 1, c1 - 1, '*']
                                    quick = jumpMoves(r1 - 1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1, '*']
                                    else:
                                        que.append(safe)

            if i == 5:
                if r1 - 1 > -1 and c1 + 1 < 16 and boardConfig[r1 - 1][c1 + 1] == '.':
                    temp = [r1 - 1, c1 + 1]
                    if temp not in myOwnList:
                        if temp not in campPos:
                            if [rowNum, colNum] not in oppCamp:
                                safe = [r1 - 1, c1 + 1, '*']
                                quick = jumpMoves(r1 - 1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 - 1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                            else:
                                if [r1 - 1, c1 + 1] in oppCamp:
                                    safe = [r1 - 1, c1 + 1, '*']
                                    quick = jumpMoves(r1 - 1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1 + 1, '*']
                                    else:
                                        que.append(safe)
                        else:
                            if color.strip() == "BLACK":
                                if r1 - 1 >= rowNum and c1 + 1 >= colNum:
                                    safe = [r1 - 1, c1 + 1, '*']
                                    quick = jumpMoves(r1 - 1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1 + 1, '*']
                                    else:
                                        que.append(safe)
                            if color.strip() == "WHITE":
                                if r1 - 1 <= rowNum and c1 + 1 <= colNum:
                                    safe = [r1 - 1, c1 + 1, '*']
                                    quick = jumpMoves(r1 - 1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 - 1, c1 + 1, '*']
                                    else:
                                        que.append(safe)
            if i == 6:
                if r1 + 1 < 16 and c1 - 1 > -1 and boardConfig[r1 + 1][c1 - 1] == '.':
                    temp = [r1 + 1, c1 - 1]
                    if temp not in myOwnList:
                        if temp not in campPos:
                            if [rowNum, colNum] not in oppCamp:
                                safe = [r1 + 1, c1 - 1, '*']
                                quick = jumpMoves(r1 + 1, c1 - 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1 - 1, '*']
                                else:
                                    que.append(safe)
                            else:
                                if [r1 + 1, c1 - 1] in oppCamp:
                                    safe = [r1 + 1, c1 - 1, '*']
                                    quick = jumpMoves(r1 + 1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1 - 1, '*']
                                    else:
                                        que.append(safe)
                        else:
                            if color.strip() == "BLACK":
                                if r1 + 1 >= rowNum and c1 - 1 >= colNum:
                                    safe = [r1 + 1, c1 - 1, '*']
                                    quick = jumpMoves(r1 + 1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1 - 1, '*']
                                    else:
                                        que.append(safe)
                            if color.strip() == "WHITE":
                                if r1 + 1 <= rowNum and c1 - 1 <= colNum:
                                    safe = [r1 + 1, c1 - 1, '*']
                                    quick = jumpMoves(r1 + 1, c1 - 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1 - 1, '*']
                                    else:
                                        que.append(safe)
            if i == 7:
                if r1 + 1 < 16 and c1 + 1 < 16 and boardConfig[r1 + 1][c1 + 1] == '.':
                    temp = [r1 + 1, c1 + 1]
                    if temp not in myOwnList:
                        if temp not in campPos:
                            if [rowNum, colNum] not in oppCamp:
                                safe = [r1 + 1, c1 + 1, '*']
                                quick = jumpMoves(r1 + 1, c1 + 1)
                                if len(quick) != 0:
                                    for i in range(0, len(quick)):
                                        safe.extend(quick[i])
                                        que.append(safe)
                                        safe = [r1 + 1, c1 + 1, '*']
                                else:
                                    que.append(safe)
                            else:
                                if [r1 + 1, c1 + 1] in oppCamp:
                                    safe = [r1 + 1, c1 + 1, '*']
                                    quick = jumpMoves(r1 + 1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1 + 1, '*']
                                    else:
                                        que.append(safe)
                        else:
                            if color.strip() == "BLACK":
                                if r1 + 1 >= rowNum and c1 + 1 >= colNum:
                                    safe = [r1 + 1, c1 + 1, '*']
                                    quick = jumpMoves(r1 + 1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1 + 1, '*']
                                    else:
                                        que.append(safe)
                            if color.strip() == "WHITE":
                                if r1 + 1 <= rowNum and c1 + 1 <= colNum:
                                    safe = [r1 + 1, c1 + 1, '*']
                                    quick = jumpMoves(r1 + 1, c1 + 1)
                                    if len(quick) != 0:
                                        for i in range(0, len(quick)):
                                            safe.extend(quick[i])
                                            que.append(safe)
                                            safe = [r1 + 1, c1 + 1, '*']
                                    else:
                                        que.append(safe)

    return que

def getPriority(board, cc, bool):

    outOfCampMoves = []
    campGoingAwayMoves = []
    campGoingOutMoves = []
    if bool:
        campPos = campPosBlack
        oppCamp = campPosWhite
        for i in range(0, 16):
            for j in range(0, 16):
                if board[i][j] == 'B' and [i, j] in campPos:
                    move = getMoves(i, j)
                    campPawn = True
                    if len(move) != 0:
                        if checkGoingOut(move):
                            eg = [i, j, move]
                            campGoingOutMoves.append(eg)

        for i in range(0, 16):
            for j in range(0, 16):
                if board[i][j] == 'B' and [i, j] in campPos:
                    move = getMoves(i, j)
                    if len(move) != 0:
                        if movingFromCenter(move, i, j):
                            eg = [i, j, move]
                            campGoingAwayMoves.append(eg)

        for i in range(0, 16):
            for j in range(0, 16):
                if board[i][j] == 'B' and [i, j] not in campPos:
                    if [i, j] in oppCamp:
                        pawnInOppCamp = True
                    else:
                        pawnInOppCamp = False
                    move = getMoves(i, j)
                    if len(move) != 0:
                        eg = [i, j, move]
                        outOfCampMoves.append(eg)

        if len(campGoingOutMoves) != 0:
            return campGoingOutMoves
        elif len(campGoingAwayMoves) != 0:
            return campGoingAwayMoves
        elif len(outOfCampMoves) != 0:
            return outOfCampMoves

    else:
        campPos = campPosWhite
        oppCamp = campPosBlack
        for i in range(15, -1, -1):
            for j in range(15, -1, -1):
               if boardConfig[i][j] == 'W' and [i, j] in campPos:
                    move = getMoves(i, j)
                    if len(move) != 0:
                        if checkGoingOut(move):
                            eg = [i, j, move]
                            campGoingOutMoves.append(eg)

        for i in range(15, -1, -1):
            for j in range(15, -1, -1):
                if boardConfig[i][j] == 'W' and [i, j] in campPos:
                    move = getMoves(i, j)
                    if len(move) != 0:
                        if movingFromCenter(move, i, j):
                            eg = [i, j, move]
                            campGoingAwayMoves.append(eg)

        for i in range(15, -1, -1):
            for j in range(15, -1, -1):
                if boardConfig[i][j] == 'W':
                    if [i, j] in oppCamp:
                        pawnInOppCamp = True
                    else:
                        pawnInOppCamp = False
                    move = getMoves(i, j)
                    if len(move) != 0:
                        eg = [i, j, move]
                        outOfCampMoves.append(eg)

        if len(campGoingOutMoves) != 0:
            return campGoingOutMoves
        elif len(campGoingAwayMoves) != 0:
            return campGoingAwayMoves
        elif len(outOfCampMoves) != 0:
            return outOfCampMoves


def checkGoingOut(arr):
    currentMove = []
    goingOut = False
    for i in range(0, len(arr)):

        currentMove = arr[i]
        length = len(currentMove)
        if len(currentMove) == 2:
            if [currentMove[0], currentMove[1]] not in campPos:
                goingOut = True
        if len(currentMove) > 2:
            if [currentMove[length - 2], currentMove[length - 3]] not in campPos:
                goingOut = True

    return goingOut


def movingFromCenter(arr, startX, startY):
    currentMove = []
    movingAway = False
    if color.strip() == "BLACK":
        for i in range(0, len(arr)):
            currentMove = arr[i]
            length = len(currentMove)
            if len(currentMove) == 2:
                if currentMove[0] >= startX and currentMove[1] >= startY:
                    movingAway = True
            else:
                if len(currentMove) > 2:
                    if currentMove[length - 2] >= int(startX) and currentMove[length - 3] >= int(startY):
                        movingAway = True
    else:
        if color.strip() == "WHITE":
            for i in range(0, len(arr)):
                currentMove = arr[i]
                length = len(currentMove)
                if len(currentMove) == 2:
                    if currentMove[0] <= startX and currentMove[1] <= startY:
                        movingAway = True
                else:
                    if len(currentMove) > 2:
                        if currentMove[length - 2] <= startX and currentMove[length - 3] <= startY:
                            movingAway = True
    return movingAway

def alphaBeta(board, depth, a, b, playerMax):

    possibleMoves = []
    bestvalue = a
    bestmove = []
    if depth == 0:
        return evaluate(board)
    if playerMax:
        value = float("-inf")
        possibleMoves = getPriority(board, cc, True)
        ans1 = possibleMoves[0]
        ans2 = ans1[2]
        ans3 = ans2[0]
        global bestMove
        bestMove = ans3
        global startingMoves
        startingMoves = [ans1[0], ans1[1]]

        for i in range(0, len(possibleMoves)):
            currentMoves = possibleMoves[i]
            startX = currentMoves[0]
            startY = currentMoves[1]
            moveNow = currentMoves[2]
            for i in range(0, len(moveNow)):
                if len(moveNow[i]) == 2:
                    newX = moveNow[i][0]
                    newY = moveNow[i][1]
                    board[startX][startY] = '.'
                    board[newX][newY] = mychar
                elif len(moveNow[i]) > 2:
                    newY = moveNow[i][len(moveNow[i]) - 2]
                    newX = moveNow[i][len(moveNow[i]) - 3]
                    board[startX][startY] = '.'
                    board[newX][newY] = mychar
                value = max(value, alphaBeta(board, depth - 1, a, b, False))
                board[newX][newY] = '.'
                board[startX][startY] = mychar
                if value >= b:
                    return value
                bestvalue = a
                a = max(a, value)
                if a != bestvalue:
                    bestMove = moveNow[i]
                    startingMoves = [startX, startY]
        return value
    else:
        value = float("inf")
        possibleMoves = getPriority(board, cc, False)
        for i in range(0, len(possibleMoves)):
            currentMoves = possibleMoves[i]
            startX = currentMoves[0]
            startY = currentMoves[1]
            moveNow = currentMoves[2]
            for i in range(0, len(moveNow)):
                if len(moveNow[i]) == 2:
                    newX = moveNow[i][0]
                    newY = moveNow[i][1]
                    board[startX][startY] = '.'
                    board[newX][newY] = oppchar
                elif len(moveNow[i]) > 2:
                    newY = moveNow[i][len(moveNow[i]) - 2]
                    newX = moveNow[i][len(moveNow[i]) - 3]
                    board[startX][startY] = '.'
                    board[newX][newY] = oppchar
                value = min(value, alphaBeta(board, depth - 1, a, b, True))
                board[newX][newY] = '.'
                board[startX][startY] = oppchar
                if value <= a:
                    return value
                b = min(b, value)
        return value


def evaluate(boardPos):
    if cc == "BLACK":
        opp = campPosWhite
        distanceBlack = 0
        distPos = 0
        distNeg = 0
        distFromCentre = 0
        finalDistance = 0
        for i in range(0, 16):
            for j in range(0, 16):
                if boardPos[i][j] == 'B':
                    currentX = i
                    currentY = j
                    for temp in opp:
                        distanceBlack = distanceBlack + math.sqrt((temp[1] - currentY) ** 2 + (temp[0] - currentX) ** 2)

        distanceBlack = distanceBlack * -1

        for i in range(0, 16):
            for j in range(0, 16):
                if boardPos[i][j] == 'B':
                    currentX = i
                    currentY = j
                    if i > j:
                        numerator = i - j
                        denom = math.sqrt(i**2 + j**2)
                        distPos = distPos + numerator / denom
                    if j > i:
                        numerator = i - j
                        denom = math.sqrt(i**2 + j**2)
                        distNeg = distNeg + numerator/denom

                    distFromCentre = distFromCentre + distPos + (-1 * distNeg)

        distFromCentre = distFromCentre * -1
        finalDistance = distFromCentre + distanceBlack
        return finalDistance
    else:
        opp = campPosBlack
        distanceWhite = 0
        distPos = 0
        distNeg = 0
        distFromCentre = 0
        finalDistance = 0
        for i in range(0, 16):
            for j in range(0, 16):
                if boardPos[i][j] == 'W':
                    currentX = i
                    currentY = j
                    for temp in opp:
                        distanceWhite = distanceWhite + math.sqrt((temp[1] - currentY) ** 2 + (temp[0] - currentX) ** 2)

        distanceWhite = distanceWhite * -1

        for i in range(0, 16):
            for j in range(0, 16):
                if boardPos[i][j] == 'W':
                    currentX = i
                    currentY = j
                    if i > j:
                        numerator = i - j
                        denom = math.sqrt(i ** 2 + j ** 2)
                        distPos = distPos + numerator / denom
                    if j > i:
                        numerator = i - j
                        denom = math.sqrt(i ** 2 + j ** 2)
                        distNeg = distNeg + numerator / denom

                    distFromCentre = distFromCentre + distPos + (-1 * distNeg)

        distFromCentre = distFromCentre * -1
        finalDistance = distFromCentre + distanceWhite
        return finalDistance

def display(arr, startX, startY):
    outputStr = ""
    currentMove = arr
    if len(currentMove) == 2:
        outputStr = outputStr + "E "
        outputStr = outputStr + str(startY)
        outputStr = outputStr + ","
        outputStr = outputStr + str(startX)
        outputStr = outputStr + " "
        outputStr = outputStr + str(currentMove[1])
        outputStr = outputStr + ","
        outputStr = outputStr + str(currentMove[0])
        fout.write(outputStr)
        fout.write("\n")

    if len(currentMove) > 2:
        stars = 0
        stars = currentMove.count('*')
        i = 0
        x = 0
        y = 1
        t = 1
        for j in range(0, stars):
            outputStr = outputStr + "J "
            outputStr = outputStr + str(startY)
            outputStr = outputStr + ","
            outputStr = outputStr + str(startX)
            outputStr = outputStr + " "
            startX = currentMove[i]
            startY = currentMove[i + 1]
            while currentMove[i] != '*':
                outputStr = outputStr + str(currentMove[t])
                if currentMove[i + 1] != "*":
                    outputStr = outputStr + ","
                t = t - 1
                i += 1
            t = t + 5
            i += 1
            outputStr = outputStr + " "

            fout.write(outputStr)
            fout.write("\n")
            outputStr = ""



if method.strip() == "SINGLE":
    if color.strip() == "BLACK":
        dirRow = [-1, +1, 0, 0, -1, -1, +1, +1]
        dirCol = [0, 0, -1, +1, -1, +1, -1, +1]
        campPawn = False
        pawnInOppCamp = False
        campPos = campPosBlack
        oppCamp = campPosWhite

        for i in range(0, 16):
            for j in range(0, 16):
                que = []
                if boardConfig[i][j] == 'B' and [i, j] in campPos:
                    move = getMoves(i, j)
                    campPawn = True
                    if len(move) != 0:
                        if checkGoingOut(move):
                            displayOut(move, i, j)
                            exit(0)

        for i in range(0, 16):
            for j in range(0, 16):
                que = []
                if boardConfig[i][j] == 'B' and [i, j] in campPos:
                    move = getMoves(i, j)
                    if len(move) != 0:
                        if movingFromCenter(move, i, j):
                            displayOut(move, i, j)
                            exit(0)

        for i in range(0, 16):
            for j in range(0, 16):
                que = []
                if boardConfig[i][j] == 'B' and [i, j] not in campPos:
                    if [i, j] in campPosWhite:
                        pawnInOppCamp = True
                    else:
                        pawnInOppCamp = False
                    move = getMoves(i, j)
                    if len(move) != 0:
                        displayOut(move, i, j)
                        exit(0)

    else:
        pawnInOppCamp = False
        dirRow = [-1, +1, 0, 0, -1, -1, +1, +1]
        dirCol = [0, 0, -1, +1, -1, +1, -1, +1]
        campPawn = False
        campPos = campPosWhite
        oppCamp = campPosBlack
        for i in range(15, -1, -1):
            for j in range(15, -1, -1):
                que = []
                if boardConfig[i][j] == 'W' and [i, j] in campPos:
                    move = getMoves(i, j)
                    if len(move) != 0:
                        if checkGoingOut(move):
                            displayOut(move, i, j)
                            exit(0)

        for i in range(0, 16):
            for j in range(0, 16):
                que = []
                if boardConfig[i][j] == 'W' and [i, j] in campPos:
                    move = getMoves(i, j)
                    if len(move) != 0:
                        if movingFromCenter(move, i, j):
                            displayOut(move, i, j)
                            exit(0)

        for i in range(15, -1, -1):
            for j in range(15, -1, -1):
                que = []
                if boardConfig[i][j] == 'W':
                    if [i, j] in campPosBlack:
                        pawnInOppCamp = True
                    else:
                        pawnInOppCamp = False
                    move = getMoves(i, j)
                    if len(move) != 0:
                        displayOut(move, i, j)
                        exit(0)


elif method.strip() == "GAME":
    cc = color.strip()
    if color.strip() == "BLACK":
        mychar = 'B'
        oppchar = 'W'
        depth = 2
        campPawn = False
        pawnInOppCamp = False
        campPos = campPosBlack
        oppCamp = campPosWhite
        alpha = float("-inf")
        beta = float("inf")
        utility = alphaBeta(boardConfig, depth, alpha, beta, True)
        display(bestMove, startingMoves[0], startingMoves[1])
        bestMove = []
        startingMoves = []

    else:
        mychar = 'W'
        oppchar = 'B'
        depth = 2
        pawnInOppCamp = False
        campPawn = False
        campPos = campPosWhite
        oppCamp = campPosBlack
        alpha = float("-inf")
        beta = float("inf")
        utility = alphaBeta(boardConfig, depth, alpha, beta, True)
        display(bestMove, startingMoves[0], startingMoves[1])
        bestMove = []
        startingMoves = []

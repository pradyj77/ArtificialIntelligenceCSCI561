f = open("inputUCS.txt", "r")

method = f.readline()

width, height = f.readline().split()
w = int(width)
h = int(height)

landingX, landingY = f.readline().split()
startX = int(landingY)
startY = int(landingX)

maxDiff = f.readline()
maxDiff = int(maxDiff)

numTarget = f.readline()

targetMatrix = []
for i in range(0, int(numTarget)):
    a, b = f.readline().strip().split()
    ans = [int(b), int(a)]
    targetMatrix.append(ans)

siteMatrix = []
trial = []
for i in range(0, int(height)):
    trial = f.readline().strip().split()
    siteMatrix.append(trial)
# print(siteMatrix)
for targetLocation in range(0, int(numTarget)):

    if method.strip() == "A*":
        print("A*")

    elif method.strip() == "BFS":

        def childCells(row, col):
            for i in range(0, 8):
                r1 = row + dirRow[i]
                c1 = col + dirCol[i]
                if r1 < 0 or c1 < 0:
                    continue
                if r1 >= h or c1 >= w:
                    continue
                if isVisited[r1][c1]:
                    continue
                if int(siteMatrix[r1][c1]) - int(siteMatrix[row][col]) > maxDiff or int(siteMatrix[row][col]) - int(
                        siteMatrix[r1][c1]) > maxDiff:
                    continue

                rowQ.append(r1)
                colQ.append(c1)
                isVisited[r1][c1] = True
                parentX[r1][c1] = row
                parentY[r1][c1] = col


        def pathToTarget(s, xtarget, ytarget, parX, parY):
            shortestPath = []

            while parX[xtarget][ytarget] != None and parY[xtarget][ytarget] != None:
                tempX = xtarget
                tempY = ytarget
                path = []

                path.append(ytarget)
                path.append(xtarget)
                shortestPath.append(path)
                xtarget = parX[tempX][tempY]
                ytarget = parY[tempX][tempY]

            start = [startY, startX]
            shortestPath.append(start)
            shortestPath.reverse()
            for item in shortestPath:
                print(str(item[0]) + "," + str(item[1]) + " ", end='')
            print()


        rowQ = []
        colQ = []
        reachedTarget = False
        isVisited = []
        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(False)
            isVisited.append(sample)
        parentX = []
        parentY = []
        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(None)
            parentX.append(sample)

        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(None)
            parentY.append(sample)

        dirRow = [-1, +1, 0, 0, -1, -1, +1, +1]
        dirCol = [0, 0, -1, +1, -1, +1, -1, +1]

        rowQ.append(startX)
        colQ.append(startY)
        isVisited[startX][startY] = True

        while len(rowQ) > 0:
            r = rowQ.pop(0)
            c = colQ.pop(0)
            if r == targetMatrix[targetLocation][0] and c == targetMatrix[targetLocation][1]:
                reachedTarget = True
                break
            childCells(r, c)

        if reachedTarget:
            pathToTarget(siteMatrix[startX][startY], targetMatrix[targetLocation][0], targetMatrix[targetLocation][1],
                         parentX, parentY)
        else:
            print("FAIL")

    elif method.strip() == "UCS":
        def childCells(row, col):
            for i in range(0, 8):
                safe = []
                r1 = row + dirRow[i]
                c1 = col + dirCol[i]

                if r1 < 0 or c1 < 0:
                    continue
                if r1 >= h or c1 >= w:
                    continue
                if int(siteMatrix[r1][c1]) - int(siteMatrix[row][col]) > maxDiff or int(siteMatrix[row][col]) - int(
                        siteMatrix[r1][c1]) > maxDiff:
                    continue

                if dirRow[i] != 0 and dirCol[i] != 0:
                    if isVisited[r1][c1]:
                        if costArr[r1][c1] > costArr[row][col] + 1:
                            costArr[r1][c1] = costArr[row][col] + 1
                        continue
                else:
                    if isVisited[r1][c1]:
                        if costArr[r1][c1] > costArr[row][col] + 10:
                            costArr[r1][c1] = costArr[row][col] + 10
                        continue

                if dirRow[i] != 0 and dirCol[i] != 0:
                    costArr[r1][c1] = costArr[row][col] + 1
                else:
                    costArr[r1][c1] = costArr[row][col] + 10

                safe.append(r1)
                safe.append(c1)
                que.append(safe)
                # colQ.append(c1)
                isVisited[r1][c1] = True
                parentX[r1][c1] = row
                parentY[r1][c1] = col


        def pathToTarget(s, xtarget, ytarget, parX, parY):
            shortestPath = []

            while parX[xtarget][ytarget] != None and parY[xtarget][ytarget] != None:
                tempX = xtarget
                tempY = ytarget
                path = []

                path.append(ytarget)
                path.append(xtarget)
                shortestPath.append(path)
                xtarget = parX[tempX][tempY]
                ytarget = parY[tempX][tempY]

            start = [startY, startX]
            shortestPath.append(start)
            shortestPath.reverse()
            for item in shortestPath:
                print(str(item[0]) + "," + str(item[1]) + " ", end='')
            print()


        def getIndex(value, arr):
            for i in range(0, h):
                for j in range(0, w):
                    if arr[i][j] == value:
                        if not isVisitedForMin[i][j]:
                            isVisitedForMin[i][j] = True
                            return i, j


        # rowQ = []
        # colQ = []
        que = []
        safe = [startX, startY]
        que.append(safe)
        print(que)
        tempIndex = 0

        reachedTarget = False

        dirRow = [-1, +1, 0, 0, -1, -1, +1, +1]
        dirCol = [0, 0, -1, +1, -1, +1, -1, +1]

        # costDict = {}
        costArr = []
        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(0)
            costArr.append(sample)

        costArr[startX][startY] = 0

        isVisited = []
        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(False)
            isVisited.append(sample)

        isVisitedForMin = []
        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(False)
            isVisitedForMin.append(sample)

        parentX = []
        parentY = []
        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(None)
            parentX.append(sample)

        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(None)
            parentY.append(sample)

        # rowQ.append(startX)
        # colQ.append(startY)
        # safe.append(startX)
        # safe.append(startY)
        # que.append(safe)
        # print(que)
        isVisited[startX][startY] = True

        while len(que) > 0:
            # print(rowQ)
            # print(colQ)
            # print(costArr)
            print(que)
            minimum = costArr[que[0][0]][que[0][1]]
            for i in range(1, len(que)):
                if costArr[que[i][0]][que[i][1]] < minimum:
                    minimum = costArr[que[i][0]][que[i][1]]
            print(minimum)
            rowNum, colNum = getIndex(minimum, costArr)
            for i in range(0, len(que)):
                if que[i] == [rowNum, colNum]:
                    tempIndex = i
                    break
            print(rowNum, colNum)
            que.pop(tempIndex)
            #colQ.remove(colNum)
            # print(rowQ)
            # print(colQ)
            childCells(rowNum, colNum)
        if costArr[targetMatrix[targetLocation][0]][targetMatrix[targetLocation][1]] != 0:
            reachedTarget = True
        if reachedTarget:
            print("Path cost is:", costArr[targetMatrix[targetLocation][0]][targetMatrix[targetLocation][1]])
            pathToTarget(siteMatrix[startX][startY], targetMatrix[targetLocation][0], targetMatrix[targetLocation][1],
                         parentX, parentY)
        else:
            print("FAIL")

f.close()

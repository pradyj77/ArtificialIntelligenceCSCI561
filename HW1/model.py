f = open("input.txt", "r")
f1 = open("output.txt", "w")
import math

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

for targetLocation in range(0, int(numTarget)):
    if method.strip() == "A*":
        def childCells(row, col):
            cost = 0
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
                    cost = computeF(r1, c1, row, col, 14)
                    if isVisited[r1][c1]:
                        if costArr[r1][c1] > costArr[row][col] + cost:
                            costArr[r1][c1] = costArr[row][col] + cost
                            parentX[r1][c1] = row
                            parentY[r1][c1] = col
                        continue
                else:
                    cost = computeF(r1, c1, row, col, 10)
                    if isVisited[r1][c1]:
                        if costArr[r1][c1] > costArr[row][col] + cost:
                            costArr[r1][c1] = costArr[row][col] + cost
                            parentX[r1][c1] = row
                            parentY[r1][c1] = col
                        continue

                costArr[r1][c1] = costArr[row][col] + cost
                safe.append(r1)
                safe.append(c1)
                que.append(safe)
                isVisited[r1][c1] = True
                parentX[r1][c1] = row
                parentY[r1][c1] = col


        def computeF(x, y, a, b, cost):

            elevationDiff = abs(int(siteMatrix[x][y]) - int(siteMatrix[a][b]))
            totalG = elevationDiff + cost
            totalH = 10 * (
                math.sqrt((targetMatrix[targetLocation][0] - x) ** 2 + (targetMatrix[targetLocation][1] - y) ** 2))
            totalF = totalG + totalH
            return totalF


        def pathToTarget(s, xtarget, ytarget, parX, parY):
            shortestPath = []

            while parX[xtarget][ytarget] != None and parY[xtarget][ytarget] != None:
                tempX = xtarget
                tempY = ytarget
                path = [ytarget, xtarget]
                shortestPath.append(path)
                xtarget = parX[tempX][tempY]
                ytarget = parY[tempX][tempY]

            start = [startY, startX]
            shortestPath.append(start)
            shortestPath.reverse()
            output = ""
            for item in shortestPath:
                output = output + (str(item[0]) + "," + str(item[1]) + " ")
            f1.write(output)
            f1.write("\n")


        def getIndex(value, arr):
            for i in range(0, h):
                for j in range(0, w):
                    if arr[i][j] == value:
                        if not isVisitedForMin[i][j]:
                            isVisitedForMin[i][j] = True
                            return i, j


        que = []
        safe = [startX, startY]
        que.append(safe)
        tempIndex = 0
        reachedTarget = False
        dirRow = [-1, +1, 0, 0, -1, -1, +1, +1]
        dirCol = [0, 0, -1, +1, -1, +1, -1, +1]
        costArr = []

        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(None)
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

        isVisited[startX][startY] = True

        while len(que) > 0:
            minimum = costArr[que[0][0]][que[0][1]]
            for i in range(1, len(que)):
                if costArr[que[i][0]][que[i][1]] < minimum:
                    minimum = costArr[que[i][0]][que[i][1]]
            rowNum, colNum = getIndex(minimum, costArr)
            for i in range(0, len(que)):
                if que[i] == [rowNum, colNum]:
                    tempIndex = i
                    break
            que.pop(tempIndex)
            childCells(rowNum, colNum)
        if costArr[targetMatrix[targetLocation][0]][targetMatrix[targetLocation][1]] != 0:
            reachedTarget = True
        if reachedTarget:
            pathToTarget(siteMatrix[startX][startY], targetMatrix[targetLocation][0], targetMatrix[targetLocation][1],
                         parentX, parentY)
        else:
            output = "FAIL"
            f1.write(output)
            f1.write("\n")

    elif method.strip() == "BFS":

        def childCells(row, col):

            for i in range(0, 8):
                safe = []
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

                safe.append(r1)
                safe.append(c1)
                que.append(safe)
                isVisited[r1][c1] = True
                parentX[r1][c1] = row
                parentY[r1][c1] = col


        def pathToTarget(s, xtarget, ytarget, parX, parY):
            shortestPath = []

            while parX[xtarget][ytarget] != None and parY[xtarget][ytarget] != None:
                tempX = xtarget
                tempY = ytarget
                path = [ytarget, xtarget]
                shortestPath.append(path)
                xtarget = parX[tempX][tempY]
                ytarget = parY[tempX][tempY]

            start = [startY, startX]
            shortestPath.append(start)
            shortestPath.reverse()
            output = ""
            for item in shortestPath:
                output = output + (str(item[0]) + "," + str(item[1]) + " ")
            f1.write(output)
            f1.write("\n")

        que = []
        safe = [startX, startY]
        que.append(safe)
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

        isVisited[startX][startY] = True

        while len(que) > 0:
            tempList = que.pop(0)
            if tempList[0] == targetMatrix[targetLocation][0] and tempList[1] == targetMatrix[targetLocation][1]:
                reachedTarget = True
                break
            childCells(tempList[0], tempList[1])

        if reachedTarget:
            pathToTarget(siteMatrix[startX][startY], targetMatrix[targetLocation][0], targetMatrix[targetLocation][1],
                         parentX, parentY)
        else:
            output = "FAIL"
            f1.write(output)
            f1.write("\n")

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
                        if costArr[r1][c1] > costArr[row][col] + 14:
                            costArr[r1][c1] = costArr[row][col] + 14
                            parentX[r1][c1] = row
                            parentY[r1][c1] = col
                        continue
                else:
                    if isVisited[r1][c1]:
                        if costArr[r1][c1] > costArr[row][col] + 10:
                            costArr[r1][c1] = costArr[row][col] + 10
                            parentX[r1][c1] = row
                            parentY[r1][c1] = col
                        continue

                if dirRow[i] != 0 and dirCol[i] != 0:
                    costArr[r1][c1] = costArr[row][col] + 14
                else:
                    costArr[r1][c1] = costArr[row][col] + 10

                safe.append(r1)
                safe.append(c1)
                que.append(safe)
                isVisited[r1][c1] = True
                parentX[r1][c1] = row
                parentY[r1][c1] = col


        def pathToTarget(s, xtarget, ytarget, parX, parY):
            shortestPath = []

            while parX[xtarget][ytarget] != None and parY[xtarget][ytarget] != None:
                tempX = xtarget
                tempY = ytarget
                path = [ytarget, xtarget]
                shortestPath.append(path)
                xtarget = parX[tempX][tempY]
                ytarget = parY[tempX][tempY]

            start = [startY, startX]
            shortestPath.append(start)
            shortestPath.reverse()
            output = ""
            for item in shortestPath:
                output = output + (str(item[0]) + "," + str(item[1]) + " ")
            f1.write(output)
            f1.write("\n")


        def getIndex(value, arr):
            for i in range(0, h):
                for j in range(0, w):
                    if arr[i][j] == value:
                        if not isVisitedForMin[i][j]:
                            isVisitedForMin[i][j] = True
                            return i, j

        que = []
        safe = [startX, startY]
        que.append(safe)
        tempIndex = 0
        reachedTarget = False
        dirRow = [-1, +1, 0, 0, -1, -1, +1, +1]
        dirCol = [0, 0, -1, +1, -1, +1, -1, +1]
        costArr = []
        for i in range(0, h):
            sample = []
            for j in range(0, w):
                sample.append(None)
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

        isVisited[startX][startY] = True

        while len(que) > 0:
            minimum = costArr[que[0][0]][que[0][1]]
            for i in range(1, len(que)):
                if costArr[que[i][0]][que[i][1]] < minimum:
                    minimum = costArr[que[i][0]][que[i][1]]
            rowNum, colNum = getIndex(minimum, costArr)
            for i in range(0, len(que)):
                if que[i] == [rowNum, colNum]:
                    tempIndex = i
                    break
            que.pop(tempIndex)
            childCells(rowNum, colNum)
        if costArr[targetMatrix[targetLocation][0]][targetMatrix[targetLocation][1]] != 0:
            reachedTarget = True
        if reachedTarget:
            pathToTarget(siteMatrix[startX][startY], targetMatrix[targetLocation][0], targetMatrix[targetLocation][1],
                         parentX, parentY)
        else:
            output = "FAIL"
            f1.write(output)
            f1.write("\n")

f.close()
f1.close()

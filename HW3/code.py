import copy

fin = open("input.txt", "r")
fout = open("output.txt", "w")

num = int(fin.readline())

char = 'c'

queryArr = []
matLitQ = []
negatedQ = True
flag = False

args1 = []
args2 = []

isResolved = True
isResolvable = True

alreadyComputed = []

for i in range(0, num):
    queryArr.append(str(fin.readline().strip()))

for i in range(0, len(queryArr)):
    matLitQ.append(queryArr[i].split())

numKB = int(fin.readline())
queryKB = []

for i in range(0, numKB):
    queryKB.append(str(fin.readline().strip()))

for i in range(0, len(queryKB)):
    if queryKB[i].find("=>") != -1:
        res = queryKB[i].split()
        for j in range(0, len(res)):
            if res[j] == "=>":
                res[j] = "|"
                temp = j
        for x in range(0, temp):
            if res[x] == "&":
                res[x] = "|"
            elif res[x] == "|":
                res[x] = "&"
            elif res[x].startswith("~"):
                res[x] = res[x].replace("~", "")
            else:
                res[x] = "~" + res[x]

        sam = " "
        queryKB[i] = sam.join(res)

matLitKB1 = []

for i in range(0, len(queryKB)):
    matLitKB1.append(queryKB[i].split())

general = []
general2 = []
sam = ""

for i in range(0, len(matLitKB1)):
    for j in range(0, len(matLitKB1[i])):
        sam = matLitKB1[i][j]
        if sam == "|":
            general.append(sam)
        else:
            if sam not in general:
                general.append(sam)
    general2.append(general)
    general = []

general3 = copy.deepcopy(general2)

toFind = ""

for i in range(0, len(general2)):
    for j in range(0, len(general2[i])):
        if general2[i][j].find("~") != -1:
            toFind = general2[i][j].replace("~", "")
            if toFind in general3[i]:
                general3[i].remove(toFind)
                general3[i].remove(general2[i][j])

matLitKB = general3


def resolve(currentStmt, predicate, currentQuery, literal):
    newStmt = []
    if literal.startswith("~"):
        prady = literal.replace("~", "")
    else:
        prady = "~" + literal

    for i in range(0, len(currentQuery)):
        if len(currentQuery[i]) > 1:
            newStmt.append(currentQuery[i])
    for i in range(0, len(currentStmt)):
        if len(currentStmt[i]) > 1:
            newStmt.append(currentStmt[i])

    newStmt.remove(literal)
    newStmt.remove(prady)
    return newStmt


def update(toChange, stmtFromKB, changeBy):
    sample = ""
    timePass = []

    for i in range(0, len(stmtFromKB)):
        if stmtFromKB[i] != "|":
            take0 = stmtFromKB[i].split("(")[0]
            take1 = stmtFromKB[i].split("(")[1]
            take2 = take1.split(")")[0]
            take3 = take2.split(",")
            for z in range(0, len(take3)):
                if take3[z] == toChange:
                    take3[z] = changeBy
            str = ""
            for z in range(0, len(take3)):
                str += take3[z]
                str += ","
            result = str[: -1]
            result = take0 + "(" + result + ")"

            sample = result
            timePass.append(sample)

    return timePass


def unify(stmt, argKB, argQ, isNew):
    unifyVar = ''
    count = 0
    index = 0
    if isNew:
        for i in range(0, len(argKB)):
            if argKB[i] != argQ[i]:
                if len(argKB[i]) == 1 and len(argQ[i]) != 1 and argKB[i].islower():
                    unifyVar = argKB[i]
                    stmt = update(unifyVar, stmt, argQ[i])
                elif len(argKB[i]) == 1 and len(argQ[i]) == 1:
                    if argKB.count(argKB[i]) > argQ.count(argQ[i]):
                        if argQ[i].islower():
                            unifyVar = argQ[i]
                            stmt = update(unifyVar, stmt, argKB[i])
                    elif argQ.count(argQ[i]) > argKB.count(argKB[i]):
                        if argKB[i].islower():
                            unifyVar = argKB[i]
                            stmt = update(unifyVar, stmt, argQ[i])
                    else:
                        if argKB[i].islower():
                            unifyVar = argKB[i]
                            stmt = update(unifyVar, stmt, argQ[i])

    else:
        for i in range(0, len(argKB)):
            if argKB[i] != argQ[i]:
                if len(argQ[i]) == 1 and len(argKB[i]) != 1:
                    unifyVar = argQ[i]
                    stmt = update(unifyVar, stmt, argKB[i])
                elif len(argKB[i]) == 1 and len(argQ[i]) == 1:
                    if argKB.count(argKB[i]) > argQ.count(argQ[i]):
                        if argQ[i].islower():
                            unifyVar = argQ[i]
                            stmt = update(unifyVar, stmt, argKB[i])
                    elif argQ.count(argQ[i]) > argKB.count(argKB[i]):
                        if argKB[i].islower():
                            unifyVar = argKB[i]
                            stmt = update(unifyVar, stmt, argQ[i])
                    else:
                        if argQ[i].islower():
                            unifyVar = argQ[i]
                            stmt = update(unifyVar, stmt, argKB[i])
    return stmt


def scanArgu(stmt, cmpStmt):

    global args1
    global args2

    args1 = []
    args2 = []

    end1 = stmt.split('(')[1]
    start1 = end1.split(')')[0]
    args1 = start1.split(',')

    end2 = cmpStmt.split('(')[1]
    start2 = end2.split(')')[0]
    args2 = start2.split(',')

    possible = True
    if args1 == args2:
        possible = True
    else:
        for i in range(0, len(args1)):
            if args1[i] != args2[i]:
                if len(args1[i]) == 1 and args1[i].islower():
                    possible = True
                elif len(args2[i]) == 1 and args2[i].islower():
                    possible = True
                else:
                    possible = False
                    return False
    return possible


def findQinKB(target, targetQuery):
    target = target + "("
    global negatedQ
    global isResolvable
    isFound = True
    setOfMatchingStmt = []
    sampleAns = []
    for i in range(0, len(matLitKB)):
        for j in range(0, len(matLitKB[i])):
            if negatedQ:
                if matLitKB[i][j].find(target) != -1 and not matLitKB[i][j].startswith("~"):

                    if matLitKB[i][j] == targetQuery.replace("~", ""):
                        if scanArgu(matLitKB[i][j], targetQuery):
                            setOfMatchingStmt.append(matLitKB[i])
                        else:
                            isResolvable = False
            else:
                if matLitKB[i][j].find(target) != -1:
                    if "~" + matLitKB[i][j] == targetQuery:
                        if scanArgu(matLitKB[i][j], targetQuery):
                            setOfMatchingStmt.append(matLitKB[i])
                        else:
                            isResolvable = False

    for i in range(0, len(matLitKB)):
        for j in range(0, len(matLitKB[i])):
            if negatedQ:
                if matLitKB[i][j].find(target) != -1 and not matLitKB[i][j].startswith("~"):
                    if (scanArgu(matLitKB[i][j], targetQuery)):
                        sampleAns = matLitKB[i]
                        setOfMatchingStmt.append(matLitKB[i])
                    else:
                        isResolvable = False
            else:
                if matLitKB[i][j].find(target) != -1:
                    if (scanArgu(matLitKB[i][j], targetQuery)):
                        sampleAns = matLitKB[i]
                        setOfMatchingStmt.append(matLitKB[i])
                    else:
                        isResolvable = False

    if len(setOfMatchingStmt) != 0:
        return setOfMatchingStmt
    else:
        return False


def getArg(stmt1, stmt2):
    crnt = stmt2.split('(')[0]
    stm = ""
    if stmt2.startswith("~"):
        crnt = crnt.replace("~", "")
    else:
        crnt = "~" + crnt

    crnt = crnt + "("

    for i in range(0, len(stmt1)):
        if stmt1[i].find(crnt) != -1:
            stm = stmt1[i]

    argu1 = []
    argu2 = []

    end1 = stm.split('(')[1]
    start1 = end1.split(')')[0]
    argu1 = start1.split(',')

    end2 = stmt2.split('(')[1]
    start2 = end2.split(')')[0]
    argu2 = start2.split(',')
    return argu1, argu2


def solution(queryArray):
    global negatedQ
    global args1
    global args2
    global isResolved
    global flag
    global alreadyComputed

    for i in range(0, len(queryArray)):
        query = queryArray[i]
        if query in alreadyComputed:
            continue
        else:
            alreadyComputed.append(query)
            crntPredicate = query.split('(')[0]
            if query.startswith("~"):
                negatedQ = True
                crntPredicate = crntPredicate.replace("~", "")
            else:
                negatedQ = False
                crntPredicate = "~" + crntPredicate
            currentQSet = findQinKB(crntPredicate, query)
            if currentQSet == False:
                continue
            else:
                for p in range(0, len(currentQSet)):
                    currentQ = currentQSet[p]
                    argument1, argument2 = getArg(currentQ, query)
                    newQ = unify(currentQ, argument1, argument2, True)
                    newQArray = unify(queryArray, argument1, argument2, False)
                    updatedQ = resolve(newQ, crntPredicate, newQArray, newQArray[i])
                    backupQuery = query
                    query = updatedQ
                    if len(query) == 0:
                        fout.write("TRUE\n")
                        isResolved = True
                        flag = True
                        break
                    else:
                        solution(query)
                        query = backupQuery
                        if isResolved == True:
                            flag = True
                            break


for i in range(0, len(matLitQ)):
    currentQ = []
    alreadyComputed = []
    flag = False

    isResolved = False
    if (matLitQ[i][0].startswith("~")):
        current = matLitQ[i][0].replace("~", "")
        currentQ.append(current)
        solution(currentQ)
    else:
        current = "~" + matLitQ[i][0]
        currentQ.append(current)
        solution(currentQ)

    if flag == False:
        fout.write("FALSE\n")

fin.close()
fout.close()

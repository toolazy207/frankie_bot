import random
import re


def dicemaxmin2(msg):
    newStr = list(msg)
    resultStr = "**Results**: "
    outputStr = "**Output**: "

    for i, value in enumerate(newStr):
        if "+" in value:
            newStr[i] = value.replace("+", " t ")

        elif "-" in value:
            newStr[i] = value.replace("-", " _ ")

        elif "*" in value:
            newStr[i] = value.replace("*", " x ")

        elif "/" in value:
            newStr[i] = value.replace("/", " | ")

    newStr = "".join(newStr)

    newStr = (re.split(r'\s', newStr))

    newList = []
    tempDieList = []
    for value in newStr:
        rollStr = ""

        if "k" in value and "l" not in value:
            dieString = value
            newDie = (re.split(r'[d, k]', dieString))
            timesDice = int(newDie[0])
            timesDiceVal = int(newDie[0])
            typeOfDice = int(newDie[1])
            maxFinder = int(newDie[-1])
            tempMaxFinder = maxFinder
            dieList = []

            while timesDice != 0:
                dieRoll = random.randint(1, int(typeOfDice))
                if timesDice != 1:
                    dieList.append(str(dieRoll))
                    rollStr += (str(dieRoll) + ", ")
                else:
                    dieList.append(str(dieRoll))
                    rollStr += (str(dieRoll))
                timesDice -= 1
            maxList = ""

            while maxFinder != 0:
                maxRoll = max(dieList, key=lambda x: int(x))
                if maxFinder == 1:
                    maxList += maxRoll
                else:
                    maxList += maxRoll + "+"
                dieList.remove(max(dieList, key=lambda x: int(x)))
                maxFinder -= 1
            diceStr = f"{timesDiceVal}d{typeOfDice}k{tempMaxFinder} ({rollStr})"
            value = eval(maxList)
            tempDieList.append(diceStr)

        elif "k" in value and "l" in value:
            dieString = value
            newDie = (re.split(r'[d, kl]', dieString))
            timesDice = int(newDie[0])
            timesDiceVal = int(newDie[0])
            typeOfDice = int(newDie[1])
            minFinder = int(newDie[-1])
            tempMinFinder = minFinder
            dieList = []

            while timesDice != 0:
                dieRoll = random.randint(1, int(typeOfDice))
                if timesDice != 1:
                    dieList.append(str(dieRoll))
                    rollStr += (str(dieRoll) + ", ")
                else:
                    dieList.append(str(dieRoll))
                    rollStr += (str(dieRoll))
                timesDice -= 1
            (dieList)
            minList = ""

            while minFinder != 0:
                minRoll = min(dieList, key=lambda x: int(x))
                if minFinder == 1:
                    minList += minRoll
                else:
                    minList += minRoll + "+"
                dieList.remove(min(dieList, key=lambda x: int(x)))
                minFinder -= 1
            diceStr = f"{timesDiceVal}d{typeOfDice}kl{tempMinFinder} ({rollStr})"
            value = eval(minList)
            tempDieList.append(diceStr)

        elif "d" in value and "k" not in value and "l" not in value:
            dieString = value
            newDie = dieString.split("d")
            if newDie[0] == "":
                timesDice = 1
                timesDiceVal = 1
                val1 = True
            else:
                timesDice = int(newDie[0])
                timesDiceVal = int(newDie[0])
            typeOfDice = newDie[-1]
            dieList = ""

            while timesDice != 0:
                dieRoll = random.randint(1, int(typeOfDice))
                if timesDice != 1:
                    dieList += (str(dieRoll) + "+")
                    rollStr += (str(dieRoll) + ", ")
                else:
                    dieList += (str(dieRoll))
                    rollStr += (str(dieRoll))
                timesDice -= 1
            diceStr = f"{timesDiceVal}d{typeOfDice} ({rollStr})"
            tempDieList.append(diceStr)
            value = (eval(dieList))
        newList.append(value)

    newStrStr = ""

    for v in newStr:
        if "d" in v:
            for res in tempDieList:
                tempRes = res.split(" (")
                tempRes1 = tempRes[0][1:]
                if tempRes[0] == v:
                    outputStr += res
                elif tempRes1 == v:
                    outputStr += res

        elif "t" in v:
            v = " + "
            outputStr += v
        elif "_" in v:
            v = " - "
            outputStr += v
        elif "x" in v:
            v = " * "
            outputStr += v
        elif "|" in v:
            v = " / "
            outputStr += v
        else:
            outputStr += v
    for val in newList:
        if val == "t":
            val = "+"
            newStrStr += val
        elif val == "_":
            val = "-"
            newStrStr += val
        elif val == "x":
            val = "*"
            newStrStr += val
        elif val == "|":
            val = "/"
            newStrStr += val
        elif val != "t" or val != "_" or val != "x" or val != "|":
            newStrStr += str(val)

    evalList = eval(newStrStr)
    resultStr += str(evalList)

    totalStr = f"{outputStr}\n{resultStr}"
    return totalStr

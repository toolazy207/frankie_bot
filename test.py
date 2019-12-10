import random


def dicebot(message):
    mess = message.split("d")
    mod = 0
    modIncrement = 0
    diceRollStr = "**Rolls**: "
    modStr = "**Mod**: "
    while "+" or "-" in mess:
        if "-" in mess[1]:
            while modIncrement == 0:
                negString = mess[1]
                modIncrement += 1
                negStringSplit = negString.split("-")
                typeOfDie = int(negStringSplit[0])
                negStringSplit[0] = "0"
                for num in negStringSplit:
                    mod += (int(num) * (-1))
                break
            break

        elif "+" in mess[1]:
            while modIncrement == 0:
                posString = mess[1]
                modIncrement += 1
                posStringSplit = posString.split("+")
                typeOfDie = int(posStringSplit[0])
                posStringSplit[0] = "0"
                for num in posStringSplit:
                    mod += int(num)
                break
            break
        else:
            typeOfDie = int(mess[1])
            break
    if mess[0] != "":
        timesDice = int(mess[0])
    else:
        timesDice = 1
    total = 0
    print("Mod: " + str(mod))
    print("Rolls: ", end="")
    while timesDice != 0:
        diceRoll = random.randint(1, typeOfDie)

        if timesDice != 1:
            diceRoll = random.randint(1, typeOfDie)
            total += diceRoll
            diceRollStr += (str(diceRoll) + ", ")
            print(str(diceRoll) + ", ", end="")
        else:
            total += diceRoll
            diceRollStr += str(diceRoll)
            print(str(diceRoll))

        timesDice -= 1

    total += mod
    resultString = ("**Results**: " + str(total))
    modStr += str(mod)
    endStr = f"{modStr}\n{diceRollStr}\n{resultString}"
    return endStr


def dicemax(message):
    mess = message.split("d")
    maxmess = mess[1].split("k")
    dieType = maxmess[0]
    modIncrement = 0
    mod = 0
    total = 0
    diceRollStr = "**Rolls**: "
    maxRollStr = "**Max Rolls**: "
    maxList = []
    resultStr = "**Results**: "
    if mess[0] == "":
        timesDice = 1
    else:
        timesDice = int(mess[0])
    while "+" or "-" in maxmess[1]:
        if "+" in maxmess[1]:
            while modIncrement == 0:
                maxmessPlus = maxmess[-1].split("+")
                maxmessMod = int(maxmessPlus[0])
                maxmessPlus[0] = "0"
                for num in maxmessPlus:
                    mod += int(num)
                modIncrement += 1
                break
            break

        elif "-" in maxmess[1]:
            while modIncrement == 0:
                maxmessMinus = maxmess[-1].split("-")
                maxmessMod = int(maxmessMinus[0])
                maxmessMinus[0] = "0"
                for num in maxmessMinus:
                    mod -= int(num)
                modIncrement += 1
                break
            break

        else:
            maxmessMod = int(maxmess[-1])
            break

    modString = ("**Mod**: " + str(mod))

    while timesDice != 0:
        diceRoll = random.randint(1, int(dieType))

        if timesDice != 1:
            diceRoll = random.randint(1, int(dieType))
            maxList.append(str(diceRoll))
            diceRollStr += (str(diceRoll) + ", ")
        else:
            maxList.append(str(diceRoll))
            diceRollStr += str(diceRoll)
        timesDice -= 1
    print(maxList)
    maxRollList = []
    while maxmessMod != 0:
        maxRoll = max(maxList, key=lambda x: int(x))
        if maxmessMod == 1:
            maxRollStr += str(maxRoll)
            maxRollList.append(str(maxRoll))
        else:
            maxRollStr += (str(maxRoll) + ", ")
            maxRollList.append(str(maxRoll))
        maxList.remove(max(maxList, key=lambda x: int(x)))
        maxmessMod -= 1
    for number in maxRollList:
        total += int(number)

    resultStr += str(total)
    endStr = f"{modString}\n{diceRollStr}\n{maxRollStr}\n{resultStr}"
    return endStr


def dicemin(message):
    mess = message.split("d")
    minmess = mess[1].split("kl")
    dieType = minmess[0]
    modIncrement = 0
    mod = 0
    total = 0
    diceRollStr = "**Rolls**: "
    minRollStr = "**Min Rolls**: "
    minList = []
    resultStr = "**Results**: "
    if mess[0] == "":
        timesDice = 1
    else:
        timesDice = int(mess[0])
    while "+" or "-" in minmess[1]:
        if "+" in minmess[1]:
            while modIncrement == 0:
                minmessPlus = minmess[-1].split("+")
                minmessMod = int(minmessPlus[0])
                minmessPlus[0] = "0"
                for num in minmessPlus:
                    mod += int(num)
                modIncrement += 1
                break
            break

        elif "-" in minmess[1]:
            while modIncrement == 0:
                minmessMinus = minmess[-1].split("-")
                minmessMod = int(minmessMinus[0])
                minmessMinus[0] = "0"
                for num in minmessMinus:
                    mod -= int(num)
                modIncrement += 1
                break
            break

        else:
            minmessMod = int(minmess[-1])
            break

    modString = ("**Mod**: " + str(mod))

    while timesDice != 0:
        diceRoll = random.randint(1, int(dieType))

        if timesDice != 1:
            diceRoll = random.randint(1, int(dieType))
            minList.append(str(diceRoll))
            diceRollStr += (str(diceRoll) + ", ")
        else:
            minList.append(str(diceRoll))
            diceRollStr += str(diceRoll)
        timesDice -= 1
    minRollList = []
    while minmessMod != 0:
        minRoll = min(minList, key=lambda x: int(x))
        if minmessMod == 1:
            minRollStr += str(minRoll)
            minRollList.append(str(minRoll))
        else:
            minRollStr += (str(minRoll) + ", ")
            minRollList.append(str(minRoll))
        minList.remove(min(minList, key=lambda x: int(x)))
        minmessMod -= 1

    for number in minRollList:
        total += int(number)
    resultStr += str(total)

    endStr = f"{modString}\n{diceRollStr}\n{minRollStr}\n{resultStr}"
    return endStr

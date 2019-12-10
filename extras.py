import random


def helper():
    helpStr = "Examples (Use \"/\" for the prefix):\n\n/d20\n\n/2d20\n\n/2d20k1 - Returns the highest roll\n\n/2d20kl1 - Returns the lowest roll\n\nDoes basic operations: +, -, *, /, %\n\n/gen classpect - Generates classpect\n\n/gen invite - Generates invite link\n\n/2 [dice] - Rolls iterations of dice\n\n/vibe [item] - Vibe checks something\n\n/scritch [number] - Gives the bot scritches, maybe for luck\n\n/chars add [char] - Adds a character to the server's list\n\n/chars remove [char] - Removes a character from the server's list\n\n/chars list - Displays a list of all the characters within the server\n\n/chars random - Picks a random character from the character list\n"
    return helpStr


def mathdice(message):
    mathStr = "**Output**: "
    resultStr = "**Results**: "
    mathStrYee = ""
    for char in message:
        if char == "+":
            char = " + "
            mathStrYee += char
        elif char == "-":
            char = " - "
            mathStrYee += char
        elif char == "*":
            char = " \* "
            mathStrYee += char
        elif char == "/":
            char = " / "
            mathStrYee += char
        else:
            mathStrYee += char
    evalChecker = eval(message)
    mathStr += mathStrYee
    resultStr += str(evalChecker)
    totalStr = f"{mathStr}\n{resultStr}"
    print(totalStr)
    return totalStr


def gogtiergen():
    classes = ["Heir", "Mage", "Witch", "Seer", "Knight", "Page", "Rogue", "Thief", "Maid", "Sylph", "Bard", "Prince"]
    aspects = ["Time", "Space", "Breath", "Blood", "Light", "Void", "Heart", "Mind", "Hope", "Rage", "Life", "Doom"]

    cChoice = random.choice(classes)
    aChoice = random.choice(aspects)

    outputStr = f"**God Tier**: {cChoice} of {aChoice}"
    print(outputStr)
    return outputStr


def vibe_check(msg):
    total = 0
    vibeString = "**Vibe Check**: "
    vibes = ["homestuck", "timetables"]
    for char in msg:
        value = ord(char)
        total += value
        vChoice = random.choice(vibes)
        if vChoice == "homestuck":
            total += random.randint(1, 413)
        elif vChoice == "timetables":
            total += random.randint(1, 2359)
    if total % 2 == 0:
        vibeString += f"{msg} passed!"
    else:
        vibeString += f"{msg} failed!"
    print(vibeString)
    return vibeString


def scritches(msg):
    scritchString = "**Times Scritched**: "
    total = 0
    total += int(msg)
    scritchString += str(total)
    print(scritchString)
    return scritchString


gogtiergen()

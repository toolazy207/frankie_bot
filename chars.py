import random

def charsadd(server, char):
    serverName = server
    charName = char

    charFile = open(f"{serverName}.txt", "a+")

    charFile.write(f"{charName}\n")

    charFile.close()
    return f"{charName} added!"


def charslist(server):
    serverName = server
    charFile = open(f"{serverName}.txt", "r+")

    charStr = ""
    for char in charFile:
        if char == "":
            pass
        else:
            print(char)
            charStr += char

    charFile.close()
    return charStr

def charsremove(server, char):
    serverName = server
    charName = char

    with open(f"{serverName}.txt", "r+") as charFile:
        lines = charFile.readlines()
    with open(f"{serverName}.txt", "w") as charFile:
        for line in lines:
            if line[:-1] == charName:
                continue
            else:
                charFile.write(line)

        charFile.close()
    return f"{charName} removed!"

def charsrandom(server):
    serverName = server

    charList = []

    charFile = open(f"{serverName}.txt", "r+")

    for line in charFile:
        charList.append(line)

    charFile.close()

    output = random.choice(charList)
    outputStr = f"**Character**: {output}"

    return outputStr

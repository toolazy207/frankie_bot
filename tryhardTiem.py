import re
import stringShenanigans as ss


def multiroll(msg):
    yeet = re.split(r'\s', msg)
    loopDoer = int(yeet[0])
    outputStr = ""
    while loopDoer != 0:
        newMessage = ss.dicemaxmin2(yeet[1])
        outputStr += f"{newMessage}\n\n"
        loopDoer -= 1
    print(outputStr)
    return outputStr


def invite():
    inviteStr = "<https://discordapp.com/api/oauth2/authorize?client_id=649689135178842151&permissions=31744&scope=bot>"
    return inviteStr

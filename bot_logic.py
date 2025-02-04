import random

def gen_pass(pass_length):
    caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(caracter)

    return password

def gen_emoji():
    emoji = ["💀", "😎","😵‍💫" ,"🥳", "🤡","🤑","😰","😮","❤️"]
    return random.choice(emoji)


def coin_flip():
    giro = random.randint(0, 2)
    if giro == 0:
        return "Cara"
    else:
        return "cruz"

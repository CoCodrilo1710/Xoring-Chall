import sys
import random


def urmatoarea_litera():
    seed = 0
    lungime=len(s2)-1
    for litera in s2:
        seed += ord(litera)
    random.seed(seed)
    while True:
        yield s2[random.randint(0, lungime)]

try:

    s1 = sys.argv[1]  # encrypt / decrypt
    s2 = sys.argv[2]  # pass
    s3 = sys.argv[3]  # input
    s4 = sys.argv[4]  # output

    parola = urmatoarea_litera()

    if s1 == "encrypt":

        f = open(f"{s3}")
        g = open(f"{s4}", "w")
        s = f.read()

        a_list = [bin(ord(a) ^ ord(next(parola)))[2:].zfill(8) for a in s]
        g.writelines("".join(a_list))
        f.close()
        g.close()

    else:
        f = open(f"{s3}")
        g = open(f"{s4}", "w")
        s = f.read()

        decoded = []
        while len(s) > 0:
            decodeS = s[:8]
            ascii = int(decodeS, 2)
            decoded.append(chr(ascii ^ ord(next(parola))))
            s = s[8:]

        g.write("".join(decoded))
        f.close()
        g.close()
except IndexError:
    raise SystemExit(f"Usage: python3  {sys.argv[0]} encrypt/decrypt key input output ")
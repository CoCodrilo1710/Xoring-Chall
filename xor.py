import sys
import random


def urmatoarea_litera():
    seed = 0
    lungime = len(s2) - 1
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
        g = open(f"{s4}", "wb")
        s = f.read()

        for a in s:
            g.write((ord(a) ^ ord(next(parola))).to_bytes(1, "big"))
        f.close()
        g.close()

    else:
        f = open(f"{s3}", "rb")
        g = open(f"{s4}", "w")

        decoded = []
        bits = f.read(1)
        while bits:
            ascii = int.from_bytes(bits, "big")
            decoded.append(chr(ascii ^ ord(next(parola))))
            bits = f.read(1)

        g.write("".join(decoded))
        f.close()
        g.close()
except IndexError:
    raise SystemExit(f"Usage: python3  {sys.argv[0]} encrypt/decrypt key input output ")

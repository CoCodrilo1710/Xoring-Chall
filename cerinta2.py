from collections import Counter
import sys

def lungime_cheie(biti, lg_max):
    shifted = []
    for k in range(1, lg_max + 1):
        shifted.append(shift_biti(biti, k))
    aparitii = [[0, 0]]
    for k in range(1, lg_max + 1):
        aparitii.append([procent(biti, shifted[k - 1]), k])
    aparitii.sort(reverse=True)
    posibile_chei = []
    last_key = 0
    for ap in aparitii[1:]:
        current = ap[0]
        if current < last_key * 0.8:
            break
        posibile_chei.append(ap)
        last_key = current
    posibile_chei.sort(key=lambda posibile_chei: posibile_chei[1])
    lungimi = [posibile_chei[0]]
    for lg1 in posibile_chei[1:]:
        tg = True
        for lg2 in lungimi:
            if lg1[1] % lg2[1] == 0:
                tg = False
        if tg:
            lungimi.append(lg1)
    return sorted(lungimi, reverse=True)


def shift_biti(biti, shift):
    return biti[shift:] + biti[:shift]


def procent(text, shifted):
    k = 0
    for it in range(len(text)):
        if text[it] == shifted[it]: k += 1
    return int(k / len(text) * 1000) / 10


def geseste_cheie(text, lg, most_common_byte=32):
    cheie = bytearray([0] * lg)
    for x in range(lg):
        list = []
        for y in range(x, len(text), lg):
            list.append(text[y])
        frecvent = Counter(list).most_common(1)[0][0]
        cheie[x] = most_common_byte ^ frecvent
    return cheie


def decript(biti, cheie):
    final = bytearray()
    for i in range(len(biti)):
        final.append(biti[i] ^ cheie[i % len(cheie)])
    return final



s1 = sys.argv[1]
s2 = sys.argv[2]
input_file = s1    # de decryptat
output_file = s2   # textul decryptat
lg_max = 45
cheie = None
most_frequent = 32

text = open(input_file, 'rb').read()

lungime_candidat = lungime_cheie(text, lg_max)
print("Lungimea posibilei chei: ")
for proc, lg in lungime_candidat:
    print("   ", lg, " - ", proc, "%", sep='')
lg_cheie = lungime_candidat[0][1]

if lg_cheie:
    cheie = geseste_cheie(text, lg_cheie, most_frequent)
    print("Am gasit o cheie:", cheie.decode("utf-8"))

with open(output_file, 'wb') as fout:
    fout.write(decript(text, cheie))

fout.close()

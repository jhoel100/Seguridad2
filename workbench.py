from plotly.subplots import make_subplots
import plotly.express as px
from skimage import data
import plotly.graph_objects as go
import numpy as np
import cv2
import matplotlib.pyplot as plt
"""# Sec lab"""

import unicodedata as ud
import pprint
import math


def preprocess(text):
    text = ''.join(c for c in ud.normalize('NFD', text)
                   if ud.category(c) != 'Mn' and c.isalnum())
    text = text.upper()
    return text


def chr_to_num_ES(ch):
    alphabet = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'Ñ': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }
    return alphabet[ch]


def num_to_chr_ES(num):
    alphabet = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'Ñ',
        15: 'O',
        16: 'P',
        17: 'Q',
        18: 'R',
        19: 'S',
        20: 'T',
        21: 'U',
        22: 'V',
        23: 'W',
        24: 'X',
        25: 'Y',
        26: 'Z',
    }
    if num < 0:
        num += 27
    return alphabet[num]


def vigenere_encode(msg, key):
    encoded = ''
    for i, ch in enumerate(msg):
        m = (chr_to_num_ES(ch) + chr_to_num_ES(key[i % len(key)])) % 27
        encoded += num_to_chr_ES(m)
    return encoded


def vigenere_decode(msg, key):
    decoded = ''
    for i, ch in enumerate(msg):
        m = (chr_to_num_ES(ch) - chr_to_num_ES(key[i % len(key)])) % 27
        decoded += num_to_chr_ES(m)
    # print(decoded)
    return decoded


def counter(msg):
    counter = dict()
    for m in msg:
        if m not in counter: counter[m] = 1
        else: counter[m] += 1
    return counter


def bar(cc, key, vowels=False):
    fig = None
    if not vowels:
        fig = px.histogram({
            'letters': cc.keys(),
            'count': cc.values()
        },
                           x='letters',
                           y='count',
                           title=key)
        fig.update_xaxes(categoryorder='total descending')
    else:
        fig = px.histogram({
            'letters': cc.keys(),
            'count': cc.values()
        },
                           x='letters',
                           y='count',
                           title=key,
                           category_orders={
                               'letters': [
                                   'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J',
                                   'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
                                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                               ]
                           })
    return fig


msg = """Creer que es posible es el paso número uno hacia el éxito. Despertarse y
pensar en algo positivo puede cambiar el transcurso de todo el día. No eres lo suficientemente
viejo como para no iniciar un nuevo camino hacia tus sueños. Levántate cada mañana creyendo
que vas a vivir el mejor día de tu vida"""
# msg="""Dentro de veinte años estarás más decepcionado por las cosas que
# no hiciste, que por las que hiciste. Así que suelta las amarras. Navega lejos del puerto
# seguro. Atrapa los vientos alisios en tus velas. Explora. Sueña. Descubre."""

msg = preprocess(msg)
print("MSG:", msg)
"""
14. Muestre las frecuencias de cada letra del mensaje original usando como claves
POSITIVO, HIELO y MAR, compare y concluya sobre la variación de las frecuencias
en base a la longitudde la clave.Verifique el resultado usando la aplicación
desarrollada en la práctica anterior
"""

key = "POSITIVO"
# key="SABIDURIA"
print(key)
e = vigenere_encode(msg, key)
print(e)
cc = counter(e)
fig = bar(
    cc,
    key,
)
fig.show()
# format_counter(cc)

key = "HIELO"
print(key)
e = vigenere_encode(msg, key)
print(e)
cc = counter(e)
fig = bar(
    cc,
    key,
)
fig.show()
# format_counter(cc)

key = "MAR"
print(key)
e = vigenere_encode(msg, key)
print(e)
cc = counter(e)
fig = bar(
    cc,
    key,
)
fig.show()
"""
15. Desarrolle un algoritmo que encuentre el texto claro si recibió la cifra
WPIXHVYYOSRTECSZBEEGHUUFWRWTZGRWUFSRIWESSXVOHAIHOHWWHCWH
UZOBOZEAOYBMCRLTEYOTI, y se sabe que ha cifrado con la clave HIELO
"""

msg = preprocess("""WPIXHVYYOSRTECSZBEEGHUUFWRWTZGRWUFSRIWESSXVOHAIHOHWWHCWH
UZOBOZEAOYBMCRLTEYOTI""")
key = preprocess("HIELO")
txt = vigenere_decode(msg, key)
print(txt)
"""
19. Criptoanalizar el siguiente criptograma mod 27, encontrar la clave y
el texto en claro.
"""

msg = preprocess("""MAXYHGAVAPUUGZHEGZQOWOBNIPQKRNÑMEXIGONIICUCAWIGCTEAGMNOL
RSZJNLWÑAWWIGLDDZSNIZDNBIXGZLAYMXÑCVEKIETMOEOPBEWPTNIXCXUI
HMECXLNOCECYXEQPBWUFANIICÑJIKISCZUAILBGSOANKBFWUAYWNSCHLCW
YDZHDZAQVMPTVGFGPVAJWFVPUOYMXCWERVLQCZWECIFVITUZSNCZUAIKBF
MÑALIEGLBSZLQUXÑOHWOCGHNYWÑQKDANZUDIFOIMXNPHNUWQOKLMVBN
NKRMKONDPDPNMIKAWOXMEEIVEKGBGSFHVADWPGOYMHOIUEEIPGOLENZBS
CHAGKQTZDRÑMÑNWTUZIÑCMÑAXKQUWDLVANNIHLÑCQNWGEHIPGZDTZTÑN
WÑEEWFUMGIÑXNTWXNVIXCZOAZSOQUVENDNFWUSZYHGLRACPGGUGIYWH
OTRMZUGQQDDZIZFWHVVSHCUGOGIFKBXAXPBOBRDVDUCMVTKGIKDRSZLUQ
SDVPMXVIVEYMFGTEANIMQLHLGPQOHRYWCFEWFOISNÑPUAYINNÑXNÑPGKW
GOILQGAFOILQTAHEIIDWMÑEÑXNEPRCVDQTURSK""")

# msg = preprocess("""LNUDVMUYRMUDVLLPXAFZUEFAIOVWVMUOVMUEVMUEZCUDVSYWCIVCFGUCU
# NYCGALLGRCYTIJTRNNPJQOPJEMZITYLIAYYKRYEFDUDCAMAVRMZEAMBLEXPJC
# CQIEHPJTYXVNMLAEZTIMUOFRUFC""")
print(msg)


def get_trigrams(msg):
    # trigram = [0]*3
    msg = [c for c in msg]
    pmatch = [0] * 3
    tcount = dict()
    tpos = dict()
    for i in range(len(msg) - 2):
        trigram = msg[i:i + 3]
        str_trigram = ''.join(trigram)
        if str_trigram not in tcount:
            tcount[str_trigram] = 0
            tpos[str_trigram] = []
            previdx = -1
            for j in range(len(msg) - 2):
                if i + 1 <= j and j <= i + 2:
                    continue
                pmatch = msg[j:j + 3]
                if pmatch == trigram:
                    tcount[str_trigram] += 1
                    len_tri = len(tpos[str_trigram])
                    if previdx != -1:
                        tpos[str_trigram].append(j - previdx)
                    previdx = j
    return tcount, tpos


def splitter(msg, space):
    msg = [c for c in msg]
    # results = [ [] for _ in range(space)]
    results = [''] * space
    # for i in range(0,len(msg)-space-1,space):
    for i in range(0, len(msg), space):
        ss = ''.join(msg[i:i + space])
        for j in range(space):
            if i + j >= len(msg):
                continue
            results[j] = results[j] + msg[i + j]
        # print(ss)
    pprint.pprint(results)
    return results


tri_count, tri_pos = get_trigrams(msg)
tri_pos = sorted(tri_pos.items(), key=lambda x: len(x[1]), reverse=True)
tri_pos = tri_pos[:5]
pprint.pprint(tri_pos)

positions = []
for pair in tri_pos:
    positions.extend(pair[1])

print(positions)
gcd = math.gcd(min(positions), max(positions))
print(gcd)
sub = splitter(msg, gcd)

cc_list = []
for s in sub:
    cc = counter(s)
    cc_list.append(cc)
    fig = bar(cc, s, vowels=True)
    fig.show()

cc = counter(msg)
# pprint.pprint(cc)
fig = bar(cc, 'msg')
fig.show()

# cc_list[0] = sorted(cc_list[0].items(), key=lambda x: x[1], reverse=True)
# cc_list
# pprint.pprint(cc_list[0])
cracked = ''
for i in range(len(cc_list)):
    cracked += sorted(cc_list[i].items(), key=lambda x: x[1],
                      reverse=True)[:1][0][0]
    print(sorted(cc_list[i].items(), key=lambda x: x[1], reverse=True)[:3])
print(cracked)

# for c in cracked:
# 14 es multiplo de 7
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('H') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('E') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('Z') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('M') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('Q') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('G') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('W') - chr_to_num_ES('O')))
print("")
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('V') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('A') - chr_to_num_ES('A')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('N') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('I') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('N') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('C') - chr_to_num_ES('E')))
print(
    num_to_chr_ES(
        chr_to_num_ES('A') + chr_to_num_ES('Z') - chr_to_num_ES('E')))

vigenere_decode(msg, "DAVINCI")

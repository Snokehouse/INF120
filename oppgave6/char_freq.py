"""
Created on Tue Nov  1 07:37:57 2022

__author__: maria nybo
__email__: maria.nmbu@nmbu.no
"""

with open('norec_corpus.txt', 'r', encoding='utf-8') as nor:
    letters = {}
    antall = 0
    exclude_chars = [
    ' ', '\n', ',', '.', '-', '–', '—', '*', '(', ')',
    '«', '»', ':', ';', '’', '?', "'", '"', '/', '!', '…',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for line in nor:
        linje = line.lower()
        for bokstav in linje:
            if bokstav in exclude_chars:
                continue
            elif bokstav not in exclude_chars:
                antall += 1
                try:
                    letters[bokstav] += 1
                except:
                    letters[bokstav] = 1
                    
prosent = []
for key in letters:
    prosent.append((key, int(letters[key])*100/antall))
    
def order_by(tup):
    return tup[1]

sortert = sorted(prosent, key = lambda tall: tall[1], reverse = True)

print(f'Counted letters: {antall}')
for ledd in sortert:
    print(f'{ledd[0]}: {ledd[1]:.3f}%')
    
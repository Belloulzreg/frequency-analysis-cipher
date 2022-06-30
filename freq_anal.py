import re 
import matplotlib.pyplot as plt 
from collections import Counter
#with open('./text.txt', 'r') as file:
#  file = file.read()
#file 
file = 'DJ DK C QLXDWI WF SDGDU PCX. XLRLU KQCSLKBDQK, KJXDHDET FXWZ C BDIILE RCKL, BCGL PWE JBLDX FDXKJ GDSJWXO CTCDEKJ JBL LGDU TCUCSJDS LZQDXL. IYXDET JBL RCJJUL, XLRLU KQDLK ZCECTLI JW KJLCU KLSXLJ QUCEK JW JBL LZQDXL’K YUJDZCJL PLCQWE, JBL ILCJB KJCX, CE CXZWXLI KQCSL KJCJDWE PDJB LEWYTB QWPLX JW ILKJXWO CE LEJDXL QUCELJ. QYXKYLI RO JBL LZQDXL’K KDEDKJLX CTLEJK, QXDESLKK ULDC XCSLK BWZL CRWCXI BLX KJCXKBDQ, SYKJWIDCE WF JBL KJWULE QUCEK JBCJ SCE KCGL BLX QLWQUL CEI XLKJWXL FXLLIWZ JW JBL TCUCVO…'
letters = re.findall('[A-Z]', file)
words = file.split(" ")
letters_frequency = Counter(letters)
words_frequency = Counter(words)
letters_frequency = sorted(letters_frequency.items(), key=lambda x:x[0])
letters_frequency = dict(letters_frequency)
words_frequency = sorted(words_frequency.items(), key=lambda x:x[0])
words_frequency = dict(words_frequency)
plt.bar(range(len(letters_frequency)), list(letters_frequency.values()), align='center' )
plt.xticks(range(len(letters_frequency)), list(letters_frequency.keys()))
plt.title('Letters Frequency')
plt.show()
plt.figure(figsize=(80, 40))
plt.bar(range(len(words_frequency)), list(words_frequency.values()), align='center' )
plt.xticks(range(len(words_frequency)), list(words_frequency.keys()), rotation=45)
plt.title('Words Frequency')
plt.show()

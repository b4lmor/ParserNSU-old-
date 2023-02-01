import json
import csv
from parsers import get_data_A, get_data_B

get_data_A()

with open(f'result.json', mode='r', encoding='utf-8') as file:
    fit_pi = json.load(file)[0]

get_data_B()

with open(f'result.json', mode='r', encoding='utf-8') as file:
    fit_st = json.load(file)[0]

data = fit_pi['table'] + fit_st['table']

for i in range(len(data)):
    if data[i]['disciplines'][3]['point'] == '✓':
        data[i]['sumPointTotal'] = '300'

data.sort(key=lambda x: int(x['sumPointTotal']), reverse=True)

correct_data = []
all_data = []
for card in data:

    if card['snils'] in correct_data:
        continue
    correct_data.append(card['snils'])
    all_data.append((card['snils'], card['sumPointTotal']))

print(len(correct_data))
print(all_data)

with open('all_data.csv', mode='w', encoding='cp1251', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(all_data)
# snils_cnt = set()
# for card in data:
#     snils_cnt.add(card['snils'])
#     if card['snils'] == '207-413-866 49':
#         ...#print(card, len(snils_cnt))

# snils_cnt = len(snils_cnt)
# print(snils_cnt)
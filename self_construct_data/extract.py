import json
from collections import OrderedDict


f1 = open('data1.csv')
f2 = open('data2.csv')

f1.readline()
f2.readline()
datas = []

for idx, line in enumerate(f1):
    line = line.strip()
    print(idx, line)
    if line == '':
        datas.append(one_dialogue)
        continue
    tokens = line.split('\t')
    print(tokens)
    if len(tokens) == 2:
        d_id = tokens[1].split()[0]
        one_dialogue = OrderedDict()
        one_dialogue['id'] = d_id
        one_dialogue['turns'] = []
        s_id = 0
    else:
        if len(tokens) == 3:
            speaker, zh, en = tokens
            pronoun, full_zh = None, None
        elif len(tokens) == 5:
            speaker, zh, en, pronoun, full_zh = tokens
        else:
            print('error!!', idx, line, tokens)
            exit(0)
        one_turn = OrderedDict()
        one_turn['turn_id'] = s_id
        s_id += 1
        one_turn['speaker'] = speaker
        one_turn['zh'] = zh
        one_turn['en'] = en
        if pronoun is not None:
            one_turn['pronoun'] = pronoun
            if full_zh is None:
                print('error2!!', idx, line)
                exit(0)
            one_turn['full_zh'] = full_zh
        one_dialogue['turns'].append(one_turn)

first = True
for idx, line in enumerate(f2):
    line = line.strip()
    print(idx, line)
    if line == '':
        datas.append(one_dialogue)
        first = True
        continue
    tokens = line.split('\t')
    print(tokens)

    if first:
        if len(tokens) == 4:
            d_id, speaker, zh, en = tokens
            pronoun, full_zh, wrong_zh = None, None, None
        elif len(tokens) == 6:
            d_id, speaker, zh, en, pronoun, full_zh = tokens
            wrong_zh = None
        elif len(tokens) == 7:
            d_id, speaker, zh, en, pronoun, full_zh, wrong_zh = tokens
            if pronoun == '':
                pronoun, full_zh = None, None
        else:
            exit(0)
        one_dialogue = OrderedDict()
        one_dialogue['id'] = d_id
        one_dialogue['turns'] = []
        first = False
        s_id = 0
    else:
        if len(tokens) == 3:
            speaker, zh, en = tokens
            pronoun, full_zh, wrong_zh = None, None, None
        elif len(tokens) == 5:
            speaker, zh, en, pronoun, full_zh = tokens
            wrong_zh = None
        elif len(tokens) == 6:
            speaker, zh, en, pronoun, full_zh, wrong_zh = tokens
            if pronoun == '':
                pronoun, full_zh = None, None
        else:
            exit(0)
    one_turn = OrderedDict()
    one_turn['turn_id'] = s_id
    s_id += 1
    one_turn['speaker'] = speaker
    one_turn['zh'] = zh
    one_turn['en'] = en
    if pronoun is not None:
        one_turn['pronoun'] = pronoun
        if full_zh is None:
            print('error2!!', idx, line)
            exit(0)
        one_turn['full_zh'] = full_zh
        
    if wrong_zh is not None:
        one_turn['wrong_zh'] = wrong_zh
    one_dialogue['turns'].append(one_turn)

with open('raw.json', 'w', encoding='utf-8') as fw:
    fw.write(json.dumps(datas, indent=4, ensure_ascii=False))

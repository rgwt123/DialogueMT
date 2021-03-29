import json
from collections import OrderedDict

from sacremoses import MosesTokenizer

en_tokenizer = MosesTokenizer(lang='en')

with open('raw.json', 'r') as f:
    datas = json.load(f, object_pairs_hook=OrderedDict)

num_sent = 0
num_words = [0, 0]
num_wrong = 0
num_dp = 0
dp = {}
for data in datas:
    d_id = data['id']
    turns = data['turns']
    for turn in turns:
        num_sent += 1
        turn_id = turn['turn_id']
        speaker = turn['speaker']
        zh = turn['zh']
        en = turn['en']
        num_words[0] += len(zh)
        num_words[1] += len(en_tokenizer.tokenize(en))
        
        if 'pronoun' in turn:
            pronoun = turn['pronoun'].strip().lower()
            pronouns = pronoun.split('/')
            for t in pronouns:
                if t in dp:
                    dp[t] += 1
                else:
                    dp[t] = 1
            num_dp += len(pronouns)
            full_zh = turn['full_zh']
        if 'wrong_zh' in turn:
            wrong_zh = turn['wrong_zh']
            num_wrong += 1
        

print('sentences number:', num_sent)
print('words number:', num_words)
print('wrong sentences number:', num_wrong)
print('drop pronouns:', num_dp)
print('drop pronouns:', dp)


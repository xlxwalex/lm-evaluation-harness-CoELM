import pandas as pd
import json
import os

orig_path = os.path.join(os.path.dirname(__file__),  "secret_data/human_annotations/eng_gold_data.csv")
df = pd.read_csv(orig_path, header=None)
input = df.iloc[0]
target = df[1:]
targets = [[] for _ in range(len(input))]
print(targets)
for i in range(28):
    row = df.iloc[1+i]
    items = [c.lower() for c in row]
    print(items)
    for j,item in enumerate(items):
        try:
            if item not in targets[j]:
                targets[j].append(item)
        except:
            print(j)
            print(targets)
            exit(1)

d = []

# Default prompt
template = "The past tense of verb {} is {}"
for i, t in zip(input, targets):
    d.append({"text": template.format(i, ('-').join(t))})
with open('./wug_data.json', 'w') as f:
    json.dump(d, f)
print(d)

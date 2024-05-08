import json

with open("wug_data.json", 'r') as fp:
    data = json.load(fp)

ENGLISH_SHOTS = [
    ("test", "tested"),
    ("teach", "taught"),
    ("build", "built"),
    ("sing", "sang"),
    ("hit", "hit")
]

out_data = []
shots = ""
for element in ENGLISH_SHOTS:
    shots += "The past tense of verb {} is {}. ".format(element[0], element[1])
for item in data:
    question = shots + item["text"]
    item["text"] = question
    out_data.append(item)

with open("wug_data-5shots.json", "w") as fp:
    fp.write(json.dumps(out_data, indent=4))

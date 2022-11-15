import json

with open("uni-dict.txt", "r") as f:
    json_str = f.read()

univs = json.loads(json_str)


def get_acronim(title):
    words = title.split(" ")
    acronim = "".join([word[0] for word in words])
    return acronim

def is_acronim(key):
    words = key.split(" ")
    return len(words) <= 1

converted_univ = {}

for k in univs.keys():

    if is_acronim(k):
        acronim = k
    else:
        acronim = get_acronim(k)

    converted_univ[acronim] = {"short": acronim, "long": k, "list": []}

    for v in univs[k]:

        jump_add = False

        if is_acronim(v):
            continue

        list_acronim = get_acronim(v)

        for l in converted_univ[acronim]["list"]:
            if l["short"] == list_acronim:
                jump_add = True

        if not jump_add:
            converted_univ[acronim]["list"].append({
                "short": get_acronim(v),
                "long": v
            })

with open("converted-dict.json", "w") as f:
    f.write(json.dumps(converted_univ))
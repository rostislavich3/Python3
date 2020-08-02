import json

# put JSON file in the open clause
with open("file.json", 'r', encoding="UTF-8") as f:
    persons = json.load(f)
    # print(json.dumps(persons["policies"], indent = 4, sort_keys=True))
    policies = json.dumps(persons['policies'])
    users = []
    for user in persons["policies"]:
        res = user['name']
        if "OWNER_" in res:
            str(res)
            print(res.split("OWNER_")[1])

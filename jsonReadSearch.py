import json

with open('data.json') as f:
    data = json.load(f)
    for dict in data[:]:
        activity_text = dict["Activity"]
        with open('activity_file.json', 'a') as json_file:
            json.dump(activity_text, json_file)
        risk_text = dict["Risk"]
        with open('risk_file.json', 'a') as json_file:
            json.dump(risk_text, json_file)
        mitigation_text = dict["Mitigation"]
        with open('mitigation_file.json', 'a') as json_file:
            json.dump(mitigation_text, json_file)
with open("activity_file.json") as f:
    activity_list = f.read().split('""')
    with open('activity_listFile.json', 'a') as json_file:
        json.dump(activity_list, json_file,indent=2)
        json_file.write('\n')
with open("risk_file.json") as f:
    risk_list=f.read().split('""')
    with open('risk_listFile.json', 'a') as json_file:
        json.dump(risk_list, json_file,indent=2)
        json_file.write('\n')
with open("mitigation_file.json") as f:
    mitigation_list=f.read().split('""')
    with open('mitigation_listFile.json', 'a') as json_file:
        json.dump(mitigation_list, json_file,indent=2)
        json_file.write('\n')
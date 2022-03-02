import json

with open('ccg_apr2021_EN_BUC.json', 'r') as ccg_file:
    ccg = json.load(ccg_file)

with open('lhb_apr2020_WA_BUC.json', 'r') as lhb_file:
    lhb = json.load(lhb_file)

ccg["features"].extend(lhb["features"])

for feature in ccg["features"]:
    feature["properties"] = {
        "AREACD": feature["properties"]["AREACD"],
        "AREANM": feature["properties"]["AREANM"]
    }

with open('ccg_apr2021_and_lhb_apr2020.json', 'w') as f:
    json.dump(ccg, f)

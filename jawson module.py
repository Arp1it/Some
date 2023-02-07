import json

data1 = '{"var1":"arpit", "var2":50}'
print(data1)
# print(data1["var1"])

parsed = json.loads(data1)
print(parsed)
print(parsed["var1"])
print(type(parsed))

data2 = {
    "channel_name": "Arpit",
    "cars": ["lambogini", "bmw", "bugati"],
    "fridge": (540, "roti"),
    "fridge": (540, "roti"),
    "frige": ("roti", 540),
    "isbad":False
}

print(data2)

par = json.dumps(data2)
print(par)
print(type(par))
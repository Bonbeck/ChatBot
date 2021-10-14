import json

dicionario = {
    "tecnologias cotidianas":
    {
        "hardware": ["celular", "computador", "consoles", "carro", "eletro-domestico"],
        "software": 
        {
            "programação":   ["python", "git", "notion", "VSCode",],
            "Sistema Operacionais": ["windows", "linux", "mac", "IOS", "android"],
            "softwares de controle de hardware": "firmware",
            "jogo": "CS",
            "apps": "facebook",
        }
    },
    "tecnologias científicas":
    {
        "invenções": ["remédios", "energia", "internet", "bluetooth", "wi-fi", "meios de transportes"]
    },
    "tecnologias aeroespaciais":
    {
        "espaço": ["satelite", "foguete", "estações"],
        "terra": ["gps", "rádio", "travesseiro da nasa"]
    }
}

with open("tecnologias.json", "w") as jsonFile:
    json.dump(dicionario, jsonFile, ensure_ascii=False)

with open("tecnologias.json") as jsonFile:
    json = json.load(jsonFile)

"""print(json)"""

#for valor in json:
#    print(valor)

for valor in json:
    print(json[valor])
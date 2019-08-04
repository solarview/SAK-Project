import json
import urllib.request
import os


# id_treatment(id, name, version, document, images( id : image data //Not now))
# how to call image id in doc: $$0$$

def update_treatments():
    data = json.loads(
        urllib.request.urlopen(
            "http://sakproject.ml/treatments_list.json").read().decode())  # data ( id : integer , version : integer)
    if not os.path.isdir("../resources/treatments"):
        os.mkdir("../resources/treatments")
    for i in range(len(data)):
        if not os.path.isfile("../resources/treatments/" + data[i]["id"] + "_treatment.sak"):
            f = open(i + "_treatment.sak", "w+")
            f.write(urllib.request.urlopen("http://sakproject.ml/" + i + "_treatments.sak").read().decode())
            f.close()
        else:
            f = open(i + "_treatment.sak", "r+")
            d = json.loads(f.read())
            if int(d["version"]) < data[i]["version"]:
                f.close()
                f = open(i + "_treatment.sak", "w+")
                f.write(urllib.request.urlopen("http://sakproject.ml/" + i + "_treatments.sak").read().decode())
                f.close()


def get_treatment_list() -> list:
    file_list = os.listdir("../resources/treatments/")
    treatment_list = []
    for fname in file_list:
        f = open("../resources/treatments/" + fname, "r+")
        treatment_list.append(json.loads(f.read())["name"])
    return treatment_list

import csv

def toCSV(file,varName):
    with open(file, newline='',encoding='utf-8-sig') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        data = {}
        for row in spamreader:
            key = row[0]
            value = row[1]
            data[key] = value
        pyFile = open(varName + ".py","x",encoding='utf-8-sig')
        pyFile.write(varName + " = " + str(data))
        pyFile.close()

toCSV("./utils/zProdukt.csv","products")
toCSV("./utils/zArbeitsgange.csv","workspace")
toCSV("./utils/zFehlergrunde.csv","faultReason")
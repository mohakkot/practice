import json
if __name__ == '__main__':
    client_json = {"name":"FFF","description":"","phone":"(123) 456-8964","email":"mohak.kothari@scryanalytics.com","startDate":{"$date":{"$numberLong":"946713600000"}},"endDate":{"$date":{"$numberLong":"1830326400000"}},"rounding":"1","dueDetails":[{"alert":{"$numberInt":"1"},"dueDate":"2019-02-01T08:00:00.000Z","type":"Balance Sheet","email":"monisha.puttaraju@scryanalytics.com","frequency":"Monthly"},{"alert":{"$numberInt":"1"},"dueDate":"2019-02-01T08:00:00.000Z","type":"Income Statement","email":"mohak.kothari@scryanalytics.com","frequency":"Monthly"}],"__v":{"$numberInt":"0"}}

    for i in range(0,26):
        for j in range(1,5):
            client_json["name"] = chr(i+65)+chr(i+65)+str(j)
            print(json.dumps(client_json))
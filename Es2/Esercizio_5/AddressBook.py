import json
"""data={}
data['contact']=[]
data['contact'].append({
    "name":"Lorenzo",
    "surname":"Costa",
    "email":"costalorenzo@gmail.com"
})
with open('Esercizio_5/contacts.json', 'w') as outfile:
    json.dump(data, outfile)"""
class AddressBook:
    def show(self):
        with open('Esercizio_5/contacts.json') as json_file:
            data = json.load(json_file)
            for p in data:
                print('Name: ' + p[3])
                print('Surname: ' + p[1])
                print('Email: ' + p[2])
                print('')

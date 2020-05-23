import cherrypy
import json
#non funziona come gli altri esercizi, python3 Ex3.py non fa nulla
@cherrypy.expose
class ConvertsTemp:
    exposed=True
    def PUT(self,**params):
        output={}
        #controllo i parametri
            #acquisisco i parametri
        body=cherrypy.request.body.read()
        json_body=json.loads(body.decode('utf-8'))
        originalUnit=json_body['originalUnit']
        targetUnit=json_body['targetUnit']
        originalValues=float(json_body['values'])

        #dichiaro array che conterra i valori convertiti
        targetValues=[]
        #converto la temperatura per ogni valore nell'insieme di originalValues
        for value in originalValues:
            if(originalUnit=='K'):
                if(targetUnit=='C'):
                    targetValues.append(originalValue-273.15)
                elif(targetUnit=='F'):
                    targetValues.append(((originalValue-273.15)*9/5)+32)
            elif(originalUnit=='C'):
                if(targetUnit=='K'):
                    targetValues.append(originalValue+273.15)
                elif(targetUnit=='F'):
                    targetValues.append((originalValue*9/5)+32)
            elif(originalUnit=='F'):
                if(targetValue=='K'):
                    targetValues.append(((originalValue-32)*5/9)+273.15)
                elif(targetValue=='C'):
                    targetValues.append((originalValue-32)*5/9)

        output={
        "originalValue":originalValues,
        "originalUnit":originalUnit,
        "targetValue":targetValues,
        "targetUnit":targetUnit,
        }

        return json.dumps(output)

if __name__ == '__main__':
    conf = {
        "/": {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }

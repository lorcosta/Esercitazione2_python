import cherrypy
import json

@cherrypy.expose
class ConvertsTemp():
    def GET(self,*uri,**params):#cos'è l'asterisco singolo e doppio
        output={}
        #controllo i parametri
        if (params!={} and len(params.items())==3):
            #acquisisco i parametri
            originalUnit=params['originalUnit']
            targetUnit=params['targetUnit']
            originalValue=float(params['value'])

            #converto la temperatura
            if(originalUnit=='K'):
                if(targetUnit=='C'):
                    targetValue=originalValue-273.15
                elif(targetUnit=='F'):
                    targetValue=((originalValue-273.15)*9/5)+32
            elif(originalUnit=='C'):
                if(targetUnit=='K'):
                    targetValue=originalValue+273.15
                elif(targetUnit=='F'):
                    targetValue=(originalValue*9/5)+32
            elif(originalUnit=='F'):
                if(targetValue=='K'):
                    targetValue=((originalValue-32)*5/9)+273.15
                elif(targetValue=='C'):
                    targetValue=(originalValue-32)*5/9

            output={
            "originalValue":originalValue,
            "originalUnit":originalUnit,
            "targetValue":targetValue,
            "targetUnit":targetUnit
            }

            return json.dumps(output)#cos'è dumps()

        else:
            raise cherrypy.HTTPError(404,"Parametri errati.")

if __name__ == '__main__':
    conf = {
        "/": {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }

    cherrypy.tree.mount(ConvertsTemp(), "/", conf)
    cherrypy.engine.start()
    cherrypy.engine.block()

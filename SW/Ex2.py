import cherrypy
import json

@cherrypy.expose
class ConvertsTemp():
    def GET(self,*uri):
        output={}
        #controllo i parametri
        if len(uri)==4:
            #acquisisco i parametri
            originalUnit=uri[2]
            targetUnit=uri[3]
            originalValue=float(uri[1])

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
            "targetUnit":targetUnit,
            "style":"RESTful-style"
            }

            return json.dumps(output)

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

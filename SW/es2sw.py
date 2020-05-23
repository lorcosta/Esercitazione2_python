import cherrypy
import json

class Converter:
	exposed = True
	def GET(self, *uri):
		if len(uri) == 4:
			value = float(uri[1])
			originalUnit = uri[2]
			targetUnit = uri[3]

			if originalUnit == 'C':
				if targetUnit == 'K':
					convertedValue = value + 273.15
				elif targetUnit == 'F':
					convertedValue = (value * (9/5)) + 32

			elif originalUnit == 'K':
				if targetUnit == 'C':
					convertedValue = value - 273.15
				elif targetUnit == 'F':
					convertedValue = ((value - 273.15) * (9/5)) + 32

			elif originalUnit == 'F':
				if targetUnit == 'C':
					convertedValue = (value - 32) * (5/9)
				elif targetUnit == 'K':
					convertedValue = ((value -32) * (5/9)) + 273.15

			output = {
			"orignalValue": value,
			"originalUnit": originalUnit,
			"convertedValue": convertedValue,
			"targetUnit": targetUnit
			}

			return json.dumps(output)

		else:
			raise cherrypy.HTTPError(404, "Numero di parametri insufficiente")

if __name__ == '__main__':
	#Standard configuration to serve the url "localhost:8080"
	conf={
		'/':{
		'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
		'tool.session.on':True
		}
	}

	cherrypy.tree.mount(Converter(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()

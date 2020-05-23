import cherrypy
import json

class Converter:
	exposed = True

	def PUT(self, **params):
		body = cherrypy.request.body.read()
		json_body = json.loads(body.decode('utf-8'))
		values = json_body["values"]
		originalUnit = json_body["originalUnit"]
		targetUnit = json_body["targetUnit"]

		convertedValues = []
		for value in values:
			if originalUnit == 'C':
				if targetUnit == 'K':
					convertedValues.append(value + 273.15)
				elif targetUnit == 'F':
					convertedValues.append((value * (9/5)) + 32)

			elif originalUnit == 'K':
				if targetUnit == 'C':
					convertedValues.append(value - 273.15)
				elif targetUnit == 'F':
					convertedValues.append(((value - 273.15) * (9/5)) + 32)

			elif originalUnit == 'F':
				if targetUnit == 'C':
					convertedValues.append((value - 32) * (5/9))
				elif targetUnit == 'K':
					convertedValue.append(((value -32) * (5/9)) + 273.15)

		output = {
		"toBeConverted": values,
		"originalUnit": originalUnit,
		"converted": convertedValues,
		"targetUnit": targetUnit
		}

		return (json.dumps(output))

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

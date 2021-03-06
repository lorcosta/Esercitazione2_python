import paho.mqtt.client as PahoMQTT
import json, time
from datetime import datetime
import random
import string

class Publisher:
    def __init__(self, clientID,topic,broker):
        self.clientID = clientID
        # create an instance of paho.mqtt.client
        self._paho_mqtt = PahoMQTT.Client(self.clientID, clean_session=True) # register the callback
        self._paho_mqtt.on_connect = self.OnConnect
        self.topic=topic
        self.messageBroker = broker
        def start (self):
            #manage connection to broker
            self._paho_mqtt.connect(self.messageBroker, port=1883)
            self._paho_mqtt.loop_start()
        def stop (self):
            self._paho_mqtt.loop_stop()
            self._paho_mqtt.disconnect()
        def myPublish(self, topic, message):
            # publish a message with a certain topic
            self._paho_mqtt.publish(topic, message, 2)
            print(f"Published at topic: {self.topic}")
        def onConnect(self, paho_mqtt, userdata, flags, rc):
            print(f"Connected to {self.messageBroker} with result code: {rc}")
if __name__ == "__main__":

    try:
        with open("files/ID.json", "rb") as f:
            content = json.load(f)
            clientID = content["clientID"]

    except FileNotFoundError:
        lenght = 5
        clientID = "".join(random.choices(string.ascii_letters + string.digits, k=lenght)) #genera un ID random
        with open("files/ID.json", "w") as f:
            dict = {"clientID": clientID}
            json.dump(dict, f)

    topic = "/iot/led/this/better/be/unique/%s" %clientID
    broker = "mqtt.eclipse.org"
    publisherID = clientID+"p"
    pub = Publisher(publisherID, topic, broker)
    pub.start()
    time.sleep(1)
    while True:
        user_input = input('Digita "on" per accendere la luce, "off" per spegnerla... ')
        if user_input.casefold() == "on":
            ledOn = True
        elif user_input.casefold() == "off":
            ledOn = False
        elif user_input.casefold() == "q":
            break
        else:
            print("Input non valido, riprova.")
            continue

        instructions = {
        "led_on": ledOn,
        "date": str(datetime.now()),
        "clientID": publisherID
        }

        pub.myPublish(json.dumps(instructions))

    pub.stop()
    print("Publisher disconnected.")

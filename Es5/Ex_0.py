import paho.mqtt.client as PahoMQTT
import time
class MyPublisher:
    def __init__(self, clientID,broker):
        self.clientID = clientID
        # create an instance of paho.mqtt.client
        self._paho_mqtt = PahoMQTT.Client(self.clientID, False) # register the callback
        self._paho_mqtt.on_connect = self.myOnConnect
        self.messageBroker = broker
        def start (self):
            #manage connection to broker
            self._paho_mqtt.connect(self.messageBroker, 1883)
            self._paho_mqtt.loop_start()
        def stop (self):
            self._paho_mqtt.loop_stop()
            self._paho_mqtt.disconnect()
        def myPublish(self, topic, message):
            # publish a message with a certain topic
            self._paho_mqtt.publish(topic, message, 2)
        def myOnConnect (self, paho_mqtt, userdata, flags, rc):
            print ("Connected to %s with result code: %d" % (self.messageBroker,rc))
class MySubscriber:
    def __init__(self, clientID,topic,broker):
        self.clientID = clientID
        # create an instance of paho.mqtt.client
        self._paho_mqtt = PahoMQTT.Client(clientID, False)
            # register the callback
        self._paho_mqtt.on_connect = self.myOnConnect
        self._paho_mqtt.on_message = self.myOnMessageReceived
        self.topic = topic self.messageBroker = broker
    def start (self):
        #manage connection to broker
        self._paho_mqtt.connect(self.messageBroker, 1883)
        self._paho_mqtt.loop_start()
        # subscribe for a topic
        self._paho_mqtt.subscribe(self.topic, 2)
    def stop (self):
        self._paho_mqtt.unsubscribe(self.topic)
        self._paho_mqtt.loop_stop()
        self._paho_mqtt.disconnect()
    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to %s with result code: %d" % (self.messageBroker, rc))
    def myOnMessageReceived (self, paho_mqtt , userdata, msg):
        # A new message is received
        print ("Topic:'" + msg.topic+"', QoS: '"+str(msg.qos)+"' Message:'"+str(msg.payload) + "'")

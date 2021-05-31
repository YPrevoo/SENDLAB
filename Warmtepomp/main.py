import paho.mqtt.client as mqtt
import datetime

localhost = mqtt.Client("test")
sendlab = mqtt.Client()

def on_connect_sendlab(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("#")

def on_connect_localhost(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Pi Connected at: " + datetime.now())

    client.subscribe("homie/daikin-heatingunit/spaceheating/1-operation-targettemperature")
    client.subscribe("homie/daikin-heatingunit/spaceheating/1-sensor-indoortemperature")
    client.subscribe("homie/daikin-heatingunit/spaceheating/1-sensor-outdoortemperature")
    client.subscribe("homie/daikin-heatingunit/spaceheating/1-operation-roomtemperatureauto")
    client.subscribe("homie/daikin-heatingunit/spaceheating/1-operation-roomtemperaturecooling")
    client.subscribe("homie/daikin-heatingunit/spaceheating/1-operation-roomtemperatureheating")
    client.subscribe("homie/daikin-heatingunit/spaceheating/1-consumption")

    client.subscribe("homie/daikin-heatingunit/domestichotwatertank/2-sensor-tanktemperature")
    client.subscribe("homie/daikin-heatingunit/domestichotwatertank/2-operation-targettemperature")
    client.subscribe("homie/daikin-heatingunit/domestichotwatertank/2-consumption")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


localhost.on_connect = on_connect_localhost
localhost.on_message = on_message

sendlab.on_connect = on_connect_sendlab
sendlab.on_message = on_message

localhost.connect("localhost", 1883, 60)

#sendlab.username_pw_set("server", password="servernode")
sendlab.username_pw_set("node", password="smartmeternode")
sendlab.connect("sendlab.nl", 11884, 60)


timestamp = datetime.now()
while( 1 ):
    localhost.loop()
    sendlab.loop()

    timediff = datetime.now() - timestamp
    if ( timediff.seconds > 10 ):
        print("test")
        timestamp = datetime.now()
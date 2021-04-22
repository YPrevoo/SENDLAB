#include <MQTTAdapter.h>

MQTTAdapter::MQTTAdapter(Client &client)
{
    mqtt.setClient(client);
    mqtt.setBufferSize(2048);
    
    mqtt.setServer(MQTT_SERVER_HOST, MQTT_SERVER_PORT);
}

void MQTTAdapter::connect()
{
    while (!mqtt.connected())
    {
        mqtt.connect(MQTT_ID);
        if (mqtt.connected())
        {
            // connected
        }
    }
}

void MQTTAdapter::disconnect()
{
    mqtt.disconnect();
}

bool MQTTAdapter::connected()
{
    return mqtt.connected();
}

void MQTTAdapter::subscribe(char topic[])
{
    mqtt.subscribe(topic);
}

void MQTTAdapter::setCallback(std::function<void(char *, uint8_t *, unsigned int)> callback)
{
    mqtt.setCallback(callback);
}

void MQTTAdapter::publish(char topic[], char message[])
{
    mqtt.publish(topic, message);
}
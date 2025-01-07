import paho.mqtt.publish as publish

# Définir le broker
# broker_address = "broker.hivemq.com"
broker_address = "test.mosquitto.org"

# Définir le sujet (topic) sur lequel publier
# topic = "snir/bts/2023/msg"
topic = "meteo/mesures/snir2/message"


# Définir le message à publier
message = "j'aime le sucre"

# Publier le message
publish.single(topic, message, hostname=broker_address)

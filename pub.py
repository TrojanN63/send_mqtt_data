import paho.mqtt.client as mqtt
import time
import pandas as pd
import json

client = mqtt.Client()
client.connect("localhost", 1883, 60)

print("Enviando mensagens...")

for i in range(100):
    data = pd.read_csv('data.csv')
    msg = json.dumps({
        "forces": [float(data['pl1'][i]), float(data['pl2'][i]), float(data['pr1'][i]), float(data['pr2'][i])],
        "xvy": "2v2"
    })
    client.publish("players_data", msg)
    time.sleep(0.5)

client.disconnect()
print("Publisher desconectado")

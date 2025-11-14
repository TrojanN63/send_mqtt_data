import paho.mqtt.client as mqtt

# Callback quando uma mensagem chegar
def on_message(client, userdata, message):
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("players_data")  # tópico de teste

print("Subscriber conectado, esperando mensagens...")
client.loop_forever()

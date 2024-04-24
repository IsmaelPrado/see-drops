# Imports
import network
from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin, PWM
import time

# Configuración MQTT
MQTT_BROKER = "172.20.10.6"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "see-drops"
MQTT_PORT = 1883

# Variable para almacenar el estado del switch
switch_state = "apagar"

def wifi_connect():
    print ("Conectando", end="")
    sta_if = network.WLAN (network.STA_IF)
    sta_if.active(True)
    sta_if.connect("ElGerasxd", "xdpapi23")
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("Wi Fi is connected")
    
def llegada_mensaje(topic, msg):
    global switch_state
    print(msg)  # Imprimir mensaje recibido (opcional)
    if msg == b'encender':
        switch_state = "encender"
    elif msg == b'apagar':
        switch_state = "apagar"

def publicar_mensaje(client, msg, topic):
    client.publish(topic, msg)

def leer_sensor(pin):
    contador = 0
    tiempo_inicial = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), tiempo_inicial) < 1000:  # Lee durante 1 segundo
        if pin.value():
            contador += 1
        time.sleep_ms(10)
    return contador

def parpadear_led(led):
    for _ in range(5):  # Parpadear 5 veces
        led.value(1)  # Encender
        time.sleep(0.1)
        led.value(0)  # Apagar
        time.sleep(0.1)

def sonar_piezo(piezo):
    piezo.freq(2000)  # Frecuencia del sonido (2000 Hz)
    piezo.duty(600)   # Ciclo de trabajo al 50%
    time.sleep(0.1)
    piezo.duty(0)     # Apagar el sonido

# Configurar pines y objetos PWM
pin_sensor1 = Pin(22, Pin.IN)  # Pin D14
pin_sensor2 = Pin(23, Pin.IN)  # Pin D27
led1 = Pin(21, Pin.OUT)  # LED en pin 15
led2 = Pin(15, Pin.OUT)
piezo1 = PWM(Pin(2))
piezo2 = PWM(Pin(5))

# Inicializar LED y piezos
led1.value(0)
led2.value(0)
piezo1.duty(0)
piezo2.duty(0)

def main():
    global switch_state
    wifi_connect()  # Conectar a WiFi
    
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado en %s, al tópico %s" % (MQTT_BROKER, MQTT_TOPIC))

    while True:
        lectura1 = leer_sensor(pin_sensor1)
        lectura2 = leer_sensor(pin_sensor2)

        print(lectura1, lectura2)

        # Publicar las lecturas de los sensores en MQTT
        publicar_mensaje(client, "{}".format(lectura1), MQTT_TOPIC + "-1")
        publicar_mensaje(client, "{}".format(lectura2), MQTT_TOPIC + "-2")

        # Activar los piezos y LEDs si la lectura está entre 20 y 80 y el switch está en "encender"
        if switch_state == "encender":
            if 20 <= lectura1 <= 80:
                parpadear_led(led1)
                sonar_piezo(piezo1)

            if 20 <= lectura2 <= 80:
                parpadear_led(led2)
                sonar_piezo(piezo2)

        time.sleep(3)  # Espera 1 segundo antes de volver a leer

if __name__ == "__main__":
    main()

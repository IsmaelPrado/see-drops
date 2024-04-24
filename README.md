# 🌊 **See-Drops: Documentación Completa del Proyecto IoT 2024** 🌐
Contiene la documentacion del proyecto para IoT 2024

## Integrantes
- Hernández López Gerardo - 1222100437
- Manuel Martínez Jassiel Noe - 1222100440
- Prado Salazar Cristian Ismael - 1222100451

## Lista del Hardware utilizado
| Id | Componente | Descripción | Imagen | Cantidad | Costo total |
|----|------------|-------------|--------|----------|-------------|
| 1  | Sensor de flujo | Detecta el flujo de agua en los tubos | ![Sensor de flujo](https://silicio.mx/media/catalog/product/cache/1/image/650x650/5e06319eda06f020e43594a9c230972d/p/o/pow110d3b/Sensor-de-flujo-de-agua-1_2---31.jpg) | 2 | $150 |
| 2  | Minibomba de agua | Bomba de agua compacta para generar flujo | ![Minibomba de agua](https://m.media-amazon.com/images/I/51tWuXbjoHL._AC_UF894,1000_QL80_DpWeblab_.jpg) | 4 | $98 |
| 3  | Llave de paso | Controla el flujo de agua en los tubos | ![Llave de paso](https://static.grainger.com/rp/s/is/image/Grainger/29F225_AS01) | 2 | $94 |
| 4  | Tubo de PVC | Conecta los componentes del sistema de detección de fugas | ![Tubo de PVC](https://electricaseis.com.mx/111-home_default/tubo-pvc-hidraulico-3-4.jpg) | 4 | $45 |
| 5  | Boquilla para llave de paso | Permite enroscar la llave de paso en los tubos | ![Boquilla para llave de paso](https://http2.mlstatic.com/D_NQ_NP_869485-MLM70126575449_062023-O.webp) | 4 | $30 |
| 6  | Codo de tres salidas | Se coloca entre los tubos para direccionar el flujo | ![Codo de tres salidas](https://cdn.homedepot.com.mx/productos/338438/338438-z.jpg) | 2 | $15 |
| 7  | Manguera trasparente 3/8| Conecta las bombas y sensores de flujo con el sistema | ![Manguera]([imagen_manguera.jpg](https://cdn.homedepot.com.mx/productos/101320/101320-d.jpg)) | 4 | $40 |
| 8  | Termofit | Material para las conexiones entre componentes | ![Termofit](https://casram.mx/wp-content/uploads/2022/05/Termofit-tubing-1.jpg) | 5 metros | $25 |
| 9  | ESP32 | Microcontrolador para el sistema IoT | ![ESP32](https://m.media-amazon.com/images/I/61o2ZUzB4XL._AC_UF894,1000_QL80_DpWeblab_.jpg) | 1 | $320 |
| 10 | Buzzer | Emite sonido de alerta ante detección de fugas | ![Buzzer](https://m.media-amazon.com/images/I/517iEhc31GL._AC_UF894,1000_QL80_.jpg) | 2 | $160 |
| 11 | LED | Indica estados o condiciones del sistema | ![LED](https://www.steren.com.mx/media/catalog/product/cache/0236bbabe616ddcff749ccbc14f38bf2/image/15879bb11/led-ultrabrillante-de-5-mm-color-rojo.jpg) | 2 | $2 |
| 12 | Cable de estaño (color rojo y negro) | Utilizado para las conexiones eléctricas | ![Cable de estaño](https://www.steren.com.mx/media/catalog/product/cache/0236bbabe616ddcff749ccbc14f38bf2/image/208864211/alambre-esta-ado-para-conexiones-de-color-negro-calibre-22-awg.jpg) | 12 metros (6 rojos, 6 negros) | $144 |
| 13 | Cinta aislante | Aísla y protege las conexiones eléctricas | ![Cinta aislante]([i(https://cdn.homedepot.com.mx/productos/862736/862736-d.jpg)) | 1 | $60 |
| 14 | Caja de plástico | Contenedor para guardar los componentes del sistema | ![Caja de plástico](https://m.media-amazon.com/images/I/51ze1QScdPL._AC_UF894,1000_QL80_.jpg) | 1 | $40 |
| 15 | Raspberry Pi | Placa de computadora para almacenamiento de datos y control del sistema | ![Raspberry Pi](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg/1200px-Raspberry_Pi_4_Model_B_-_Side.jpg) | 1 | Prestada |


## Lista de Software utilizado
| Id | Software   | Version   | Tipo            |
|----|------------|-----------|-----------------|
| 1  | Thonny     | 3.3.7     | IDE             |
| 2  | Node-RED   | 2.3.2     | Plataforma IoT  |
| 3  | Grafana    | 8.3.6     | Plataforma IoT  |
| 4  | PostgreSQL | 14.2      | Sistema de gestión de bases de datos |


## Visión del producto
Como es habitual en agilidad, la comunicación se ve enormemente potenciada cuando acompañamos nuestro cometido con elementos visuales. En este proyecto, se busca desarrollar un sistema de detección de fugas para casas que no solo ahorre gastos, sino que también garantice un mejor cuidado del agua al resolver las fugas de manera eficiente.
    
    PARA Propietarios de viviendas preocupados por el ahorro de gastos y el cuidado del agua.
    QUIEN Tienen la necesidad de detectar y solucionar fugas de agua de manera rápida y precisa para reducir los costos asociados y garantizar un uso responsable del agua.
    EL Producto LeakGuard QUE ES UN sistema de detección de fugas avanzado basado en sensores de flujo y análisis inteligente.
    QUE Ofrece alertas inmediatas ante cualquier fuga de agua detectada, permitiendo una intervención temprana y eficaz para evitar pérdidas innecesarias.
    A DIFERENCIA DE Otras soluciones de detección de fugas que pueden ser menos precisas o carecen de capacidad de análisis inteligente para una detección temprana.
    NUESTRO PRODUCTO Se destaca por su capacidad de detección precisa y análisis inteligente, lo que garantiza un ahorro significativo en gastos relacionados con fugas de agua y promueve un uso más responsable y sostenible del recurso.

Como consejo derivado de mi experiencia para la utilización de este patrón de forma positiva, si hay elementos en negativo en la parte de A DIFERENCIA DE, propongo escribirlos en positivo en NUESTRO PRODUCTO, convierte nuestro mensaje en más positivo y por tanto en más poderoso.

"Un enunciado de visión exitoso
es lo suficientemente convincente
para ser ampliamente compartido,
conciso y fácil de recordar"
Referencia:


    Menzinsky, A. (2017). ¿Cómo se realiza la visión del producto?. Scrum.menzinsky.com. Retrieved 19 January 2017, from ¿Cómo se realiza la visión del producto?


## Conexiones
Aquí mostramos las conexiones de nuestro proyecto:

![seedrops}](https://github.com/IsmaelPrado/see-drops/assets/135056065/65ae2622-8123-42c4-b23d-00e3a4aa5d5c)
![seedropspbc](https://github.com/IsmaelPrado/see-drops/assets/135056065/7a7f20d5-43d8-481c-870f-0033ec77c128)
![seadropsESpematico](https://github.com/IsmaelPrado/see-drops/assets/135056065/9bf0bd3f-e4f8-46ca-b290-141d36e38e00)





## Funcionalidades

| Id | Historia de usuario | Prioridad | Estimación | Cómo probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
| 1  | Como administrador, quiero visualizar gráficos en Grafana que muestren el historial de consumo de agua en la vivienda. | Alta | 6 puntos | 1. Acceder a Grafana como administrador. 2. Verificar que los gráficos muestren el historial de consumo de agua. | Equipo de Desarrollo |
| 3  | Como administrador, quiero recibir alertas en Grafana cuando se detecte una fuga de agua en alguna vivienda. | Alta | 5 puntos | 1. Configurar las alertas en Grafana para detectar fugas de agua. 2. Simular una fuga de agua y verificar que se reciba la alerta en Grafana. | Equipo de Desarrollo |
| 5  | Como administrador, quiero poder exportar los datos históricos de consumo de agua y detección de fugas en Grafana para análisis externos. | Media | 8 puntos | 1. Iniciar sesión como administrador en Grafana. 2. Acceder a la función de exportación de datos históricos y verificar que se puedan exportar los datos correctamente. | Equipo de Desarrollo |
| 6  | Como usuario, quiero recibir alertas audibles a través de un buzzer cuando se detecte una fuga de agua en mi hogar. | Alta | 5 puntos | 1. Simular una fuga de agua en la maqueta. 2. Verificar que el buzzer emita un sonido para alertar sobre la fuga. | Equipo de Desarrollo |
| 7 | Como usuario, quiero que el sistema registre y almacene los datos de flujo de agua en una base de datos en la Raspberry Pi para su análisis y seguimiento. | Alta | 8 puntos | 1. Generar flujo de agua en la maqueta. 2. Verificar que los datos de flujo se almacenen correctamente en la base de datos de la Raspberry Pi. | Equipo de Desarrollo |
1. Configurar las alertas en Grafana para detectar fugas de agua utilizando los datos de la base de datos en la Raspberry Pi. 2. Simular una fuga de agua en una área específica y verificar que se reciba la alerta en Grafana y el buzzer emita el sonido correspondiente. | Equipo de Desarrollo |


# Evidencias de funcionamiento
- Fotografías de evidencia de conexión física
![ac2cade8-9b52-4ba6-ad4b-9225b53cbdff](https://github.com/IsmaelPrado/see-drops/assets/135056065/6592b461-b29b-488d-901c-10de20be7950)
![84d4d307-df8f-49e7-aeda-146a99d7070b](https://github.com/IsmaelPrado/see-drops/assets/135056065/17e2dda4-ab99-4de9-bb75-24d07d683b21)
![45384688-cfa6-4949-8004-de16786159ec](https://github.com/IsmaelPrado/see-drops/assets/135056065/d784d95c-57ec-4252-842a-c5c55dacb4c9)


- Captura de pantalla de flujos de Node RED
![377f7beb-a7b0-4b06-999c-b3ea67bc3366](https://github.com/IsmaelPrado/see-drops/assets/135056065/3db0f471-f138-4a4d-af30-6969db09c66c)

![ee9ddcb7-8454-415b-bf34-578e9f14b134](https://github.com/IsmaelPrado/see-drops/assets/135056065/63dfe434-f708-431d-8f32-36f62a2cf9b4)

![a3b73ac6-73c0-43fd-84fe-edf8c747e284](https://github.com/IsmaelPrado/see-drops/assets/135056065/fc93d983-feda-48d5-8a5b-eba2ef68164e)

![784155a9-817b-4f82-aa64-9810956b4856](https://github.com/IsmaelPrado/see-drops/assets/135056065/ae86aadd-a253-41fd-992d-2688dc09d183)

- Captura de las pantallas del proyecto DASHBOARD y Pantalla de la ESP32
![0096fb19-e08d-46cc-8fdd-9c2b94f4f5d4](https://github.com/IsmaelPrado/see-drops/assets/135056065/a9bb647f-cec8-4af2-9c9f-fae22c278b45)

![343155ed-cd72-42fe-b052-093fd1071c87](https://github.com/IsmaelPrado/see-drops/assets/135056065/a0bb15d3-0837-4230-b93a-cadab90df032)

![06dbe8cf-a78b-465d-9400-88127edca973](https://github.com/IsmaelPrado/see-drops/assets/135056065/3c2889d9-ea04-4018-949a-e36ea6efd98a)

- Código fuente
  
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
  ![b50feb53-8f15-4298-b5e9-e5def6aef74f](https://github.com/IsmaelPrado/see-drops/assets/135056065/dbdb455d-7bc7-4b30-b578-158da670845e)

# Video demostrativo de las funcionalidades del proyecto: https://youtu.be/3VXkXP6eLUQ?si=QHWZukGNufMEGZiN

## Carta de Agradecimiento:

![5daf1664-c143-4c48-99b6-0531410c0462](https://github.com/IsmaelPrado/see-drops/assets/135056065/aa5f8c8e-044c-46ee-b5be-88708c0d14ff)


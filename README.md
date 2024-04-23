# Documentación del Proyecto Ver-Gotas IoT 2024
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



## Funcionalidades

| Id | Historia de usuario | Prioridad | Estimación | Cómo probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
| 1  | Como administrador, quiero visualizar gráficos en Grafana que muestren el historial de consumo de agua en la vivienda. | Alta | 6 puntos | 1. Acceder a Grafana como administrador. 2. Verificar que los gráficos muestren el historial de consumo de agua. | Equipo de Desarrollo |
| 3  | Como administrador, quiero recibir alertas en Grafana cuando se detecte una fuga de agua en alguna vivienda. | Alta | 5 puntos | 1. Configurar las alertas en Grafana para detectar fugas de agua. 2. Simular una fuga de agua y verificar que se reciba la alerta en Grafana. | Equipo de Desarrollo |
| 5  | Como administrador, quiero poder exportar los datos históricos de consumo de agua y detección de fugas en Grafana para análisis externos. | Media | 8 puntos | 1. Iniciar sesión como administrador en Grafana. 2. Acceder a la función de exportación de datos históricos y verificar que se puedan exportar los datos correctamente. | Equipo de Desarrollo |
| 6  | Como usuario, quiero recibir alertas audibles a través de un buzzer cuando se detecte una fuga de agua en mi hogar. | Alta | 5 puntos | 1. Simular una fuga de agua en la maqueta. 2. Verificar que el buzzer emita un sonido para alertar sobre la fuga. | Equipo de Desarrollo |
| 7 | Como usuario, quiero que el sistema registre y almacene los datos de flujo de agua en una base de datos en la Raspberry Pi para su análisis y seguimiento. | Alta | 8 puntos | 1. Generar flujo de agua en la maqueta. 2. Verificar que los datos de flujo se almacenen correctamente en la base de datos de la Raspberry Pi. | Equipo de Desarrollo |
| 9 | Como administrador, quiero recibir alertas en Grafana cuando se detecte una fuga de agua en alguna área específica de la vivienda, utilizando los datos de la base de datos en la Raspberry Pi y la información del buzzer. | Alta | 8 puntos | 1. Configurar las alertas en Grafana para detectar fugas de agua utilizando los datos de la base de datos en la Raspberry Pi. 2. Simular una fuga de agua en una área específica y verificar que se reciba la alerta en Grafana y el buzzer emita el sonido correspondiente. | Equipo de Desarrollo |

## Prototipo en dibujo
- Coloca la imagen de tu proyecto al iniciar el desarrollo

# Evidencias de funcionamiento
- Captura de pantalla de flujos de Node RED
- Captura de las pantallas del proyecto DASHBOARD y Pantalla de la ESP32
- Video demostrativo de las funcionalidades del proyecto
- Código fuente (PROHIBIDO PONER COMPRIMIDOS)

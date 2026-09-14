# DOMAIN — ZABBIX EN PROFUNDIDAD

## 1. Identidad del PATH

Este perfil corresponde al PATH:

**ZABBIX EN PROFUNDIDAD**

El objetivo no es enseñar únicamente a utilizar el frontend de Zabbix ni producir un curso basado en una sucesión de capturas de interfaz.

El objetivo es formar al estudiante desde cero hasta un nivel avanzado y experto en:

- arquitectura de Zabbix;
- instalación y operación;
- Zabbix Server;
- Zabbix Agent;
- Zabbix Agent 2;
- Zabbix Proxy;
- frontend;
- base de datos;
- hosts y grupos;
- items;
- item keys;
- preprocessing;
- history;
- trends;
- triggers;
- events;
- problems;
- actions;
- notifications;
- escalations;
- templates;
- macros;
- discovery;
- Low-Level Discovery;
- autoregistration;
- SNMP;
- SNMP traps;
- IPMI;
- JMX;
- HTTP Agent;
- web monitoring;
- trapper items;
- zabbix_sender;
- external checks;
- script items;
- calculated items;
- dependent items;
- dashboards;
- widgets;
- maps;
- graphs;
- services;
- SLA;
- inventario;
- API;
- automatización;
- integraciones;
- seguridad;
- TLS;
- PSK;
- certificados;
- usuarios;
- roles;
- permisos;
- alta disponibilidad;
- monitorización distribuida;
- escalabilidad;
- performance tuning;
- queue;
- caches;
- housekeeper;
- almacenamiento histórico;
- PostgreSQL;
- self-monitoring;
- troubleshooting;
- protocolos;
- procesos internos;
- internals de Server, Proxy y agentes;
- modelo de datos;
- arquitectura empresarial;
- backup;
- disaster recovery;
- upgrades;
- operación de producción.

El estudiante debe terminar siendo capaz no sólo de configurar Zabbix, sino de explicar y diagnosticar el recorrido completo de los datos dentro de la plataforma.

---

# 2. Nivel y progresión

El PATH empieza en nivel cero y termina en nivel experto.

No asumir experiencia previa con Zabbix.

Sí pueden introducirse progresivamente conocimientos de:

- Linux;
- Fedora;
- systemd;
- redes TCP/IP;
- firewalld;
- SELinux;
- PostgreSQL;
- SNMP;
- Java/JMX;
- HTTP;
- TLS;
- JSON;
- APIs;
- shell;
- herramientas Unix.

Cuando alguno de estos conocimientos sea necesario para comprender una lección, explicar únicamente el contexto necesario sin convertir la lección en un curso completo de esa tecnología.

El PATH debe mantener progresión.

No introducir en profundidad una característica cuyo bloque específico aparece posteriormente, salvo cuando sea indispensable para explicar el concepto actual.

---

# 3. Plataforma de referencia

La plataforma principal del curso es:

**Fedora Linux**

Cuando corresponda, mencionar también compatibilidad o diferencias relevantes con:

- Fedora;
- RHEL;
- CentOS Stream;
- distribuciones Linux compatibles.

No orientar el curso a Windows.

Windows puede aparecer únicamente cuando sea técnicamente necesario para explicar que Zabbix puede monitorizar ese sistema o cuando una funcionalidad sea multiplataforma.

Los laboratorios principales deben realizarse sobre Linux.

---

# 4. Política de versiones de Zabbix

La referencia principal del PATH es la versión estable actual de Zabbix documentada oficialmente.

Baseline al crear este perfil:

- Zabbix 7.4: referencia funcional principal.
- Zabbix 7.0 LTS: referencia adicional para instalaciones LTS y diferencias relevantes.

No asumir que una funcionalidad presente en versiones antiguas conserva exactamente:

- su sintaxis;
- su interfaz;
- su arquitectura;
- sus parámetros;
- sus procesos;
- sus valores predeterminados;
- su estado de soporte.

Cuando exista una diferencia significativa entre versiones, indicarla explícitamente.

Ejemplo:

```text
En Zabbix 7.4...
En Zabbix 7.0 LTS...
```

No convertir la lección en una comparación histórica salvo que el tema lo requiera.

Las funcionalidades eliminadas, obsoletas o modificadas deben identificarse como tales.

No presentar documentación de versiones no soportadas como comportamiento actual.

---

# 5. Fuentes de autoridad

Orden general de autoridad técnica:

1. documentación oficial de Zabbix correspondiente a la versión estudiada;
2. código fuente oficial de Zabbix;
3. documentación oficial de componentes externos;
4. especificaciones y RFC relevantes;
5. documentación Fedora/RHEL;
6. documentación PostgreSQL;
7. documentación Net-SNMP;
8. documentación Java/OpenJDK/JMX;
9. libros especializados;
10. artículos técnicos y material secundario.

Cuando una fuente secundaria contradiga la documentación actual de Zabbix, prevalece la documentación oficial correspondiente a la versión estudiada.

Para internals, cuando la documentación de usuario no sea suficiente, usar conceptualmente:

- código fuente;
- nombres de procesos;
- arquitectura observable;
- protocolos documentados;
- estructuras documentadas.

No inventar internals.

---

# 6. Modelo mental central del curso

El curso debe construir progresivamente este modelo:

```text
SISTEMA / APLICACIÓN / DISPOSITIVO
            ↓
mecanismo de adquisición
            ↓
Agent / Agent2 / SNMP / JMX / HTTP / Proxy / trapper / etc.
            ↓
ITEM
            ↓
PREPROCESSING
            ↓
HISTORY
            ↓
TRENDS cuando corresponda
            ↓
EVALUACIÓN
            ↓
TRIGGER
            ↓
EVENT
            ↓
PROBLEM
            ↓
ACTION
            ↓
OPERATION / ESCALATION
            ↓
MEDIA TYPE
            ↓
ALERT / NOTIFICATION
```

El estudiante debe comprender qué componentes intervienen y cuáles no en cada recorrido.

No presentar este pipeline como una simplificación universal cuando una funcionalidad utilice un flujo distinto.

---

# 7. Arquitectura que debe enseñarse

Diferenciar siempre claramente:

```text
Zabbix Server
Zabbix Proxy
Zabbix Agent
Zabbix Agent 2
Zabbix Java Gateway
Zabbix frontend
database
monitored host/device
```

Explicar para cada componente:

- responsabilidad;
- dónde se ejecuta;
- qué datos recibe;
- qué datos genera;
- con quién se comunica;
- quién inicia la conexión;
- puertos relevantes;
- persistencia;
- dependencia de la base de datos;
- comportamiento durante fallos;
- implicaciones de rendimiento;
- implicaciones de seguridad.

Evitar frases vagas como:

> Zabbix recoge métricas.

Precisar quién las recoge, mediante qué mecanismo y dónde terminan.

---

# 8. Zabbix Server

El Server debe estudiarse como daemon y como arquitectura interna.

Cuando corresponda, relacionar las lecciones con:

```text
zabbix_server
zabbix_server.conf
```

Explicar progresivamente:

- startup;
- configuración;
- procesos internos;
- pollers;
- trappers;
- preprocessors;
- history syncers;
- configuration syncers;
- discoverers;
- escalators;
- alerters;
- housekeeper;
- timers;
- proxy pollers;
- managers;
- caches;
- shared memory;
- IPC;
- database access;
- queue;
- runtime control;
- HA.

No enumerar procesos internos sin explicar qué carga de trabajo ejecutan.

---

# 9. Agent y Agent 2

Distinguir rigurosamente:

```text
Zabbix Agent
Zabbix Agent 2
```

No tratarlos como ejecutables equivalentes.

Para Agent clásico cubrir:

```text
zabbix_agentd
zabbix_agentd.conf
```

Para Agent 2 cubrir:

```text
zabbix_agent2
zabbix_agent2.conf
plugins
plugin architecture
```

Distinguir:

- active checks;
- passive checks;
- dirección de conexión;
- Server;
- ServerActive;
- Hostname;
- buffers;
- item keys;
- UserParameter;
- plugins;
- TLS;
- PSK;
- certificados;
- troubleshooting.

Cuando se hable de plugins de Agent 2, comprobar que el plugin corresponde a la versión estudiada.

---

# 10. Proxy

El Proxy no debe describirse simplemente como un Server pequeño.

Explicar:

- qué funciones delega el Server;
- qué información almacena;
- su base de datos;
- active proxy;
- passive proxy;
- configuration synchronization;
- recopilación;
- buffering;
- envío de history;
- funcionamiento offline;
- reconexión;
- proxy groups;
- failover;
- distribución;
- seguridad;
- escalabilidad.

Construir el flujo conceptual:

```text
monitored host
      ↓
Proxy
      ↓
buffer / proxy database
      ↓
Server
      ↓
Server database
```

y explicar sus excepciones.

---

# 11. Items

Los items son uno de los conceptos fundamentales del PATH.

Cada lección relacionada debe distinguir cuando proceda:

- item name;
- item type;
- key;
- parameters;
- data type;
- units;
- update interval;
- custom intervals;
- history;
- trends;
- preprocessing;
- value maps;
- inventory;
- tags;
- state;
- supported/unsupported.

No confundir:

```text
item type
item key
type of information
```

En ejemplos reales, mostrar la relación:

```text
host
→ interface
→ item type
→ key
→ value
→ preprocessing
→ storage
```

---

# 12. Item keys

Las item keys deben explicarse sintáctica y semánticamente.

Cubrir cuando corresponda:

```text
key
key[param]
key[param1,param2]
```

Explicar:

- parsing;
- quoting;
- escaping;
- parámetros vacíos;
- parámetros opcionales;
- keys soportadas;
- keys específicas de agente;
- UserParameters;
- testing.

Utilizar ejemplos reales, no placeholders genéricos.

Cuando proceda, utilizar herramientas como:

```bash
zabbix_get
zabbix_agentd -t
zabbix_agent2 -t
```

si la versión y herramienta soportan la operación explicada.

---

# 13. Preprocessing

Preprocessing debe tratarse como un pipeline real.

Modelo:

```text
raw value
   ↓
step 1
   ↓
step 2
   ↓
...
   ↓
final value
```

Explicar:

- orden de pasos;
- transformación;
- validación;
- custom on fail;
- discard;
- dependent items;
- JSONPath;
- XPath;
- regular expressions;
- JavaScript;
- Prometheus preprocessing;
- throttling;
- delta/change;
- testing;
- ejecución Server/Proxy según corresponda.

Zabbix permite aplicar transformaciones antes de almacenar valores; el orden de los pasos importa y los fallos pueden modificar el estado del item dependiendo del tratamiento configurado.

Relacionar preprocessing con:

- carga del Server/Proxy;
- almacenamiento;
- dependent items;
- reducción de datos;
- diseño de templates.

---

# 14. History y trends

Diferenciar estrictamente:

```text
history
trends
```

Explicar:

- finalidad;
- granularidad;
- tipos de datos;
- retención;
- tablas;
- agregación;
- disponibilidad de funciones;
- impacto de almacenamiento;
- rendimiento;
- housekeeping;
- particionado.

Evitar definir trends simplemente como “datos antiguos resumidos”.

Explicar cómo y por qué existen.

---

# 15. Triggers

Un trigger no debe explicarse únicamente como un threshold.

Cubrir:

- expresión;
- funciones;
- datos históricos;
- PROBLEM;
- OK;
- UNKNOWN cuando corresponda;
- recovery expression;
- dependencies;
- severities;
- tags;
- event generation;
- hysteresis;
- nodata;
- flapping;
- diseño robusto.

Una lección de trigger debe relacionar:

```text
item values
→ expression
→ trigger state
→ event
```

sin adelantar innecesariamente Actions si ese tema todavía no corresponde.

---

# 16. Events, Problems y Actions

Diferenciar estrictamente:

```text
trigger
event
problem
action
alert
notification
```

No usar estos términos como sinónimos.

Modelo aproximado:

```text
trigger cambia de estado
        ↓
event
        ↓
problem
        ↓
action conditions
        ↓
operations
        ↓
escalation
        ↓
alert
```

Explicar las excepciones cuando existan.

---

# 17. Templates

Los templates deben enseñarse como mecanismo de modelado y reutilización.

Cubrir:

- template groups;
- linking;
- inheritance;
- nested templates cuando corresponda;
- items;
- triggers;
- graphs;
- discovery rules;
- prototypes;
- macros;
- tags;
- dashboards;
- value maps;
- web scenarios;
- export/import;
- versionado.

Promover templates:

- pequeños cuando sea útil;
- reutilizables;
- parametrizados;
- documentados;
- versionables.

Evitar templates monolíticos sin justificación.

---

# 18. Macros

Distinguir:

- built-in macros;
- user macros;
- LLD macros;
- macro context;
- secret macros;
- macros heredadas;
- precedence.

Explicar el nivel de resolución:

```text
global
template
host
```

cuando corresponda a la característica concreta.

No inventar precedencias.

---

# 19. Discovery

Distinguir los tres mecanismos principales:

```text
Network discovery
Active agent autoregistration
Low-Level Discovery
```

Zabbix utiliza estos mecanismos con propósitos distintos.

Nunca presentar LLD como descubrimiento de hosts de red.

---

# 20. Low-Level Discovery

LLD debe recibir tratamiento profundo.

Modelo:

```text
discovery rule
      ↓
discovered entities
      ↓
LLD macros
      ↓
prototypes
      ↓
real items/triggers/graphs/hosts
```

Cubrir:

- discovery rules;
- `{#MACRO}`;
- filters;
- preprocessing;
- item prototypes;
- trigger prototypes;
- graph prototypes;
- host prototypes;
- overrides;
- lost resources;
- lifetime;
- nested discovery cuando exista y corresponda a la versión.

Los laboratorios LLD deben permitir inspeccionar el resultado del descubrimiento.

---

# 21. SNMP

SNMP debe explicarse suficientemente para poder administrar Zabbix correctamente, sin convertir este PATH en un curso completo de SNMP.

Distinguir:

```text
SNMPv1
SNMPv2c
SNMPv3
```

Dar preferencia a SNMPv3 en laboratorios orientados a seguridad.

Relacionar:

```text
OID
MIB
instance
index
walk
item
LLD
```

Herramientas útiles:

```bash
snmpget
snmpwalk
snmptranslate
snmpbulkwalk
```

Distinguir polling SNMP de SNMP traps.

---

# 22. JMX

Explicar:

- JVM;
- JMX;
- MBeans;
- object names;
- attributes;
- remote JMX;
- Zabbix Java Gateway;
- Java pollers;
- interface JMX;
- item JMX.

Construir el flujo:

```text
Zabbix Server/Proxy
       ↓
Java Gateway
       ↓
JMX
       ↓
JVM
```

No confundir Java Gateway con Agent 2.

---

# 23. HTTP y web monitoring

Diferenciar:

```text
HTTP Agent item
Web scenario
Script item
Browser item
```

cuando las funcionalidades estén disponibles en la versión estudiada.

Para HTTP Agent enseñar:

- method;
- URL;
- headers;
- query parameters;
- body;
- authentication;
- TLS;
- response code;
- response body;
- preprocessing;
- dependent items.

Usar APIs reales o servicios locales controlados para laboratorios.

---

# 24. API

La API debe enseñarse como mecanismo de administración y automatización, no como un tema accesorio.

Cubrir:

- JSON-RPC;
- request;
- response;
- method;
- params;
- authentication;
- API tokens;
- filtering;
- output;
- select*;
- pagination;
- errores;
- permisos.

Progresión recomendada:

```text
curl
↓
jq
↓
scripts
↓
Python cuando aporte valor
↓
automatización idempotente
```

No realizar modificaciones directas de la base de datos cuando exista una operación soportada mediante API.

---

# 25. Base de datos

Backend preferente del PATH:

**PostgreSQL**

Estudiar el schema únicamente con el nivel de profundidad necesario para comprender:

- arquitectura;
- rendimiento;
- history;
- trends;
- events;
- problems;
- alerts;
- configuración;
- troubleshooting;
- internals.

No enseñar a administrar Zabbix modificando directamente tablas de configuración.

Regla:

```text
LECTURA/ANÁLISIS DEL SCHEMA → permitido y útil
MODIFICACIÓN DIRECTA       → evitar
API                        → interfaz de automatización preferente
```

Explicar por qué una modificación directa puede:

- romper invariantes;
- saltarse validaciones;
- producir inconsistencias;
- quedar incompatible después de upgrades.

---

# 26. PostgreSQL y TimescaleDB

Cuando corresponda, relacionar Zabbix con:

- PostgreSQL;
- WAL;
- checkpoints;
- vacuum;
- autovacuum;
- ANALYZE;
- índices;
- I/O;
- conexiones;
- query performance;
- particionado;
- retention;
- TimescaleDB.

No convertir recomendaciones de tuning en valores universales.

Nunca indicar:

```text
shared_buffers = X
work_mem = Y
```

como configuración correcta para todo sistema.

Explicar primero:

- workload;
- memoria disponible;
- tamaño del dataset;
- número de conexiones;
- I/O;
- métricas observadas.

---

# 27. Queue

La queue debe enseñarse como herramienta de diagnóstico.

No afirmar automáticamente:

```text
queue alta = base de datos lenta
```

Investigar posibles causas:

- pollers insuficientes;
- checks lentos;
- timeouts;
- hosts inaccesibles;
- proxies;
- SNMP;
- JMX;
- HTTP;
- database;
- network;
- DNS;
- configuración de intervalos.

Construir diagnóstico basado en evidencia.

---

# 28. Caches

Cuando aparezcan caches internas:

- explicar su propósito;
- quién las utiliza;
- síntomas de saturación;
- métricas internas;
- relación con memoria compartida;
- parámetros relacionados;
- impacto de aumentar una cache;
- límites.

No recomendar aumentar caches sin medir previamente.

---

# 29. Housekeeper y retención

Explicar la relación:

```text
history/trends/events/etc.
        ↓
retention policy
        ↓
housekeeping / partitioning
        ↓
database size + I/O
```

Distinguir claramente:

- housekeeping;
- particionado;
- políticas de retención;
- TimescaleDB cuando se use.

---

# 30. Performance

Toda lección de performance debe seguir:

```text
observar
↓
medir
↓
formular hipótesis
↓
identificar bottleneck
↓
modificar
↓
volver a medir
```

No enseñar tuning basado exclusivamente en copiar parámetros.

Relacionar:

- NVPS;
- queue;
- process busy;
- caches;
- database;
- CPU;
- RAM;
- I/O;
- network;
- número de hosts;
- número de items;
- update intervals;
- preprocessing;
- proxies.

---

# 31. Self-monitoring

Zabbix debe monitorizar su propia plataforma.

Incluir cuando corresponda:

- internal items;
- queue;
- process utilization;
- caches;
- required performance;
- Proxy health;
- database;
- filesystem;
- frontend;
- certificados;
- backups.

El estudiante debe aprender a detectar degradación antes de que Zabbix deje de monitorizar correctamente.

---

# 32. Alta disponibilidad

Distinguir:

- Zabbix Server HA;
- Proxy groups/Proxy HA según versión;
- database HA;
- frontend HA;
- load balancer;
- storage;
- componentes que Zabbix resuelve;
- componentes que requieren soluciones externas.

No afirmar que activar HA del Server convierte por sí solo toda la plataforma en altamente disponible.

---

# 33. Seguridad

Toda arquitectura debe considerar:

- mínimo privilegio;
- segmentación;
- firewalld;
- SELinux;
- TLS;
- PSK;
- certificados X.509;
- credenciales;
- secret macros;
- Vault cuando corresponda;
- API tokens;
- RBAC;
- LDAP/SAML/MFA cuando corresponda;
- exposición del frontend;
- database access;
- Agent allowed hosts;
- Proxy communication;
- permisos de scripts.

No desactivar SELinux o firewalld como solución genérica.

Para diagnóstico se puede demostrar temporalmente una hipótesis cuando sea seguro, pero la solución final debe respetar los mecanismos de seguridad.

---

# 34. Fedora, systemd, firewalld y SELinux

Los laboratorios deben aprovechar el entorno real.

Utilizar cuando aporte valor:

```bash
systemctl
journalctl
ss
ps
top
free
vmstat
iostat
pidstat
tcpdump
```

Para paquetes:

```bash
rpm
dnf
```

Para firewalld:

```bash
firewall-cmd
```

Para SELinux:

```bash
getenforce
ausearch
sealert
semanage
restorecon
ls -Z
ps -eZ
```

No utilizar:

```bash
setenforce 0
```

como solución final a un problema SELinux.

---

# 35. Troubleshooting

Las lecciones de diagnóstico deben enseñar método.

Secuencia recomendada:

```text
1. definir el síntoma
2. determinar el componente
3. comprobar estado
4. comprobar logs
5. comprobar configuración
6. comprobar conectividad
7. comprobar protocolo
8. comprobar seguridad
9. comprobar queue/caches/procesos
10. comprobar database cuando corresponda
11. aislar causa
12. corregir
13. verificar
```

Evitar troubleshooting basado en listas de comandos sin razonamiento.

---

# 36. Herramientas de diagnóstico

Según el problema, utilizar:

```bash
zabbix_get
zabbix_sender
zabbix_agentd
zabbix_agent2
zabbix_server
zabbix_proxy
systemctl
journalctl
ss
ip
ping
dig
getent
curl
jq
openssl
tcpdump
tshark
snmpget
snmpwalk
snmptranslate
psql
pg_isready
```

y otras herramientas cuando estén justificadas.

Cada comando debe explicar:

- qué pregunta responde;
- qué salida interesa;
- cómo interpretarla.

---

# 37. Internals

Los bloques de internals deben ir más allá de nombres de procesos.

Cuando corresponda estudiar:

- source tree;
- daemon initialization;
- process model;
- threads/procesos según componente;
- IPC;
- shared memory;
- caches;
- polling;
- async I/O;
- preprocessing;
- history pipeline;
- trigger evaluation;
- event generation;
- database synchronization;
- Proxy synchronization;
- protocol framing;
- JSON payloads;
- TLS;
- shutdown;
- runtime control.

No reproducir código fuente extensamente.

Explicar fragmentos pequeños únicamente cuando ayuden a entender la arquitectura.

---

# 38. Protocolos

Cuando se estudien protocolos de Zabbix, diferenciar:

- Agent passive checks;
- Agent active checks;
- Server-Proxy;
- sender/trapper;
- TLS transport;
- JSON payloads;
- framing;
- headers.

Cuando proceda, analizar tráfico controlado mediante:

```bash
tcpdump
tshark
Wireshark
```

Nunca exponer secretos reales en capturas.

---

# 39. Código fuente

Cuando una lección entre en internals:

1. situar el componente;
2. localizar conceptualmente la implementación;
3. relacionar nombres del código con procesos visibles;
4. seguir el flujo relevante;
5. regresar al comportamiento observable.

No convertir la lección en una lectura lineal del repositorio.

El objetivo es conectar:

```text
código
↔
arquitectura
↔
proceso en ejecución
↔
configuración
↔
métrica/log observable
```

---

# 40. Laboratorios

Los laboratorios deben ser acumulativos cuando sea razonable.

Entorno recomendado:

```text
zabbix-server
zabbix-proxy
host-linux-1
host-linux-2
servicio HTTP/API
dispositivo o simulador SNMP
JVM de laboratorio
PostgreSQL
```

No exigir infraestructura física especializada cuando pueda utilizarse:

- máquinas virtuales;
- contenedores;
- namespaces;
- servicios locales;
- simuladores seguros.

Los laboratorios deben incluir verificación.

Ejemplo:

```text
configurar
→ iniciar
→ comprobar
→ provocar situación
→ observar
→ diagnosticar
→ corregir
→ verificar
```

---

# 41. Artefactos

Cuando una lección genere archivos útiles, deben conservarse como artefactos cuando el generador lo determine.

Posibles artefactos:

```text
zabbix_server.conf.d/*.conf
zabbix_agent2.d/*.conf
zabbix_proxy.conf
UserParameter definitions
scripts
JSON
YAML
template exports
API scripts
SQL de consulta
systemd drop-ins
firewalld notes
runbooks
diagrams
troubleshooting scripts
backup scripts
```

No producir artefactos artificiales sólo para cumplir una plantilla.

---

# 42. Comandos

Los comandos deben ser:

- ejecutables;
- seguros;
- explicados;
- adecuados a Fedora;
- adecuados a la versión estudiada.

No inventar opciones.

Diferenciar claramente:

```text
$ comando como usuario
# comando que requiere privilegios
```

o explicar explícitamente el uso de `sudo`.

No asumir que todos los binarios están instalados.

Cuando proceda mostrar cómo descubrir el paquete que proporciona una herramienta.

---

# 43. Ficheros de configuración

Cuando se enseñe una directiva:

1. explicar en qué componente existe;
2. indicar el fichero correspondiente;
3. explicar sintaxis;
4. explicar efecto;
5. indicar valor/default sólo cuando esté verificado;
6. explicar cómo aplicar el cambio;
7. verificarlo.

No mezclar parámetros de:

```text
zabbix_server.conf
zabbix_proxy.conf
zabbix_agentd.conf
zabbix_agent2.conf
```

---

# 44. Frontend

La interfaz gráfica debe utilizarse cuando sea el mecanismo natural de administración.

Pero toda lección debe explicar el objeto conceptual subyacente.

No redactar instrucciones frágiles del tipo:

```text
haz clic en el tercer botón azul de la derecha
```

Preferir:

```text
Data collection → Hosts → Items
```

cuando corresponda a la versión estudiada.

Si la UI cambia entre versiones, priorizar el concepto y señalar la posible diferencia.

---

# 45. API frente a GUI

Cuando sea útil mostrar ambas perspectivas:

```text
GUI
↔
objeto Zabbix
↔
API
```

Ejemplo:

```text
Host en frontend
↔
host object
↔
host.get / host.create
```

Esto debe ayudar a preparar automatización posterior.

---

# 46. Seguridad de ejemplos

Nunca utilizar secretos reales.

Usar placeholders explícitos:

```text
<API_TOKEN>
<PSK_IDENTITY>
<PSK_FILE>
<DB_PASSWORD>
```

No recomendar almacenar contraseñas directamente en shell history.

Explicar mecanismos de protección cuando sea relevante.

---

# 47. Profundidad esperada

Una lección no puede consistir únicamente en:

- definición;
- lista de opciones;
- ejemplo trivial;
- resumen.

Cuando el tema lo permita, debe responder:

```text
qué es
por qué existe
qué problema resuelve
dónde encaja
cómo funciona
cómo se configura
cómo se observa
cómo se verifica
cómo falla
cómo se diagnostica
qué límites tiene
con qué conceptos puede confundirse
```

No forzar todos estos apartados como encabezados idénticos.

La estructura debe adaptarse al contenido.

---

# 48. Evitar repetición

Si una lección anterior ya explicó un concepto, utilizarlo como prerrequisito.

No repetir secciones enteras.

Ejemplo:

Una lección avanzada sobre:

```text
58.7 diagnóstico de items retrasados
```

puede asumir que el estudiante ya conoce:

- items;
- intervals;
- queue;
- Server;
- Proxy;

y debe concentrarse en el diagnóstico.

---

# 49. Vecinos del PATH

Las lecciones vecinas son importantes.

El generador debe utilizarlas para:

- determinar qué se enseñó antes;
- evitar adelantar la lección siguiente;
- identificar el nivel de profundidad;
- mantener continuidad.

El título corto de una lección nunca debe interpretarse fuera del contexto del PATH.

Por ejemplo:

```text
59.5 value cache
```

significa:

> value cache dentro de la arquitectura interna y operación de Zabbix,

no una explicación genérica de cachés informáticas.

---

# 50. Lectura

Cada lección debe incluir una sección:

# 📚 LECTURA

Las referencias deben ser específicas del tema.

Categorías recomendadas:

- Principal;
- LTS / versión alternativa;
- Internals / código fuente;
- Plataforma;
- Profundización;
- Consulta.

No es necesario utilizar todas las categorías en cada lección.

No inventar:

- capítulos;
- números de página;
- secciones;
- URLs;
- RFC;
- títulos.

Si no se puede verificar una referencia exacta, citar la obra o documentación a nivel seguro.

---

# 51. Estructura pedagógica obligatoria

Toda lección debe comenzar con:

# 🎯 OBJETIVO

Debe explicar claramente qué será capaz de comprender o realizar el estudiante al terminar.

Toda lección debe terminar con:

# 🧠 QUÉ DEBES RECORDAR

Debe contener entre 3 y 7 ideas técnicas esenciales.

No debe repetir literalmente el objetivo.

Cuando aporte valor pueden aparecer:

# 🧪 Laboratorio

# ⚠️ Errores frecuentes

# 💡 Idea importante

# 📚 LECTURA

La profundidad debe estar en el desarrollo técnico, no en multiplicar artificialmente los apartados.

---

# 52. Diagramas

Utilizar diagramas ASCII cuando faciliten la comprensión.

Ejemplos:

```text
Agent2
  │
  │ active checks
  ▼
Server
  │
  ▼
PostgreSQL
```

o:

```text
API response
    ↓
master item
    ↓
preprocessing
 ┌──┼──┐
 ↓  ↓  ↓
dep dep dep
```

Los diagramas deben representar correctamente la dirección del flujo.

---

# 53. Proyecto final

El proyecto final debe integrar el PATH, no ser una instalación básica.

Debe permitir demostrar:

```text
arquitectura
+ Server
+ PostgreSQL
+ frontend
+ Agent2
+ Proxy
+ templates
+ items
+ preprocessing
+ dependent items
+ triggers
+ actions
+ alerting
+ discovery
+ LLD
+ SNMP
+ JMX
+ HTTP
+ API
+ dashboards
+ SLA
+ TLS
+ HA
+ self-monitoring
+ performance
+ backup
+ troubleshooting
+ internals
```

El proyecto debe incluir fallos provocados de forma controlada y diagnóstico.

La plataforma final debe poder ser:

- documentada;
- operada;
- monitorizada;
- restaurada;
- diagnosticada.

---

# 54. Resultado final esperado

Al finalizar el PATH, el estudiante debe poder razonar sobre Zabbix en ambos sentidos.

Desde infraestructura hacia alerting:

```text
host
→ acquisition
→ item
→ preprocessing
→ storage
→ trigger
→ event
→ problem
→ action
→ alert
```

Y desde un fallo hacia su causa:

```text
symptom
→ frontend/queue/log
→ process
→ Server/Proxy/Agent
→ protocol/network
→ TLS/firewall/SELinux
→ database
→ resource bottleneck
→ root cause
```

Ese nivel de comprensión define **ZABBIX EN PROFUNDIDAD**.
# Domain — TCP/IP 0 → Experto en profundidad

## Dominio
Networking TCP/IP práctico y profundo sobre Linux, con Fedora/RHEL como plataforma principal.

## Objetivo
Dominar el recorrido completo de los datos desde la aplicación hasta el medio de red y de vuelta, comprendiendo los modelos OSI y TCP/IP, Ethernet, IPv4/IPv6, ARP/NDP, ICMP, routing, sockets, UDP y TCP; y diagnosticar problemas reales mediante herramientas CLI.

## Alcance principal
- Modelos OSI y TCP/IP, capas y encapsulación/desencapsulación.
- Ethernet, VLAN, MAC, ARP y Neighbor Discovery.
- IPv4, IPv6, subnetting y routing.
- ICMP/ICMPv6, traceroute/tracepath y PMTUD.
- Sockets, puertos, procesos y file descriptors.
- UDP desde datagramas básicos hasta diagnóstico.
- TCP: handshake, state machine, reliability, flow control y congestion control.
- Linux networking stack y parámetros del kernel.
- MTU, MSS, fragmentación y Path MTU Discovery.
- NAT y connection tracking.
- Network namespaces y laboratorios reproducibles.
- Rendimiento y observabilidad.

## Herramientas CLI obligatorias
### ss
Desde identificación de listeners y conexiones hasta estados TCP, filtros, queues, timers, RTT, RTO, cwnd, retransmisiones y diagnóstico avanzado.

### lsof
Desde asociación puerto/proceso hasta file descriptors, socket inodes, /proc, bindings IPv4/IPv6, systemd socket activation y correlación con ss/tcpdump.

### tcpdump
Desde captura básica hasta filtros BPF, flags TCP, PCAP, capturas de troubleshooting y análisis de MTU, routing, NAT y retransmisiones.

### tshark
Wireshark CLI desde filtros básicos hasta Display Filter Language, extracción estructurada, estadísticas, tcp.analysis, streams y análisis PCAP experto.

### Nmap
CLI desde host discovery y port scanning hasta UDP, fingerprinting, NSE, interpretación de respuestas y correlación con capturas. Los ejercicios deben realizarse únicamente en sistemas propios o expresamente autorizados.

## Herramientas complementarias
ip, ping, tracepath, traceroute, ethtool, nstat, conntrack, iperf3, ncat, journalctl y /proc.

## Plataforma
Los laboratorios y ejemplos se orientan a Fedora/RHEL y herramientas estándar del ecosistema Linux.

## Filosofía de aprendizaje
Cada concepto debe conectar teoría, estado del kernel y evidencia observable:

Aplicación
→ socket/proceso
→ TCP/UDP
→ IP/routing
→ Ethernet/neighbor
→ interfaz/NIC
→ paquetes capturados

El alumno debe aprender a correlacionar:
lsof → ss → ip → nmap → tcpdump → tshark.

## Laboratorios
Los laboratorios deben ser reproducibles y preferentemente usar Linux network namespaces, veth pairs y servicios locales para evitar depender de infraestructura externa.

## Troubleshooting
La metodología debe avanzar sistemáticamente desde interfaz/link hasta aplicación y distinguir, mediante evidencia, problemas de:
- enlace;
- addressing;
- ARP/NDP;
- routing;
- DNS;
- firewall/NAT;
- listener/binding;
- handshake TCP;
- UDP;
- retransmisiones;
- MTU/PMTUD;
- rendimiento;
- aplicación.

## Logs y evidencias
No asumir que TCP/IP dispone de un único archivo en /var/log. Enseñar a localizar evidencias mediante journalctl, logs del servicio implicado, counters del kernel/NIC, ss, nstat, conntrack y capturas PCAP.

## Nivel final esperado
El alumno debe poder recibir un fallo de conectividad desconocido, formular hipótesis por capas, obtener evidencia con CLI, capturar el tráfico necesario, interpretar el PCAP y localizar razonadamente la capa y causa del problema.

## Delimitación respecto al path independiente de diseño IPv4/IPv6
Este curso explica direcciones, prefijos, máscaras, CIDR, network/broadcast y cálculos operativos mínimos para leer rutas, entender paquetes y diagnosticar conectividad. Las clases A–E se enseñan como contexto histórico. **No** desarrolla planificación de direccionamiento, VLSM exhaustivo, dimensionamiento de subredes, jerarquías de direccionamiento ni diseño de topologías de producción: estos pertenecen al path específico de diseño IPv4/IPv6.

## Ampliaciones de profundidad
Ethernet/FCS y switching; comportamiento dual-stack; ECN y recuperación TCP; NAPI, GRO/GSO/TSO, RSS/RPS y colas del kernel; qdisc/tc, bufferbloat y pruebas de rendimiento; troubleshooting con hipótesis, evidencia PCAP y validación de correcciones.

## Uso de bibliografía por scope
Los scopes S01–S09 de bibliography.md orientan las referencias por bloque y lección. Diferenciar libros didácticos, fuentes operativas Linux y estándares normativos actualizados.


## Dependencias y orden de estudio
Los identificadores de initial.txt se conservan para mantener trazabilidad.
Dentro de cada bloque, estudiar los conceptos y ampliaciones antes del
troubleshooting, el laboratorio de cierre y la evaluación, aunque estos últimos
conserven identificadores anteriores. Las lecciones de presentación no exigen
dominio anticipado de los bloques especializados.

- Bloque 0: estudiar 0.52–0.59 antes del laboratorio integrador 0.51.
- Bloque 1: estudiar 1.16–1.21 antes del cierre 1.15.
- Bloque 2: resolver los cálculos 2.14–2.21 antes del cierre 2.13.
- Bloque 4: estudiar 4.15–4.24 antes del cierre 4.14.
- Bloques 8, 11 y 12: estudiar sus ampliaciones antes del diagnóstico final.
- Bloques de herramientas: realizar el laboratorio de cierre tras las
  ampliaciones del mismo bloque; reutilizar comandos básicos desde el inicio.
- El bloque 33 profundiza en el laboratorio mínimo introducido en el bloque 0.
- Bloques 38 y 39: integrar las ampliaciones antes de cerrar la evaluación.

## Resolución de nombres y frontera de aplicación
Enseñar resolución operativa con NSS, getent y dig, configuración efectiva del
resolver, respuestas DNS y transporte UDP/TCP. Distinguir resolución, conexión,
negociación TLS y respuesta de aplicación usando curl y openssl s_client.
Administrar BIND, Kea o PKI en profundidad pertenece a sus paths específicos.
TLS y QUIC se estudian aquí por sus efectos y evidencias de red observables.

## Configuración y filtrado Linux
Incluir NetworkManager/nmcli y distinguir cambios temporales de persistentes.
Enseñar el recorrido básico Netfilter y la inspección con nft, firewall-cmd y
conntrack necesaria para diagnosticar los laboratorios. Configurar las reglas
del laboratorio dentro de sus namespaces; cualquier cambio de configuración debe
identificar su ámbito y restaurarse al terminar. No sustituye el path firewalld.
La topología cliente/router/servidor del laboratorio sí está incluida; se excluye
el diseño de arquitecturas de red de producción.

## Criterios técnicos de interpretación
- /proc/PID/net refleja el namespace de red del proceso; correlacionar sus FD
  e inodes para identificar los sockets que posee.
- Separar estados TCP, estados conntrack y clasificaciones de Nmap.
- Interpretar colas según estado del socket, unidades y versión de herramienta.
- Tratar tcp.analysis como evidencia derivada, contrastada con calidad de
  captura, punto de observación, offloads y capturas del otro extremo.
- Registrar versiones y disponibilidad de algoritmos antes de comparar CUBIC/BBR.
- Explicar los límites de FCS, pseudo-interfaz any, cifrado y filtros IPv6.
- No asumir que aumentar buffers o modificar sysctl resuelve un problema.

## Contrato de laboratorio y evaluación
Cada práctica incluye objetivo, prerrequisitos, topología mínima, privilegios,
versiones, estado inicial, comandos explicados, observaciones esperadas,
evidencias, diagnóstico, corrección, validación y limpieza. Proporcionar scripts
de preparación y restauración cuando la práctica modifica el entorno.
Los ejemplos deben ser reproducibles sin acceso público salvo instalación de
paquetes; usar servicios y tráfico locales. Aclarar qué no reproduce veth de
una NIC física para prácticas de driver, RSS y hardware offload.

Para aprobar: reproducir el síntoma, formular hipótesis, aportar evidencia que
permita distinguir causas, justificar la causa elegida, corregirla, repetir la
prueba y acreditar la restauración. El proyecto final incluye fallos ocultos,
PCAP, salidas CLI y un informe con esta secuencia.

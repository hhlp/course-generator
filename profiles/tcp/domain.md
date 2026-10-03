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

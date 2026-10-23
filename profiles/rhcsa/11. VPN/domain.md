# Dominio — OpenVPN + WireGuard

## Propósito

Este itinerario desarrolla dominio progresivo de redes privadas virtuales sobre Linux, con especialización práctica y profunda en OpenVPN y WireGuard. El objetivo no es limitarse a desplegar un túnel funcional, sino comprender el comportamiento de la red, criptografía, routing, firewall, DNS, MTU, seguridad, observabilidad, automatización e internals necesarios para diseñar y operar soluciones VPN mantenibles.

## Plataforma principal

- Fedora y RHEL como plataformas Linux de referencia.
- systemd para gestión de servicios.
- NetworkManager y `nmcli` cuando corresponda.
- firewalld y nftables para filtrado, forwarding y NAT.
- SELinux en modo enforcing.
- `iproute2` para direccionamiento, routing y policy routing.
- OpenSSL y Easy-RSA para los componentes PKI de OpenVPN.
- `wg` y `wg-quick` para WireGuard.
- Ansible como mecanismo principal de automatización.
- Terraform como complemento de infraestructura cuando exista infraestructura externa que aprovisionar.

## Alcance técnico

### Fundamentos compartidos
IPv4, IPv6, CIDR, routing, forwarding, NAT, UDP/TCP, TUN/TAP, MTU/MSS, DNS, namespaces y modelos full-tunnel/split-tunnel.

### Criptografía
Criptografía simétrica y asimétrica, AEAD, hashes, HMAC, intercambio de claves, forward secrecy, PKI, X.509 y ciclo de vida de claves.

### OpenVPN
Arquitectura cliente-servidor, canales de control y datos, TLS, PKI, Easy-RSA, perfiles `.ovpn`, routing, CCD/`iroute`, autenticación, operación mediante systemd, management interface, hardening y troubleshooting.

### WireGuard
Peers, claves, handshake, Noise, cryptokey routing, `AllowedIPs`, endpoints, roaming, `PersistentKeepalive`, `wg`, `wg-quick`, NetworkManager, policy routing e internals de la implementación Linux.

### Integración Linux
firewalld, nftables, SELinux, systemd, NetworkManager, journald, iproute2, namespaces, Podman y componentes de observabilidad.

### Nivel avanzado
Policy-Based Routing, múltiples tablas, `fwmark`, multi-WAN, routing dinámico con FRRouting, OSPF/BGP sobre túneles, alta disponibilidad, multi-site, HA, automatización y análisis de código/internals.

## Filosofía del curso

El curso debe explicar primero el mecanismo y después la configuración. Cada directiva o comando importante debe relacionarse con el efecto que produce en interfaces, tablas de routing, firewall, resolución DNS o flujo de paquetes.

Las lecciones prácticas deben favorecer la inspección del estado real del sistema mediante herramientas como:

```bash
ip addr
ip route
ip rule
ss
wg show
firewall-cmd
nft
journalctl
tcpdump
tracepath
iperf3
openssl
```

## Progresión

1. Fundamentos de networking y criptografía.
2. OpenVPN desde instalación hasta administración avanzada.
3. WireGuard desde configuración básica hasta cryptokey routing e internals.
4. Integración con el stack Fedora/RHEL.
5. Seguridad, observabilidad y rendimiento.
6. Automatización e Infrastructure as Code.
7. Arquitecturas multi-site, routing avanzado y HA.
8. Internals y debugging.
9. Laboratorios expertos.
10. Proyecto final de arquitectura y operación.

## Laboratorios

Los laboratorios deben ser reproducibles y, cuando sea viable, construirse mediante máquinas virtuales o network namespaces para evitar depender de infraestructura externa.

Deben cubrir como mínimo:

- OpenVPN remote-access.
- OpenVPN site-to-site.
- WireGuard remote-access.
- WireGuard site-to-site.
- Full tunnel.
- Split tunnel.
- IPv4/IPv6 dual stack.
- DNS y split DNS.
- NAT y forwarding.
- firewalld y nftables.
- Policy routing.
- Multi-site.
- HA.
- Observabilidad.
- Automatización con Ansible.
- Diagnóstico de fallos intencionados.

## Metodología de troubleshooting

El diagnóstico debe comenzar observando el sistema antes de modificar la configuración. La secuencia pedagógica preferida es:

```text
servicio / proceso
        ↓
estado + logs
        ↓
interfaz y direcciones
        ↓
routing / policy routing
        ↓
firewall / NAT
        ↓
DNS
        ↓
MTU / MSS
        ↓
captura de paquetes
```

En OpenVPN se debe enseñar a correlacionar los logs propios del servidor y cliente con journald, TLS/PKI, NetworkManager, firewalld/nftables y eventos SELinux. Deben explicarse los niveles `verb`, las directivas `log`, `log-append` y `status`, la interpretación de errores frecuentes y el riesgo de habilitar logging excesivamente detallado en producción.

En WireGuard se debe remarcar que el modelo de diagnóstico es diferente: `wg show` y el estado observable del túnel —handshake, RX/TX, endpoint, `AllowedIPs` y keepalive— son fundamentales y se complementan con journald, logs del kernel, NetworkManager, firewall, SELinux y captura de paquetes.

El estudiante debe aprender a correlacionar timestamps y evidencias procedentes de distintas capas, y a distinguir entre:

- logs de aplicación o servicio;
- estado operativo;
- métricas;
- eventos del kernel;
- eventos del firewall;
- denegaciones SELinux/AVC;
- capturas de paquetes.

No se debe cambiar múltiples parámetros simultáneamente para intentar resolver un fallo. Cada hipótesis debe comprobarse con evidencia y cada cambio debe poder relacionarse con el resultado observado.


## Seguridad

No se debe enseñar a solucionar problemas desactivando permanentemente SELinux o el firewall. Los fallos deben diagnosticarse y corregirse conservando las protecciones del sistema.

Las claves privadas, PSK, certificados y credenciales utilizadas en ejemplos deben ser ficticios o generados específicamente para los laboratorios.

## Relación con otros itinerarios

Este PATH puede apoyarse en itinerarios independientes de systemd, SELinux, firewalld, Ansible y observabilidad. Aquí esos componentes se estudian específicamente desde la perspectiva de OpenVPN y WireGuard, evitando repetir innecesariamente cursos completos de cada tecnología.

## Relación con Identity & Access Management (IAM)

El itinerario debe enseñar explícitamente dos modos de operación: VPN autónoma sin IAM centralizado y VPN integrada con una plataforma central de identidad. La integración es opcional y no debe convertirse en requisito para aprender o desplegar OpenVPN o WireGuard.

### OpenVPN
OpenVPN puede funcionar de forma independiente mediante su PKI, certificados y mecanismos propios, y también puede actuar como consumidor de IAM cuando la autenticación se integra con PAM/SSSD y servicios centrales como LDAP, Kerberos o FreeIPA. El curso debe distinguir autenticación, autorización, certificados y pertenencia a grupos, así como estudiar dependencias, fallos y logs de cada capa.

### WireGuard
WireGuard no debe presentarse como consumidor directo de PAM, LDAP, Kerberos o FreeIPA. Su identidad nativa se basa en claves públicas de peers y cryptokey routing. IAM puede participar en un plano de control externo que autorice, aprovisione, retire o audite peers, pero no sustituye el mecanismo criptográfico nativo del túnel.

### Principio pedagógico
Cada tecnología se estudiará primero sin IAM para comprender su modelo nativo. Después se añadirá la integración centralizada cuando corresponda. Los laboratorios deben permitir comparar dependencia, disponibilidad, lifecycle, revocación, auditoría y troubleshooting en ambos modelos.

## Resultado esperado

Al finalizar, el estudiante debe ser capaz de diseñar, desplegar, asegurar, automatizar, observar, diagnosticar y mantener arquitecturas OpenVPN y WireGuard desde escenarios de acceso remoto sencillos hasta redes site-to-site, multi-site y de alta disponibilidad.


## Revisión aplicada y orden de estudio

Se conservan los 38 bloques y las 764 lecciones de origen; se añaden lecciones
sin cambiar los identificadores existentes. El bloque 9B se sitúa después del
21: requiere haber aprendido peers, configuración, routing y diagnóstico.
Las lecciones existentes se desarrollarán junto con las precisiones siguientes.

## Contrato técnico de integración IAM

OpenVPN usa un plugin o verificador explícito. La ruta preferida del laboratorio
es OpenVPN → plugin auth-pam → servicio PAM dedicado → pam_sss/SSSD → FreeIPA.
Verificar la ruta del plugin, el paquete, los permisos y las fases PAM que ejecuta
la versión instalada. La validación de contraseña mediante un backend Kerberos
no equivale a SSO nativo de OpenVPN con un TGT. LDAP directo es una alternativa
comparativa; debe identificar su verificador, TLS y reglas de autorización.

Autenticar una contraseña no basta para conceder acceso. Comprobar autorización
mediante la fase account, grupos y, cuando corresponda, HBAC con el servicio PAM
configurado. Verificarlo con usuario permitido y denegado. Documentar cómo se
vincula el certificado con la identidad central para evitar combinaciones ajenas.

MFA exige verificar compatibilidad entre cliente, plugin y proveedor. Enseñar
renegociación y tokens sin dar por hecho que se consulta IAM en cada renovación.
Con auth-gen-token, revisar lifetime, renewal y external-auth según el manual de
la versión. Un token o una sesión existente pueden sobrevivir a la baja de una
cuenta hasta aplicar las medidas previstas. La baja completa incluye denegación
de nuevas conexiones, cierre de sesiones, política de certificados y auditoría.
La interfaz de management debe quedar restringida; no exponerla sin protección.

La caché de SSSD y la autenticación offline tienen una política explícita y
pruebas. Comparar IAM caído, DNS fallido, reloj desajustado, contraseña inválida,
cuenta bloqueada, grupo no autorizado y certificado revocado. No habilitar acceso
offline de forma implícita para resolver una caída del proveedor.

WireGuard mantiene su autenticación por claves. El plano externo registra la
relación usuario/dispositivo/clave pública, autoriza y reconcilia peers. Generar
claves privadas en el extremo cuando sea viable y conservarlas fuera del
inventario público. La baja debe eliminar el peer del estado operativo y de la
fuente persistente. Medir la demora de reconciliación: una baja en IAM por sí sola
no retira una clave ya configurada, y un controlador caído no interrumpe por sí
mismo los túneles existentes. Conservar evidencia de cada decisión.

## Routing, gestores y límites

Distinguir ruta en la FIB, selección del peer por destino y validación de origen
por AllowedIPs. El filtrado por servicio/puerto corresponde al firewall.
wg configura WireGuard; wg-quick y NetworkManager pueden añadir direcciones,
rutas, reglas y DNS. Explicar qué gestor crea cada objeto y utilizar uno por
interfaz. Table, Address y DNS son extensiones de wg-quick, no campos nativos
intercambiables con wg setconf. SaveConfig requiere especial atención cuando se
utilizan plantillas declarativas. No publicar dumps con claves privadas o PSK.

PersistentKeepalive mantiene mappings NAT cuando hace falta; no proporciona un
servicio de descubrimiento, hole punching coordinado ni relay. Para CGNAT en
ambos extremos diseñar un gateway alcanzable o componentes externos explícitos.
En routing dinámico verificar que los prefijos aprendidos estén autorizados por
AllowedIPs y estudiar OSPF con vecinos unicast o mecanismos adicionales según
la topología, sin asumir replicación multicast entre todos los peers.

## Laboratorios reproducibles y aceptación

El generador debe desarrollar cada laboratorio con topología, inventario,
versiones, prerrequisitos, configuración completa, comandos, comprobaciones,
fallos intencionados, restauración y limpieza. Los cuatro archivos definen el
currículo; los scripts y playbooks se desarrollarán dentro de sus lecciones.

Topología mínima local: WAN simulada 192.0.2.0/24, sede A 10.10.10.0/24,
sede B 10.20.20.0/24, pool OpenVPN 10.250.0.0/24 y enlaces WireGuard dentro de
10.251.0.0/24, subdivididos según escenario. Para IPv6 utilizar subredes distintas
de 2001:db8::/32 exclusivamente en el laboratorio aislado. Estas redes de
documentación no se anuncian a Internet. Cada sede tiene gateway y host de
pruebas; añadir cliente remoto, servidor DNS y proveedor IAM opcional. Probar
primero sin IAM. Para IAM usar VMs con systemd, sincronización de hora y DNS
correctos; los namespaces bastan para muchos ensayos de paquetes/routing.

| Escenario | Prueba positiva | Prueba negativa o fallo |
| --- | --- | --- |
| OpenVPN autónomo | Certificado válido y acceso a servicio | CRL, expiración y certificado ajeno |
| OpenVPN con IAM | Usuario autorizado y certificado asociado | Grupo denegado, cuenta bloqueada, caída de IAM |
| MFA y sesión | Autenticación y renovación previstas | Token expirado y baja durante sesión |
| WireGuard autónomo | Acceso con peer y prefijo correctos | Clave retirada y origen no autorizado |
| WireGuard gestionado | Alta y baja reconciliadas | Controlador caído y peer persistente obsoleto |
| Full tunnel dual-stack | Egreso esperado en IPv4/IPv6 | Caída del túnel, fuga DNS y reconexión |
| Site-to-site | Servicio entre LAN A y LAN B | Ruta de retorno ausente y firewall denegando |
| Routing dinámico | Prefijos aprendidos y tráfico real | Ruta válida en FIB con AllowedIPs insuficiente |
| HA | Reconexión y rutas recuperadas | Gateway caído, retorno y split-brain |
| Recuperación | Restauración reproducible | Backup antiguo con peer/certificado revocado |

Cada prueba conserva comandos, código de salida, estado esperado/observado y
marcas de tiempo sin secretos. Registrar tiempo de interrupción y demora de
revocación con un umbral definido por el escenario. Un ping o un handshake no
sustituye la prueba de acceso al servicio autorizado ni la prueba de denegación.

## Alta disponibilidad y dependencias

Un floating IP no replica automáticamente sesiones OpenVPN, estado criptográfico
WireGuard ni conntrack. Explicar qué conexiones se restablecen, cuáles se pierden
y qué mecanismos recuperan rutas/endpoints. Preferir para el primer laboratorio
WireGuard gateways con claves distintas y selección de camino explícita; estudiar
identidad compartida solo en active/passive con fencing y prevención de split-brain.
Medir fallo y retorno. Incorporar DNS, IAM, PKI, controlador y gestión de secretos
al análisis de SPOF, backup y recuperación. No prometer continuidad sin pruebas.

## Versiones, paquetes y operación

Registrar versión de SO, kernel, OpenVPN, wireguard-tools, NetworkManager,
OpenSSL, plugins y repositorios utilizados. Separar Fedora de cada versión RHEL:
comprobar disponibilidad, soporte y rutas reales sin reutilizar paquetes de otra
versión mayor. Usar el manual correspondiente al binario instalado; las opciones
de DCO y compatibilidad pueden variar. Comparar DCO con procesamiento userspace
cuando esté disponible. Desactivar compresión en las configuraciones modernas y
estudiar opciones legacy únicamente en migraciones delimitadas.

Los logs pueden residir en journald y, si se configura, en /var/log; no asumir
un archivo común a todas las instalaciones. Enseñar persistencia del journal,
rotación, permisos, auditoría y correlación temporal con PAM/SSSD/SELinux.

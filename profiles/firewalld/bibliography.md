# BIBLIOGRAPHY — FIREWALLD EN PROFUNDIDAD — FEDORA

## Criterio

En este PATH la documentación oficial es la fuente principal. Firewalld, Fedora, nftables y NetworkManager evolucionan, por lo que la bibliografía debe utilizarse para construir fundamentos y la documentación instalada/online para confirmar sintaxis y comportamiento de la versión utilizada.

## Principal — firewalld

1. **firewalld — Official Documentation**
   Fuente principal para arquitectura, zonas, servicios, puertos, rich rules, ipsets, policies, NAT, forwarding, runtime/permanent y herramientas de administración.

2. **firewalld manual pages**
   Especialmente:
   - `firewalld(1)`
   - `firewall-cmd(1)`
   - `firewall-offline-cmd(1)`
   - `firewalld.conf(5)`
   - `firewalld.zone(5)`
   - `firewalld.service(5)`
   - `firewalld.policy(5)`
   - `firewalld.richlanguage(5)`
   - `firewalld.ipset(5)`
   - `firewalld.helper(5)`
   - `firewalld.icmptype(5)`
   - `firewalld.direct(5)` cuando sea necesario estudiar compatibilidad o mecanismos históricos.

## Plataforma — Fedora

3. **Fedora Documentation**
   Referencia para administración de red y seguridad en Fedora, paquetes, servicios, systemd, NetworkManager y comportamiento específico de la distribución.

4. **Documentación y manuales instalados en Fedora**
   La versión instalada debe comprobarse con herramientas como `rpm`, `dnf`, `man` y opciones `--help`. Son una referencia especialmente importante cuando la documentación externa corresponde a otra versión.

## Backend y fundamentos — Netfilter / nftables

5. **nftables Wiki / Netfilter Project Documentation**
   Fuente para comprender tables, chains, hooks, priorities, sets, maps, expressions, connection tracking, NAT y el ruleset generado o utilizado por firewalld.

6. **nft(8)**
   Referencia operativa para inspeccionar el ruleset y comprender la sintaxis nftables relevante para diagnóstico.

7. **Netfilter documentation**
   Para arquitectura del filtrado de paquetes en el kernel, hooks, conntrack y NAT.

## Red en Linux

8. **iproute2 manual pages and documentation**
   `ip(8)`, `ss(8)` y herramientas relacionadas para interfaces, direcciones, rutas, sockets y diagnóstico.

9. **Linux kernel networking documentation**
   Fuente de profundización para forwarding, IPv4/IPv6, namespaces, Netfilter y parámetros de red del kernel cuando el PATH alcance temas internos.

## NetworkManager

10. **NetworkManager Documentation**
    Referencia para perfiles de conexión, interfaces y asociación con zonas de firewall.

11. **nmcli(1)** y **nm-settings-nmcli(5)**
    Consulta práctica para configuración y diagnóstico de conexiones.

## systemd y logging

12. **systemd manual pages**
    Principalmente `systemctl(1)`, `systemd.service(5)` y documentación de dependencias/unidades cuando se estudie el servicio firewalld.

13. **journalctl(1)**
    Fuente principal para inspección de logs y troubleshooting del daemon.

## SELinux

14. **SELinux Project / Fedora SELinux documentation**
    Para distinguir control de acceso obligatorio de filtrado de red y diagnosticar situaciones donde firewall y política SELinux interactúan.

15. **semanage(8)**, **ausearch(8)** y herramientas SELinux relacionadas
    Consulta para puertos etiquetados, AVC y troubleshooting cuando corresponda.

## Seguridad y diseño

16. **NIST SP 800-41 — Guidelines on Firewalls and Firewall Policy**
    Referencia conceptual para política de firewall, mínimo privilegio, diseño, administración y revisión.

17. **RFCs de IETF relevantes**
    Utilizar como profundización para IPv4, IPv6, TCP, UDP, ICMP/ICMPv6 y comportamiento de protocolos. No es necesario convertir el PATH en un curso de lectura de RFCs; se consultan cuando aclaran comportamiento normativo.

## Orden de uso recomendado

**Principal:** documentación oficial de firewalld + manual pages de la versión instalada.
**Plataforma:** Fedora Documentation.
**Backend:** nftables / Netfilter.
**Integración:** NetworkManager, systemd y SELinux.
**Fundamentos y diseño:** documentación del kernel, IETF y NIST.

## Regla para generación de lecciones

La bibliografía sirve como mapa de fuentes, no como límite del contenido. Cada lección debe integrar varias fuentes cuando sea necesario, priorizar documentación primaria y actual, diferenciar conceptos vigentes de mecanismos históricos y evitar afirmar que un comportamiento dependiente de versión es universal.

## Referencias complementarias por scope experto

### IP sets, rich rules y policies
- Documentación oficial y páginas de manual de la versión instalada: `firewall-cmd(1)`, `firewalld.richlanguage(5)`, `firewalld.ipset(5)` y `firewalld.policy(5)`. Consultar ejemplos y opciones compatibles con la versión de Fedora utilizada.

### D-Bus y Python
- API D-Bus oficial de firewalld y documentación de la biblioteca Python distribuida con el paquete; introspección de la interfaz instalada como fuente de verdad.

### Netfilter y tracing
- `nft(8)`, documentación del proyecto nftables sobre monitor, trace, counters y hooks; `conntrack(8)` y documentación de conntrack-tools.

### Automatización
- Documentación oficial de la colección `ansible.posix` y del módulo `ansible.posix.firewalld`; verificar versión, opciones admitidas y requisitos de Python/firewalld.
- Documentación de Molecule para pruebas de roles y entornos reproducibles.

### Virtualización y contenedores
- Documentación oficial de Podman/Netavark, Docker Engine y libvirt para integración de redes y firewall, con advertencias explícitas sobre diferencias por versión.

### Seguridad, operación y pruebas
- Manuales `firewalld.conf(5)`, `journalctl(1)`, `tcpdump(8)`, `ip(8)`, `ss(8)` y documentación del kernel sobre `rp_filter`, forwarding y namespaces.
- Documentación de Fedora sobre SELinux, NetworkManager y systemd.

**Criterio de vigencia:** comprobar expresamente disponibilidad de `firewallctl`, direct rules, lockdown y demás mecanismos históricos o dependientes de versión; no tratarlos como interfaces universales.

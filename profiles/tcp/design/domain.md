# Domain — IP Addressing, Subnetting, VLSM e IPv6

## Dominio
Diseño y administración del direccionamiento de redes TCP/IP, con énfasis práctico en IPv4, IPv6, subnetting, CIDR, FLSM, VLSM, sumarización, dual-stack, IPAM y troubleshooting sobre Linux/Fedora/RHEL.

## Alcance
El curso parte de binario, decimal y hexadecimal y progresa hasta diseño empresarial. El direccionamiento classful A/B/C/D/E se estudia como fundamento histórico; el diseño moderno se realiza con CIDR. Incluye cálculo manual, razonamiento binario, métodos rápidos, automatización con Python y validación real en Linux.

## Competencias finales
- Interpretar IPv4 e IPv6 a nivel de bits y prefijos.
- Identificar red, broadcast, rango de hosts y pertenencia a subred.
- Convertir máscaras y prefijos CIDR.
- Diseñar FLSM y VLSM sin solapamientos.
- Realizar supernetting y sumarización de rutas.
- Diseñar planes IPv4, IPv6 y dual-stack jerárquicos y escalables.
- Utilizar /31, /32, /127 y /128 correctamente según el caso.
- Documentar direccionamiento mediante tablas e IPAM.
- Configurar y verificar direccionamiento con `ip`, `nmcli` y herramientas Linux.
- Automatizar cálculos y validaciones mediante `ipaddress` de Python.
- Diagnosticar errores de máscara, gateway, routing, ARP/NDP, DAD y solapamientos.

## Entorno principal
Fedora/RHEL y herramientas estándar de Linux. Los conceptos son independientes del fabricante y aplicables a routers, switches L3, servidores, virtualización, cloud y redes empresariales.

## Metodología
Cada tema debe combinar teoría, representación binaria/hexadecimal cuando corresponda, cálculo manual, ejemplos progresivos, laboratorio y troubleshooting. Las lecciones deben comenzar con 🎯 OBJETIVO y terminar con 🧠 QUÉ DEBES RECORDAR. Usar 🧪 Laboratorio/ejemplos, ⚠️ Errores frecuentes y 💡 Idea importante cuando aporten valor.

## Fuera de alcance principal
El curso no pretende sustituir un PATH completo de routing dinámico, switching, DNS, DHCP, seguridad o análisis de protocolos. Estos temas se introducen únicamente cuando son necesarios para comprender el direccionamiento y su troubleshooting.


## Scopes de aprendizaje
- S01: fundamentos de direccionamiento y representación binaria/hexadecimal.
- S02: IPv4, máscaras, clases históricas y direcciones especiales.
- S03: subnetting IPv4, cálculo directo e inverso.
- S04: CIDR, FLSM y VLSM, planificación y restricciones.
- S05: supernetting, agregación y sumarización exacta.
- S06: IPv6, tipos de direcciones y diseño de subredes.
- S07: diseño empresarial, jerarquías, dual-stack y renumeración.
- S08: configuración, verificación y troubleshooting Fedora/RHEL.
- S09: automatización con Python e IPAM.
- S10: normas RFC y registros IANA (transversal).

## Criterios de profundidad y evaluación
- En los cálculos: justificar bits, prefijos, fronteras, rangos y excepciones, no solo memorizar tablas.
- Incluir problemas directos e inversos, soluciones paso a paso, ejercicios de práctica autónoma y comprobación con herramientas.
- En VLSM: restricciones, reservas de crecimiento, fragmentación, ausencia de solapamientos y uso eficiente del espacio.
- En IPv6: hexadecimal, límites de prefijos, jerarquía de /48, /56, /60 y /64, y casos /127 y /128.
- En diseño: documentar supuestos, asignaciones, capacidad, políticas, riesgos, migración y rollback.
- El proyecto final debe incluir memoria de cálculo, tabla IPAM, validación automatizada y evidencia de troubleshooting.

## Separación respecto al PATH TCP/IP
Este PATH profundiza en cálculos y diseño de direccionamiento. Protocolos TCP/UDP, análisis exhaustivo de capturas, routing dinámico, DNS y DHCP completos pertenecen a sus PATH independientes; aquí solo se tratan las interfaces imprescindibles para el diseño y diagnóstico.

## Precisiones técnicas obligatorias
- Separar pertenencia matemática a un prefijo, alcance on-link y ruta elegida por el sistema. `ip route get` consulta una decisión de ruta; verificar pertenencia con AND o `ipaddress`.
- En IPv6, una dirección asignada no declara automáticamente su prefijo on-link. Explicar RA, flags L/A y la diferencia entre asignación por SLAAC/DHCPv6 y aprendizaje del router por RA, en el alcance necesario para diseñar direccionamiento.
- La fusión elemental requiere dos bloques hermanos contiguos del mismo tamaño y alineados. Un conjunto de bloques de tamaños distintos también puede reducirse mediante fusiones sucesivas; distinguir unión exacta, conjunto mínimo de CIDR y superred con sobrecobertura.
- IPv6 no tiene broadcast. En `ipaddress`, interpretar `broadcast_address` como límite superior numérico del prefijo IPv6; explicar `hosts()` y sus casos /31, /32, /127 y /128 conforme a la documentación de la versión utilizada.
- No enumerar ni materializar el conjunto de hosts de una /64. Validar prefijos con intervalos, enteros, contención e iteración acotada.
- En IPAM, distinguir contenedores de asignaciones. La contención padre-hijo es válida; los conflictos de asignaciones se evalúan dentro de la misma familia y VRF o dominio de direccionamiento. La reutilización entre dominios aislados debe quedar documentada y revisarse al interconectarlos.
- ULA: distinguir fc00::/7 del espacio de asignación local fd00::/8 y generar Global ID según RFC 4193; evitar prometer ausencia absoluta de colisiones.

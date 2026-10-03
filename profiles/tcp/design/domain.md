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

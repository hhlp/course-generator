# DOMAIN — FIREWALLD EN PROFUNDIDAD — FEDORA

## Identidad del dominio

Este PATH enseña administración de firewall en Fedora con **firewalld** como interfaz de alto nivel y **nftables** como tecnología subyacente principal. El objetivo no es memorizar `firewall-cmd`, sino comprender el modelo completo: tráfico, zonas, servicios, puertos, interfaces, sources, rich rules, ipsets, NAT, forwarding, políticas, persistencia, integración y diagnóstico.

## Alcance

El dominio cubre el PATH 0–38, conservando las lecciones originales de 0–26 y añadiendo especialización de 27–38:

0. Fundamentos de firewall en Linux
1. Arquitectura de firewalld
2. Instalación y estado en Fedora
3. Configuración y archivos
4. Modelo runtime y permanent
5. Zonas
6. Interfaces y zonas
7. Sources
8. Servicios
9. Puertos
10. Protocolos
11. ICMP
12. Rich Rules
13. Policies
14. Forwarding
15. NAT
16. Connection tracking
17. Direct interface y reglas de bajo nivel
18. firewalld y nftables
19. Logging y diagnóstico
20. firewalld + systemd
21. firewalld + SELinux
22. IPv6
23. Seguridad y diseño
24. Investigación de problemas
25. Laboratorios
26. Proyecto final - firewalld-debugger
27. IP sets en profundidad
28. Rich rules avanzadas
29. Policies avanzadas
30. D-Bus y API de firewalld
31. nftables y Netfilter avanzado
32. Logging y observabilidad avanzada
33. Seguridad operativa y recuperación
34. Automatización con Ansible
35. Virtualización y contenedores
36. Troubleshooting experto
37. Laboratorios expertos
38. Proyecto experto integrador — firewalld architecture & debugger

## Plataforma de referencia

La plataforma principal es Fedora. Las explicaciones deben partir del comportamiento, paquetes, servicios, herramientas y convenciones actuales de Fedora. Cuando existan diferencias relevantes con RHEL u otras distribuciones, pueden mencionarse como contexto, pero no deben desplazar el foco del PATH.

## Modelo conceptual obligatorio

La enseñanza debe mantener separados estos niveles:

**Aplicación / servicio → firewalld → backend nftables → kernel / netfilter → tráfico de red**

`firewalld` no debe presentarse como sinónimo de `nftables`. Firewalld proporciona una abstracción dinámica basada en zonas, servicios, políticas y otros objetos; nftables permite observar y comprender las reglas efectivamente instaladas en el kernel.

## Conceptos nucleares

El alumno debe terminar dominando:

- firewall stateful y seguimiento de conexiones;
- ingress, egress y forwarding;
- zonas y niveles de confianza;
- asociación de interfaces y sources;
- servicios predefinidos y personalizados;
- apertura de puertos y protocolos;
- rich rules;
- ipsets;
- masquerading y NAT;
- port forwarding;
- forwarding entre redes;
- políticas entre zonas;
- IPv4 e IPv6;
- configuración runtime y permanent;
- XML y objetos persistentes de firewalld;
- recarga y sincronización de configuración;
- integración con systemd;
- interacción con NetworkManager;
- límites de responsabilidad entre firewall y SELinux;
- backend nftables;
- inspección del ruleset;
- logging, diagnóstico y troubleshooting;
- mínimo privilegio, reducción de superficie y diseño seguro;
- automatización idempotente;
- recuperación ante errores y prevención de pérdida de acceso remoto.

## Reglas pedagógicas del dominio

Cada lección comienza con `🎯 OBJETIVO`.

El desarrollo debe ser profundo y progresivo. Debe explicar qué problema resuelve el mecanismo, cómo funciona, cómo se administra, cómo se verifica y qué errores son habituales.

Cuando aporten valor se incorporan `🧪 Laboratorio/ejemplos`, `⚠️ Errores frecuentes` y `💡 Idea importante`.

Cada lección termina con `🧠 QUÉ DEBES RECORDAR`, condensando entre 3 y 7 ideas fundamentales. No debe limitarse a repetir el objetivo.

Los comandos deben explicarse. No basta con enumerarlos.

## Seguridad operativa

Toda operación que pueda bloquear SSH, cambiar la zona de una interfaz, modificar forwarding, eliminar reglas o alterar el comportamiento remoto debe tratarse con cautela. Antes de aplicar cambios potencialmente disruptivos, la lección debe enseñar a:

1. inspeccionar el estado actual;
2. identificar la interfaz y zona relevantes;
3. probar preferentemente en runtime;
4. verificar desde otra sesión cuando sea posible;
5. persistir solo después de validar;
6. conocer un procedimiento de recuperación.

## Runtime y permanent

Esta distinción es transversal a todo el PATH.

**Runtime** representa el estado activo de firewalld y es apropiado para inspección y pruebas controladas.

**Permanent** representa la configuración persistente que se recuperará tras recargas o reinicios.

El alumno debe aprender cuándo modificar cada ámbito y cómo evitar sobrescribir accidentalmente una configuración válida mediante operaciones de sincronización mal entendidas.

## firewalld y nftables

Nftables se utiliza para comprender el resultado de bajo nivel, diagnosticar y relacionar firewalld con Netfilter. El PATH no debe fomentar la modificación manual del ruleset administrado por firewalld como práctica ordinaria.

La inspección mediante `nft list ruleset` debe conectarse con los objetos configurados mediante firewalld para enseñar trazabilidad entre abstracción y reglas efectivas.

## firewalld y NetworkManager

Debe explicarse cómo las conexiones e interfaces gestionadas por NetworkManager se relacionan con zonas de firewalld. Los ejemplos deben evitar la falsa idea de que la asignación de zonas solo existe dentro de `firewall-cmd`.

## firewalld y SELinux

Firewall y SELinux resuelven problemas distintos. Permitir tráfico en firewalld no garantiza que un servicio pueda realizar una operación que SELinux prohíba, y permitir una operación mediante SELinux no abre tráfico bloqueado por el firewall.

## Automatización

La automatización debe perseguir estados declarativos e idempotentes. Debe verificarse el estado antes y después del cambio, evitar aperturas excesivas y distinguir claramente pruebas temporales de configuración persistente.

## Resultado esperado

Al finalizar, el alumno debe poder diseñar, implementar, auditar y diagnosticar un firewall Fedora real; explicar por qué una comunicación está permitida o bloqueada; rastrear la configuración desde firewalld hasta nftables; integrar el firewall con servicios, interfaces, NetworkManager, systemd y SELinux; y recuperar el sistema de configuraciones incorrectas.

## Profundidad técnica obligatoria (ampliación)

Cada tema relevante deberá explicar modelo conceptual, condiciones previas, sintaxis y parámetros, archivos persistentes, ejecución en Fedora, verificación observable, comportamiento runtime/permanent, seguridad y rollback, errores frecuentes y diagnóstico multicapa. No se asumirán opciones ni objetos disponibles sin comprobar la versión instalada.

Los laboratorios deben indicar topología, requisitos, comandos comentados, resultados esperados, pruebas negativas, limpieza y recuperación. Se deben distinguir explícitamente hechos derivados de la documentación de hipótesis del laboratorio.

## Competencias avanzadas y límites

- Rastrear tráfico host/forwarded y sus decisiones a través de zonas, sources, policies, rich rules y nftables.
- Utilizar IP sets y prioridades de forma verificable.
- Diagnosticar IPv6 sin bloquear protocolos imprescindibles para Neighbor Discovery y PMTUD.
- Automatizar con Ansible y D-Bus sin perder idempotencia ni acceso remoto.
- Entender la convivencia con NetworkManager, libvirt, Podman y Docker según versiones y backend.
- Auditar logs de daemon y paquetes, counters, conntrack y tracing en entornos controlados.
- Documentar reversión y recuperación para cada cambio disruptivo.

Este PATH no sustituye cursos completos de nftables, Ansible, SELinux o redes; profundiza únicamente en los mecanismos necesarios para administrar firewalld a nivel experto.

## Evaluación y proyecto

Cada bloque avanzado incluye verificación práctica y al menos un escenario de fallo. El bloque 26 conserva el proyecto original firewalld-debugger; el bloque 38 lo integra en una arquitectura multi-zona y dual-stack con pruebas, automatización y runbook de recuperación.

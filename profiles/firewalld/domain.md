# DOMAIN — FIREWALLD EN PROFUNDIDAD — FEDORA

## Identidad del dominio

Este PATH enseña administración de firewall en Fedora con **firewalld** como interfaz de alto nivel y **nftables** como tecnología subyacente principal. El objetivo no es memorizar `firewall-cmd`, sino comprender el modelo completo: tráfico, zonas, servicios, puertos, interfaces, sources, rich rules, ipsets, NAT, forwarding, políticas, persistencia, integración y diagnóstico.

## Alcance

El dominio cubre el PATH 0–26:

0. Fundamentos de firewall en Linux
1. Arquitectura de firewalld
2. Zonas
3. Servicios
4. Puertos
5. Interfaces
6. Rich rules
7. IP sets
8. NAT y masquerade
9. Forwarding
10. IPv6
11. Políticas
12. Runtime frente a permanent
13. Persistencia y configuración
14. firewalld + systemd
15. firewalld + NetworkManager
16. firewalld + SELinux
17. firewalld + nftables
18. Diagnóstico con `nft list ruleset`
19. Diagnóstico y troubleshooting
20. Seguridad
21. Automatización
22. Casos prácticos
23. Seguridad y diseño
24. Laboratorio integrador
25. Proyecto final
26. Bibliografía y fuentes de consulta

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

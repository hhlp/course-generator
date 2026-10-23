# Domain — Python Network Automation / Network Programmability

## Propósito

Ruta especializada de **0 en automatización de redes → experto en profundidad** para aplicar Python
a la administración, automatización, configuración, validación,
observabilidad y troubleshooting de redes, con foco práctico inicial en
**routers y switches Cisco**.

## Frontera con el PATH general de Python

Este curso **no es un curso de Python**. Se presupone dominio progresivo
del PATH general de Python. No se vuelven a enseñar desde cero
variables, tipos, colecciones, control de flujo, funciones, clases,
excepciones, comprehensions, decoradores, generators, async/await,
packaging o typing.

Cuando una capacidad de Python aparezca aquí, se enseña **su aplicación
al problema de red**. Ejemplos: `ipaddress` para validar prefijos,
`logging` para jobs y sesiones, `asyncio` para I/O concurrente, `json`
para APIs, XML para NETCONF y `ssl` para APIs seguras.

## Frontera con el PATH general de Ansible

Ansible es una herramienta importante de esta especialización, pero
**este curso no vuelve a enseñar Ansible desde cero**. Se presupone el
PATH general de Ansible.

Aquí se estudia Ansible específicamente como herramienta de Network
Automation: collections Cisco, `ansible.netcommon`, `network_cli`,
`netconf`, `httpapi`, Network Resource Modules, inventario de red,
Source of Truth, backups, desired/actual state, drift, pre/post-checks,
despliegues escalonados, rollback y troubleshooting de dispositivos de
red.

También se estudia su integración con Python, Nornir, NetBox y
pyATS/Genie, con énfasis en elegir correctamente qué capa debe resolver
cada problema y evitar duplicar responsabilidades.

## Frontera con Regex

Regex no se enseña desde cero. El PATH de Regex es la fuente de teoría y
técnica. Aquí solo se aplica cuando un output CLI necesita parsing y no
existe una interfaz estructurada o parser mantenido. Se priorizan datos
estructurados, TextFSM/ntc-templates, TTP y Genie cuando corresponda.

## Referencia principal

Se toma como referencia de partida **Python for Network Automation /
Python for Network Engineer**, de Syed Asif, especialmente su
orientación práctica hacia GNS3/Cisco y sus secciones de Paramiko,
Netmiko, NAPALM y Nornir.

La referencia no limita el alcance: el PATH la amplía hacia ingeniería
profesional con Scrapli, parsing estructurado, Jinja2, NETCONF, YANG,
RESTCONF, APIs Cisco, gNMI, pyATS/Genie, Source of Truth, NetBox,
concurrencia, compliance, testing, seguridad, CI/CD, observabilidad y
troubleshooting avanzado.

## Plataforma objetivo

Foco primario:

- Cisco IOS.
- Cisco IOS XE.
- Cisco IOS XR.
- Cisco NX-OS.
- Routers y switches Cisco.

La arquitectura se diseña para poder evolucionar a multivendor.

## Filosofía de aprendizaje

Cada tecnología relevante debe seguir, cuando aplique:

**fundamento → instalación → configuración → conexión → lectura → cambio
→ validación → logging → errores → troubleshooting → seguridad →
laboratorio → escala**

No basta con mostrar una API feliz. Las lecciones deben enseñar fallos
reales: autenticación, host keys, timeouts, prompts, parsing,
capabilities, namespaces XML, modelos YANG, certificados TLS,
concurrencia, cambios parciales y rollback.

## Stack principal

- Biblioteca estándar: pathlib, os, json, xml, ipaddress, socket, ssl,
  logging, argparse, concurrent.futures, asyncio.
- Config/datos: YAML, JSON, XML, TOML, Pydantic.
- SSH: Paramiko.
- CLI automation: Netmiko.
- CLI/NETCONF moderno: Scrapli / scrapli-netconf.
- Abstracción: NAPALM.
- Orquestación: Nornir.
- Templates: Jinja2.
- Parsing: TextFSM, ntc-templates, TTP, Genie.
- NETCONF: ncclient.
- REST/RESTCONF: requests y/o httpx.
- Model-driven: YANG, OpenConfig, gNMI/pygnmi.
- Cisco testing/validation: pyATS, Genie, Unicon.
- Source of Truth: NetBox/pynetbox.
- Testing: pytest + pyATS según responsabilidad.
- CI/CD: Git y pipelines reproducibles.
- Network automation declarativa: Ansible, ansible.netcommon y
  collections Cisco.

## Criterio de selección de herramientas

Paramiko se estudia para comprender y controlar SSH a bajo nivel.
Netmiko/Scrapli se usan para abstraer peculiaridades de CLI. NAPALM se
usa cuando su modelo multivendor y sus getters/configuration workflows
aportan valor. Nornir organiza inventario y ejecución concurrente.
NETCONF/RESTCONF/gNMI se prefieren cuando el dispositivo expone
interfaces model-driven apropiadas. pyATS/Genie se utiliza para parsing,
aprendizaje de estado, comparación y validación de red.

El alumno debe terminar siendo capaz de **justificar** la herramienta
elegida, no simplemente usar siempre la misma.

## Laboratorio

La ruta debe mantener un laboratorio reproducible con GNS3 como base de
referencia, admitiendo Cisco CML, EVE-NG, sandboxes de Cisco DevNet o
hardware cuando estén disponibles.

Las prácticas avanzan desde un dispositivo hasta topologías
multi-router/multi-switch y escenarios de fallo.

## Seguridad

Nunca se normaliza:

- Passwords hardcodeados.
- Desactivar permanentemente validación TLS.
- Aceptar host keys indiscriminadamente en producción.
- Registrar secretos.
- Ejecutar cambios masivos sin control de blast radius.
- Asumir que enviar un comando equivale a un cambio correcto.

Se enseñan secrets externos, SSH host-key verification, TLS, least
privilege, cuentas de automatización, auditoría, staged rollout y
rollback.

## Validación

Toda automatización de cambios madura sigue:

**baseline → pre-check → intended state → diff → approval/control →
change → post-check → semantic validation → report → rollback si
procede**

La validación debe comprobar estado operativo, no solo que la
configuración textual exista.

## Troubleshooting

Troubleshooting es transversal. Cada bloque debe incluir:

- Síntomas y errores típicos.
- Evidencias, logs y comandos de diagnóstico.
- Hipótesis y aislamiento por capas.
- Corrección y verificación posterior.

## Resultado final

El alumno debe poder construir y operar una plataforma de automatización
Cisco que gestione inventario, recoja estado, genere configuración,
despliegue cambios controlados, valide semánticamente la red, detecte
drift, produzca backups, registre auditoría, escale de forma segura y
diagnostique fallos del dispositivo o del propio stack de
automatización.


## Prerrequisitos y progresión revisada

«Cero» significa cero en automatización de redes. Se requieren Python general,
Linux/terminal, Git, Ethernet, VLAN, IPv4/IPv6, routing y SSH básicos.
OSPF/BGP y switching avanzado se revisan antes de las prácticas que los usan.
El PATH general de Ansible solo es prerrequisito al entrar en el bloque 28.

Antes del primer cambio se exige un protocolo mínimo: alcance de un dispositivo,
baseline, backup íntegro protegido, pre-check, candidate/diff, validación funcional
y recuperación por consola/OOB. Los bloques posteriores profundizan ese flujo.
Los fundamentos YANG están en el bloque 12 y NETCONF en el 13. DevNet se presenta
en el bloque 0; el bloque 27 desarrolla sus escenarios y alternativas.

## Contrato del laboratorio

Estos archivos son una especificación curricular. Las lecciones deben producir
configuraciones y scripts ejecutables; no se afirma que ya estén adjuntos.

- Registrar recursos CPU/RAM/disco y virtualización según las imágenes elegidas.
- Documentar imágenes obtenidas legítimamente, versiones y dependencias.
- Mantener topología, enlaces y plan de direccionamiento dual stack sin colisiones.
- Entregar configuración inicial por nodo y bootstrap de AAA/SSH y APIs soportadas.
- Fijar dependencias compatibles por herramienta; permitir entornos separados.
- Proporcionar comandos de arranque, verificación, reset y recuperación por consola.
- Validar acceso de management y tráfico de datos entre extremos.
- Conservar fixtures y alternativa local para prácticas dependientes de sandboxes.

La matriz de capacidades debe registrar plataforma, release, imagen, protocolo,
operación, soporte observado, fuente oficial, fecha y alternativa de práctica.
No se presupone que IOS, IOS XE, IOS XR y NX-OS tengan las mismas interfaces,
modelos, datastores, getters ni mecanismos de rollback. Las pruebas de escala
simuladas no acreditan capacidad real de los dispositivos.

## Estado, concurrencia y recuperación

Separar intent, configuración observada y estado operacional. La configuración
recopilada con Resource Modules no demuestra conectividad ni convergencia.
Separar backups íntegros cifrados de copias redactadas para diff/Git.
La SoT conserva autoridad por campo; descubrir estado no autoriza a sobrescribir
automáticamente el estado deseado. Toda reconciliación debe ser auditable.

Evitar cambios concurrentes mediante locks por dispositivo y revalidar el baseline
antes de escribir. Un timeout puede dejar resultado incierto: leer y reconciliar
antes de repetir la operación. Persistir estados/checkpoints de jobs y demostrar
recuperación tras caída de worker. No prometer atomicidad entre dispositivos ni
ejecución exactamente una vez sobre transportes heterogéneos.

## Entregables y evaluación

Cada bloque termina con un checkpoint que indica entregables, aprobación y
evidencias. Cada práctica debe especificar prerequisitos, versiones/capabilities,
comandos de reproducción, resultado esperado, fallo inyectado, diagnóstico,
limpieza y recuperación. Distinguir pruebas offline de validación en equipo real.
Un PASS exige evidencia funcional; un comando sin error no basta.

Ansible se organiza en unidades con subtemas: no se eliminan los temas originales
al agrupar las 326 entradas. El proyecto final exige un workflow Ansible ejecutado
desde Python con ansible-runner, validado mediante pyATS y con recuperación.
Nornir y Ansible deben tener responsabilidades distintas y compartir contratos
de inventario/resultados, sin duplicar la aplicación del mismo cambio.

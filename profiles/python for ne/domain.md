# Domain — Python Network Automation / Network Programmability

## Propósito

Ruta especializada de **0 → experto en profundidad** para aplicar Python
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

Foco primario: - Cisco IOS - Cisco IOS XE - Cisco IOS XR - Cisco NX-OS -
routers Cisco - switches Cisco

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

Nunca se normaliza: - passwords hardcodeados; - desactivar
permanentemente validación TLS; - aceptar host keys indiscriminadamente
en producción; - registrar secretos; - ejecutar cambios masivos sin
control de blast radius; - asumir que un comando enviado equivale a un
cambio correcto.

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

Troubleshooting es transversal. Cada bloque debe incluir: - síntomas; -
evidencias; - logs; - comandos/herramientas de diagnóstico; - errores
típicos; - hipótesis; - aislamiento por capas; - corrección; -
verificación posterior.

## Resultado final

El alumno debe poder construir y operar una plataforma de automatización
Cisco que gestione inventario, recoja estado, genere configuración,
despliegue cambios controlados, valide semánticamente la red, detecte
drift, produzca backups, registre auditoría, escale de forma segura y
diagnostique fallos del dispositivo o del propio stack de
automatización.

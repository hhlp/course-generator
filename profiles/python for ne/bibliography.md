# Bibliography — Python Network Automation / Network Programmability

## Referencia principal del PATH

- Syed Asif. **Python for Network Automation** / *Python for Network Engineer*.
  [Read the Docs](https://python-automation-book.readthedocs.io/en/latest/index.html). Referencia práctica principal para la
  progresión inicial de network automation, laboratorio, Paramiko,
  Netmiko, NAPALM y Nornir.

## Cisco y automatización

- Rick Graziani y Adrian Iliesiu. **Hands-On Cisco Automation with Python:
  Streamline Network Tasks Using Netmiko, NAPALM, and Nornir for Beginners**.
  Cisco Press, 2026, 1.ª edición. ISBN impreso: 9780135463192.
  [Ficha editorial](https://www.ciscopress.com/store/hands-on-cisco-automation-with-python-streamline-network-9780135463192). Referencia
  complementaria orientada a Cisco y a la progresión Netmiko → NAPALM →
  Nornir, además de interfaces programables.
- Cisco DevNet. **pyATS Documentation**.
- Cisco DevNet. **Genie Documentation**.
- Cisco DevNet. Documentación de **IOS XE Programmability**, NETCONF,
  RESTCONF, YANG y model-driven telemetry.
- Cisco DevNet. Documentación y sandboxes de **NX-OS Programmability /
  NX-API**.

## SSH y CLI automation

- Paramiko. **Official Documentation**.
- Netmiko. **Official Documentation**.
- Scrapli. **Official Documentation**.
- OpenSSH. **Manual Pages / Documentation**, como referencia operacional
  para diagnosticar SSH fuera de Python.

## Abstracción y orquestación

- NAPALM. **Official Documentation and project documentation**.
- Nornir. **Official Documentation**.
- nornir-netmiko, nornir-napalm y nornir-scrapli. Documentación de
  plugins cuando se utilicen.

## Parsing

- TextFSM. Documentación del proyecto.
- Network to Code. **ntc-templates**.
- TTP — Template Text Parser. Documentación oficial.
- Cisco Genie parsers. Documentación y catálogo soportado.

## Templates y datos

- Pallets. **Jinja Documentation**.
- PyYAML. Documentación oficial.
- Pydantic. Documentación oficial.
- Python Standard Library: `json`, `xml`, `ipaddress`, `socket`, `ssl`,
  `logging`, `concurrent.futures`, `asyncio`.

## Model-driven networking

- IETF RFC 6241 — **Network Configuration Protocol (NETCONF)**.
- IETF RFC 7950 — **The YANG 1.1 Data Modeling Language**.
- IETF RFC 8040 — **RESTCONF Protocol**.
- ncclient. Documentación oficial.
- OpenConfig. Modelos y documentación.
- gNMI Specification.
- pygnmi. Documentación del proyecto.
- pyang. Documentación del proyecto.

## Source of Truth

- NetBox. **Official Documentation**.
- pynetbox. Documentación oficial.

## Ansible aplicado a networking

- Ansible Community Documentation. **Network Getting Started / Network
  Automation**.
- Ansible Documentation. **ansible.netcommon collection**.
- Cisco Ansible Collection. **cisco.ios**.
- Cisco Ansible Collection. **cisco.iosxr**.
- Cisco Ansible Collection. **cisco.nxos**.
- Ansible Documentation. **Network Resource Modules**.
- Ansible Runner. **Official Documentation**, para integración
  programática Python ↔ Ansible.
- NetBox Ansible Collection / inventory integration. Documentación
  oficial cuando se utilice NetBox como Source of Truth.

Estas referencias se utilizan únicamente para la aplicación de Ansible a
redes; la teoría general, arquitectura y administración completa de
Ansible pertenecen al PATH específico de Ansible.

## Testing

- pytest. **Official Documentation**.
- Cisco pyATS / AEtest / Genie / Unicon. Documentación oficial.

## HTTP y APIs

- Requests. **Official Documentation**.
- HTTPX. **Official Documentation**.
- IETF HTTP/TLS RFCs relevantes según las lecciones.

## Referencias normativas y operacionales

La documentación oficial y los RFCs tienen prioridad para comportamiento
de protocolos. La documentación del fabricante tiene prioridad para
capacidades específicas de IOS, IOS XE, IOS XR y NX-OS. Antes de enseñar
sintaxis dependiente de versión, se debe verificar contra la
documentación vigente de la plataforma y release usados en el
laboratorio.


## Mapa de consulta por bloques y enlaces oficiales

Fecha de revisión bibliográfica: 2026-10-22. Registrar la versión consultada
durante cada laboratorio. Una referencia no implica soporte en todas las imágenes.

| Bloques | Fuentes oficiales y finalidad |
| --- | --- |
| 0–1, 27 | [GNS3](https://docs.gns3.com/), [Cisco DevNet](https://developer.cisco.com/), [uv](https://docs.astral.sh/uv/): laboratorio y entorno. |
| 1–2, 19, 23 | [Python](https://docs.python.org/3/), [Pydantic](https://docs.pydantic.dev/), [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation): datos y validación. |
| 2, 28 | [NetBox](https://netbox.readthedocs.io/), [pynetbox](https://pynetbox.readthedocs.io/), [netbox.netbox](https://docs.ansible.com/projects/ansible/latest/collections/netbox/netbox/): SoT e inventario. |
| 3–4 | [OpenSSH](https://www.openssh.com/manual.html), [Paramiko](https://docs.paramiko.org/): transporte y trust. |
| 5–6 | [Netmiko](https://ktbyers.github.io/netmiko/), [Scrapli](https://carlmontanari.github.io/scrapli/), [scrapli-netconf](https://scrapli.github.io/scrapli_netconf/): CLI y transportes. |
| 7 | [TextFSM](https://github.com/google/textfsm), [ntc-templates](https://ntc-templates.readthedocs.io/), [TTP](https://ttp.readthedocs.io/): parsing y fixtures. |
| 8 | [NAPALM](https://napalm.readthedocs.io/), [matriz de soporte](https://napalm.readthedocs.io/en/latest/support/): drivers y operaciones. |
| 9 | [Nornir](https://nornir.readthedocs.io/): inventario, tasks y runners; consultar además el plugin instalado. |
| 10 | [Jinja](https://jinja.palletsprojects.com/): templates y StrictUndefined. |
| 11–16 | [Cisco IOS XE](https://developer.cisco.com/iosxe/), [IOS XR](https://developer.cisco.com/iosxr/), [NX-OS](https://developer.cisco.com/nxos/): documentación por plataforma y release. |
| 12 | [RFC 7950](https://www.rfc-editor.org/rfc/rfc7950), [RFC 8342](https://www.rfc-editor.org/rfc/rfc8342), [RFC 8525](https://www.rfc-editor.org/rfc/rfc8525): YANG, NMDA y YANG Library. |
| 12 | [pyang](https://github.com/mbj4668/pyang), [YANG Suite](https://developer.cisco.com/yangsuite/), [OpenConfig](https://www.openconfig.net/): exploración y modelos. |
| 13 | [RFC 6241](https://www.rfc-editor.org/rfc/rfc6241), [RFC 6242](https://www.rfc-editor.org/rfc/rfc6242), [ncclient](https://ncclient.readthedocs.io/): operaciones, capabilities y transporte SSH. |
| 14 | [RFC 8040](https://www.rfc-editor.org/rfc/rfc8040), [RFC 8072](https://www.rfc-editor.org/rfc/rfc8072): RESTCONF y YANG Patch. |
| 14–15 | [Requests](https://requests.readthedocs.io/), [HTTPX](https://www.python-httpx.org/): clientes HTTP, TLS y errores. |
| 16 | [Especificación gNMI](https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md), [protobuf oficial](https://github.com/openconfig/gnmi), [pygnmi](https://github.com/akarneliuk/pygnmi): capabilities, Set y streams. |
| 17, 22, 25 | [Cisco pyATS](https://developer.cisco.com/pyats/), [Genie](https://developer.cisco.com/docs/genie-docs/): validación y parsers; priorizar el portal del fabricante. |
| 18 | [RFC 3414](https://www.rfc-editor.org/rfc/rfc3414), [RFC 3826](https://www.rfc-editor.org/rfc/rfc3826), [RFC 7860](https://www.rfc-editor.org/rfc/rfc7860), [RFC 2863](https://www.rfc-editor.org/rfc/rfc2863): seguridad SNMPv3 y contadores de interfaces. |
| 18 | [PySNMP](https://docs.lextudio.com/pysnmp/): biblioteca candidata; confirmar mantenimiento, API y compatibilidad antes de fijar versión. |
| 23–24 | [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/), [Vault](https://developer.hashicorp.com/vault/docs): observabilidad y secretos. |
| 25–26 | [pytest](https://docs.pytest.org/), [GitHub Actions](https://docs.github.com/en/actions): pruebas y pipeline. |
| 28 | [Networking Ansible](https://docs.ansible.com/projects/ansible/latest/network/index.html), [Resource Modules](https://docs.ansible.com/projects/ansible/latest/network/user_guide/network_resource_modules.html): configuración estructurada y estados. |
| 28 | [ansible.netcommon](https://docs.ansible.com/projects/ansible/latest/collections/ansible/netcommon/), [cisco.ios](https://docs.ansible.com/projects/ansible/latest/collections/cisco/ios/), [cisco.iosxr](https://docs.ansible.com/projects/ansible/latest/collections/cisco/iosxr/), [cisco.nxos](https://docs.ansible.com/projects/ansible/latest/collections/cisco/nxos/): contratos por módulo. |
| 28–31 | [Ansible Runner](https://ansible.readthedocs.io/projects/runner/en/stable/): ejecución Python, eventos y artifacts. |

Los bloques 20–22 y 29–31 reutilizan las fuentes de sus transportes, validadores
y plataformas; su evaluación se basa en integración, fallos y recuperación.

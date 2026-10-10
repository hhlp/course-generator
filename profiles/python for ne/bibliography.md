# Bibliography — Python Network Automation / Network Programmability

## Referencia principal del PATH

- Syed Asif. **Python for Network Automation / Python for Network
  Engineer**. Read the Docs. Referencia práctica principal para la
  progresión inicial de network automation, laboratorio, Paramiko,
  Netmiko, NAPALM y Nornir.

## Cisco y automatización

- Cisco Press. **Hands-On Cisco Automation with Python: Streamline
  Network Management with Netmiko, NAPALM, and Nornir**. Referencia
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

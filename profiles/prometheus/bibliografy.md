# bibliografy.md — Prometheus

## Principal

1. Prometheus Documentation
   - Documentación oficial de Prometheus.
   - Fuente principal para configuración, PromQL, storage, federation, remote write/read, HTTP API, alerting y operación.
   - https://prometheus.io/docs/

2. Prometheus GitHub Repository
   - Código fuente, releases, issues, ejemplos y documentación técnica.
   - Fuente principal para internals y comportamiento de versiones actuales.
   - https://github.com/prometheus/prometheus

## Componentes oficiales

3. Alertmanager Documentation
   - Routing, grouping, inhibition, silences, receivers, templates y HA.
   - https://prometheus.io/docs/alerting/latest/alertmanager/

4. Alertmanager GitHub Repository
   - Código fuente y releases.
   - https://github.com/prometheus/alertmanager

5. Node Exporter
   - Exporter de referencia para Linux y estudio de collectors.
   - https://github.com/prometheus/node_exporter

6. Blackbox Exporter
   - Probes HTTP, HTTPS, TCP, DNS e ICMP.
   - https://github.com/prometheus/blackbox_exporter

7. SNMP Exporter
   - Monitorización SNMP y generación de configuración.
   - https://github.com/prometheus/snmp_exporter

8. Pushgateway
   - Uso específico para métricas de jobs batch y limitaciones del modelo push.
   - https://github.com/prometheus/pushgateway

## Especificaciones y estándares

9. Prometheus Exposition Formats
   - Formato de exposición de métricas.
   - https://prometheus.io/docs/instrumenting/exposition_formats/

10. OpenMetrics Specification
    - Especificación relacionada con exposición e interoperabilidad de métricas.
    - https://openmetrics.io/

11. Prometheus Remote Write Specification
    - Referencia para remote write y compatibilidad entre sistemas.
    - https://prometheus.io/docs/specs/

## PromQL y operación

12. Prometheus Querying Documentation
    - PromQL, operadores, funciones, ejemplos y semántica.
    - https://prometheus.io/docs/prometheus/latest/querying/basics/

13. Prometheus Recording Rules
    - Diseño y funcionamiento de recording rules.
    - https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/

14. Prometheus Alerting Rules
    - Diseño y evaluación de alerting rules.
    - https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/

15. promtool Documentation / Command Help
    - Validación de configuraciones y reglas, testing y utilidades TSDB.

## Arquitectura e internals

16. Prometheus TSDB source code and design material
    - Código bajo tsdb/ en el repositorio Prometheus.
    - Fuente de profundización para WAL, Head, chunks, blocks, index, postings y compaction.

17. Prometheus PromQL source code
    - Parser, engine y evaluación de expresiones.
    - Fuente de profundización para los bloques de internals.

18. Prometheus discovery, scrape, rules, notifier y remote packages
    - Código fuente para seguir el pipeline interno del servidor.

## Observabilidad y SRE

19. Google — Site Reliability Engineering
    - SLI, SLO, alerting, monitoring y operación de sistemas.
    - https://sre.google/books/

20. Google — The Site Reliability Workbook
    - Prácticas aplicadas para SLO, alertas y operación.
    - https://sre.google/workbook/table-of-contents/

21. Rob Ewaschuk — My Philosophy on Alerting
    - Referencia clásica para diseño de alertas orientadas a síntomas y acción.

## Fedora y Linux

22. Fedora Documentation
    - systemd, SELinux, firewalld, administración de servicios y seguridad.
    - https://docs.fedoraproject.org/

23. systemd Documentation / man pages
    - Integración de Prometheus y exporters como servicios.
    - man systemd.service
    - man systemctl
    - man journalctl

24. SELinux Project / Fedora SELinux documentation
    - Diagnóstico y hardening de servicios.

25. firewalld Documentation
    - Exposición segura de Prometheus, Alertmanager y exporters.

## Bibliografía complementaria

26. Prometheus: Up & Running
    - Introducción y profundización práctica en Prometheus y PromQL.
    - Utilizar como complemento; validar comportamiento actual contra la documentación oficial.

27. Prometheus community integrations
    - Catálogo de exporters e integraciones.
    - Debe utilizarse para aprender a localizar herramientas, no para asumir que todo exporter comunitario tiene el mismo nivel de mantenimiento.

## Criterio de precedencia

Para comportamiento que pueda variar entre versiones:

1. documentación oficial vigente;
2. release notes/changelog;
3. código fuente de la versión estudiada;
4. documentación de Fedora para integración con el sistema;
5. libros y material complementario.

El curso no debe fijar como universal un comportamiento dependiente de versión sin indicarlo.

# bibliography.md — Prometheus

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
    - https://prometheus.io/docs/prometheus/latest/command-line/promtool/

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
    - Enlace desde las prácticas oficiales: https://prometheus.io/docs/practices/alerting/

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
    - https://docs.fedoraproject.org/en-US/quick-docs/selinux-getting-started/

25. firewalld Documentation
    - Exposición segura de Prometheus, Alertmanager y exporters.
    - https://firewalld.org/documentation/

## Bibliografía complementaria

26. Julien Pivotto y Brian Brazil — Prometheus: Up & Running, 2.ª edición. O’Reilly.
   - https://www.oreilly.com/library/view/prometheus-up/9781098131135/
    - Introducción y profundización práctica en Prometheus y PromQL.
    - Utilizar como complemento; validar comportamiento actual contra la documentación oficial.

27. Prometheus community integrations
    - Catálogo de exporters e integraciones.
    - https://prometheus.io/docs/instrumenting/exporters/
    - Debe utilizarse para aprender a localizar herramientas, no para asumir que todo exporter comunitario tiene el mismo nivel de mantenimiento.

## Criterio de precedencia

Para comportamiento que pueda variar entre versiones:

1. documentación oficial de la versión ejecutada y sus notas de versión;
2. ayuda del binario instalado y configuración efectiva;
3. código y tests del tag/commit correspondiente para detalles internos;
4. documentación de la versión de Fedora para integración con el sistema;
5. libros y material complementario.

La documentación vigente sirve para localizar conceptos; no debe reemplazar sin comprobación la de una versión anterior utilizada en el laboratorio. Registrar discrepancias y comprobar el comportamiento mediante un caso mínimo.


## Referencias ampliadas por scope (revisión profunda)

### A. Protocolos y compatibilidad
- Prometheus Remote Write specifications (1.0 y 2.0): https://prometheus.io/docs/specs/
- Prometheus configuration reference y feature flags: https://prometheus.io/docs/prometheus/latest/configuration/configuration/
- Prometheus querying functions: https://prometheus.io/docs/prometheus/latest/querying/functions/
- Prometheus native histograms: https://prometheus.io/docs/specs/native_histograms/

### B. Exporters, discovery y Kubernetes (integración, no curso de Kubernetes)
- Prometheus exporters and integrations: https://prometheus.io/docs/instrumenting/exporters/
- Prometheus Operator: https://prometheus-operator.dev/
- kube-state-metrics: https://github.com/kubernetes/kube-state-metrics

### C. HA, almacenamiento y arquitecturas (comparativa conceptual)
- Thanos documentation: https://thanos.io/tip/thanos/getting-started.md/
- Grafana Mimir documentation: https://grafana.com/docs/mimir/latest/
- VictoriaMetrics documentation: https://docs.victoriametrics.com/

### D. Seguridad, pruebas y operación
- Prometheus security model: https://prometheus.io/docs/operating/security/
- Prometheus unit testing rules: https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/
- Prometheus management API: https://prometheus.io/docs/prometheus/latest/management_api/
- systemd-analyze manual: https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html
- Ansible documentation: https://docs.ansible.com/

### E. Código e internals
- Prometheus TSDB: https://github.com/prometheus/prometheus/tree/main/tsdb
- Prometheus promql: https://github.com/prometheus/prometheus/tree/main/promql
- Go profiling pprof: https://pkg.go.dev/net/http/pprof

> Todas las referencias externas ampliadas deben contrastarse con la versión estudiada. Las plataformas externas se estudian como integración y comparación, no como PATH independientes.


## Referencias de la revisión focalizada

- Migración 2.x → 3.x: https://prometheus.io/docs/prometheus/latest/migration/
- Releases para elegir y fijar la versión estudiada: https://github.com/prometheus/prometheus/releases
- Prometheus Operator, introducción: https://prometheus-operator.dev/docs/getting-started/introduction/
- API de Operator: https://prometheus-operator.dev/docs/api-reference/api/
- Alertmanager HA: https://prometheus.io/docs/alerting/latest/high_availability/
- Alert relabeling y configuración del notifier: https://prometheus.io/docs/prometheus/latest/configuration/configuration/

Los enlaces con latest, main o tip son puntos de entrada. Para cada ejercicio, conservar URL y versión consultada; en código, reemplazar main por el tag/commit elegido. Fijar igualmente versión de Operator/CRDs y del receptor remoto cuando proceda. No se prescribe una release no verificada como universal.

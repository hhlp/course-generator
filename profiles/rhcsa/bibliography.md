# bibliography.md — RHCSA / Administración RHEL 10

## Principal
1. Asghar Ghori — *RHCSA Red Hat Enterprise Linux 10 Training and Exam Preparation Guide (EX200)*, Fourth Edition.
2. Sander van Vugt — *Red Hat RHCSA 10 Cert Guide: EX200*.

## Autoridad para certificación
- Red Hat — objetivos oficiales vigentes de Red Hat Certified System Administrator (RHCSA), EX200.
- Red Hat — documentación oficial vigente de Red Hat Enterprise Linux 10.

## Documentación técnica primaria
- Manuales y documentación instalada de RHEL 10 (`man`, `info`, `/usr/share/doc`).
- systemd documentation y manual pages.
- NetworkManager documentation.
- firewalld documentation.
- SELinux / policycoreutils documentation y guías de Red Hat.
- OpenSSH manual pages.
- RPM y DNF/libdnf documentation aplicable a RHEL 10.
- LVM2 documentation.
- XFS documentation y manual pages.
- Stratis documentation.
- Podman documentation.
- Quadlet/systemd documentation.
- chrony documentation.
- NFS/autofs manual pages y documentación RHEL.
- Apache HTTP Server y documentación RHEL de servicios web.
- Cockpit y tuned: documentación oficial y manuales instalados.

## Extensiones Fedora/Linux+
- Fedora documentation para administración de Btrfs y ampliaciones de escritorio Flatpak.
- Btrfs upstream documentation.
- Flatpak documentation.

## Complementaria recomendada
- Michael Kerrisk — *The Linux Programming Interface*, como consulta para conceptos de procesos, filesystem, señales y APIs; no como libro base de administración.
- Brendan Gregg — *Systems Performance*, como profundización conceptual de metodología y diagnóstico de rendimiento; usar solo en el alcance administrativo del PATH.


## Bibliografía complementaria estructural — Linux y administración práctica
- Michael Hausenblas — *Learning Modern Linux: A Handbook for the Cloud Native Practitioner*. Arquitectura Linux contemporánea, kernel, procesos, aislamiento y contenedores; especialmente bloques 0, 7, 8, 12, 13, 32 y 35. No sustituye la documentación de RHEL 10.
- Carla Schroder — *Linux Cookbook: Essential Skills for Linux Users and System & Network Administrators*. Recetas de administración y diagnóstico; bloques 2–6, 9–16, 18–19, 24–31 y 38. Adaptar comandos y rutas a RHEL 10.
- Daniel J. Barrett — *Linux Pocket Guide: Essential Commands*. Consulta rápida de comandos y operaciones CLI; bloques 0, 2–6, 12, 16, 24, 30 y 38. No reemplaza laboratorios ni manuales.
- Kenneth Hess — *Practical Linux System Administration: A Guide to Installation, Configuration, and Management*. Enfoque transversal de instalación, mantenimiento, seguridad y operaciones; bloques 1, 9–16, 18–21, 24–29, 34–39 y 42. Verificar diferencias de distribución y versión.

## Criterio de integración
Los libros amplían modelos mentales y ejemplos, pero las instrucciones ejecutables se contrastan con RHEL 10, la documentación instalada y los objetivos EX200 vigentes. No introducir tecnologías de cloud-native o desarrollo de kernel como requisitos del examen.

## Regla bibliográfica
Los libros RHCSA organizan y refuerzan el aprendizaje, pero no limitan el temario. No asumir que un procedimiento sigue siendo válido solo porque aparece en un libro. Verificar cambios de RHEL 10, herramientas, opciones y objetivos EX200 contra documentación oficial y manuales del sistema.

## Regla para el generador
No resumir capítulos ni reproducir texto de las fuentes. Sintetizar conocimiento, explicar desde principios operativos y construir laboratorios originales y verificables.


## Fuentes oficiales enlazadas y trazabilidad
Fecha de contraste del alcance EX200: 2026-10-22. La documentación es evolutiva; fijar versión y paquetes del laboratorio al ejecutar procedimientos.

- [Red Hat — objetivos oficiales EX200](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam): autoridad para la matriz de certificación de todos los bloques y los simulacros 40–41.
- [Documentación RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10): punto de entrada para instalación, administración, networking, seguridad y contenedores.
- [Managing file systems — RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_file_systems/index): montajes, filesystems y diagnóstico; bloques 19, 22 y 34.
- [Managing storage devices — RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_storage_devices/index): dispositivos y administración de almacenamiento; bloques 18–22.
- [Administering RHEL by using the GNOME desktop environment — RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/administering_rhel_by_using_the_gnome_desktop_environment/index): remoto Red Hat Flatpak y contexto de aplicaciones de escritorio; bloque 17.
- [Flatpak — Using Flatpak](https://docs.flatpak.org/en/latest/using-flatpak.html): operaciones sobre remotos y aplicaciones, contrastadas con RHEL; bloque 17.
- [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html): unidades timer, OnCalendar y Persistent; contrastar la versión instalada en RHEL, bloque 28.
- [chrony documentation](https://chrony-project.org/documentation.html): configuración y verificación del cliente, contrastadas con la versión de RHEL; bloque 29.

Flatpak básico, timers, cliente de tiempo y perfiles tuned pertenecen al núcleo EX200 publicado. Podman/Quadlet se conservan como ampliación RHEL+; Btrfs como Fedora/Linux+. Estos últimos no deben incorporarse por defecto a simulacros EX200. Mantener todos los libros ya incluidos como apoyo, con la autoridad oficial por delante.

# domain.md — RHCSA / Administración RHEL 10

## Propósito
Este PATH forma administradores de Red Hat Enterprise Linux 10 desde cero hasta un nivel práctico avanzado. RHCSA/EX200 es un hito verificable dentro del recorrido, no el límite del contenido.

## Fuentes y autoridad
Los libros de Asghar Ghori y Sander van Vugt son ayudas didácticas principales. No determinan el techo del PATH. Ante discrepancias prevalecen, en este orden: objetivos oficiales vigentes de EX200 para lo relativo al examen; documentación oficial vigente de RHEL 10 para comportamiento y administración; manuales y documentación instalada de la versión usada; documentación upstream cuando sea necesaria para comprender un componente.

## Etiquetas de alcance
`[CORE]`: fundamentos imprescindibles de Linux.
`[EX200]`: contenido directamente asociado a preparación RHCSA, siempre contrastado con los objetivos vigentes.
`[RHEL]` / `[RHEL+]`: administración de RHEL que puede superar el examen.
`[FEDORA]` / `[FEDORA][LINUX+]`: ampliaciones útiles en Fedora/Linux que no deben presentarse automáticamente como requisitos EX200.

## Regla pedagógica obligatoria
Toda lección comienza por `🎯 OBJETIVO`.
El cuerpo explica modelo mental, componentes, archivos, comandos, persistencia, verificación y diagnóstico.
Usar cuando aporten valor: `🧪 Laboratorio/ejemplos`, `⚠️ Errores frecuentes`, `💡 Idea importante`.
Toda lección termina por `🧠 QUÉ DEBES RECORDAR`, con 3–7 ideas esenciales y no una repetición del objetivo.

## Filosofía operacional
No basta con mostrar comandos. El alumno debe saber:
1. qué estado está observando o modificando;
2. qué componente lo controla;
3. dónde se persiste;
4. cómo verificarlo;
5. qué ocurre después de reboot;
6. cómo detectar un fallo;
7. cómo revertirlo o recuperarlo.

## Laboratorios
Priorizar máquinas RHEL 10. Usar al menos dos nodos cuando networking, SSH, NFS o servicios remotos lo requieran. Fedora puede usarse para extensiones explícitas, especialmente Btrfs y Flatpak. Los laboratorios evolucionan de guiados a escenarios sin pasos.

## Profundidad y límites
systemd, SELinux, firewalld, OpenSSH, RPM y containers deben ser autosuficientes a nivel de administración de servidor, aunque existan PATH especializados más profundos. Apache se practica como servicio de red de referencia, con VirtualHost, SELinux, firewalld, logs y validación; la administración web avanzada queda en el PATH especializado. No convertir RHCSA en un curso de desarrollo interno de cada proyecto. Btrfs se enseña con profundidad administrativa como extensión Fedora/Linux+. Flatpak se incluye como extensión de gestión de software, sin confundirlo con RPM/DNF ni con el núcleo del servidor RHEL.

## Seguridad
Mantener SELinux enforcing salvo ejercicios explícitos de diagnóstico. No recomendar desactivar firewalls o controles de seguridad como solución permanente. Explicar el impacto de operaciones destructivas y exigir backup/snapshot en laboratorios de recuperación.

## Resultado final
El alumno debe poder instalar, configurar, actualizar, securizar, observar, automatizar, diagnosticar, recuperar y documentar un servidor RHEL 10; además debe estar preparado para practicar las competencias vigentes del EX200.

## Profundidad reforzada y uso de los libros nuevos
En cada lección práctica relevante: describir prerrequisitos, paquetes y versiones, archivos y rutas, comandos con explicación de opciones, cambios runtime/persistentes, validación antes y después de reiniciar, ubicación de logs (journald y /var/log cuando exista), fallos reproducibles y recuperación segura. No inventar rutas de logs: comprobar paquete, configuración y versión.

Integrar *Learning Modern Linux* para arquitectura y aislamiento; *Linux Cookbook* para recetas originales y escenarios; *Linux Pocket Guide* para fluidez CLI; y *Practical Linux System Administration* para operación integral. Mantener los dos textos RHCSA como apoyo al examen y la documentación oficial como autoridad.

Los contenidos compartidos con PATH especializados (Bash/Zsh, systemd, SELinux, firewalld, OpenSSH, contenedores, IAM y servicios de infraestructura) serán autosuficientes para administrar RHEL 10, sin duplicar la especialización completa. Distinguir identidad local y consumo de IAM central; no implementar aquí un proveedor IAM.

## Evaluación práctica y progresión
Cada bloque operacional debe proponer observación, configuración, verificación, diagnóstico y rollback cuando aplique. Usar laboratorios guiados, fallos inducidos con snapshot y casos sin instrucciones paso a paso. Evaluar evidencias (salidas, logs, estado persistente, runbook), no solo ejecución de comandos. Etiquetar claramente las extensiones fuera de EX200.

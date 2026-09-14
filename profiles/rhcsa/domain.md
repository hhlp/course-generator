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
systemd, SELinux, firewalld, OpenSSH, RPM y containers deben ser autosuficientes a nivel de administración de servidor, aunque existan PATH especializados más profundos. No convertir RHCSA en un curso de desarrollo interno de cada proyecto. Btrfs se enseña con profundidad administrativa como extensión Fedora/Linux+. Flatpak se incluye como extensión de gestión de software, sin confundirlo con RPM/DNF ni con el núcleo del servidor RHEL.

## Seguridad
Mantener SELinux enforcing salvo ejercicios explícitos de diagnóstico. No recomendar desactivar firewalls o controles de seguridad como solución permanente. Explicar el impacto de operaciones destructivas y exigir backup/snapshot en laboratorios de recuperación.

## Resultado final
El alumno debe poder instalar, configurar, actualizar, securizar, observar, automatizar, diagnosticar, recuperar y documentar un servidor RHEL 10; además debe estar preparado para practicar las competencias vigentes del EX200.

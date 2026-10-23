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
systemd, SELinux, firewalld, OpenSSH, RPM y containers deben ser autosuficientes a nivel de administración de servidor, aunque existan PATH especializados más profundos. Apache se practica como servicio de red de referencia, con VirtualHost, SELinux, firewalld, logs y validación; la administración web avanzada queda en el PATH especializado. No convertir RHCSA en un curso de desarrollo interno de cada proyecto. Btrfs se enseña con profundidad administrativa como extensión Fedora/Linux+. Flatpak incluye un núcleo de gestión de repositorios e instalación/eliminación de aplicaciones en RHEL etiquetado [EX200]. Sus ampliaciones de sandbox, portales y escritorio se distinguen del núcleo de examen y de RPM/DNF.

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


## Alcance EX200 contrastado — 2026-10-22
Fuente: https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam

El núcleo incluye gestión de Flatpak, VFAT/ext4/XFS, timers systemd, clientes de tiempo y perfiles de ajuste. Podman/Quadlet se mantienen como ampliación [RHEL+]: no figuran en la lista de competencias publicada consultada. Btrfs se mantiene como extensión Fedora/Linux+. No convertir automáticamente todos los detalles de una herramienta en objetivos del examen. Revalidar esta matriz antes de generar simulacros y antes de reservar el examen.

## Orden y prerrequisitos
Conservar los bloques 0–42 y sus identificadores. El bloque 1 proporciona un mínimo guiado de conectividad, acceso SSH, transferencia y recuperación mediante consola; los bloques 24–25 desarrollan después su administración completa. Los ejemplos anteriores a esos bloques no deben exigir una configuración de red que aún no se haya explicado.

En Flatpak usar RHEL para el núcleo EX200; comprobar repositorios, credenciales y conectividad disponibles. Diferenciar instalación/gestión CLI de ejecución de aplicaciones gráficas, que requiere un entorno adecuado. Preparar el remoto antes de una práctica sin Internet; no inventar credenciales ni suponer acceso al catálogo.

## Criterios observables de evaluación
Para cada bloque generar un ejercicio guiado y otro sin pasos. En el segundo proporcionar estado inicial, requisitos, recursos, restricciones y resultados esperados. Solicitar evidencia mínima suficiente, y no una transcripción indiscriminada de comandos.

Criterios comunes: resultado funcional; configuración persistente cuando corresponda; explicación de la capa que controla el estado; diagnóstico basado en evidencias; recuperación o reversión segura. En ejercicios de consulta no exigir cambios, reinicio ni rollback artificiales. Para tareas destructivas usar discos y máquinas desechables identificados explícitamente.

| Bloque | Evidencia mínima del ejercicio sin pasos |
|---|---|
| 0 | Localizar documentación adecuada y justificar su uso |
| 1 | Dos nodos accesibles, consola de recuperación e inventario de versiones |
| 2 | Diagnosticar y corregir entorno de shell |
| 3 | Preservar datos y explicar rutas, enlaces y metadatos |
| 4 | Pipeline correcto con entradas difíciles y estado de salida comprobado |
| 5 | Configuración validada con diff y copia recuperable |
| 6 | Script con entradas válidas/erróneas y estados de salida observables |
| 7 | Inventario de dispositivos y nombres persistentes |
| 8 | Parámetro aplicado y persistente con reversión documentada |
| 9 | Cuentas y grupos comprobados con id/getent/chage |
| 10 | Explicar una decisión de PAM y recuperar acceso mediante consola |
| 11 | Acceso efectivo conforme a permisos, ACL y delegación sudo |
| 12 | Identificar proceso y justificar señal o prioridad |
| 13 | Servicio operativo y habilitado; apagado/reinicio ordenado |
| 14 | Arranque recuperado y parámetro del kernel verificado |
| 15 | Journal persistente y evento rastreable; rotación comprobada |
| 16 | Paquetes y repositorios verificables, incluida procedencia |
| 17 | Remoto y aplicación Flatpak gestionados en el ámbito solicitado |
| 18 | Particiones GPT verificadas sin alterar datos ajenos |
| 19 | VFAT/ext4/XFS montados y utilizados; fstab validado |
| 20 | Swap activa y persistente sin pérdida de datos |
| 21 | Capacidad ampliada y datos íntegros en las capas implicadas |
| 22 | Pool y filesystem Stratis verificables; límites documentados |
| 23 | Subvolúmenes y copias Btrfs verificables en Fedora |
| 24 | Direcciones IPv4/IPv6, rutas y resolución comprobadas |
| 25 | Acceso por clave y transferencia segura entre nodos |
| 26 | Acceso remoto efectivo acorde con reglas runtime y permanentes |
| 27 | Contextos, puertos y booleanos correctos con enforcing activo |
| 28 | Ejecución demostrada de at, cron y pareja service/timer |
| 29 | Cliente de tiempo sincronizado y locale comprobado |
| 30 | Restauración de datos y metadatos verificada |
| 31 | Montaje NFS y AutoFS comprobados desde el cliente |
| 32 | Contenedor rootless y Quadlet persistentes como RHEL+ |
| 33 | VirtualHost accesible con DNS, firewall y SELinux comprobados |
| 34 | Fallo de almacenamiento aislado y recuperación verificada |
| 35 | Perfil tuned verificado; diagnóstico de recursos con evidencias |
| 36 | Baseline de seguridad con acceso administrativo recuperable |
| 37 | Restauración con integridad y tiempos observados |
| 38 | Causa raíz respaldada por pruebas y validación posterior |
| 39 | Procedimiento repetible con prechecks, postchecks y reversión |
| 40 | Matriz de objetivos sin competencias publicadas sin cubrir |
| 41 | Simulacros separados de examen y administración ampliada |
| 42 | Entrega integral con inventario, pruebas, backups y runbook |

## Separación de evaluaciones
Los simulacros EX200 usan únicamente las competencias oficiales publicadas. Pueden usar servicios auxiliares como contexto de una tarea de SELinux, sin convertir su administración avanzada en competencia adicional del examen. Podman/Quadlet, Btrfs y demás ampliaciones tienen evaluación administrativa independiente. No presentar estas rúbricas como criterios oficiales de puntuación de Red Hat.

## Precisión operativa
Distinguir disco, partición, PV, VG, LV y filesystem antes de redimensionar. Practicar primero crecimiento no destructivo y comprobar datos; explicar por separado restricciones de reducción. No proponer reducir XFS en RHEL 10. No tratar mount -a como validación exhaustiva de fstab: combinar inspección, findmnt --verify, montajes y prueba de arranque en laboratorio.

Este PATH define contenidos y criterios de práctica. No implica que existan todavía scripts ejecutables, imágenes de VM o laboratorios probados automáticamente. La integración con el generador y los ejercicios deben validarse en su entorno real.

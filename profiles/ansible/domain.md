# DOMAIN --- ANSIBLE DE CERO A EXPERTO

## Alcance

Curso integral de Ansible con Fedora/RHEL como plataforma de sistemas.
No incluye administración de Windows. Cubre ansible-core, automatización
RHEL, networking, Podman/Buildah/Skopeo, Kubernetes/OpenShift, cloud,
IaC, CI/CD, testing, AWX, Red Hat Ansible Automation Platform, Execution
Environments, Event-Driven Ansible, desarrollo de módulos/plugins,
internals, seguridad, escala, gobernanza y arquitectura.

## Hito RHCE / Ansible

El bloque 16 es un checkpoint explícito. Todo lo anterior construye las
competencias de Ansible y administración automatizada de RHEL necesarias
para alcanzar ese nivel. No convierte el curso en una preparación
limitada al examen: desde el bloque 17 el recorrido continúa mucho más
allá de RHCE hacia Ansible/AAP profesional y arquitectura empresarial.

## Plataforma

Control node y managed Linux nodes: Fedora/RHEL. Windows queda fuera de
alcance. Las áreas de red usan las collections y transportes apropiados.
Containers se centra en Podman, Buildah, Skopeo y OCI. Orquestación
cubre Kubernetes/OpenShift. Enterprise cubre AWX/AAP.

## Estructura pedagógica

Cada lección comienza con `🎯 OBJETIVO`, desarrolla el tema con
profundidad y enfoque práctico, incluye `🧪 Laboratorio/ejemplos`,
`⚠️ Errores frecuentes` y `💡 Idea importante` cuando aporten valor, y
termina con `🧠 QUÉ DEBES RECORDAR` con 3--7 ideas esenciales.

## Profundidad

No producir simples resúmenes. Explicar qué hace cada mecanismo, cómo
funciona, cómo se configura, cómo se valida, cómo falla, cómo se
diagnostica y sus implicaciones de seguridad, mantenibilidad,
idempotencia, reproducibilidad y escala.

## Resultado

El alumno debe poder diseñar, implementar, probar, securizar, operar,
diagnosticar y gobernar una plataforma Ansible/AAP profesional.


## Contrato de profundidad reforzado

Las lecciones técnicas deben explicar prerrequisitos, mecanismo interno, sintaxis y parámetros, configuración, ejecución, validación, fallos habituales, diagnóstico, seguridad, idempotencia y mantenimiento. No sustituir estos apartados por enumeraciones superficiales. En cada laboratorio especificar plataforma, versiones, inventario, archivos, comandos, resultados esperados, verificación, repetición idempotente y limpieza o reversión.

Los contenidos puramente conceptuales pueden reemplazar el laboratorio por un análisis guiado, una comparación verificable o un experimento reproducible. No inventar resultados de ejecución. Distinguir explícitamente comportamiento demostrado, documentación y supuestos.

## Alcance y especialización

El PATH enseña cómo automatizar sistemas Fedora/RHEL, redes, containers, Kubernetes/OpenShift y proveedores cloud mediante Ansible; no reemplaza los PATH independientes de cada tecnología. Mantener Windows excluido. Explicar regex solo como aplicación de filtros de Ansible, no como curso de teoría regex.

## Hito RHCE y evaluación

El bloque 16 es un hito pedagógico, no una garantía de aprobar una certificación. Contrastarlo con los objetivos oficiales vigentes para la versión del examen. Incorporar simulacros de configuración y troubleshooting, criterios de aceptación, evidencias y pruebas de idempotencia.

## Laboratorios avanzados y proyecto final

En AWX/AAP, redes, EDA, EE y cloud exigir, cuando sea viable, instalación o preparación, configuración, validación, diagnóstico y recuperación. Si una tecnología requiere licencias o recursos externos, proporcionar alternativa de laboratorio y declarar limitaciones. El proyecto final debe incluir pruebas de aceptación automatizadas, matriz de compatibilidad, recuperación de fallos y documentación de evidencias.


## Secuencia de prerrequisitos y revisitas

Antes del hito 16, enseñar el consumo de un Execution Environment ya construido
con Podman y ansible-navigator. No exigir construir imágenes ni instalar AAP
para ese hito. El bloque 28 profundiza en construcción, dependencias, firma,
distribución y diagnóstico. El bloque 24 consume un EE fijado para ejecutar CI.

Cuando un mecanismo se revisita, conservar su contenido y aumentar la exigencia:
fundamento, semántica, experimento, diagnóstico y diseño a escala. Diferenciar
expresamente las revisitas de run_once/serial, regex, argument_specs, drift y
trazas internas; no generar dos lecciones con el mismo objetivo y laboratorio.

## Plataforma de referencia y contrato de reproducibilidad

Referencia comunitaria propuesta a fecha 2026-10-19, pendiente de validación
integral en laboratorio: Fedora 43, Python 3.14 en el controlador y
ansible-core 2.20.10. Nodos: Fedora 43 con Python 3.14 y RHEL 9 con Python 3.9.
La matriz oficial de la rama 2.20 contempla Python 3.12–3.14 en control y
3.9–3.14 en nodos. Esto no demuestra compatibilidad de todas las collections.
No modificar el Python del sistema para satisfacer las dependencias de control.

Antes de generar comandos de un laboratorio, resolver y guardar las versiones
exactas de collections, ansible-navigator, ansible-builder, ansible-runner,
Molecule, ansible-lint y sus dependencias. Registrar los RPM/imagen de SO,
intérpretes efectivos, requirements.yml con versiones exactas, lock de Python,
digest de imágenes OCI y comandos de inspección. La resolución no equivale a
una prueba de ejecución. Si no se ha ejecutado, marcarlo como pendiente.

La rama 2.20 es una referencia fijada, no una afirmación de que sea la última.
Al cambiarla, revisar mantenimiento, porting guides, intérpretes y collections,
actualizar todos los locks y ejecutar regresiones. Los laboratorios de
migración pueden usar una matriz adicional aislada de versiones anteriores.

La variante RHCE/AAP debe fijar por separado la versión de examen, RHEL,
Navigator y EE indicados por Red Hat. No trasladar automáticamente la matriz
comunitaria a un entorno soportado de AAP. Registrar AAP y sus componentes,
la topología y el método de instalación antes de dar instrucciones operativas.

## Contrato de laboratorio y límites de ejecución

Definir recursos mínimos medidos o estimados para cada escenario y distinguirlos.
Usar máquinas virtuales cuando la prueba necesite boot, kernel, almacenamiento,
SELinux o NetworkManager reales. Una prueba en contenedor no sustituye estas
evidencias. Aislar los laboratorios de red y documentar snapshots y recuperación.

Explicar dónde se ejecutan lookups, action plugins y módulos, y qué cambia con
delegate_to, conexión local y EE. Probar bootstrap sin Python mediante raw.
No presentar check mode como simulación completa ni diff como verificación
funcional: dependen del módulo, pueden omitir tareas y exponer información.

Ansible no ofrece una transacción global ni rollback automático general.
Diseñar compensaciones, backups, validación previa y restauración comprobada;
mostrar límites de block/rescue y fallos de conectividad. sudo sin contraseña
interactiva es una opción del laboratorio, no una obligación de producción.

## Templating y compatibilidad moderna

Desarrollar los cambios desde ansible-core 2.19: tipos nativos, data tagging,
confianza de plantillas y condiciones booleanas. Contrastar ejemplos con la
guía de migración de la versión objetivo. No convertir datos externos en
plantillas confiables indiscriminadamente. Crear casos negativos y regresiones
para undefined, None, tipos, coerciones y evaluación de contenido externo.

## Evidencia mínima del proyecto final

Implementar una integración real de secretos con un servicio de laboratorio;
demostrar permisos, rotación y revocación. Distribuir e instalar una collection
desde Private Hub o una alternativa Galaxy compatible, identificando diferencias
de soporte y capacidades. Generar un SBOM real del EE. Las licencias pueden
limitar la topología empresarial, pero no justifican sustituir estas pruebas
por una explicación conceptual. Declarar por separado componentes ejecutados,
diseñados y pendientes. Conservar evidencias sin credenciales ni datos sensibles.

## Dependencias del generador

Mantener la referencia compartida ../../config/pedagogy.md del perfil.
Comprobarla desde la ubicación final del repositorio: no forma parte de estos
cuatro archivos. Las claves del perfil expresan el contrato pedagógico; su
interpretación efectiva debe comprobarse en el cargador de course-generator.
No afirmar validación del generador si no se dispone de su código y configuración.

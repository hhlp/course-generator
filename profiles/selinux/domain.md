# Domain — SELinux en profundidad

## Dominio

Administración, diagnóstico, investigación, arquitectura e internals
de SELinux sobre Fedora Linux.


## Plataforma principal

Fedora Linux


## Alcance

Este PATH estudia SELinux como subsistema completo de seguridad Linux.

No está orientado exclusivamente a:

- servidores web
- bases de datos
- contenedores
- SSH
- servicios concretos

Los servicios pueden utilizarse como ejemplos, pero el conocimiento
debe ser generalizable.


## Objetivo general

Llevar al estudiante desde los fundamentos de control de acceso hasta
ser capaz de:

- administrar SELinux
- investigar políticas existentes
- localizar contexts
- comprender decisiones de acceso
- diagnosticar AVC denials
- comprender Type Enforcement
- trabajar con usuarios y roles SELinux
- comprender MLS y MCS
- administrar labels
- administrar políticas
- analizar políticas
- crear modificaciones locales
- comprender módulos
- estudiar políticas Fedora
- comprender Reference Policy
- comprender CIL
- investigar internals de SELinux


## Ejes conceptuales

El PATH debe desarrollar progresivamente:

DAC
→ MAC
→ LSM
→ SELinux
→ security contexts
→ user:role:type:level
→ types
→ domains
→ attributes
→ object classes
→ permissions
→ Type Enforcement
→ transitions
→ RBAC
→ MLS
→ MCS
→ booleans
→ labeling
→ policy
→ modules
→ auditing
→ troubleshooting
→ policy analysis
→ policy development
→ CIL
→ Reference Policy
→ internals


## Orientación Fedora

Todos los ejemplos prácticos deben asumir Fedora cuando sea posible.

Priorizar:

dnf
rpm
systemd
journalctl
auditd
ausearch
semanage
restorecon
matchpathcon
seinfo
sesearch
sepolicy
semodule

No asumir estructuras específicas de otras distribuciones cuando
Fedora utilice una diferente.


## Descubrimiento frente a memorización

Una prioridad fundamental del PATH es enseñar a descubrir la
configuración existente.

El estudiante debe aprender a responder preguntas como:

¿Qué context tiene este archivo?

¿Qué context debería tener?

¿Qué type utiliza este proceso?

¿En qué domain está ejecutándose?

¿Qué types existen?

¿Qué domains existen?

¿Qué attributes existen?

¿Qué roles existen?

¿Qué SELinux users existen?

¿Qué object classes existen?

¿Qué permissions existen?

¿Qué booleans existen?

¿Qué ports administra SELinux?

¿Qué módulos están instalados?

¿Qué regla permite este acceso?

¿Qué permiso falta o qué restricción explica la denegación?

¿Qué transición ocurre?

¿Dónde se define un file context?

¿Dónde está definida una interface?

¿Qué paquete proporciona esta política?


## Investigación de políticas

No enseñar únicamente comandos aislados.

Relacionar herramientas:

ps -eZ
ls -Z
id -Z

con:

semanage
seinfo
sesearch
sepolicy
semodule
matchpathcon
restorecon

y finalmente con:

policy source
Fedora policy
Reference Policy
CIL


## Troubleshooting

Nunca enseñar:

"SELinux bloquea algo → desactivar SELinux"

El flujo correcto debe ser aproximadamente:

observar
→ reproducir
→ identificar AVC
→ ausearch
→ interpretar source context
→ interpretar target context
→ class
→ permission
→ investigar política
→ comprobar labels
→ comprobar booleans
→ comprobar configuración
→ buscar reglas existentes
→ corregir causa
→ modificar política únicamente cuando sea necesario
→ verificar


## audit2allow

audit2allow no debe presentarse como solución automática.

Debe enseñarse como herramienta de análisis y generación asistida.

Antes de aceptar una regla deben analizarse:

- labels
- configuración
- booleans
- política existente
- interfaces disponibles
- impacto de seguridad


## Política

Distinguir claramente:

kernel policy
binary policy
policy store
policy modules
Reference Policy
Fedora policy
CIL
local policy modifications


## Internals

En bloques avanzados desarrollar:

Linux Security Modules
SELinux hooks
security server
Access Vector Cache
SID
security contexts
object managers
policy loading
policy database
libselinux
libsepol
libsemanage
policycoreutils
checkpolicy
secilc


## Laboratorios

Los laboratorios deben priorizar inspección real del sistema.

Ejemplos:

- investigar contexts
- modificar labels temporalmente
- restaurar labels
- consultar file-context database
- investigar processes/domains
- analizar AVC
- consultar reglas con sesearch
- inspeccionar policy con seinfo
- analizar booleans
- investigar ports
- inspeccionar módulos
- comparar configuración persistente y runtime
- construir módulos locales
- estudiar source policy


## Seguridad

No recomendar desactivar SELinux como mecanismo normal de resolución
de problemas.

Permissive puede utilizarse controladamente como herramienta
diagnóstica cuando sea pedagógicamente apropiado.


## Profundidad

Las lecciones no deben convertirse en resúmenes.

Cada concepto debe explicar:

qué es
por qué existe
cómo funciona
cómo observarlo
cómo administrarlo
cómo investigarlo
cómo diagnosticarlo
cómo se relaciona con el resto de SELinux


## Resultado final

Al terminar el PATH, el estudiante debe poder enfrentarse a una
máquina Fedora desconocida con SELinux habilitado y determinar
sistemáticamente:

- qué política está activa
- qué contexts existen
- cómo están etiquetados los recursos
- qué dominios están ejecutándose
- qué reglas gobiernan un acceso
- por qué un acceso fue permitido o denegado
- dónde está definida la política relevante
- cómo modificar correctamente el comportamiento
- cómo verificar que la solución es segura y persistente

## Extensión de nivel experto

Los bloques 27–31 profundizan en CIL, constraints, pruebas de regresión, automatización declarativa e ingeniería inversa. El proyecto final se desplaza al bloque 32 sin perder sus objetivos originales.

## Criterios obligatorios de profundidad

Cada lección debe incluir una explicación conceptual, mecanismos internos pertinentes, comandos reales de Fedora, interpretación de salidas, diagnóstico, riesgos, reversión y conexiones con otros bloques. No repetir fundamentos cuando se profundice en un tema: referenciar su lección previa.

## Pruebas y evidencias

Los laboratorios de políticas deben definir estado inicial, permisos esperados y prohibidos, pasos reproducibles, comprobaciones positivas y negativas, evidencias AVC cuando existan y limpieza/rollback. Las operaciones potencialmente disruptivas se realizarán en VM desechable o snapshot.

## Semántica de las decisiones

No equiparar ausencia de AVC con acceso permitido. Diferenciar permisos DAC, decisiones TE, restricciones RBAC/MLS, constraints, ramas condicionales y efectos de dontaudit. Distinguir evidencia observada, consulta estática e inferencia.

## Precisión de plataforma

No asumir rutas internas inmutables del policy store ni disponibilidad de paquetes, herramientas o políticas históricas. Comprobar en la versión Fedora del laboratorio y documentar alternativas.

## Proyecto final ampliado

El selinux-debugger debe producir explicaciones trazables, distinguir hechos de hipótesis, incorporar pruebas automatizadas, mostrar relaciones en DOT/JSON y permitir comparar estado runtime, personalizaciones locales y política instalada.

## Unidades de enseñanza y subapartados

Los identificadores x.y definen unidades del temario. Si una entrada enumera
únicamente un campo, una opción o una variante del mismo comando, desarrollarla
como subapartado de la unidad conceptual correspondiente, sin fabricar una
lección independiente. Las entradas x.y.z son subapartados de x.y. Conservar
la cobertura y profundidad; indicar los identificadores cubiertos por cada
lección y enlazar los prerrequisitos. El bloque 14 agrupa los campos AVC como
subapartados de su interpretación.

## Preparación temprana y progresión

Preparar VM, snapshot, consola de recuperación, paquetes y versiones en el
bloque 1. El bloque 26 reutiliza esa base y formaliza requisitos, evidencias
y pruebas del proyecto experto. Cada bloque avanzado añade mecanismos,
consultas o experimentos nuevos sobre los conocimientos anteriores.

## Límites técnicos obligatorios

- neverallow es una aserción de compilación; estudiarla en fuentes/CIL.
  No prometer recuperarla mediante sesearch desde la política binaria cargada.
- Diferenciar sintaxis TE de CIL, incluyendo type_transition frente a
  typetransition, type_change frente a typechange y type_member frente a
  typemember.
- Descubrir store-root en semanage.conf; /var/lib/selinux es el valor
  predeterminado documentado. No editar manualmente el almacén como flujo normal.
- Correlacionar una regla con módulos de origen requiere evidencia adicional,
  como fuentes o CIL; admitir orígenes múltiples o no determinados.
- Una consulta allow aislada no demuestra que una operación real tendrá éxito.
  Registrar política, contextos, condiciones y límites del análisis.

## Contrato de resultados del proyecto final

El debugger debe distinguir confirmado, inferido e inconcluso. Cada conclusión
incluye evidencia, procedencia, versiones y estado consultado. Cuando no pueda
determinar la causa, debe explicar qué información falta y qué comprobación
permitiría avanzar. La ausencia de una regla encontrada o de un AVC no basta
para declarar política faltante. Separar decisiones SELinux de otros controles
que puedan impedir la operación y verificar las hipótesis con pruebas reales.

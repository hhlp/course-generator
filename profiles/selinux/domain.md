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

¿Qué regla impide este acceso?

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

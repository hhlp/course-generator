# Dominio — OpenTofu

## Propósito y plataforma

Learning path autónomo de cero a experto sobre OpenTofu, en español. Comienza
con IaC y HCL y culmina en operación, migración y recuperación. Saber Terraform
es opcional. La comparación remite al bloque 21 de Terraform para quien ya
siga ese itinerario. El bloque 14 de OpenTofu desarrolla el procedimiento de
migración con pruebas y decisiones operativas.

Plataforma principal Fedora/RHEL y Linux. Usar Bash para automatización y
mostrar Zsh cuando afecte al uso interactivo, las comillas o el autocompletado.
El primer laboratorio usa `terraform_data` en un directorio desechable. La
práctica avanzada usa KVM/libvirt, cloud-init y Ansible. Los ejemplos cloud
pueden aportar contexto. Las pruebas con KMS o servicios externos usan
recursos y credenciales aislados, con un equivalente local cuando sea posible.

Usar la serie OpenTofu 1.13 como referencia curricular y fijar un parche
exacto en cada laboratorio. Registrar versión real de Core y providers,
plataforma, backend y fecha de verificación. Confirmar disponibilidad en
la documentación de la versión y con la ayuda del binario seleccionado.
Distinguir capacidad de Core, esquema del provider, API y backend.

## Progresión

| Bloques | Práctica principal | Evidencia |
| --- | --- | --- |
| 0–4 | Primer recurso, CLI diaria, HCL y grafo | Plan inicial y segundo plan vacío |
| 5–7 | Providers, módulos y operación de planes | Lock revisado, módulo versionado y diagnóstico |
| 8–10 | Adopción, state remoto y cifrado | Refactor, contención de lock, rotación y restauración |
| 11–12 | Pruebas y automatización | Suite selectiva, códigos de salida y plan aprobado |
| 13 | Fedora/RHEL, libvirt, cloud-init y Ansible | VMs accesibles, inventario y roles idempotentes |
| 14–16 | Migración, escala e incidentes | Matriz, rollback ensayado y RPO/RTO medidos |
| 17–18 | Internals y plataforma experta | Diagnóstico reproducible y defensa del diseño |

Cada lección X.1 presenta alcance, conocimientos previos, prácticas, evidencia
y relación con los bloques siguientes. En el bloque 1 practicar de inmediato
el workflow local. Repetir providers en el bloque 5, state en el 8, backend en
el 9, test en el 11 y automatización en el 12 con escenarios más exigentes.

Cada lección comienza con 🎯 OBJETIVO, identifica 📚 LECTURA y termina con
🧠 QUÉ DEBES RECORDAR, con 3–7 puntos. Incluir práctica reproducible, resultados
esperados, errores frecuentes y una idea importante según el perfil. En comandos
indicar directorio, contexto, entradas, efecto sobre state, salida y recuperación.
Diferenciar una ejecución interactiva de un pipeline.

## Contratos técnicos

- CLI. Usar `tofu` como comando principal. Las variables documentadas `TF_*`
  conservan ese prefijo. Diferenciar el JSON de eventos de `plan -json` del
  documento `show -json`. En Bash gestionar explícitamente 0, 1 y 2 para
  `plan -detailed-exitcode`. Validar comandos históricos y sus sustitutos.
- Lenguaje. Probar precedencia por nombre base entre .tf y .tofu. Enseñar las
  restricciones de evaluación temprana con un ejemplo válido y un fallo.
  Ejercitar la retirada en fases de instancias dinámicas de provider.
- Suministro. Fijar el origen completo de plugins y verificar checksums, lock
  file y plataforma. Distinguir caché, mirror y Registry de origen. Aislar
  credenciales y datos de trabajo por runner. Mostrar OCI según versión.
- State. Demostrar direccionamiento, drift, importación y refactor en copias
  o entornos de prueba. Examinar lineage y serial antes de restaurar. Verificar
  escritores antes de force-unlock. Documentar operaciones que mutan el state.
- Backend. Verificar explícitamente soporte y semántica de locking para el
  backend y versión usados. Probar contención desde dos runners. Distinguir
  migrar state y reconfigurar el cliente. Separar roots, credenciales y claves
  cuando se necesite aislamiento entre entornos.
- Cifrado. Distinguir state, planes, clave y credenciales. Tratar como sensibles
  también las exportaciones JSON y los logs. Verificar migración, fallback
  temporal, rotación, retirada de claves y restauración. Los mecanismos de
  respaldo deben preservar acceso al material de clave según la práctica.
- CI. Fijar binario y dependencias. Mantener una sola línea de escritores
  autorizados por state. Revisar el plan guardado y limitar acceso y retención.
  Si el plan caduca o cambia su contexto, generar y revisar otro.
- Migración. Inventariar pares de versiones, providers, direcciones, lock,
  backend, dependencias entre roots y capacidades divergentes. Comparar planes
  con copias aisladas. Registrar condiciones de reversión y reconciliar cambios
  reales ocurridos después del backup antes de restaurar el state.
- Recuperación. El respaldo de state y el de datos de aplicación cubren fallos
  diferentes. Medir ambos en el simulacro. Conservar evidencias sin secretos.
- Capacidades experimentales. Usar ejemplos optativos y documentar versión
  y estatus. El tronco y la rúbrica experta se basan en capacidades estables.

## Validación y cierre

Ejecutar formato, inicialización sin backend y validación en cada root
confiable. Para módulos hijos usar un root de prueba con sus aliases e
inputs. Si la configuración requiere entradas durante init, suministrarlas
al ejecutar las comprobaciones que las necesiten. fmt y validate cubren
formato y consistencia estática. Plan y test amplían la evidencia con
fixtures, permisos y alcance de laboratorio explícitos.

La entrega 18.9 integra dos raíces, módulos reutilizables, máquinas virtuales,
Ansible, backend privado, locking, cifrado, pruebas y pipeline. Incluye un
ensayo de migración y runbooks de recuperación. En 18.10 demostrar un segundo
plan sin cambios, recuperación de state y datos por separado, evidencia de
RPO/RTO y explicación de las condiciones de compatibilidad.

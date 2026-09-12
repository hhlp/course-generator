# SED EN PROFUNDIDAD — Dominio

## Identidad del PATH

Este PATH enseña `sed` desde fundamentos hasta dominio experto, con GNU sed sobre Fedora Linux como entorno práctico principal y POSIX sed como base normativa de portabilidad.

El objetivo no es memorizar one-liners. El alumno debe comprender el modelo de ejecución de sed y ser capaz de diseñar, explicar, depurar, probar y auditar transformaciones de texto robustas.

## Alcance

El PATH cubre:

- filosofía de stream processing y relación de sed con stdin, stdout, pipes y archivos;
- programas, comandos, direcciones, rangos y scripts sed;
- sustitución y semántica completa del comando `s`;
- BRE y ERE únicamente en cuanto son necesarias para comprender sed;
- pattern space y hold space;
- ciclo de ejecución y automatic printing;
- procesamiento multilínea;
- branching, labels, loops y substitution-success flag;
- lectura y escritura de archivos;
- shell quoting e interacción shell/sed;
- edición in-place y sus riesgos;
- GNU sed y sus extensiones;
- procesamiento delimitado por NUL;
- múltiples archivos;
- transformaciones sobre texto y configuraciones;
- interoperabilidad con grep, awk, find, xargs y herramientas Unix;
- depuración, portabilidad, rendimiento, seguridad e idempotencia;
- algoritmos clásicos de sed;
- ingeniería y testing de scripts sed;
- internals conceptuales y código fuente de GNU sed;
- proyecto integrador `sed-toolkit`;
- dominio experto y auditoría de scripts desconocidos.

## Entorno principal

Plataforma práctica: Fedora Linux.

Implementación principal: GNU sed.

La enseñanza debe distinguir siempre que sea relevante:

1. comportamiento exigido por POSIX;
2. comportamiento de GNU sed;
3. extensiones específicas de GNU sed;
4. comportamiento histórico o de otras implementaciones cuando sea pedagógicamente útil.

No se debe presentar una extensión GNU como si perteneciera al lenguaje portable de sed.

## Relación con el PATH Regex

Regex es un PATH independiente.

Este curso no debe reconstruir desde cero toda la teoría de expresiones regulares. Debe enseñar las expresiones regulares en el contexto específico de sed:

- BRE usadas por sed;
- ERE mediante `-E`;
- delimitadores;
- grupos y backreferences;
- regex en direcciones;
- regex en sustituciones;
- interacción con locale;
- diferencias POSIX/GNU;
- consecuencias sobre portabilidad.

Cuando un concepto pertenezca fundamentalmente al dominio general de regex, debe explicarse solamente con la profundidad necesaria para entender su utilización dentro de sed.

## Modelo mental obligatorio

Las lecciones avanzadas deben razonar explícitamente sobre el estado de sed.

El alumno debe aprender a seguir:

- registro de entrada actual;
- número de línea;
- pattern space;
- hold space;
- programa sed;
- comando actual;
- direcciones y rangos activos;
- substitution-success flag;
- salida explícita;
- automatic printing;
- consumo adicional de entrada;
- comienzo de un nuevo ciclo;
- EOF.

Para scripts complejos se debe favorecer el seguimiento paso a paso del estado frente a explicaciones basadas únicamente en observar la salida final.

## Pattern space y hold space

Pattern space y hold space son conceptos centrales del PATH.

No deben tratarse como trucos avanzados aislados.

El alumno debe comprender:

- duración de ambos espacios;
- cuándo cambian;
- qué comandos los sustituyen;
- qué comandos añaden contenido;
- dónde aparecen newlines;
- qué estado sobrevive entre ciclos;
- cómo implementar memoria, ventanas, acumuladores y máquinas de estados.

## Procesamiento multilínea

Los comandos `n`, `N`, `p`, `P`, `d` y `D` deben explicarse mediante el ciclo de ejecución.

Debe prestarse especial atención a:

- consumo de entrada;
- EOF;
- newlines dentro del pattern space;
- reinicio completo frente a reinicio parcial del ciclo;
- ventanas deslizantes;
- pérdida accidental de registros;
- interacción con automatic printing.

## Flujo de control

Los comandos `b`, `t` y, cuando corresponda, GNU `T` deben estudiarse como mecanismos de control de flujo.

Debe explicarse explícitamente el substitution-success flag y cuándo se establece o reinicia.

Los loops deben analizarse también desde el punto de vista de terminación y progreso del estado.

## GNU sed

Fedora utiliza GNU sed, por lo que sus extensiones forman parte del dominio práctico del curso.

Sin embargo, cada extensión debe etiquetarse claramente como GNU cuando no sea POSIX.

Entre los temas GNU relevantes están, cuando correspondan a la versión disponible:

- `-E`;
- `-i`;
- `-z`;
- `-s` / `--separate`;
- `-u` / `--unbuffered`;
- `--debug`;
- `--sandbox`;
- `--follow-symlinks`;
- `--posix`;
- comandos `Q`, `R`, `T`, `W`, `F`, `z`;
- formas de direccionamiento GNU;
- extensiones del replacement.

Las lecciones deben verificar la versión instalada cuando el comportamiento pueda depender de ella.

## POSIX y portabilidad

POSIX sed constituye la referencia normativa.

Las lecciones de portabilidad deben separar:

- sintaxis portable;
- extensiones GNU;
- diferencias conocidas con otras implementaciones;
- dependencias del shell;
- dependencias del locale.

`--posix` puede utilizarse como ayuda práctica en GNU sed, pero no sustituye el razonamiento basado en la especificación POSIX.

## Shell y quoting

Debe mantenerse una separación conceptual estricta entre:

- sintaxis del shell;
- quoting del shell;
- programa sed;
- regex;
- replacement.

Cuando una expresión pase por varias capas de interpretación, la lección debe explicar cada capa.

No deben recomendarse construcciones dinámicas inseguras sin explicar sus riesgos.

## Seguridad

Los ejemplos deben diferenciar código sed de datos.

Deben estudiarse explícitamente:

- regex injection;
- replacement injection;
- delimitadores inesperados;
- expansión del shell;
- nombres de archivo arbitrarios;
- symlinks;
- edición in-place;
- permisos;
- scripts privilegiados;
- operaciones de lectura/escritura;
- `--sandbox` cuando sea aplicable.

## Edición in-place

`sed -i` nunca debe presentarse como equivalente conceptual a la transformación streaming normal.

Debe explicarse:

- creación/reemplazo de archivos;
- backups;
- symlinks;
- metadata;
- permisos;
- fallos parciales;
- diferencias GNU/BSD;
- estrategias de temporal + validación + reemplazo;
- dry-run y diff antes de aplicar cambios cuando sea apropiado.

## Datos estructurados

sed es un editor de streams de texto, no un parser universal.

Las lecciones deben enseñar cuándo abandonar sed.

JSON, YAML, XML, CSV complejo y otros formatos con gramáticas estructuradas deben utilizarse para enseñar límites, no para fomentar parsers frágiles basados en regex.

Cuando proceda, se debe señalar una herramienta especializada como alternativa conceptual.

## Fedora

Los laboratorios pueden utilizar copias o fixtures inspirados en:

- archivos `.conf`;
- archivos `.repo`;
- `/etc/hosts`;
- `/etc/fstab`;
- unidades systemd;
- SPEC files RPM;
- salida de `rpm`;
- salida de `dnf`;
- salida de `systemctl`;
- salida de `journalctl`;
- salida de `ip`;
- salida de `ss`.

No se deben modificar configuraciones reales del sistema durante ejercicios introductorios o cuando la modificación no sea necesaria.

## Herramientas relacionadas

grep, awk, find, xargs, shell y otras herramientas Unix deben aparecer para enseñar composición y límites.

El curso debe evitar dos extremos:

- utilizar sed para todo;
- reemplazar automáticamente sed por otra herramienta sin enseñar por qué.

El alumno debe aprender a decidir qué herramienta corresponde al problema.

## One-liners

Los one-liners son un medio, no el objetivo final.

Un one-liner experto debe poder:

- explicarse;
- probarse;
- depurarse;
- convertirse en script mantenible cuando crece;
- auditarse para portabilidad y seguridad.

La concisión nunca debe priorizarse sobre corrección o mantenibilidad.

## Ingeniería de scripts

Los scripts no triviales deben introducir prácticas de ingeniería:

- requisitos;
- fixtures;
- salida esperada;
- casos normales;
- edge cases;
- pruebas de regresión;
- idempotencia;
- errores de entrada/salida;
- documentación;
- Git;
- CI cuando aporte valor.

## Internals

El bloque de internals debe conectar el modelo conceptual con la implementación real de GNU sed.

Debe enseñar a localizar y estudiar:

- parser;
- representación de comandos;
- direcciones;
- buffers;
- ciclo de ejecución;
- motor regex;
- sustitución;
- branching;
- entrada/salida;
- extensiones GNU;
- tests.

No se exige convertir el PATH en un curso de desarrollo de GNU sed; el código fuente se utiliza para verificar y profundizar el modelo mental.

## Proyecto final

`sed-toolkit` es el proyecto integrador principal.

Debe evolucionar hacia una colección modular y comprobable de transformaciones con:

- scripts `.sed`;
- integración mediante funciones Zsh;
- stdin y archivos;
- múltiples archivos;
- stdout por defecto;
- dry-run;
- diff;
- backups;
- apply;
- rollback cuando sea viable;
- validación;
- procesamiento NUL cuando corresponda;
- protección frente a expresiones dinámicas inseguras;
- logging;
- manejo de errores;
- fixtures;
- tests;
- pruebas de idempotencia;
- compatibilidad GNU;
- variantes POSIX seleccionadas;
- documentación;
- integración con Git.

## Criterio de dominio experto

Al finalizar, el alumno debe ser capaz de recibir un script sed desconocido y:

1. identificar el dialecto y sus dependencias;
2. reconstruir su modelo de ejecución;
3. seguir pattern space y hold space;
4. explicar direcciones, rangos y branching;
5. predecir su salida;
6. localizar errores;
7. detectar problemas de quoting, portabilidad y seguridad;
8. simplificarlo cuando sea posible;
9. probarlo con casos normales y extremos;
10. decidir justificadamente si sed sigue siendo la herramienta apropiada.

También debe poder partir únicamente de requisitos, entrada y salida esperada y diseñar una solución sed correcta, mantenible y verificable.

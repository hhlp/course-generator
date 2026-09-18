# Domain — sed

## Identidad del curso

**Nombre:** sed — Learning Path 0 → Experto
**Plataforma principal:** Fedora
**Implementación principal:** GNU sed
**Shell de laboratorio:** Bash/Zsh
**Idioma:** Español

## Propósito

Este curso enseña `sed` desde cero hasta un dominio avanzado, tratándolo como un
lenguaje especializado para seleccionar, transformar y procesar streams de texto,
no simplemente como una colección de comandos de sustitución.

El alumno debe terminar siendo capaz de leer, explicar, depurar, diseñar y mantener
programas `sed`, comprendiendo su modelo interno de ejecución.

## Alcance

El dominio incluye:

- modelo Unix de stdin, stdout, pipes y streams;
- sintaxis y ciclo de ejecución de `sed`;
- impresión automática y `-n`;
- direcciones y rangos;
- comando `s`;
- BRE y ERE;
- backreferences;
- comandos de eliminación, inserción, adición y cambio;
- lectura y escritura;
- pattern space;
- hold space;
- procesamiento multilínea;
- `n`, `N`, `d`, `D`, `p`, `P`;
- `h`, `H`, `g`, `G`, `x`;
- labels;
- `b`, `t` y extensiones GNU relacionadas;
- loops y pequeñas máquinas de estados;
- scripts `.sed`;
- edición in-place;
- quoting e interacción con shell;
- GNU sed;
- POSIX sed;
- procesamiento NUL;
- múltiples archivos;
- integración con `grep`, `awk`, `find` y `xargs`;
- transformación de configuraciones y logs;
- debugging;
- seguridad;
- rendimiento;
- portabilidad;
- internals.

## Modelo mental obligatorio

El curso debe reforzar continuamente el siguiente modelo:

`entrada → pattern space → direcciones → comandos → hold space/estado → salida → siguiente ciclo`

Las explicaciones avanzadas no deben presentar `sed` como magia sintáctica. Cada
transformación compleja debe poder explicarse siguiendo el estado del pattern
space, hold space, flujo de control y ciclo de ejecución.

## Expresiones regulares

Las regex forman parte del curso solamente en el contexto necesario para dominar
`sed`.

Se estudiarán:

- BRE;
- ERE;
- anchors;
- clases POSIX;
- cuantificadores;
- agrupación;
- alternancia cuando corresponda;
- backreferences;
- escaping;
- interacción entre regex, shell quoting y `sed`.

El curso puede recordar fundamentos de regex, pero debe evitar convertirse en un
segundo learning path completo de expresiones regulares.

## GNU sed y POSIX

GNU sed será la implementación principal porque Fedora es la plataforma de
laboratorio.

Toda característica relevante debe clasificarse conceptualmente como:

- portable POSIX;
- extensión GNU;
- comportamiento cuya portabilidad requiere atención.

El alumno debe aprender tanto a aprovechar GNU sed como a reconocer cuándo una
solución deja de ser portable.

## Fedora

Los ejemplos reales pueden utilizar copias o fixtures inspirados en:

- archivos `.conf`;
- `/etc/hosts`;
- `/etc/fstab`;
- archivos `.repo`;
- unidades systemd;
- SPEC files RPM;
- salida de `rpm`;
- salida de `dnf`;
- salida de `systemctl`;
- salida de `journalctl`;
- herramientas de red.

Nunca debe requerirse modificar configuraciones críticas reales para completar un
laboratorio.

## Relación con otras herramientas

El curso debe enseñar las fronteras de responsabilidad:

**grep** → localizar/filtrar texto.
**sed** → seleccionar y transformar streams.
**awk** → procesamiento de registros y campos con lógica más estructurada.
**find** → localizar objetos del filesystem.
**xargs** → construir ejecuciones a partir de streams de argumentos.

También debe enseñarse cuándo una transformación debería pasar a Perl, Python,
`jq`, `yq` u otro parser especializado.

## Datos estructurados

No se debe enseñar `sed` como parser general de JSON, YAML, XML, HTML o CSV
complejo.

Estos formatos se utilizarán principalmente para demostrar los límites de una
herramienta basada en transformación textual y para aprender a seleccionar una
herramienta adecuada.

## Seguridad

Las lecciones avanzadas deben cubrir:

- edición destructiva;
- backups;
- symlinks;
- permisos;
- datos no confiables;
- regex injection;
- replacement injection;
- generación dinámica de programas sed;
- validación previa;
- dry-run;
- uso apropiado de `--sandbox`;
- principio de mínimo privilegio.

## Rendimiento

El alumno debe comprender:

- naturaleza streaming de `sed`;
- buffering;
- coste de regex;
- pattern spaces grandes;
- procesos innecesarios;
- pipelines;
- medición;
- relación entre rendimiento, claridad y mantenibilidad.

## Metodología

Cada concepto debe avanzar preferentemente mediante:

`concepto → sintaxis → ejemplo mínimo → ejemplo real → explicación del estado interno → laboratorio → errores frecuentes`

Las lecciones avanzadas deben incluir trazado manual del ciclo de ejecución cuando
sea útil.

## Proyecto final

El proyecto final será un `sed-toolkit` modular capaz de realizar transformaciones
reutilizables sobre fixtures de configuraciones y salidas de herramientas Fedora.

Debe incluir:

- scripts `.sed`;
- stdin y archivos;
- dry-run;
- diff previo;
- backups;
- validación;
- manejo de errores;
- tests;
- idempotencia;
- documentación;
- identificación explícita de dependencias GNU;
- variantes POSIX de operaciones seleccionadas.

## Criterio de dominio experto

Al finalizar, el alumno debe poder recibir una transformación desconocida y:

1. definir claramente entrada y salida;
2. decidir si `sed` es apropiado;
3. diseñar direcciones y regex;
4. decidir si necesita estado o procesamiento multilínea;
5. implementar la transformación;
6. explicar pattern space y hold space durante su ejecución;
7. depurarla;
8. probar edge cases;
9. evaluar seguridad y portabilidad;
10. simplificarla o migrarla a otra herramienta cuando `sed` deje de ser la opción adecuada.

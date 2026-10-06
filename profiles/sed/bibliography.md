# Bibliografía — sed de 0 a experto

## Libro principal

### Daniel A. Goldman — *Definitive Guide to sed: Tutorial and Reference*

Referencia bibliográfica principal del learning path.

Se utilizará especialmente para:

- fundamentos de `sed` y su modelo de procesamiento;
- comandos y direccionamiento;
- sustituciones y expresiones regulares;
- pattern space y hold space;
- procesamiento multilínea;
- labels, branching y loops;
- construcción y comprensión de scripts `sed`;
- técnicas avanzadas y resolución de problemas mediante transformaciones de streams.

El libro se utilizará como guía pedagógica, pero el PATH no quedará limitado a su
índice ni a una versión concreta de la implementación.

## Segunda referencia principal

### Dale Dougherty; Arnold Robbins — *sed & awk*

Referencia clásica para comprender `sed` dentro del ecosistema Unix de procesamiento
de texto y para establecer con precisión la frontera entre `sed` y `awk`.

Se utilizará especialmente para:

- fundamentos y filosofía Unix del procesamiento de texto;
- direccionamiento, comandos y scripts `sed`;
- pattern space, hold space y procesamiento multilínea;
- diseño de transformaciones y scripts no triviales;
- relación entre expresiones regulares, `sed` y `awk`;
- transición desde transformaciones orientadas a líneas hacia procesamiento por registros y campos;
- construcción de pipelines `grep` / `sed` / `awk`;
- criterios para decidir cuándo `awk` expresa una solución con mayor claridad que `sed`.

No convierte este PATH en un curso completo de `awk`: los capítulos y ejemplos de `awk`
se utilizarán para comparación, integración y delimitación de responsabilidades.

## Documentación oficial principal

### GNU sed manual

Referencia normativa práctica para la implementación utilizada principalmente en
Fedora: GNU sed.

Debe consultarse para:

- sintaxis actual;
- opciones de línea de comandos;
- comandos GNU;
- extensiones de GNU sed;
- `--debug`;
- `--sandbox`;
- `-z`;
- edición in-place;
- direcciones GNU;
- comportamiento de pattern space y hold space;
- diferencias respecto al modo POSIX.

## Estándar POSIX

### POSIX — `sed`

Referencia para distinguir el lenguaje portable de las extensiones específicas de
GNU sed.

Debe utilizarse especialmente en las lecciones de:

- BRE;
- comandos estándar;
- direccionamiento;
- comportamiento portable;
- scripts POSIX;
- comparación GNU sed / POSIX sed.

## Documentación del sistema

Como referencias complementarias durante los laboratorios:

- `man sed`
- `info sed`
- `sed --help`
- `sed --version`

## Política bibliográfica del curso

La prioridad será:

1. *Definitive Guide to sed: Tutorial and Reference* — Daniel A. Goldman, como referencia principal específica de `sed`.
2. *sed & awk* — Dale Dougherty y Arnold Robbins, como segunda referencia principal para el enfoque Unix, diseño de scripts e integración `sed`/`awk`.
3. GNU sed manual, como referencia técnica y normativa práctica de GNU sed.
4. POSIX `sed`, como referencia de portabilidad y comportamiento estándar.
5. Manuales instalados en Fedora para comprobaciones y laboratorios.

Cada lección debe terminar con referencias concretas relacionadas con el contenido
estudiado, evitando añadir bibliografía que no haya sido realmente utilizada.

# Dominio — OpenPGP, GnuPG y Sequoia PGP

## Propósito
Formación progresiva de cero a experto sobre el estándar OpenPGP, la operación de GnuPG y Sequoia PGP, y su aplicación en Fedora, correo, Git, cadena de suministro y software Rust.

## Alcance
- **Estándar:** criptografía aplicada, RFC 9580, compatibilidad RFC 4880, certificados, paquetes, firmas, cifrado, revocación y políticas.
- **GnuPG:** administración de claves, CLI, agentes, dirmngr, smartcards, integración con Fedora, diagnósticos y automatización.
- **Sequoia:** CLI sq, confianza/autenticación, certificados, políticas, interoperabilidad y desarrollo con sequoia-openpgp.
- **Aplicaciones:** correo PGP/MIME, Git, firmas de artefactos, RPM/DNF, pipelines, scripts, hardware tokens, respuesta a incidentes.

## Resultados verificables
1. Explicar la diferencia entre confidencialidad, firma criptográfica y autenticación de identidad.
2. Construir, certificar, publicar, revocar y restaurar identidades OpenPGP con separación de claves.
3. Ejecutar operaciones seguras en GnuPG y Sequoia y diagnosticar fallos con evidencias.
4. Probar interoperabilidad con una matriz de algoritmos, versiones de certificado y formatos.
5. Implementar una aplicación Rust que firme/verifique y cifre/descifre mediante Sequoia.
6. Integrar verificaciones en Git, Fedora/RPM y CI sin exponer secretos.
7. Diseñar políticas de gestión de claves y procedimientos de recuperación.

## Método didáctico
Cada lección desarrolla objetivo, prerequisitos, conceptos, arquitectura, comandos o API con explicación de opciones, laboratorio reproducible, validación, errores frecuentes, seguridad, troubleshooting y criterios de salida. Los laboratorios usan identidades ficticias, claves efímeras y entornos aislados. Se incluyen checkpoints y proyecto integrador.

## Restricciones y límites
- Fedora Linux como plataforma principal; no depender de servicios públicos ni claves reales para los ejercicios.
- No enseñar criptografía matemática exhaustiva ni repetir el path general de Rust, Bash, IAM o Regex: explicar lo necesario y enlazar conceptos.
- No confundir validación criptográfica con identidad autenticada.
- Distinguir los estándares OpenPGP, S/MIME, SSH y las firmas nativas de RPM.
- Tratar el soporte de RFC 9580, claves v6, AEAD, smartcards y comandos de sq como dependiente de versiones concretas.
- No recomendar algoritmos obsoletos ni prácticas inseguras salvo en ejercicios aislados de compatibilidad.

## Evaluación
Checkpoints por bloque, pruebas automatizadas de interoperabilidad, simulacro de revocación y restauración, auditoría de seguridad y defensa de proyecto final.

## Estructura
28 bloques numerados del 0 al 27. Lecciones N.x, ampliaciones N.x.y cuando se necesiten. `initial.txt` es la fuente de verdad del orden y de los títulos.

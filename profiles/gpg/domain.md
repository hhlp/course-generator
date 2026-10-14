# Dominio — OpenPGP, GnuPG y Sequoia PGP

## Propósito
Formación progresiva de cero a experto sobre OpenPGP (RFC 9580 y legado), operación avanzada de GnuPG y Sequoia PGP, desarrollo Rust con `sequoia-openpgp` e integración segura en Fedora, correo, Git, RPM y automatización.

## Alcance por scope

- **S1 Fundamentos:** criptografía aplicada, modelo de amenazas, privacidad y correo.
- **S2 Estándar:** certificados, paquetes, firmas, cifrado, v4/v6, AEAD, interoperabilidad y conformidad.
- **S3 GnuPG:** CLI, claves, subclaves, trust, gpg-agent, dirmngr, scdaemon, keyboxd, Assuan, backup y revocación.
- **S4 Sequoia CLI:** sq, certificados, autenticación, políticas, almacenes, scripting y troubleshooting.
- **S5 Sequoia Rust:** Cert, parsing, serialización, streams, cifrado, verificación, políticas, helpers, tests y fuzzing.
- **S6 Integraciones:** Fedora, PGP/MIME, Git, RPM/DNF, Ansible, CI/CD y systemd.
- **S7 Seguridad:** hardware tokens, hardening, incidentes, auditoría y pruebas adversariales.

## Resultados verificables

1. Distinguir firma criptográfica válida de autenticación de identidad y autorización.
2. Crear, certificar, publicar, renovar, revocar, respaldar y restaurar claves con primaria offline y subclaves operativas.
3. Administrar GnuPG, gpg-agent, dirmngr, keyboxd y scdaemon, incluyendo diagnóstico de sockets y políticas.
4. Automatizar gpg y sq de manera segura mediante resultados estructurados, códigos de salida y control de versiones.
5. Construir matrices reproducibles de interoperabilidad GnuPG/Sequoia, con casos positivos, negativos, v4/v6 y AEAD.
6. Desarrollar CLI Rust con `sequoia-openpgp` para firmar, verificar, cifrar y descifrar, con políticas y pruebas.
7. Operar hardware tokens con plan de pérdida, recuperación, rotación y revocación.
8. Integrar verificaciones en correo, Git, RPM, Ansible y CI sin filtrar secretos.
9. Interpretar paquetes OpenPGP y diagnosticar entradas malformadas sin exponer claves.
10. Defender un diseño experto con modelo de amenazas, evidencias, runbooks y auditoría final.

## Método didáctico

Cada lección: 🎯 objetivo, prerrequisitos, fundamentos, arquitectura, comandos y opciones o API explicados, 🧪 laboratorio reproducible, validación y resultados esperados, ⚠️ errores, seguridad y troubleshooting, 💡 ideas y 🧠 puntos para recordar. Cada sublección N.x.y desarrolla una competencia comprobable y no sustituye la lección N.x.

Los laboratorios emplean Fedora, identidades ficticias Alice/Bob/Carol, claves de prueba y entornos locales aislados. Las pruebas deben incluir casos negativos, incompatibilidades y fallos reproducibles.

## Restricciones y límites

- No depender de servicios públicos ni de claves o secretos reales.
- No duplicar cursos generales de Rust, Bash, IAM, Regex o RPM packaging; explicar solo integración OpenPGP.
- No tratar algoritmos obsoletos como opciones recomendadas; estudiar legado solo en laboratorio aislado.
- No equiparar verificación de firma con identidad autenticada o confianza.
- No asumir soporte de RFC 9580, claves v6, AEAD, tarjetas o sintaxis sq: registrar versiones y comprobar capacidades.
- No publicar secretos, passphrases ni plaintext en argumentos, logs, CI o archivos temporales.

## Evaluación

Checkpoints por bloque; pruebas de conformidad y compatibilidad; restauración y revocación; herramienta Rust funcional; CI verificable; simulacro de incidente; defensa técnica de proyecto final.

## Estructura y fuente de verdad

28 bloques numerados del 0 al 27. Se conserva cada lección N.x del original; las ampliaciones N.x.y se insertan bajo su lección padre. `initial.txt` determina orden y títulos. Bibliografía organizada por S1–S7.

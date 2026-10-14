# Bibliografía — OpenPGP, GnuPG y Sequoia PGP

## Política de fuentes

La obra de Michael W. Lucas aporta el enfoque práctico e histórico. RFC 9580 es la referencia normativa principal; la documentación de cada versión instalada determina la sintaxis y las capacidades reales. Ningún ejemplo de un libro antiguo se considera seguro por defecto.

## S1 — Fundamentos, criptografía aplicada y correo

- **Michael W. Lucas — PGP & GPG: Email for the Practical Paranoid.** No Starch Press. Obra principal práctica, contextualizada históricamente.
- **GNU Privacy Handbook.** https://www.gnupg.org/gph/en/manual.html — fundamentos y flujos tradicionales; contrastar prácticas antiguas.

## S2 — Normativa OpenPGP y formatos

- **RFC 9580 — OpenPGP.** https://www.rfc-editor.org/rfc/rfc9580.html — norma moderna.
- **RFC 4880 — OpenPGP Message Format.** https://www.rfc-editor.org/rfc/rfc4880.html — legado e interoperabilidad.
- **RFC 3156 — MIME Security with OpenPGP.** https://www.rfc-editor.org/rfc/rfc3156.html — PGP/MIME.
- **RFC 7929 — DANE Bindings for OpenPGP.** https://www.rfc-editor.org/rfc/rfc7929.html — registros OPENPGPKEY en DNS.
- **IANA — OpenPGP Parameters.** https://www.iana.org/assignments/pgp-parameters/pgp-parameters.xhtml — registros y algoritmos; verificar actualizaciones.

## S3 — GnuPG, agentes, CLI y ciclo de vida

- **GnuPG — Documentation.** https://www.gnupg.org/documentation/ — manuales gpg, gpgv, gpg-agent, gpgconf, dirmngr, scdaemon, gpg-connect-agent.
- **GnuPG — Manual de la versión instalada.** `gpg --version`, `gpg --help`, `man gpg`, `man gpg-agent`, `man gpgconf`; autoridad operativa local.

## S4 — Sequoia PGP, sq y autenticación

- **Sequoia PGP — Documentation.** https://sequoia-pgp.org/docs/ — arquitectura y herramientas.
- **Sequoia — sq User Guide.** https://book.sequoia-pgp.org/ — flujos CLI; validar con `sq --help`.

## S5 — Sequoia Rust API y testing

- **sequoia-openpgp — API Reference.** https://docs.rs/sequoia-openpgp/ — Cert, políticas, parsing, streams y helpers.
- **The Rust Programming Language.** https://doc.rust-lang.org/book/ — referencia transversal, sin duplicar el path Rust.
- **The Cargo Book.** https://doc.rust-lang.org/cargo/ — features, tests y builds.

## S6 — Fedora, RPM, Git y automatización

- **Fedora Documentation.** https://docs.fedoraproject.org/ — SELinux, sistema y herramientas.
- **RPM Project — Documentation.** https://rpm.org/documentation.html — firmas RPM y verificación.
- **Git Documentation.** https://git-scm.com/docs — firma y verificación de commits y tags.
- **GitHub Actions Documentation.** https://docs.github.com/en/actions — integración CI y permisos.
- **Ansible Documentation.** https://docs.ansible.com/ — distribución idempotente y validaciones.

## S7 — Hardware tokens, seguridad y conformidad

- **OpenPGP Card — especificación y documentación del proyecto.** https://www.g10code.com/p-card.html — protocolo de tarjeta; cotejar versión del dispositivo.
- **Yubico — OpenPGP.** https://developers.yubico.com/PGP/ — procedimientos de token; no asumir equivalencia entre modelos.
- **GnuPG y Sequoia — documentación de seguridad y notas de versión.** Referencia para compatibilidad, correcciones y políticas.

## Matriz de aplicación por bloques

| Bloques | Scopes principales |
|---|---|
| 0–3 | S1, S2 |
| 4–12 | S2, S3 |
| 13 | S3, S7 |
| 14 | S1, S2, S3 |
| 15–17 | S2, S4 |
| 18–19 | S2, S3, S4, S7 |
| 20 | S2, S5 |
| 21–23 | S3, S4, S6 |
| 24–27 | S2–S7 |

## Reglas de uso

1. Separar especificación, comportamiento de implementación y elección pedagógica.
2. Documentar versión, backend criptográfico y sistema operativo en cada laboratorio.
3. Verificar soporte de v6, AEAD, algoritmos, smartcards y comandos antes de ejecutar.
4. No confundir firmas OpenPGP, firmas Git, firmas nativas RPM, SSH y S/MIME.
5. No requerir servicios públicos ni claves reales para los laboratorios.

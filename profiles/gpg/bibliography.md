# Bibliografía — OpenPGP, GnuPG y Sequoia PGP

## Obra principal

1. Michael W. Lucas. **PGP & GPG: Email for the Practical Paranoid**. No Starch Press. Texto práctico de referencia; contrastar comandos y recomendaciones antiguas con las versiones actuales.

## Normativa esencial

2. IETF. **RFC 9580 — OpenPGP** (2024). https://www.rfc-editor.org/rfc/rfc9580.html — referencia normativa principal para OpenPGP moderno.
3. IETF. **RFC 4880 — OpenPGP Message Format** (2007). https://www.rfc-editor.org/rfc/rfc4880.html — lectura histórica para interoperabilidad y formatos heredados; RFC 9580 lo sustituye.
4. IETF. **RFC 3156 — MIME Security with OpenPGP**. https://www.rfc-editor.org/rfc/rfc3156.html — PGP/MIME.
5. IETF. **RFC 7929 — DNS-Based Authentication of Named Entities (DANE) Bindings for OpenPGP**. https://www.rfc-editor.org/rfc/rfc7929.html — OPENPGPKEY DNS.

## GnuPG y Linux

6. GnuPG Project. **Manual de GnuPG y documentación de componentes**. https://www.gnupg.org/documentation/ — gpg, gpgv, gpg-agent, gpgconf, dirmngr, gpgsm.
7. GnuPG Project. **The GNU Privacy Handbook**. https://www.gnupg.org/gph/en/manual.html — fundamentos prácticos, contextualizados históricamente.
8. Fedora Project. **Documentación de seguridad, RPM y DNF**. https://docs.fedoraproject.org/ — integración Linux y verificación de paquetes.
9. RPM Project. **Documentación oficial**. https://rpm.org/documentation.html — firmas y validación RPM.

## Sequoia PGP y Rust

10. Sequoia PGP. **Documentación oficial y guías de sq**. https://sequoia-pgp.org/docs/ — consultar por versión.
11. Sequoia PGP. **sq User Guide**. https://book.sequoia-pgp.org/ — flujos CLI, certificados y autenticación.
12. Sequoia PGP. **API de sequoia-openpgp**. https://docs.rs/sequoia-openpgp/ — bibliotecas Rust y ejemplos.
13. Rust Project. **The Rust Programming Language**. https://doc.rust-lang.org/book/ — consulta transversal para desarrollo con Sequoia.
14. Rust Project. **Cargo Book**. https://doc.rust-lang.org/cargo/ — dependencias, tests y builds.

## Uso de la bibliografía

- Prioridad: RFC 9580 para comportamiento normativo moderno; manuales de las versiones instaladas para sintaxis ejecutable.
- El libro principal aporta el itinerario práctico y la perspectiva de correo seguro, no sustituye documentación de GnuPG/Sequoia contemporánea.
- Verificar compatibilidad real de claves v6, AEAD, algoritmos y dispositivos antes de ejecutar laboratorios cruzados.
- No equiparar firmas RPM, OpenPGP, SSH y S/MIME: identificar estándares, herramientas y almacenes de confianza de cada caso.

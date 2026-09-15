# Registro de aprendizajes

## 2026-09-15 — Baseline inicial

### 1. Cámara
**Problema:** slight handheld / movimiento natural provocaba cambios de auto y letreros.
**Aprendizaje:** usar `Static customer POV`, `Locked shot`, y prohibir explícitamente zoom, pan, tilt, reframing y dolly.

### 2. Continuidad
**Problema:** el auto y los letreros se deformaban.
**Aprendizaje:** nombrar objetos concretos que deben permanecer sin cambios y exigir primer frame fijado.

### 3. Branding
**Problema:** texto podía mutar durante la animación.
**Aprendizaje:** `CHAPUMAKOS` debe estar integrado como elemento físico del escenario y protegido en el prompt.

### 4. Voces
**Problema:** Grok mezclaba cliente y Mako; incluso generaba voz femenina.
**Aprendizaje:** usar contraste extremo:
- Cliente: joven, tenor limpio, ligeramente nasal.
- Mako: mayor, barítono grave, sereno, ronco ligero, barrio, picardía.
Asignar `<AUDIO_0>` al cliente y `<AUDIO_1>` a Mako únicamente cuando realmente se usen `reference_audios` en Reference-to-Video.

### 5. Diálogo
**Problema:** primeros guiones eran demasiado largos y explicativos.
**Aprendizaje:** usar respuestas breves y absurdas.
Ejemplo aprobado:
- “¿Y mi carro?”
- “Ahí va, jefe.”
- “Lleva tres días ahí arriba.”
- “Por eso va volando.”
- “¿Ya encontró la falla?”
- “Sí.”
- “¿Cuál era?”
- “Que estaba fallando.”

### 6. Mako
**Aprendizaje:** Mako no debe hablar pausado como si buscara una excusa. La excusa ya está lista. Voz serena; respuesta rápida.

### 7. Imágenes de referencia
**Problema:** una cola incorrecta arruinó una versión.
**Aprendizaje:** validar anatomía antes de animar, especialmente cola, manos, pies y escala.

## 2026-09-15 — EP-001 Mako mecánico — errores de Prompt 2

### 8. Cliente fuera de cuadro mal interpretado
**Síntoma:** el cliente no aparece visualmente, y Grok a veces trata de reasignar el turno de diálogo al único personaje visible.
**Regla nueva:** en este formato el cliente NO aparece jamás; existe únicamente como `OFF-SCREEN YOUNG MAN VOICE FROM BEHIND THE CAMERA`. No mostrar cuerpo, cara, manos, reflejo, sombra ni silueta.

### 9. Voz del cliente convertida a mujer
**Síntoma:** aunque el prompt decía cliente masculino, Grok generó una voz femenina.
**Corrección:** no depender solo de una descripción global. Repetir en CADA turno del cliente: `OFF-SCREEN YOUNG ADULT MAN, MALE VOICE ONLY, clearly masculine tenor`.
**Regla nueva:** para este episodio y formato, cada línea del cliente debe reafirmar que es un hombre joven. No usar solo `CUSTOMER` como etiqueta.

### 10. Mako diciendo líneas del cliente
**Síntoma:** Mako mueve la boca y pronuncia preguntas asignadas al cliente.
**Corrección:** ownership estricto de turnos y timeline con tiempos. Cada turno del cliente debe incluir:
- `OFF-SCREEN YOUNG MAN SPEAKS ONLY`
- `Mako is silent`
- `Mako's mouth stays fully closed`
Y cada turno de Mako debe decir `MAKO SPEAKS ONLY`.

### 11. Diferenciación vocal insuficiente
**Síntoma:** aunque ambas voces son masculinas, pueden sonar demasiado parecidas.
**Aprendizaje:** la diferencia debe definirse por TIMBRE, REGISTRO, EDAD PERCIBIDA, RESONANCIA y TEXTURA, no solo por actitud.
- CUSTOMER = joven, tenor, limpio, brillante, ligeramente nasal.
- MAKO = 50–60, barítono grave, resonancia de pecho, sereno, confiado, ligeramente ronco/rasposo, picardía de barrio.

### 12. Timeline mejora asignación de hablantes
**Hallazgo externo:** usuarios de Grok Imagine reportan mejores resultados cuando el diálogo está dividido por timestamps, un solo hablante por bloque y una instrucción explícita de lo que hace el otro personaje en silencio.
**Regla nueva:** para conversaciones de dos voces usar bloques temporales claros, sin solapamiento, y reservar pequeñas pausas de 0.2–0.4 s entre cambios de hablante cuando el ritmo lo permita.

### 13. Error persistente específico: “Me voy a quejar”
**Síntoma:** Mako pronuncia `Me voy a quejar` aunque pertenece al cliente.
**Corrección prioritaria:** aislar esa línea en su propio bloque de tiempo, precedida y seguida por una micro-pausa, y repetir dentro de ese bloque que el hablante es `OFF-SCREEN YOUNG ADULT MAN — MALE VOICE ONLY`; Mako permanece con boca cerrada durante todo ese bloque.

### 14. Límite real de Grok
**Hallazgo:** hay reportes recientes de intercambio de voces incluso usando referencias. El prompting reduce el fallo, pero no garantiza 100%.
**Regla de ahorro de créditos:** si una misma asignación de voz falla 2–3 veces con el prompt optimizado, dejar de iterar a ciegas. Para producción estable usar Reference-to-Video con `reference_audios` reales/preset si están disponibles, o generar la actuación visual y añadir la voz fuera de cámara en edición.

### 15. Patrón confirmado que SÍ funcionó
**Resultado:** la versión final con timeline, micro-pausas y speaker ownership explícito funcionó correctamente.
**Patrón aprobado para reutilizar en todos los videos de este formato:**
- cámara fija desde POV del interlocutor;
- solo Mako visible;
- cliente únicamente como voz masculina fuera de cámara;
- cada línea dentro de un bloque temporal propio;
- `MAKO SPEAKS ONLY` en turnos de Mako;
- `OFF-SCREEN YOUNG ADULT MAN — MALE VOICE ONLY` en turnos del cliente;
- durante voz del cliente, repetir `Mako remains completely silent`, `Mako's mouth stays fully closed`, `Mako does NOT lip-sync`;
- micro-pausa de 0.2–0.4 s entre cambios de hablante;
- para líneas que Grok reasigna con frecuencia, añadir una cláusula especial de propiedad exclusiva de esa frase.
**Regla maestra:** este patrón pasa a ser el baseline oficial para futuros diálogos Mako + cliente fuera de cámara. No volver al formato simple `CUSTOMER:` / `MAKO:` sin timeline.

## 2026-09-15 — EP-002 Mako entrenador / farmear aura

### 16. Mako salió con voz femenina
**Síntoma:** aunque la voz oficial de Mako es masculina grave, Grok generó voz femenina.
**Corrección:** reafirmar también EN CADA TURNO DE MAKO `MAKO — OLDER MALE VOICE ONLY, low baritone, never female` y no depender solo del bloque global de voz.
**Regla nueva:** las dos voces se fijan por turno, no solo al inicio del prompt.

### 17. Mako volvió a decir líneas del cliente
**Síntoma:** Mako habló durante bloques del cliente.
**Corrección:** mantener el patrón aprobado del EP-001 sin simplificarlo: timeline, micro-pausas, ownership explícito y boca cerrada durante todo bloque del cliente.
**Regla nueva:** no reducir las restricciones de speaker lock aunque el episodio cambie de oficio o temática.

### 18. Movimiento incoherente con el diálogo
**Síntoma:** en un video de `farmear aura`, la actuación física no estaba ligada de forma suficiente a lo que Mako decía.
**Aprendizaje:** cuando el chiste depende de una acción física, cada línea debe tener su acción sincronizada dentro del mismo bloque temporal.
**Ejemplo:** al decir `Pecho arriba. Mirada lejos.`, Mako debe elevar suavemente el pecho y dirigir la mirada a un punto lejano durante ESA línea, no antes ni después.
**Regla nueva:** diálogo y movimiento forman una sola instrucción temporal. No usar gestos genéricos si la frase describe una acción concreta.

### 19. Consulta obligatoria del repositorio antes de generar
**Regla de proceso:** antes de crear cualquier imagen, guion o prompt de animación, consultar las especificaciones vigentes en GitHub: prompt maestro, reglas de voz, ficha del personaje, continuidad visual y registro de aprendizajes. No trabajar solo desde memoria si el repositorio ya contiene una regla oficial.

### 20. Mako necesita sonar como señor, no solo “male”
**Síntoma:** incluso con `MALE ONLY` Grok puede asignar una voz femenina o demasiado juvenil.
**Corrección:** describir positivamente la identidad acústica en cada turno: `MATURE MEXICAN MAN, 55–65, deep low baritone, strong chest resonance, naturally rough and slightly hoarse from age, calm and confident`.
**Regla nueva:** para Mako no usar solo género; fijar género + edad percibida + registro + resonancia + textura en cada bloque de voz.

### 21. Reference audio es la vía técnica más fuerte
**Hallazgo oficial xAI:** Grok Imagine Video 1.5 Reference-to-Video acepta hasta 3 voces preset mediante `reference_audios` + `voice_id`, etiquetadas como `<AUDIO_0>`, `<AUDIO_1>`, etc. Los tags por sí solos no fijan una voz si no se envían referencias de audio.
**Regla de ahorro de créditos:** en UI sin selector de voz, el prompt textual es best-effort. Si el género de Mako vuelve a fallar reiteradamente, usar Reference-to-Video con preset voice si está disponible o reemplazar la voz en edición.

### 22. Movimiento Six Seven investigado
**Hallazgo:** el gesto viral `six seven / 6-7` se reconoce por las dos manos abiertas a la altura del pecho, como una balanza: una mano sube mientras la otra baja y luego alternan. Fuentes recientes describen que funciona mejor con movimientos rápidos y no demasiado altos.
**Aplicación EP-002:** cuando Mako diga `Farmear aura`, ejecutar durante esa misma frase el gesto Six Seven: codos cerca del torso, ambas manos abiertas a la altura del pecho, palmas orientadas hacia arriba o ligeramente planas según la referencia, alternando arriba/abajo de forma corta y rítmica 2–3 veces; rostro serio, párpados a medio ojo, sin sonreír.
**Regla nueva:** cuando se use una pose/trend real, investigar primero el gesto y describirlo físicamente; no inventar una pose genérica.

## Regla de mantenimiento
Cada nuevo error real debe documentarse aquí con:
- fecha
- episodio
- síntoma
- causa probable
- corrección aplicada
- regla nueva o modificada

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

## Regla de mantenimiento
Cada nuevo error real debe documentarse aquí con:
- fecha
- episodio
- síntoma
- causa probable
- corrección aplicada
- regla nueva o modificada

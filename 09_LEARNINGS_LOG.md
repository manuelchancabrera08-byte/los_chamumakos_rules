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
Asignar `<AUDIO_0>` al cliente y `<AUDIO_1>` a Mako cuando se use Reference-to-Video.

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
**Regla nueva:** en este formato el cliente NO aparece jamás; existe únicamente como `OFF-SCREEN MALE CUSTOMER VOICE FROM BEHIND THE CAMERA`. No mostrar cuerpo, cara, manos, reflejo, sombra ni silueta.

### 9. Voz del cliente convertida a mujer
**Síntoma:** aunque el prompt decía cliente masculino, Grok generó una voz femenina.
**Corrección:** repetir de forma compacta y no ambigua: `MALE ONLY`, `young adult MAN`, `unmistakably masculine tenor`, `NEVER female`, y contrastar explícitamente contra Mako.
**Regla nueva:** para este episodio y formato, el cliente siempre es hombre joven, tenor limpio, claro, más agudo y ligeramente nasal.

### 10. Mako diciendo líneas del cliente
**Síntoma:** Mako mueve la boca y pronuncia preguntas asignadas al cliente.
**Corrección:** ownership estricto de turnos:
- `CUSTOMER` habla únicamente líneas CUSTOMER como audio fuera de cámara.
- Durante CUSTOMER, la boca de Mako permanece completamente cerrada.
- `MAKO` habla únicamente líneas MAKO.
- Durante MAKO, solo la boca de Mako se mueve.
**Regla nueva:** cada prompt con diálogo debe incluir `Never let Mako speak or lip-sync CUSTOMER lines` y `Never let CUSTOMER speak MAKO lines`.

### 11. Diferenciación vocal insuficiente
**Síntoma:** aunque ambas voces son masculinas, pueden sonar demasiado parecidas.
**Aprendizaje:** la diferencia debe definirse por TIMBRE, REGISTRO, EDAD PERCIBIDA, RESONANCIA y TEXTURA, no solo por actitud.
- CUSTOMER = joven, tenor, limpio, brillante, ligeramente nasal.
- MAKO = 50–60, barítono grave, resonancia de pecho, sereno, confiado, ligeramente ronco/rasposo, picardía de barrio.

## Regla de mantenimiento
Cada nuevo error real debe documentarse aquí con:
- fecha
- episodio
- síntoma
- causa probable
- corrección aplicada
- regla nueva o modificada

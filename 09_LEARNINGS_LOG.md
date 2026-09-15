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

## Regla de mantenimiento
Cada nuevo error real debe documentarse aquí con:
- fecha
- episodio
- síntoma
- causa probable
- corrección aplicada
- regla nueva o modificada

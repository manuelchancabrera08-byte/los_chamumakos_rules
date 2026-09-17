# Plantilla maestra — Google Flow

Esta es la plantilla principal para producción nueva de Los Chapumakos.

## Formato de producción
- Motor principal: Google Flow.
- Duración objetivo del proyecto: aproximadamente 10 segundos por clip.
- Formato habitual: vertical 9:16.
- Una idea cómica principal por clip.
- Antes de escribir el prompt consultar `04_AUDIO_VOICE_RULES.md`, `05_DIALOGUE_STYLE.md`, `09_LEARNINGS_LOG.md`, ficha del personaje y reglas visuales.

## Prioridades
1. Identidad correcta del personaje.
2. Voz correcta.
3. Diálogo corto y natural.
4. Acción física coherente con cada línea.
5. Continuidad visual.
6. Ritmo suficiente para rematar dentro del clip.

## Google Flow — voz
Cuando esté disponible, preferir Ingredients > Voices.

Para Mako:
- crear/usar voz guardada como `Mako`;
- referenciarla como `@Voice: Mako`;
- no reinventar la voz en cada clip;
- usar la descripción oficial de `04_AUDIO_VOICE_RULES.md` para Voice Performance;
- la identidad central actual es **hombre mexicano de barrio de mediana edad, barítono, nasal, con presencia, ronquito ligero, pícaro y colmilludo**;
- evitar empujarlo a una voz de anciano, abuelo o barítono excesivamente profundo.

## Estructura recomendada del prompt

```text
Animate the provided reference image into a short vertical 9:16 ultra-realistic scene for Google Flow.

REFERENCE LOCK:
Keep Mako exactly consistent with the reference image: same face, fur, dark head pattern, half-lowered eyelids, body proportions, tail, clothing and scale. Mako is a small realistic monkey, never human-sized. Keep the same environment, props, lighting, branding and camera composition.

CAMERA:
Static POV from the customer/interlocutor. Camera remains fixed. No unnecessary zoom, pan, tilt, reframing or cinematic camera movement.

MAKO PERFORMANCE:
Mako is calm, confident and colmilludo. He never looks surprised by his own answers. He is not rigid: allow subtle weight shifts, tiny foot adjustments in place, natural shoulder movement, head movement and hand gestures. He does not leave his position unless the scene explicitly requires it.

VOICE:
@Voice: Mako
Mako sounds like a Mexican neighborhood man around 45–55, medium male baritone with clear presence and natural chest support, noticeable nasal-forward resonance, slightly rough and lightly hoarse but not elderly, lived-in street voice, relaxed Mexican barrio cadence, sly mischievous undertone, strong picardía and colmillo, dry playful irony, subtle smirk in the voice, quick confident answers as if he already knows the excuse. Conversational and natural, streetwise and present, never theatrical, never announcer-like, never elderly, never overly deep or cinematic.

OFF-SCREEN CUSTOMER:
Young adult Mexican man, 22–30, masculine light tenor, clean and clear voice. Customer remains completely off-screen.

SPEAKER OWNERSHIP:
When the customer speaks, Mako stays silent and his mouth remains closed. When Mako speaks, only Mako articulates the line. Never swap dialogue.

SCENE RHYTHM:
Keep dialogue concise enough to play naturally within about 10 seconds. Short pauses only. Do not rush speech unnaturally.

ACTION + DIALOGUE:
Every important physical action must match the exact line being spoken OR happen immediately after a line when the line is introducing the action.
If Mako says something like `Este es el siguiente ejercicio.`, he should finish the sentence and then immediately enter the exact pose with no dead pause.
Never use labels like `aura pose` by themselves. Describe the full biomechanics of the pose.

DIALOGUE:
[Write 4–6 short turns maximum, or fewer if the joke lands earlier.]

AUDIO:
Natural location ambience only. No music unless requested. Dialogue must be clear and conversational Mexican Spanish.

STYLE:
Dry everyday Mexican humor. The characters never perform the joke. Mako treats the absurd answer as completely normal and logical.
```

## Regla especial para trends / poses / ejercicios
Si una escena depende de una referencia cultural o movimiento reconocible:
1. investigar primero cómo se ve realmente;
2. describir la biomecánica del movimiento en el prompt;
3. sincronizarlo con la frase exacta o hacerlo inmediatamente después si la frase introduce la demostración;
4. evitar decir solo el nombre del trend esperando que Flow lo interprete correctamente;
5. mantener los pies y el peso corporal vivos y naturales sin desplazar a Mako innecesariamente;
6. si Flow ignora una pose genérica, sustituirla por una postura corporal completa con pies, rodillas, torso, brazos, manos, cabeza y mirada definidos.

### Ejemplo operativo — pose de aura tipo power-up
Después de `Este es el siguiente ejercicio.` Mako entra inmediatamente en una pose de poder muy marcada: ambos pies separados sobre el soporte, uno apenas adelantado; rodillas ligeramente flexionadas; pecho elevado; torso firme; ambos codos doblados y llevados hacia atrás; puños cerrados colocados a ambos lados de la cadera; hombros abajo; barbilla ligeramente baja; mirada intensa y lejana con párpados a medio ojo. Mantiene la pose como si estuviera acumulando energía, con tensión contenida y un pequeño cambio de peso, sin desplazarse.

## Regla de ahorro de créditos
- Validar primero la imagen de referencia.
- Validar la voz personalizada antes del video.
- Revisar que el diálogo realmente cabe en 10 segundos.
- Revisar que cada movimiento importante esté descrito físicamente.
- No generar hasta que esos cuatro puntos estén claros.

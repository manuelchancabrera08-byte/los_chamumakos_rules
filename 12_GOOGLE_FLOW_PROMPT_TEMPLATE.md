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
- usar la descripción oficial de `04_AUDIO_VOICE_RULES.md` para Voice Performance.

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
Mako sounds like an older Mexican man from the neighborhood: around 60–70, medium-low baritone, slightly nasal, naturally rough and lightly hoarse from age, relaxed barrio cadence, sly playful undertone, dry irony and streetwise confidence. Conversational, natural, never theatrical or announcer-like.

OFF-SCREEN CUSTOMER:
Young adult Mexican man, 22–30, masculine light tenor, clean and clear voice. Customer remains completely off-screen.

SPEAKER OWNERSHIP:
When the customer speaks, Mako stays silent and his mouth remains closed. When Mako speaks, only Mako articulates the line. Never swap dialogue.

SCENE RHYTHM:
Keep dialogue concise enough to play naturally within about 10 seconds. Short pauses only. Do not rush speech unnaturally.

ACTION + DIALOGUE:
Every important physical action must match the exact line being spoken. If the line names a pose, trend, exercise, object or gesture, perform the recognizable physical action during that line. Never substitute a random pose.

DIALOGUE:
[Write 4–6 short turns maximum, or fewer if the joke lands earlier.]

Example structure:
MAKO: "[short line]"
Action: [exact physical movement tied to line]

CUSTOMER, off-screen: "[short question]"
Mako listens silently, mouth closed, with only a small natural reaction.

MAKO: "[short absurd answer]"
Action: [exact synchronized movement]

CUSTOMER, off-screen: "[short objection]"

MAKO: "[dry punchline]"
Action: [small final movement/reaction]

AUDIO:
Natural location ambience only. No music unless requested. Dialogue must be clear and conversational Mexican Spanish.

STYLE:
Dry everyday Mexican humor. The characters never perform the joke. Mako treats the absurd answer as completely normal and logical.
```

## Regla especial para trends / poses / ejercicios
Si una escena depende de una referencia cultural o movimiento reconocible:
1. investigar primero cómo se ve realmente;
2. describir la biomecánica del movimiento en el prompt;
3. sincronizarlo con la frase exacta;
4. evitar decir solo el nombre del trend esperando que Flow lo interprete correctamente;
5. mantener los pies y el peso corporal vivos y naturales sin desplazar a Mako innecesariamente.

## Regla de ahorro de créditos
- Validar primero la imagen de referencia.
- Validar la voz personalizada antes del video.
- Revisar que el diálogo realmente cabe en 10 segundos.
- Revisar que cada movimiento importante esté descrito físicamente.
- No generar hasta que esos cuatro puntos estén claros.

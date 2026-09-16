# Plantilla maestra para Grok

Esta plantilla es el baseline oficial. Antes de crear cualquier prompt nuevo hay que consultar también `04_AUDIO_VOICE_RULES.md`, `09_LEARNINGS_LOG.md`, la ficha del personaje y las reglas visuales vigentes.

## Regla de producción
No volver al formato simple `CUSTOMER:` / `MAKO:` sin timeline. Usar siempre bloques temporales, micro-pausas, ownership explícito de cada línea y acciones coherentes con lo que se dice.

```text
Use the provided [CHARACTER / SCENE] image as the exact pinned first frame.

Create a 15-second vertical 9:16 ultra-realistic video.

IMPORTANT:
The first frame must remain exactly consistent with the provided image.
Keep the same environment, objects, lighting, signs, branding and overall composition.

CHARACTER:
[Character] is a small realistic monkey, NOT human-sized.
Keep exactly the same face, fur, head pattern, eyes, tail, body proportions, full outfit and footwear.

CAMERA:
Static customer POV.
Completely locked shot.
No zoom, pan, tilt, reframing, dolly, drift or cinematic movement.

STRICT CONTINUITY:
Nothing may appear, disappear, duplicate, morph, resize or shift unnaturally.
Do not alter CHAPUMAKOS signs or lettering.
Do not alter background objects unless physically touched.
Maintain realistic gravity, balance, hand movement, tail movement, body motion and mouth movement.

VISIBLE / OFF-SCREEN RULE:
Only [CHARACTER] is visible on screen.
The customer NEVER appears visually.
The customer exists only as an OFF-SCREEN HUMAN MALE VOICE from behind the camera.

STRICT SPEAKER LOCK:
There are exactly TWO MALE VOICES.
VOICE A = OFF-SCREEN YOUNG ADULT MAN.
VOICE B = [CHARACTER].
Never swap voices or lines.
Never generate a female voice for either speaker.

VOICE CONTINUITY:
The voice heard in the FIRST line of each speaker becomes that speaker's FIXED voice identity for the entire clip.
Do not recast, regenerate, feminize, masculinize, age-shift or change timbre between turns.

WHEN OFF-SCREEN MAN SPEAKS:
- [CHARACTER] remains completely silent.
- [CHARACTER]'s mouth stays fully closed.
- [CHARACTER] does NOT lip-sync.
- [CHARACTER] may only react silently with eyes, head or body.

WHEN [CHARACTER] SPEAKS:
- only [CHARACTER]'s mouth moves.
- only [CHARACTER] produces that line.

VOICE A — OFF-SCREEN YOUNG ADULT MAN:
MALE ONLY. Human man, 22–30. Clearly masculine light tenor. Clean, bright, clear, smooth, slightly nasal. Neutral Mexican Spanish. Never female or androgynous.

VOICE B — MAKO WHEN CHARACTER IS MAKO:
MATURE MEXICAN MAN, 55–65, MALE VOICE ONLY. Deep low baritone. Strong chest resonance. Clearly mature masculine timbre. Naturally rough and slightly hoarse from age. Calm, serene, confident, streetwise, dry humor, picardía. Never female, feminine, androgynous, youthful, high-pitched, falsetto, cartoonish or announcer-like.

IMPORTANT:
Repeat the relevant voice identity INSIDE EVERY dialogue block; do not rely only on this global description.

PERFORMANCE:
Restrained acting. No cartoon exaggeration.
Actions must match the spoken words.
Every physical gesture must have a reason in the dialogue.
If the dialogue describes, demonstrates or names a movement, the character performs that movement during that exact spoken block.
Do not perform unrelated gestures.

DIALOGUE TIMELINE — DO NOT REASSIGN:

[0.0–Xs]
MAKO — MATURE MEXICAN MAN, 55–65, MALE VOICE ONLY, DEEP LOW BARITONE, slightly rough/hoarse from age:
"[LINE]"
[Describe the exact movement that visually matches this line.]

[Xs–Xs]
BRIEF SILENCE.
No one speaks.

[Xs–Xs]
OFF-SCREEN YOUNG ADULT MAN — MALE VOICE ONLY, 22–30, LIGHT TENOR:
"[LINE]"
Mako remains completely silent.
Mako's mouth stays fully closed.
Mako does NOT lip-sync.
[Describe only a silent reaction if needed.]

Repeat this structure for every line.
Reserve 0.2–0.4 seconds of silence between speaker changes whenever possible.

AUDIO:
No music unless explicitly required.
Only subtle realistic environmental ambience.
Natural Mexican Spanish.
Only the visible character receives visible lip-sync.

STYLE:
Dry everyday humor.
Short, direct, deadpan dialogue.
Confident absurdity.
```

## Regla especial de movimientos
Para videos donde el chiste depende de una acción física (ejercicio, pose, baile, oficio, demostración, herramienta, objeto):
- investigar primero el movimiento real/trend cuando exista una referencia pública;
- describir físicamente el movimiento, no solo nombrarlo;
- describir la acción dentro del MISMO bloque temporal de la línea que la justifica;
- cada acción debe comenzar y terminar de forma físicamente coherente;
- evitar gestos genéricos que no tengan relación con la frase;
- mantener el personaje en su soporte físico si el entorno es de escala humana;
- nunca sacrificar speaker lock por añadir movimiento.

## Regla técnica de voces
Si se trabaja en Grok Imagine Video 1.5 Reference-to-Video y la interfaz/API permite `reference_audios`, preferir una voz preset seleccionada/escuchada previamente y asignarla con `voice_id`. Los tags `<AUDIO_0>`, `<AUDIO_1>` solo deben usarse cuando realmente existen referencias de audio asociadas. Si no hay selector/reference audio, el control textual de voz es best-effort y no puede garantizar por sí solo el género/timbre.

# Reglas oficiales de audio y voces

## Motor de producción actual
La producción principal de Los Chapumakos usa **Google Flow**. Grok queda como referencia histórica/alternativa.

## Regla de escena
- El interlocutor/cliente normalmente NO aparece en cuadro cuando el formato sea POV.
- Si está fuera de cámara, existe únicamente como voz humana detrás de la cámara.
- No mostrar cuerpo, cara, manos, reflejo, sombra ni silueta salvo que el episodio lo pida expresamente.
- Cada hablante conserva su propia identidad vocal durante todo el clip.

## Separación estricta de hablantes
Cuando haya dos voces:
- Cada personaje dice únicamente sus líneas.
- Nunca intercambiar diálogo.
- Cuando habla el cliente fuera de cámara, Mako mantiene la boca cerrada y reacciona solo con ojos, cabeza, postura, manos o micro-movimientos de pies.
- Cuando habla Mako, solo su boca articula esa línea.

## Cliente — voz base
- Hombre joven, aproximadamente 22–30 años.
- Tenor masculino ligero.
- Limpio, claro, brillante y ligeramente nasal.
- Español mexicano neutro.
- Puede sonar confundido, impaciente o incrédulo según la escena.
- Claramente más joven y más agudo que Mako.

## Mako — VOZ OFICIAL ACTUAL
Mako debe sonar como **un hombre mexicano de barrio de mediana edad, natural, nasal y rasposo**, con picardía y colmillo. La prioridad ya NO es que suene viejo ni muy grave: debe sonar presente, callejero y conversacional.

### Identidad acústica
- Hombre mexicano de aproximadamente **40–50 años percibidos**.
- Registro **barítono medio**, masculino y con presencia clara.
- Cuerpo vocal natural, pero sin exceso de pecho ni profundidad de narrador.
- **Nasalidad frontal clara**, con resonancia en nariz y máscara facial.
- Timbre **seco y ligeramente apretado**, no suave ni redondo.
- Textura **rasposa/gritty**, con un borde seco natural.
- Evitar abusar de `hoarse`: demasiada ronquera empuja la voz hacia anciano. Preferir **dry gritty edge + slight vocal fry**.
- Ligero `vocal fry` o quiebre seco al final de algunas frases.
- Articulación relajada, cotidiana, no perfecta de estudio.
- Cadencia de barrio mexicano: respuesta rápida, relajada, segura y con colmillo.
- Picardía audible: parece que siempre sabe algo que el cliente no sabe.
- Ironía seca y juguetona.
- Algunas terminaciones pueden caer ligeramente hacia abajo, como si la respuesta fuera obvia.
- Debe sentirse una voz humana real, imperfecta y vivida, como vendedor, mecánico o vecino que trata con gente todo el día.

### Color vocal buscado
Pensar en: **hombre mexicano de barrio de 40–50, voz media-barítono, bastante nasal hacia adelante, seca, raspada/gritty, con pequeño fry al final, muy natural, pícaro y colmilludo; cero locutor, cero abuelo.**

### NO debe sonar
- femenino;
- adolescente o veinteañero;
- anciano;
- abuelo;
- barítono demasiado profundo;
- demasiado ronco/cansado;
- suave, redondo o cálido de narrador;
- limpio o pulido de locutor;
- voz de estudio;
- cinematográfico;
- teatral;
- caricaturesco;
- villano;
- narrador de comercial;
- como alguien intentando hacer una voz chistosa.

### Descripción recomendada para Google Flow / Custom Voice
`Mexican neighborhood man, around 40–50 years old. Medium male baritone, not deep. Strong forward nasal placement in the nose and facial mask. Dry, slightly pinched tone with a natural gritty rasp, not elderly hoarseness. Slight vocal fry and a dry crack at some phrase endings. Relaxed everyday Mexican barrio cadence, casual articulation, clipped or softened endings, quick confident replies, sly mischievous undertone, strong picardía and colmillo, dry playful irony. Sounds like a neighborhood mechanic or street vendor who talks to customers all day and always has an answer ready. Natural, imperfect, unpolished, streetwise. Never warm narrator, never smooth studio voice, never elderly, never theatrical, never announcer-like, never overly deep.`

### Frase de prueba recomendada
Antes de usar créditos de video, probar la voz con una línea típica como:
`Ándele, joven... así mero. ¿Pa' qué le movemos más?`

Criterio de aprobación:
- la nasalidad debe notarse sin sonar tapado;
- la textura debe sentirse seca/rasposa, no enferma;
- la edad debe sentirse 40–50, no abuelo;
- la picardía debe venir de la cadencia, no de sobreactuar;
- la voz debe sonar callejera y natural, no profesional de estudio.

## Google Flow — estrategia de calibración de voz
La voz se calibra **fuera del video** antes de gastar créditos de animación.

### Flujo recomendado
1. Crear o editar la voz personalizada guardada como **Mako**.
2. Elegir una voz base masculina de mediana edad, de tono medio y con algo de nasalidad; evitar bases demasiado graves o suaves.
3. Usar la descripción oficial anterior en `Voice Performance`.
4. Probar exactamente la misma frase corta varias veces.
5. Cambiar **una sola variable por prueba**: nasalidad, raspado/grit, edad percibida o cadencia. No cambiar todo a la vez.
6. Aprobar la voz únicamente cuando una prueba aislada ya suene a Mako.
7. Después usar `@Voice: Mako` en los videos y no volver a redefinir la identidad desde cero.

## Regla de ahorro de créditos
- Primero validar la voz con la previsualización de voz.
- Después generar el video.
- Si la voz guardada ya está aprobada, NO volver a redefinirla desde cero en cada clip.
- Si un modelo concreto no permite referencias de voz, la descripción textual es best-effort; no gastar iteraciones indefinidas intentando corregir el timbre solo con más adjetivos.

## Ambiente y final de audio
- Sin música salvo que el episodio lo requiera.
- Ambiente realista y discreto.
- Sonido de locación natural.
- No introducir sonidos cuya fuente contradiga lo visible.
- **No generar risas, chuckles, giggles, carcajadas, risas de fondo, audience laughter ni reacción cómica automática**, salvo que el guion las pida de forma explícita.
- Después de la última línea no añadir vocalizaciones, risitas ni ad-libs inventados.
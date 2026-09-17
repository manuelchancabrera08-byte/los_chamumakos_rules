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
- **Nasalidad frontal perceptible**, con la resonancia colocada hacia nariz y máscara facial.
- Voz **seca, ligeramente apretada/pinzada y un poco áspera**.
- **Rasposidad ligera y ronquera natural**, especialmente al final de algunas frases.
- Puede tener un toque mínimo de vocal fry / quiebre seco al cerrar ciertas palabras, sin exagerar.
- Debe sentirse una voz humana real, no pulida: un poco imperfecta, vivida y de calle.
- Cadencia relajada de barrio mexicano.
- Picardía audible: parece que siempre sabe algo que el cliente no sabe.
- Colmillo, seguridad callejera y una sonrisa apenas perceptible en la voz, sin convertirla en caricatura.
- Ironía seca y juguetona.
- Ritmo ágil pero tranquilo: responde rápido porque ya tiene la excusa lista.
- Articulación ligeramente relajada, como conversación cotidiana; no dicción perfecta de estudio.
- Puede arrastrar levemente una sílaba, cortar algún final o meter una inflexión pícara en `joven`, `jefe`, `ándele`, `mire`, sin exagerar.

### Color vocal buscado
Pensar en: **hombre mexicano de barrio de unos 40–50, barítono medio, nasal hacia adelante, seco, un poco rasposo, muy natural, pícaro y colmilludo; voz de vendedor/mecánico/vecino que trata con clientes todo el día y siempre tiene una salida**.

La picardía viene de la seguridad, la ironía, la nasalidad y la cadencia, no de hacer una voz chistosa.

### NO debe sonar
- femenino;
- adolescente o veinteañero;
- anciano;
- abuelo;
- barítono demasiado profundo;
- limpio o pulido de locutor;
- voz de estudio;
- cinematográfico;
- teatral;
- caricaturesco;
- villano;
- narrador de comercial;
- como alguien intentando hacer una voz chistosa.

### Descripción recomendada para Google Flow / Custom Voice
`Mexican neighborhood man, around 40–50 years old, medium male baritone with clear vocal presence, forward nasal resonance placed in the nose and front of the face, dry slightly pinched tone, naturally rough with a light raspy edge and mild hoarseness, slightly imperfect lived-in street voice, relaxed Mexican barrio cadence, casual articulation, subtle vocal fry at some phrase endings, sly mischievous undertone, strong picardía and colmillo, dry playful irony, quick confident answers as if he already knows the excuse, conversational, natural and unpolished, like a neighborhood vendor or mechanic who talks to customers all day; never elderly, never announcer-like, never polished studio voice, never theatrical, never overly deep or cinematic.`

### Frase de prueba recomendada
Antes de usar créditos de video, probar la voz con una línea típica como:
`Ándele, joven... así mero. ¿Pa' qué le movemos más?`

Si esa frase no suena nasal, seca, ligeramente rasposa, mexicana, natural, pícara y de barrio, NO aprobar todavía la voz.

## Google Flow — referencia de voz
La vía preferida para continuidad vocal es usar **Ingredients > Voices** y una voz de un solo hablante.

### Flujo recomendado
1. Crear una voz personalizada y guardarla con el nombre **Mako**.
2. Elegir una voz base masculina de mediana edad que ya tenga presencia y algo de nasalidad.
3. En `Voice Performance`, usar la descripción oficial anterior.
4. Probarla con una frase corta típica de Mako antes de gastar créditos de video.
5. En los prompts de video, referenciarla como `@Voice: Mako` cuando Flow lo permita.

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
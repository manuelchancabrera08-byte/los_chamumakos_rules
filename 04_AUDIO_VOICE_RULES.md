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
Mako debe sonar como **un hombre mexicano de barrio con picardía y colmillo**, con presencia vocal clara, no como locutor ni como una voz genérica grave.

### Identidad acústica
- Hombre mexicano de aproximadamente **45–55 años percibidos**.
- Registro **barítono medio**, masculino, presente y con cuerpo, pero nunca bajo extremo ni voz de tráiler.
- **Nasalidad perceptible y frontal**, con la resonancia colocada hacia nariz y máscara facial.
- Timbre vivido y de calle, pero más joven y presente que una voz de anciano.
- **Ligera aspereza y ronquera natural**, solo lo suficiente para dar textura; no debe sonar cansado ni frágil.
- Cadencia relajada de barrio mexicano.
- Picardía audible: parece que siempre sabe algo que el cliente no sabe.
- Colmillo, seguridad callejera y una sonrisa apenas perceptible en la voz, sin convertirla en caricatura.
- Ironía seca y juguetona.
- Frases dichas con naturalidad, como conversación real de calle, no actuación de comedia.
- Ritmo ágil pero tranquilo: responde rápido porque ya tiene la excusa lista.
- Puede arrastrar levemente una sílaba, cortar algún final o meter una inflexión pícara en palabras como `joven`, `jefe`, `ándele`, `mire`, sin exagerar.

### Color vocal buscado
Pensar en: **hombre de barrio mexicano de mediana edad, nasal, barítono, ronquito ligero, pícaro, colmilludo, seguro, con presencia y con la sensación de que ya se las sabe todas**.

No debe sonar agresivo ni delincuencial. La picardía viene de la seguridad, la ironía y la cadencia, no de gritar ni sobreactuar.

### NO debe sonar
- femenino;
- adolescente o veinteañero;
- anciano frágil;
- abuelo cansado;
- limpio de locutor;
- demasiado profundo/cinematográfico;
- teatral;
- caricaturesco;
- villano;
- narrador de comercial;
- como alguien intentando hacer una voz chistosa.

### Descripción recomendada para Google Flow / Custom Voice
`Mexican neighborhood man, around 45–55 years old, medium male baritone with clear presence and natural chest support, noticeable nasal-forward resonance placed in the nose and front of the face, slightly rough and lightly hoarse but not elderly, lived-in street voice, relaxed Mexican barrio cadence, sly mischievous undertone, strong picardía and colmillo, dry playful irony, subtle smirk in the voice, quick confident answers as if he already knows the excuse, conversational and natural, streetwise and present, never theatrical, never announcer-like, never youthful, never elderly, never overly deep or cinematic.`

### Frase de prueba recomendada
Antes de usar créditos de video, probar la voz con una línea típica como:
`Ándele, joven... así mero. ¿Pa' qué le movemos más?`

Si esa frase no suena a hombre mexicano de barrio de mediana edad, nasal, barítono, pícaro y colmilludo, NO aprobar todavía la voz.

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

## Ambiente
- Sin música salvo que el episodio lo requiera.
- Ambiente realista y discreto.
- Sonido de locación natural.
- No introducir sonidos cuya fuente contradiga lo visible.

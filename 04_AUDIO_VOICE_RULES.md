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
Mako NO debe sonar como locutor ni como una voz genérica grave. Debe sonar como **un señor mexicano de barrio con picardía**.

### Identidad acústica
- Hombre mexicano de aproximadamente **60–70 años percibidos**.
- Registro **barítono medio-bajo**, con peso de pecho pero sin exagerar a voz de tráiler.
- Timbre envejecido y vivido.
- **Ligeramente nasal**.
- **Naturalmente áspero, ronquito y algo rasposo**, como una voz gastada por la edad.
- Cadencia relajada de barrio mexicano.
- Picardía, colmillo y seguridad callejera.
- Un toque de ironía seca y juguetona, pero sin actuar el chiste.
- Habla como un señor que ya tiene la respuesta lista y considera completamente normal lo absurdo que está diciendo.
- Puede arrastrar levemente alguna sílaba o cortar finales de forma natural, sin caricatura.

### NO debe sonar
- femenino;
- juvenil;
- limpio de locutor;
- demasiado profundo/cinematográfico;
- teatral;
- caricaturesco;
- villano;
- narrador de comercial;
- como alguien intentando hacer una voz chistosa.

### Descripción recomendada para Google Flow / Custom Voice
`Older Mexican man, around 60–70, medium-low baritone, slightly nasal, naturally rough and lightly hoarse from age, lived-in neighborhood voice, relaxed Mexican barrio cadence, sly playful undertone, dry irony, streetwise confidence, warm but colmilludo, conversational and natural, never theatrical, never announcer-like, never youthful.`

## Google Flow — referencia de voz
La vía preferida para continuidad vocal es usar **Ingredients > Voices** y una voz de un solo hablante.

### Flujo recomendado
1. Crear una voz personalizada y guardarla con el nombre **Mako**.
2. Elegir una voz base masculina madura que ya se acerque al timbre deseado.
3. En `Voice Performance`, pegar/adaptar la descripción oficial anterior.
4. Probarla con una frase corta típica de Mako antes de gastar créditos de video.
5. En los prompts de video, referenciarla como `@Voice: Mako` cuando Flow lo permita.

Google Flow permite crear voces personalizadas y describir su rendimiento vocal; las referencias de voz funcionan en generaciones que usan Ingredients. Por eso, para Mako se debe preferir una voz guardada sobre intentar reinventar el timbre solo con adjetivos en cada prompt.

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

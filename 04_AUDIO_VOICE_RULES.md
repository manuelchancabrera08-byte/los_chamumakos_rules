# Reglas oficiales de audio y voces

## Motor de producción actual
La producción principal de Los Chapumakos usa **Google Flow**. Grok queda como referencia histórica/alternativa.

## Regla de escena
- El interlocutor/cliente normalmente NO aparece en cuadro cuando el formato sea POV.
- Si está fuera de cámara, existe únicamente como voz humana detrás de la cámara.
- No mostrar cuerpo, cara, manos, reflejo, sombra ni silueta salvo que el episodio lo pida expresamente.
- Cada hablante conserva su propia identidad vocal durante todo el clip.

## Separación estricta de hablantes
Cuando haya dos voces, usar un bloqueo explícito y redundante:
- declarar que existen EXACTAMENTE dos voces;
- enumerar literalmente qué líneas puede decir Mako y qué líneas puede decir el cliente;
- prohibir que intercambien líneas;
- prohibir solapamiento;
- repetir el ownership dentro de cada bloque temporal.

Cuando habla el cliente fuera de cámara:
- `OFF-SCREEN YOUNG ADULT MAN — MALE VOICE ONLY`;
- Mako permanece completamente en silencio;
- boca completamente cerrada;
- sin lip-sync;
- sin susurro, reacción vocal ni sonido humano de Mako.

Cuando habla Mako:
- `MAKO SPEAKS ONLY`;
- el cliente queda completamente en silencio;
- solo Mako articula la línea.

## Lip-sync de Mako
No basta con indicar que Mako habla. En cada línea crítica:
- articulación visible desde el PRIMER FONEMA;
- boca, mandíbula y hocico se mueven durante TODA la frase;
- la articulación continúa hasta la ÚLTIMA SÍLABA;
- la boca se cierra solo DESPUÉS de terminar la línea;
- nunca reproducir voz de Mako con boca congelada o cerrada;
- mantener movimiento facial realista de mono, sin boca caricaturesca ni gestos humanos exagerados.

## Cliente — voz base
- Hombre joven, aproximadamente 22–30 años.
- Tenor masculino ligero.
- Limpio, claro y ligeramente más brillante que Mako.
- Español mexicano natural.
- Puede sonar confundido, impaciente o incrédulo según la escena.
- Claramente más joven y más agudo que Mako.

## Mako — VOZ OFICIAL ACTUAL
La voz objetivo aprobada es **hombre mexicano adulto de barrio, aproximadamente 40–50 años, serio, sereno, raspado, natural y con colmillo**.

### Identidad acústica
- Voz masculina media; no extremadamente grave.
- No perseguir un barítono profundo ni voz de locutor.
- Nasalidad frontal ligera y natural.
- Timbre claramente seco, raspado y algo granulado.
- Puede tener un toque gastado/ahumado, sin sonar anciano.
- Cadencia mexicana de barrio/mercado/taller/puesto.
- Ritmo calmado, sereno y relajado; NO acelerado.
- Puede usar micro-pausas de 0.3–0.5 s para una reacción seca sin parecer que busca excusa.
- Articulación informal e imperfecta: consonantes algo suavizadas y finales relajados cuando suene natural.
- Picardía tranquila, colmillo e ironía seca.
- Debe sonar como mecánico, comerciante, vendedor de tianguis o locatario que trata con clientes todo el día.

### NO debe sonar
- voz genérica de IA;
- narrador de TikTok/redes;
- formal;
- corporativo;
- locutor;
- narrador de comercial;
- presentador;
- podcast host;
- actor teatral;
- caricaturesco;
- demasiado grave;
- anciano/abuelo;
- excesivamente limpio o pulido;
- excitado, rápido o hiperactivo.

### Descripción recomendada para Google Flow
`Real Mexican neighborhood man, around 40–50 years old. Medium male speaking voice, not overly deep. Clearly raspy, dry, slightly grainy and rough around the edges, with a subtle worn/smoky texture. Slight nasal-forward resonance without sounding congested. Calm, serene, relaxed, grounded and unhurried. Informal Mexican barrio cadence, natural imperfect diction, softened consonants and slightly relaxed endings when appropriate. Streetwise, strong colmillo, quiet picardía and dry irony. Sounds like a neighborhood mechanic, tianguis vendor, market stall owner or local shopkeeper who talks to customers all day. Serious and matter-of-fact; never performs the joke. Not a generic AI narrator, not TikTok/social-media voice, not radio/commercial/podcast voice, not theatrical, not elderly, not polished, not excessively deep.`

## Google Flow — estrategia de voz
- Si hay una voz guardada de Mako ya aprobada, reutilizarla.
- Si la interfaz actual no permite cargar/referenciar voz, mantener exactamente el mismo descriptor textual entre generaciones.
- No cambiar edad, registro, raspado y ritmo a la vez después de un fallo; cambiar una sola variable por prueba.
- Si una voz ya salió bien en un clip, no volver a rediseñarla en el siguiente prompt.

## Ambiente y silencios
El audio ambiental debe ser mínimo y no humano:
- room tone natural;
- ventilación sutil;
- equipo o ambiente no verbal muy tenue.

PROHIBIDO salvo que el guion lo pida explícitamente:
- música;
- radio;
- televisión;
- noticiero;
- audio grabado;
- locutor;
- PA system;
- podcast;
- comerciales;
- conversaciones de fondo;
- voces lejanas;
- crowd chatter;
- cualquier habla inteligible de fondo;
- risas de cualquier tipo;
- laugh track;
- sitcom laughter;
- audience laughter;
- chuckles;
- giggles;
- carcajadas;
- reacciones cómicas;
- ad-libs inventados;
- vocalizaciones posteriores a una línea.

Durante cada bloque `NO DIALOGUE`, no debe existir NINGUNA voz humana. Las pausas son intencionales y no se rellenan con risas ni comentarios.

## Regla de ahorro de créditos
Si una versión ya tiene la voz correcta, conservar el bloque de voz prácticamente sin cambios y corregir únicamente el fallo concreto del siguiente intento.
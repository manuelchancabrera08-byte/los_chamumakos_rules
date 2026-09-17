# Plantilla maestra — Google Flow

Esta es la plantilla principal para producción nueva de Los Chapumakos.

## Formato de producción
- Motor principal: Google Flow.
- Duración objetivo: aproximadamente 10 segundos por clip.
- Formato habitual: vertical 9:16.
- Una idea cómica principal por clip.
- Antes de escribir el prompt consultar `04_AUDIO_VOICE_RULES.md`, `05_DIALOGUE_STYLE.md`, `09_LEARNINGS_LOG.md`, ficha del personaje y reglas visuales.
- Cada clip nuevo debe escribirse como prompt independiente a partir de la imagen de referencia suministrada. Solo usar lenguaje de continuidad (`continue`, `Part 2`, etc.) si el usuario lo pide expresamente.

## Prioridades
1. Identidad correcta del personaje.
2. Realismo de mono real.
3. Voz correcta.
4. Separación estricta de hablantes.
5. Lip-sync visible de Mako.
6. Diálogo corto y natural.
7. Acción física coherente con cada línea.
8. Continuidad visual de objetos.
9. Aprovechar casi toda la duración disponible.

## REFERENCE LOCK
El primer frame de la imagen de referencia es la autoridad visual.

Para Mako proteger explícitamente:
- mismo rostro;
- mismo pelaje y patrón oscuro de cabeza;
- mismos párpados a medio ojo / semicerrados;
- mismas proporciones de mono pequeño;
- misma cola, manos y pies;
- misma ropa y accesorios;
- mismo entorno, iluminación, branding y composición.

## REALISMO DE MAKO
Mako debe verse como un **mono capuchino real haciendo cosas humanas**, no como un humano vestido de mono.

Incluir cuando sea importante:
- `REAL SMALL CAPUCHIN MONKEY`;
- `NOT human-sized`;
- `NOT a human in a monkey costume`;
- `NOT animated character / mascot / humanoid monkey`;
- anatomía animal real;
- gravedad, peso, balance e inercia reales;
- movimientos restringidos por biomecánica de mono;
- manos/pies animales;
- pelaje realista, no plástico ni de juguete;
- sin movimiento cartoon, elástico, rebotado o teatral.

## MAKO — rostro y actuación
- Párpados SIEMPRE a medio ojo / semicerrados, salvo instrucción excepcional.
- Expresión serena, confiada, ligeramente escéptica y con colmillo.
- Nunca ojos muy abiertos por defecto.
- Nunca reacción exagerada.
- Mako es serio, calmado y sereno.
- Puede usar microbeats de 0.3–0.5 s antes de responder cuando mejoren el humor seco.
- La pausa no debe parecer duda o improvisación nerviosa.
- Nunca se ríe ni actúa el chiste.

## VOZ DE MAKO
Si existe una voz guardada aprobada y la interfaz la permite, reutilizarla. Si no, usar el descriptor textual oficial de `04_AUDIO_VOICE_RULES.md` sin reinventarlo.

Identidad resumida actual:
- hombre mexicano de barrio, 40–50;
- voz masculina media, no demasiado grave;
- claramente seca y raspada, algo granulada;
- ligeramente nasal hacia el frente;
- calmada, serena, relajada;
- ritmo no acelerado;
- dicción informal e imperfecta;
- colmillo, picardía tranquila e ironía seca;
- cero locutor, cero narrador genérico de IA, cero voz corporativa.

## OFF-SCREEN CUSTOMER
- Hombre mexicano joven, 22–30.
- Tenor masculino ligero.
- Limpio y más brillante que Mako.
- Siempre fuera de cámara si el formato es POV.
- No mostrar cara, cuerpo, manos, reflejo, sombra ni silueta salvo que el episodio lo exija.

## ABSOLUTE SPEAKER LOCK
Para dos voces, NO usar únicamente etiquetas simples `CUSTOMER:` / `MAKO:`.

Incluir:
1. `There are EXACTLY TWO voices`.
2. Enumerar literalmente las frases permitidas de Mako.
3. Enumerar literalmente las frases permitidas del cliente.
4. Prohibir el intercambio de líneas.
5. Prohibir solapamiento.
6. Dentro de CADA turno del cliente repetir que Mako está completamente silencioso y con boca cerrada.
7. Dentro de CADA turno de Mako indicar `MAKO SPEAKS ONLY`.

Plantilla:

```text
MAKO is allowed to speak ONLY these exact lines:
1. “...”
2. “...”

THE OFF-SCREEN CUSTOMER is allowed to speak ONLY these exact lines:
1. “...”
2. “...”

WHEN CUSTOMER SPEAKS:
Mako produces absolutely NO voice.
Mako's mouth stays completely CLOSED.
No lip-sync.
No whisper or vocal reaction.

WHEN MAKO SPEAKS:
Only Mako produces speech.
The customer is completely silent.
```

## MAKO LIP-SYNC
En cada turno de Mako, especialmente el remate final:

```text
Visible articulation begins on the FIRST PHONEME.
Mouth, jaw and muzzle move naturally through the ENTIRE line.
Articulation continues through the FINAL SYLLABLE.
Mako closes his mouth only AFTER the final word is completely finished.
Never play Mako's voice over a frozen or closed mouth.
```

Mantener articulación visible pero físicamente creíble para un mono real. No usar boca humana exagerada ni formas cartoon.

## CÁMARA
Default para este formato:
- `Static customer POV`;
- `Locked camera`;
- no zoom;
- no pan;
- no tilt;
- no dolly;
- no reframing.

## TIMELINE
- Cada línea debe tener su propio bloque temporal.
- Un solo hablante por bloque.
- Usar micro-pausas de 0.3–0.5 s cuando mejoren el deadpan.
- No comprimir el diálogo hasta volverlo acelerado.
- La acción física principal debe ocurrir durante la línea que la motiva o inmediatamente después si la frase introduce la acción.
- Preferir terminar el último diálogo alrededor de 9.4–9.8 s y dejar unas décimas de cierre visual.

## OBJETOS Y CONTINUIDAD
Si Mako sostiene un objeto en la referencia y luego necesita las manos libres, resolverlo explícitamente.

Patrón robusto:
`lower → place on a logical surface → release → object remains visible and stable`.

Nunca permitir que una tabla, herramienta, producto u otro objeto desaparezca mágicamente.
Preferir colocar/apoyar antes que lanzar, salvo que lanzar sea parte del chiste.

## AUDIO
Ambiente muy discreto y no humano.

Default:
- room tone;
- ventilación sutil;
- ruido no verbal muy tenue.

Prohibido salvo solicitud expresa:
- música;
- radio;
- TV;
- noticiero;
- voces grabadas;
- locutor;
- PA;
- podcast;
- comerciales;
- conversaciones de fondo;
- voces lejanas;
- crowd chatter;
- habla inteligible ambiental;
- risas de cualquier tipo;
- laugh track;
- sitcom/audience laughter;
- chuckles/giggles;
- ad-libs;
- reacciones cómicas automáticas.

Durante `NO DIALOGUE`, no debe existir ninguna voz humana. El silencio es intencional.

## COMEDY STYLE
Humor mexicano de barrio, seco y deadpan.

- Nadie actúa el chiste.
- Mako trata su lógica absurda como totalmente normal.
- El cliente pregunta/reclama de forma genuina.
- Las pausas pueden ser parte del remate.
- Mako permanece serio y sereno.
- Un cierre físico puede funcionar mejor que añadir otra explicación: cobrar, extender la mano, cerrar una puerta, señalar algo, etc., siempre con acción simple y clara.

## Regla de ahorro de créditos
- Validar primero la imagen de referencia.
- Si una versión ya tiene voz correcta, NO rediseñar el bloque de voz.
- Si el realismo visual ya funciona, cambiar solo el error concreto.
- Revisar speaker lock antes de generar.
- Revisar lip-sync antes de generar.
- Revisar objetos en manos antes de generar.
- Revisar que no haya instrucción que invite risas o voces de fondo.
- Revisar que el diálogo respire y quepa en 10 segundos.
- Después de un resultado aprobado, convertirlo en baseline y evitar reescribirlo innecesariamente.
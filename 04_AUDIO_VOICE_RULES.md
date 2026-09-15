# Reglas oficiales de audio y voces

## Regla de escena para estos videos
- El cliente NO aparece en cuadro.
- El cliente existe únicamente como voz humana masculina fuera de cámara, situada detrás de la cámara / POV.
- No mostrar cuerpo, cara, manos, reflejo, sombra ni silueta del cliente.
- Para este episodio y formato, el cliente es SIEMPRE HOMBRE.

## Separación estricta
Cuando haya dos hablantes:
- El cliente habla únicamente sus líneas.
- Mako habla únicamente sus líneas.
- Nunca intercambiar voces.
- Nunca intercambiar diálogo.
- Cuando habla el cliente, la boca de Mako permanece completamente cerrada.
- Mako puede reaccionar con ojos o expresión mientras escucha, pero NO debe mover los labios.
- Cuando habla Mako, solo la boca de Mako se mueve.
- Las líneas marcadas `CUSTOMER` pertenecen exclusivamente a la voz masculina fuera de cámara.
- Las líneas marcadas `MAKO` pertenecen exclusivamente a Mako.

## Cliente — voz oficial para este formato
- Hombre joven, 22–30 años.
- Voz inequívocamente masculina.
- Tenor masculino ligero.
- Tono más alto que Mako.
- Voz limpia, clara, brillante y ligeramente nasal.
- Español mexicano neutro.
- Puede sonar confundido, impaciente o molesto según el guion.
- Sin ronquera.
- Sin voz grave.
- Sin barrio.
- Sin sarcasmo.
- Nunca mujer.
- Nunca voz femenina o andrógina.
- Debe sentirse acústicamente como una persona distinta de Mako y de otra generación.

## Mako — voz oficial
- Hombre adulto/mayor de 55–65 años.
- Voz inequívocamente masculina y madura.
- Barítono bajo, grave, claramente más bajo que el cliente.
- Resonancia fuerte de pecho.
- Sereno, tranquilo y muy seguro.
- Textura gastada por la edad: ligeramente ronca, áspera y rasposa, pero natural.
- Picardía de barrio.
- Colmillo.
- Sarcasmo seco y natural.
- Sonido de señor mexicano experimentado que siempre tiene una respuesta lista.
- Responde rápido, pero no atropellado.
- No duda buscando la excusa: la respuesta parece ya preparada.
- No juvenil.
- No voz limpia de locutor.
- No falsete.
- No agudo.
- No caricaturesco.
- Nunca voz femenina.

### Frase de lock recomendada EN CADA TURNO DE MAKO
`MAKO — MATURE MEXICAN MAN, 55–65, MALE VOICE ONLY, DEEP LOW BARITONE, strong chest resonance, naturally rough and slightly hoarse from age, calm and confident, NEVER female, NEVER high-pitched.`

## Contraste obligatorio
El modelo debe interpretar dos hombres completamente diferentes:
- `CUSTOMER` = joven + tenor + limpio + claro + algo nasal.
- `MAKO` = señor 55–65 + barítono bajo + pecho + voz gastada/ronca + sereno + picardía.

No basta con cambiar la actitud: el TIMBRE, REGISTRO, EDAD PERCIBIDA, RESONANCIA y TEXTURA deben ser diferentes.

## Grok Imagine Video 1.5 — regla técnica importante
La documentación oficial de xAI indica que el método fiable para fijar identidad vocal en Reference-to-Video es usar `reference_audios` con un `voice_id` preset y etiquetarlo en el prompt como `<AUDIO_0>`, `<AUDIO_1>`, etc.

- Hasta 3 voces preset por generación.
- Los `voice_id` vienen del catálogo oficial de Text-to-Speech.
- Si NO se están enviando `reference_audios`, escribir `<AUDIO_0>` o `<AUDIO_1>` en texto NO fija realmente una voz.
- En la interfaz de Grok, si no existe selector de voz/reference audio, la descripción textual de género/edad/timbre es solo una instrucción de mejor esfuerzo y puede fallar.
- Para ahorrar créditos: si una voz cambia de género repetidamente aun con speaker lock y timeline, no añadir más y más texto indefinidamente; usar voz preset/reference audio si la interfaz/API lo permite, o sustituir la voz en edición.

### Si se usa Reference-to-Video con voces reales/preset
- Cliente = `<AUDIO_0>`.
- Mako = `<AUDIO_1>`.
- Mantener siempre esa asignación.
- No reutilizar el mismo timbre para ambos.
- En el prompt escribir explícitamente que `<AUDIO_0>` pertenece solo al hombre joven fuera de cámara y `<AUDIO_1>` solo a Mako.
- Probar previamente las voces en el playground de xAI y elegir para Mako una voz que acústicamente suene masculina, madura, grave y con peso. La documentación describe voces como `leo` (authoritative and strong), `orion` (rich, cinematic, resonant), `atlas` (confident, commanding, reassuring), `rex` (confident and clear), pero xAI no etiqueta su género en esa tabla; escuchar antes de elegir.

## Ambiente
- Sin música salvo que el episodio lo requiera.
- Ambiente realista y discreto.
- No introducir sonidos cuya fuente implique nuevos objetos visibles.

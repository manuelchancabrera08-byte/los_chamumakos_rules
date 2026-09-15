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
- Hombre de 50–60 años.
- Voz inequívocamente masculina.
- Barítono grave, claramente más bajo que el cliente.
- Voz serena, tranquila y muy segura.
- Resonancia de pecho.
- Ligeramente áspera / ronca / rasposa, sin exageración.
- Picardía de barrio.
- Colmillo.
- Sarcasmo seco y natural.
- Sonido de trabajador mexicano experimentado que siempre tiene una respuesta lista.
- Responde rápido, pero no atropellado.
- No duda buscando la excusa: la respuesta parece ya preparada.
- No caricaturesco.
- No locutor.
- No villano.
- No juvenil.
- Nunca voz femenina.

## Contraste obligatorio
El modelo debe interpretar dos hombres completamente diferentes:
- `CUSTOMER` = joven + tenor + limpio + claro + algo nasal.
- `MAKO` = mayor + barítono grave + pecho + ligeramente ronco + sereno + picardía.

No basta con cambiar la actitud: el TIMBRE, REGISTRO, EDAD PERCIBIDA, RESONANCIA y TEXTURA deben ser diferentes.

## Grok Imagine Video 1.5
Si se usa Reference-to-Video:
- Cliente = `<AUDIO_0>`
- Mako = `<AUDIO_1>`
- Mantener siempre esa asignación.
- No reutilizar el mismo timbre para ambos.
- En el prompt escribir explícitamente que `<AUDIO_0>` es una voz masculina humana fuera de cámara y que `<AUDIO_1>` pertenece exclusivamente al personaje visible Mako.

## Ambiente
- Sin música salvo que el episodio lo requiera.
- Ambiente realista y discreto.
- No introducir sonidos cuya fuente implique nuevos objetos visibles.

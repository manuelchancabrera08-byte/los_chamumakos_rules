# Registro de aprendizajes

## 2026-09-15 — Baseline inicial

### 1. Cámara
**Problema:** slight handheld / movimiento natural provocaba cambios de auto y letreros.
**Aprendizaje:** usar `Static customer POV`, `Locked shot`, y prohibir explícitamente zoom, pan, tilt, reframing y dolly.

### 2. Continuidad
**Problema:** el auto y los letreros se deformaban.
**Aprendizaje:** nombrar objetos concretos que deben permanecer sin cambios y exigir primer frame fijado.

### 3. Branding
**Problema:** texto podía mutar durante la animación.
**Aprendizaje:** `CHAPUMAKOS` debe estar integrado como elemento físico del escenario y protegido en el prompt.

### 4. Voces
**Problema:** Grok mezclaba cliente y Mako; incluso generaba voz femenina.
**Aprendizaje:** usar contraste extremo:
- Cliente: joven, tenor limpio, ligeramente nasal.
- Mako: mayor, barítono grave, sereno, ronco ligero, barrio, picardía.
Asignar `<AUDIO_0>` al cliente y `<AUDIO_1>` a Mako únicamente cuando realmente se usen `reference_audios` en Reference-to-Video.

### 5. Diálogo
**Problema:** primeros guiones eran demasiado largos y explicativos.
**Aprendizaje:** usar respuestas breves y absurdas.
Ejemplo aprobado:
- “¿Y mi carro?”
- “Ahí va, jefe.”
- “Lleva tres días ahí arriba.”
- “Por eso va volando.”
- “¿Ya encontró la falla?”
- “Sí.”
- “¿Cuál era?”
- “Que estaba fallando.”

### 6. Mako
**Aprendizaje:** Mako no debe hablar pausado como si buscara una excusa. La excusa ya está lista. Voz serena; respuesta rápida.

### 7. Imágenes de referencia
**Problema:** una cola incorrecta arruinó una versión.
**Aprendizaje:** validar anatomía antes de animar, especialmente cola, manos, pies y escala.

## 2026-09-15 — EP-001 Mako mecánico — errores de Prompt 2

### 8. Cliente fuera de cuadro mal interpretado
**Síntoma:** el cliente no aparece visualmente, y Grok a veces trata de reasignar el turno de diálogo al único personaje visible.
**Regla nueva:** en este formato el cliente NO aparece jamás; existe únicamente como `OFF-SCREEN YOUNG MAN VOICE FROM BEHIND THE CAMERA`. No mostrar cuerpo, cara, manos, reflejo, sombra ni silueta.

### 9. Voz del cliente convertida a mujer
**Síntoma:** aunque el prompt decía cliente masculino, Grok generó una voz femenina.
**Corrección:** no depender solo de una descripción global. Repetir en CADA turno del cliente: `OFF-SCREEN YOUNG ADULT MAN, MALE VOICE ONLY, clearly masculine tenor`.
**Regla nueva:** para este episodio y formato, cada línea del cliente debe reafirmar que es un hombre joven. No usar solo `CUSTOMER` como etiqueta.

### 10. Mako diciendo líneas del cliente
**Síntoma:** Mako mueve la boca y pronuncia preguntas asignadas al cliente.
**Corrección:** ownership estricto de turnos y timeline con tiempos. Cada turno del cliente debe incluir:
- `OFF-SCREEN YOUNG MAN SPEAKS ONLY`
- `Mako is silent`
- `Mako's mouth stays fully closed`
Y cada turno de Mako debe decir `MAKO SPEAKS ONLY`.

### 11. Diferenciación vocal insuficiente
**Síntoma:** aunque ambas voces son masculinas, pueden sonar demasiado parecidas.
**Aprendizaje:** la diferencia debe definirse por TIMBRE, REGISTRO, EDAD PERCIBIDA, RESONANCIA y TEXTURA, no solo por actitud.
- CUSTOMER = joven, tenor, limpio, brillante, ligeramente nasal.
- MAKO = 50–60, barítono grave, resonancia de pecho, sereno, confiado, ligeramente ronco/rasposo, picardía de barrio.

### 12. Timeline mejora asignación de hablantes
**Hallazgo externo:** usuarios de Grok Imagine reportan mejores resultados cuando el diálogo está dividido por timestamps, un solo hablante por bloque y una instrucción explícita de lo que hace el otro personaje en silencio.
**Regla nueva:** para conversaciones de dos voces usar bloques temporales claros, sin solapamiento, y reservar pequeñas pausas de 0.2–0.4 s entre cambios de hablante cuando el ritmo lo permita.

### 13. Error persistente específico: “Me voy a quejar”
**Síntoma:** Mako pronuncia `Me voy a quejar` aunque pertenece al cliente.
**Corrección prioritaria:** aislar esa línea en su propio bloque de tiempo, precedida y seguida por una micro-pausa, y repetir dentro de ese bloque que el hablante es `OFF-SCREEN YOUNG ADULT MAN — MALE VOICE ONLY`; Mako permanece con boca cerrada durante todo ese bloque.

### 14. Límite real de Grok
**Hallazgo:** hay reportes recientes de intercambio de voces incluso usando referencias. El prompting reduce el fallo, pero no garantiza 100%.
**Regla de ahorro de créditos:** si una misma asignación de voz falla 2–3 veces con el prompt optimizado, dejar de iterar a ciegas. Para producción estable usar Reference-to-Video con `reference_audios` reales/preset si están disponibles, o generar la actuación visual y añadir la voz fuera de cámara en edición.

### 15. Patrón confirmado que SÍ funcionó
**Resultado:** la versión final con timeline, micro-pausas y speaker ownership explícito funcionó correctamente.
**Patrón aprobado para reutilizar en todos los videos de este formato:**
- cámara fija desde POV del interlocutor;
- solo Mako visible;
- cliente únicamente como voz masculina fuera de cámara;
- cada línea dentro de un bloque temporal propio;
- `MAKO SPEAKS ONLY` en turnos de Mako;
- `OFF-SCREEN YOUNG ADULT MAN — MALE VOICE ONLY` en turnos del cliente;
- durante voz del cliente, repetir `Mako remains completely silent`, `Mako's mouth stays fully closed`, `Mako does NOT lip-sync`;
- micro-pausa de 0.2–0.4 s entre cambios de hablante;
- para líneas que Grok reasigna con frecuencia, añadir una cláusula especial de propiedad exclusiva de esa frase.
**Regla maestra:** este patrón pasa a ser el baseline oficial para futuros diálogos Mako + cliente fuera de cámara. No volver al formato simple `CUSTOMER:` / `MAKO:` sin timeline.

## 2026-09-15 — EP-002 Mako entrenador / farmear aura

### 16. Mako salió con voz femenina
**Síntoma:** aunque la voz oficial de Mako es masculina grave, Grok generó voz femenina.
**Corrección:** reafirmar también EN CADA TURNO DE MAKO `MAKO — OLDER MALE VOICE ONLY, low baritone, never female` y no depender solo del bloque global de voz.
**Regla nueva:** las dos voces se fijan por turno, no solo al inicio del prompt.

### 17. Mako volvió a decir líneas del cliente
**Síntoma:** Mako habló durante bloques del cliente.
**Corrección:** mantener el patrón aprobado del EP-001 sin simplificarlo: timeline, micro-pausas, ownership explícito y boca cerrada durante todo bloque del cliente.
**Regla nueva:** no reducir las restricciones de speaker lock aunque el episodio cambie de oficio o temática.

### 18. Movimiento incoherente con el diálogo
**Síntoma:** en un video de `farmear aura`, la actuación física no estaba ligada de forma suficiente a lo que Mako decía.
**Aprendizaje:** cuando el chiste depende de una acción física, cada línea debe tener su acción sincronizada dentro del mismo bloque temporal.
**Ejemplo:** al decir `Pecho arriba. Mirada lejos.`, Mako debe elevar suavemente el pecho y dirigir la mirada a un punto lejano durante ESA línea, no antes ni después.
**Regla nueva:** diálogo y movimiento forman una sola instrucción temporal. No usar gestos genéricos si la frase describe una acción concreta.

### 19. Consulta obligatoria del repositorio antes de generar
**Regla de proceso:** antes de crear cualquier imagen, guion o prompt de animación, consultar las especificaciones vigentes en GitHub: prompt maestro, reglas de voz, ficha del personaje, continuidad visual y registro de aprendizajes. No trabajar solo desde memoria si el repositorio ya contiene una regla oficial.

### 20. Mako necesita sonar como señor, no solo “male”
**Síntoma:** incluso con `MALE ONLY` Grok puede asignar una voz femenina o demasiado juvenil.
**Corrección:** describir positivamente la identidad acústica en cada turno: `MATURE MEXICAN MAN, 55–65, deep low baritone, strong chest resonance, naturally rough and slightly hoarse from age, calm and confident`.
**Regla nueva:** para Mako no usar solo género; fijar género + edad percibida + registro + resonancia + textura en cada bloque de voz.

### 21. Reference audio es la vía técnica más fuerte
**Hallazgo oficial xAI:** Grok Imagine Video 1.5 Reference-to-Video acepta hasta 3 voces preset mediante `reference_audios` + `voice_id`, etiquetadas como `<AUDIO_0>`, `<AUDIO_1>`, etc. Los tags por sí solos no fijan una voz si no se envían referencias de audio.
**Regla de ahorro de créditos:** en UI sin selector de voz, el prompt textual es best-effort. Si el género de Mako vuelve a fallar reiteradamente, usar Reference-to-Video con preset voice si está disponible o reemplazar la voz en edición.

### 22. Movimiento Six Seven investigado
**Hallazgo:** el gesto viral `six seven / 6-7` se reconoce por las dos manos abiertas a la altura del pecho, como una balanza: una mano sube mientras la otra baja y luego alternan.
**Aplicación EP-002:** cuando Mako diga `Farmear aura`, ejecutar durante esa misma frase el gesto Six Seven: codos cerca del torso, ambas manos abiertas a la altura del pecho, palmas orientadas hacia arriba o ligeramente planas según la referencia, alternando arriba/abajo de forma corta y rítmica 2–3 veces; rostro serio, párpados a medio ojo, sin sonreír.
**Regla nueva:** cuando se use una pose/trend real, investigar primero el gesto y describirlo físicamente; no inventar una pose genérica.

### 23. Realismo de celular sin destruir continuidad
**Síntoma:** el video todavía puede verse demasiado limpio/cinematográfico.
**Corrección:** pedir estética de celular real mediante imperfecciones ópticas y de sensor, NO mediante movimiento espacial de cámara: exposición automática leve, rango dinámico limitado, balance de blancos imperfecto, enfoque con respiración mínima, ruido fino de sensor, compresión moderada y audio de micrófono de celular.
**Regla nueva:** `smartphone realism` no significa handheld libre. Mantener encuadre fijo y usar imperfecciones de imagen/sonido para vender realismo.

### 24. Última frase con audio pero sin lip-sync
**Síntoma:** Mako pronuncia una línea final, pero deja la boca quieta durante parte o toda la frase.
**Corrección:** en cada bloque de Mako, especialmente el último, declarar que la articulación comienza con el primer fonema y continúa sin interrupción hasta la última sílaba; la boca debe cerrar únicamente DESPUÉS de terminar la última palabra.
**Regla nueva:** no basta con `only Mako's mouth moves`. Para líneas críticas usar `continuous visible articulation from first phoneme to final syllable; do not stop mouth movement before the final word is fully spoken`.

### 25. Límite confirmado: prompt textual no fija identidad vocal
**Corrección de proceso:** no prometer que una descripción como `old male, deep baritone, hoarse` va a resolver por sí sola la edad/timbre en la UI de Grok. Según la documentación investigada, la fijación fuerte de identidad vocal requiere `reference_audios` + `voice_id` en Reference-to-Video. En la UI sin esa función, la voz descrita por texto sigue siendo best-effort y puede salir joven.
**Regla de ahorro de créditos:** después de un nuevo fallo de edad/timbre en UI, no seguir aumentando adjetivos ni longitud del prompt. Cambiar a voz referenciada/preset o separar el audio del video.

## 2026-09-17 — Migración de producción a Google Flow

### 26. Google Flow pasa a ser el motor principal
**Cambio:** los clips nuevos se producen en Google Flow y el objetivo operativo del proyecto pasa a ser aproximadamente 10 segundos por clip.
**Regla nueva:** el guion debe diseñarse desde el inicio para ese tiempo. No escribir un diálogo largo y luego intentar comprimirlo.

### 27. Nueva definición aprobada de la voz de Mako
**Observación del usuario:** la voz anterior sonaba demasiado genérica/grave y no tenía suficiente identidad de viejo de barrio.
**Nueva dirección:** Mako debe sonar como un señor mexicano de unos 60–70 años percibidos, barítono medio-bajo, ligeramente nasal, voz vivida y gastada, naturalmente áspera/ronquita, cadencia relajada de barrio, picardía, colmillo e ironía seca.
**Regla nueva:** no definirlo simplemente como `deep old male`. La identidad central es `señor de barrio con picardía`, natural y conversacional, no locutor.

### 28. Google Flow permite referencias de voz
**Hallazgo oficial de Google Flow:** en generaciones con Ingredients se pueden añadir referencias de voz, crear una voz personalizada, describir su Voice Performance y referenciarla mediante `@Voice`.
**Aplicación:** crear una voz personalizada guardada como **Mako**, probarla primero con el preview de voz y reutilizarla en clips posteriores. Esto debe preferirse a intentar fijar el timbre únicamente con texto en cada generación.
**Regla de ahorro de créditos:** validar la voz antes del video.

### 29. Nuevo ADN de guion confirmado por muestras
**Observación:** el estilo buscado funciona mejor cuando una situación normal recibe una respuesta absurda dicha con absoluta seriedad. El personaje no “cuenta” el chiste ni se ríe.
**Regla nueva:** pregunta/reclamo normal → respuesta breve → objeción → Mako redobla la lógica absurda → remate seco. No es obligatorio usar todos los pasos si el remate llega antes.
**Para 10 s:** usar normalmente 4–6 intervenciones breves, una sola idea cómica y cero explicación innecesaria.

### 30. Mako debe estar vivo aunque permanezca en el mismo lugar
**Observación:** Mako puede verse demasiado rígido si solo mueve la boca o las manos.
**Regla nueva:** permitir cambios sutiles de peso, micro-movimientos de pies/talones, hombros, cabeza y postura, sin desplazarse ni abandonar su soporte. Toda acción principal sigue ligada al diálogo.

### 31. Acción reconocible, no pose aleatoria
**Problema:** al nombrar un trend como `farmear aura`, Flow puede no ejecutar una pose útil si solo se menciona el nombre.
**Regla nueva:** describir biomecánica completa. Si una línea introduce la acción (`Este es el siguiente ejercicio.`), terminar la frase y entrar inmediatamente en la pose sin pausa muerta.

### 32. Prompt visual de gimnasio aprobado
**Resultado:** la estructura actual del prompt de Flow para Mako entrenador funciona correctamente en identidad visual, cámara, pose y ownership de diálogo.
**Regla nueva:** no rehacer ese prompt desde cero; cuando el resultado visual ya es correcto, hacer cambios mínimos y aislados.

### 33. No dejar cola muerta al final del clip
**Síntoma:** una generación terminó narrativamente cerca de 8.8 s y dejó alrededor de 1–1.2 s sin acción útil.
**Corrección:** diseñar el último intercambio para terminar cerca de 9.6–9.9 s, dejando solo unas décimas de cierre visual.
**Regla nueva:** en clips de 10 s, medir el guion para aprovechar casi todo el tiempo disponible. Si sobran 1–2 s, añadir un remate ultracorto útil antes que una pose vacía prolongada.

### 34. Risitas automáticas de Flow no son parte del estilo
**Síntoma:** Flow añadió risas/chuckles al final aunque el guion no las pedía.
**Corrección:** prohibir explícitamente laughter, chuckles, giggles, audience laughter, comedy reactions, ad-libs y post-dialogue vocalizations.
**Regla nueva:** Los Chapumakos no llevan risas automáticas. El humor debe quedar seco.

### 35. Voz de Mako sigue sin estar aprobada
**Síntoma:** cambiar edad/gravedad/ronquera no ha producido todavía la identidad deseada.
**Diagnóstico:** demasiada énfasis en `old/deep/hoarse` empuja a voz de abuelo o narrador; lo buscado parece depender más de colocación nasal, sequedad, grit/rasp, fry ligero, articulación cotidiana y cadencia de barrio.
**Nueva estrategia:** calibrar la voz fuera del video y cambiar una sola variable por prueba. Base sugerida: hombre mexicano 40–50, barítono medio no profundo, fuerte resonancia nasal frontal, tono seco ligeramente pinzado, borde gritty/rasp natural, vocal fry leve al final, articulación relajada, picardía y colmillo. Evitar `very hoarse`, `deep bass`, `elderly`.
**Regla de ahorro:** no usar créditos de video para buscar la voz. Aprobar primero la voz en pruebas aisladas y luego aplicarla a `@Voice: Mako`.

## 2026-09-17 — Baseline aprobado tras pruebas reales de Flow

### 36. La voz finalmente aprobada es más serena y menos “pícara rápida”
**Resultado:** el usuario aprobó la voz obtenida con una descripción de hombre mexicano de barrio de aproximadamente 40–50 años, voz media, claramente raspada/seca, algo granulada, ligeramente nasal hacia el frente, calmada, serena, relajada y no acelerada.
**Regla nueva:** esta dirección SUPERA las descripciones históricas de 60–70/deep baritone y también la idea de `quick confident delivery`. Mako no debe sonar como abuelo ni como pícaro acelerado. Su identidad actual es seria, tranquila, raspada, natural, de barrio y con colmillo.

### 37. Speaker lock más fuerte: enumerar frases permitidas
**Síntoma:** Flow seguía haciendo que Mako hablara líneas del cliente aun con ownership general.
**Corrección aprobada:** declarar `There are EXACTLY TWO voices` y enumerar literalmente qué frases puede decir cada voz. Además, dentro de cada bloque del cliente repetir que Mako no produce voz, mantiene la boca cerrada y no hace lip-sync.
**Regla nueva:** para clips Mako + cliente fuera de cámara, el prompt debe incluir lista explícita de líneas permitidas por hablante; no depender únicamente de `MAKO SPEAKS ONLY` / `CUSTOMER SPEAKS ONLY` global.

### 38. Lip-sync debe definirse como articulación continua
**Síntoma:** Mako podía hablar con la boca quieta o detener la articulación antes de terminar la frase.
**Corrección aprobada:** exigir movimiento visible de boca, mandíbula y hocico desde el primer fonema hasta la última sílaba, cerrando la boca solo después de terminar.
**Regla nueva:** este bloque debe conservarse en futuros prompts, especialmente para la última línea.

### 39. Silencios de Flow deben bloquear cualquier voz humana
**Síntoma:** en pausas sin diálogo aparecieron risas o sonidos humanos de fondo.
**Corrección aprobada:** además de prohibir risas, declarar que durante cada `NO DIALOGUE` no existe NINGUNA voz humana y que el silencio es intencional.
**Regla nueva:** ambiente solo no humano y muy discreto: room tone, ventilación y ruido no verbal mínimo. Prohibir radio, TV, noticiero, recorded speech, PA, podcast, conversaciones, voces lejanas, laugh track, chuckles, giggles y ad-libs.

### 40. Mako debe verse como mono real haciendo cosas humanas
**Síntoma:** algunas referencias parecían un humano vestido de mono o un personaje semirreal.
**Corrección aprobada:** insistir en `REAL SMALL CAPUCHIN MONKEY`, anatomía animal real, manos/pies de mono, peso, balance, gravedad e inercia reales; prohibir humanoid monkey, human in costume, mascot, CGI/cartoon behavior.
**Regla nueva:** la prioridad visual es “mono real primero, personaje/trabajador después”. Los actos humanos deben ser ejecutados por un cuerpo de mono real.

### 41. Párpados a medio ojo son identidad permanente
**Resultado:** el usuario confirmó que los párpados semicerrados transmiten tranquilidad y confianza y deben mantenerse siempre.
**Regla nueva:** proteger `HALF-LOWERED / HALF-CLOSED EYELIDS` en reference lock, actuación y cierre. No abrir los ojos ampliamente salvo petición expresa.

### 42. Objetos en mano no pueden desaparecer al iniciar una acción
**Síntoma:** la tabla que Mako sostenía desaparecía mágicamente cuando entraba en la pose.
**Corrección aprobada:** resolver físicamente el objeto antes de la acción: bajar → colocar sobre superficie lógica → soltar → mantener visible y quieto.
**Regla nueva:** si Mako necesita liberar una mano, describir explícitamente el destino del objeto. Preferir colocar/apoyar antes que lanzar para reducir fallos de física.

### 43. Cada nuevo clip con nueva imagen se escribe como prompt independiente
**Corrección de proceso:** aunque narrativamente sea “segunda parte”, si el usuario dará una nueva imagen de referencia, NO usar `continue`, `Part 1`, `same final state` ni asumir estado del clip anterior.
**Regla nueva:** tratar la nueva imagen como autoridad absoluta del primer frame y redactar un prompt completo e independiente. Solo usar continuidad textual si el usuario la pide expresamente.

### 44. El remate físico puede cerrar mejor que más diálogo
**Resultado aprobado:** después de la lógica absurda, Mako puede cerrar con una acción simple, seria y coherente. Ejemplo aprobado: `Son quinientos pesos.` mientras extiende una mano vacía, palma arriba, cobrando al cliente sin sonreír.
**Regla nueva:** cuando funcione, reservar 0.3–0.5 s finales para sostener la acción del remate. La acción debe ser simple, anatómicamente creíble y sincronizada con la línea.

### 45. No reescribir un baseline que ya funciona
**Resultado:** el prompt independiente con reference lock + realismo animal + voz aprobada + speaker lock enumerado + lip-sync continuo + silencios estrictos + timeline funcionó muy bien.
**Regla de ahorro de créditos:** este conjunto pasa a ser baseline. En futuros clips cambiar diálogo, timing y acciones necesarias, pero conservar intactos los bloques que ya resolvieron voz, realismo, separación de hablantes, lip-sync y audio.

## Regla de mantenimiento
Cada nuevo error real debe documentarse aquí con:
- fecha
- episodio
- síntoma
- causa probable
- corrección aplicada
- regla nueva o modificada

## 2026-09-18 — Cruce de voces en Google Flow

### 46. Separación dura entre cambios de hablante
**Síntoma:** en algunos clips Google Flow empieza la voz del siguiente hablante antes de que termine completamente la voz anterior, aunque el ownership de líneas sea correcto.

**Causa probable:** los bloques temporales quedan demasiado pegados y Flow estira ligeramente la duración real de una frase, provocando solapamiento en el cambio de hablante.

**Corrección:** entre CADA cambio de hablante insertar un bloque explícito de `NO DIALOGUE` de aproximadamente 0.3–0.5 s. Dentro de ese bloque declarar `BOTH VOICES COMPLETELY SILENT` y `The previous speaker's voice must be fully finished before the next speaker begins`.

**Regla nueva:** nunca colocar un turno de MAKO inmediatamente adyacente a un turno del CUSTOMER ni viceversa. Todo cambio de hablante debe tener una pequeña zona muerta de audio. Los bloques pueden tocarse solo si es el mismo hablante.

**Refuerzo global:** añadir al speaker lock:
- `NO OVERLAP UNDER ANY CIRCUMSTANCE.`
- `One voice must be completely finished before the other voice begins.`
- `Do not extend any spoken line beyond its assigned timestamp block.`
- `Do not start the next spoken line early.`

**Regla de ahorro de créditos:** cuando el problema sea cruce de voces, NO cambiar las voces ni reescribir el baseline. Corregir únicamente separación temporal y bloqueo de overlap.


## 2026-09-18 — Fallback económico cuando Flow cruza voces

### 47. Si dos voces siguen fallando, sacar al cliente del audio generado
**Síntoma:** aun con speaker lock, pausas duras y líneas más cortas, Google Flow puede cruzar turnos o cambiar la identidad vocal de Mako.

**Impacto:** cada reintento cuesta créditos; repetir pruebas del mismo fallo deja de ser económicamente aceptable.

**Corrección robusta:** si una escena Mako + cliente fuera de cámara falla por cruce de voces o voz incorrecta después de una versión bien estructurada, NO seguir añadiendo instrucciones al prompt ni regenerando a ciegas. Generar en Flow SOLO la voz de Mako y la actuación visual completa. Los turnos del cliente se representan como bloques temporales de silencio con reacción de Mako, y la voz del cliente se añade después en edición.

**Regla nueva de producción:** para preservar créditos, el modo de mayor estabilidad es:
- Flow genera visual + voz de Mako solamente;
- durante los futuros turnos del cliente: `NO GENERATED SPEECH`, boca de Mako cerrada y reacción visual;
- mantener huecos temporales exactos para insertar la voz del cliente en Filmora/edición;
- cero segunda voz generada en Flow;
- si la voz de Mako ya funcionó, conservar exactamente su descriptor aprobado.

**Regla de ahorro de créditos:** después de comprobar un fallo persistente de speaker crossing, el siguiente intento debe usar el modo de una sola voz, no otra variación de prompt con dos voces.


## 2026-09-18 — Corrección basada en dos prompts confirmados por el usuario

### 48. Los prompts que SÍ funcionan no usan pausa dura en cada cambio de hablante
**Evidencia confirmada por el usuario:** dos prompts distintos funcionaron correctamente en Google Flow: el clip de pozole y el primer clip del iPhone.

**Hallazgo importante:** ambos prompts permiten cambios de hablante directamente adyacentes en algunos puntos del timeline. Por lo tanto, la regla 46 de insertar obligatoriamente 0.3–0.5 s de silencio entre CADA cambio de hablante queda INVALIDADA como regla universal.

**Nueva regla:** conservar exactamente la arquitectura del prompt que ya funcionó para esa escena. No introducir pausas adicionales, locks nuevos, ni redundancias no presentes en el baseline funcional salvo que un error específico lo requiera.

### 49. No reforzar la voz aprobada con descripciones nuevas
**Hallazgo:** los prompts funcionales usan el descriptor oficial de Mako sin capas extra de `same man / same pitch / same timbre / do not generate a new voice`.
**Nueva regla:** cuando un prompt ya produjo la voz correcta, copiar el bloque vocal literalmente. No añadir nuevas restricciones acústicas ni reformularlo, porque eso puede hacer que Flow reinterprete la identidad vocal.

### 50. Para segunda parte del mismo concepto, usar el prompt funcional del primer clip como plantilla literal
**Nueva regla:** si el primer clip de una escena ya funcionó, el siguiente clip debe derivarse de ESE prompt funcional, no de una versión posterior “mejorada”. Cambiar únicamente:
- líneas permitidas;
- timeline estrictamente necesario;
- acciones nuevas;
- cierre físico.
Todo lo demás debe permanecer textual y estructuralmente igual.

### 51. Regla 47 — fallback de una sola voz NO aplica si el usuario requiere audio completo en Flow
**Corrección:** la estrategia de una sola voz + edición externa no debe proponerse como solución principal cuando el usuario necesita las dos voces dentro de Flow. Solo usarla si el usuario la pide expresamente.


## 2026-09-18 — Fallo crítico confirmado: Flow reasigna la voz off-screen a Mako

### 52. Un solo personaje visible + voz off-screen no es confiable en esta configuración
**Síntoma confirmado:** en la segunda parte del video del iPhone, durante los turnos del cliente fuera de cámara, Google Flow hizo hablar a Mako en su lugar.

**Condiciones de la escena:** una sola toma, cámara fija, un solo personaje visible, sin cambios de escena, movimiento mínimo y diálogo corto.

**Conclusión operativa:** en esta configuración, el prompt textual por sí solo NO garantiza que una voz off-screen sea mantenida separada del único rostro visible. Flow puede reasignar el diálogo del cliente al personaje visible aunque el ownership esté explicitado.

**Regla nueva de ahorro de créditos:** NO volver a gastar créditos intentando resolver este fallo únicamente con nuevas variaciones de prompt textual. Si el usuario exige dos voces completas dentro de Flow, se debe considerar esta combinación no confiable hasta contar con un mecanismo de voz/referencia que fije de forma real la identidad de cada hablante.

**Importante:** no interpretar este fallo como falta de detalle del prompt. Añadir más restricciones, pausas, labels o redundancia NO ha demostrado resolverlo de forma consistente.

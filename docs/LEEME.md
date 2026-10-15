# Harness de agente

Skills, tools, contexto, dispatch controlado, recuperación, caché y ejecución durable.

## Ver el frontend

Demos guiadas del frontend con datos ficticios: chat, configuración de agentes y memoria del negocio. Son recorridos con guion de la generación anterior del producto; la implementación del harness se documenta más abajo.

### Creación de agentes personalizados · 85s

https://github.com/user-attachments/assets/418023e3-7c39-4082-ba8b-140ba44dab4a

[Abrir la demo a pantalla completa](https://chalsai.com/demo.html?script=custom-agents&utm_source=github&utm_medium=portfolio&utm_campaign=ai-agent-harness) · [Descargar MP4](demos/custom-agents.mp4)

### Memoria y contexto del negocio · 18s

https://github.com/user-attachments/assets/f6010d59-6e71-4ab9-a506-86d2e1059547

[Abrir la demo a pantalla completa](https://chalsai.com/demo.html?script=memory-brain&utm_source=github&utm_medium=portfolio&utm_campaign=ai-agent-harness) · [Descargar MP4](demos/memory-brain.mp4)

[Procedencia de los vídeos](demos/manifest.json).

## Qué demuestra este caso

El harness completo requiere Agents SDK, registros internos y servicios de runtime. La demo verifica la construcción local de claves de caché, sin llamar a un LLM.

**Resultado del proyecto:** Implementación histórica demostrable; la ejecución completa desde cada host no se acredita con esta muestra.

## Probar el componente

Requiere Python 3.10 o posterior. No necesita instalar dependencias, introducir claves ni conectar una cuenta.

```sh
python3 -I demo.py
```

La demo usa datos sintéticos y rechaza conexiones de red y subprocesos. Verifica 5 comportamientos del código original. [Resultados](../verification.json).

## Recorrido del código

[source/sample.py](../source/prompt_cache.py) es la muestra ejecutable. Módulo original completo, sin cambios. [Procedencia completa](../provenance.json).

- [E12 Ensamblaje del agente, sesión de skills y contexto de runtime](../evidence/E12.md)
- [E13 Discovery, validación, catálogo y ciclos de co-loading](../evidence/E13.md)
- [E14 Estado de skills, precondiciones y superficie activa de tools](../evidence/E14.md)
- [E15 Dispatch, autorización de skill, contratos y recuperación de bucles](../evidence/E15.md)
- [E16 Streaming, trazas y gate de presupuesto de contexto](../evidence/E16.md)
- [E17 Prompt cache por prefijo estable, canal y versión](../evidence/E17.md)
- [E18 Runs/eventos Firestore, claims, secuencia y heartbeat](../evidence/E18.md)
- [E39 Sandbox implementado y desactivado por defecto](../evidence/E39.md)

## Alcance

Este caso conserva una selección de una construcción mayor. Los identificadores de infraestructura y clientes se han anonimizado donde corresponde; la procedencia registra las modificaciones. Para ejecutarla completa se necesitarían sus adaptadores y servicios; esta muestra no despliega ni modifica Chals AI.

[Portada en inglés](../README.md) · [Arquitectura](architecture.md) · [Decisiones](decisions.md) · [Recorrido del código](code-tour.md).

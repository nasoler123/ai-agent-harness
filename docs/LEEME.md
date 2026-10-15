# Harness de agente

Skills, tools, contexto, dispatch controlado, recuperación, caché y ejecución durable.

## Ver el agente

**Chals AI — AI Assistant for Google Sheets.** El asistente dentro de la interfaz de la hoja de cálculo. La muestra Python de este repositorio se centra en la construcción de claves de caché.

[![Reproducir Chals AI — AI Assistant for Google Sheets](https://i.ytimg.com/vi/Oo4Bd8iGeUY/hqdefault.jpg)](https://www.youtube.com/watch?v=Oo4Bd8iGeUY)

[Ver en YouTube](https://www.youtube.com/watch?v=Oo4Bd8iGeUY) · [Procedencia del vídeo](demos/manifest.json).

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

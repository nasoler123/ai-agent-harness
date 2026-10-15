# Harness de agente de IA

**La capa de ejecución del asistente de Chals AI**

*Un caso de Chals AI — construido por Ignacio Soler.*

Construí la capa de ejecución que conecta un asistente de IA con skills, herramientas y capacidades de la aplicación. Gestiona qué herramientas están disponibles, cómo se ejecutan las llamadas, cómo se prepara el contexto y cómo se resuelven los fallos y reintentos.

Construí este proyecto yo solo, de principio a fin, utilizando herramientas de IA para toda la programación. Me encargué de la definición del producto, las decisiones técnicas, la implementación, la integración y la validación.

[Ver el agente](#ver-el-agente) · [Explorar la implementación](#explorar-la-implementación) · [Probar el componente](#probar-el-componente) · [English](../README.md)

## Qué construí

- Carga de skills, controles de capacidades y ejecución de herramientas.
- Gestión del presupuesto de contexto y construcción de claves de caché de prompts.
- Lógica de recuperación y persistencia de eventos de ejecución.

**Estado:** Implementado entre mayo y julio de 2026 como parte de una generación anterior de Chals AI.

## Ver el agente

**Chals AI — AI Assistant for Google Sheets.** Este vídeo de producto muestra el asistente dentro de Google Sheets. El material técnico de abajo recoge componentes seleccionados de la implementación del agente.

[![Reproducir Chals AI — AI Assistant for Google Sheets](https://i.ytimg.com/vi/Oo4Bd8iGeUY/hqdefault.jpg)](https://www.youtube.com/watch?v=Oo4Bd8iGeUY)

[Ver en YouTube](https://www.youtube.com/watch?v=Oo4Bd8iGeUY) · [Procedencia del vídeo](demos/manifest.json).

![Arquitectura de Harness de agente de IA](overview.svg)

## Explorar la implementación

El componente ejecutable contiene el constructor original de claves locales de caché de prompts. Los extractos de código documentan el trabajo más amplio: carga de skills, ejecución de herramientas, gestión de contexto, recuperación y persistencia de eventos.

| Recurso | Qué puedes consultar |
|---|---|
| [prompt_cache.py](../source/prompt_cache.py) | Componente original ejecutable |
| [demo.py](../demo.py) | Datos sintéticos y 5 comportamientos comprobados |
| [Arquitectura](architecture.md) | Sistema completo y alcance de la muestra |
| [Decisiones de diseño](decisions.md) | Decisiones y referencias al código |
| [Recorrido del código](code-tour.md) | 8 extractos seleccionados de la implementación |
| [Procedencia](../provenance.json) | Rutas originales, commits, hashes y modificaciones documentadas |

<details>
<summary>Ver los extractos seleccionados</summary>

- [E12 Ensamblaje del agente, sesión de skills y contexto de runtime](../evidence/E12.md)
- [E13 Discovery, validación, catálogo y ciclos de co-loading](../evidence/E13.md)
- [E14 Estado de skills, precondiciones y superficie activa de tools](../evidence/E14.md)
- [E15 Dispatch, autorización de skill, contratos y recuperación de bucles](../evidence/E15.md)
- [E16 Streaming, trazas y gate de presupuesto de contexto](../evidence/E16.md)
- [E17 Prompt cache por prefijo estable, canal y versión](../evidence/E17.md)
- [E18 Runs/eventos Firestore, claims, secuencia y heartbeat](../evidence/E18.md)
- [E39 Sandbox implementado y desactivado por defecto](../evidence/E39.md)

</details>

**Tecnologías del proyecto:** Python · OpenAI Agents SDK · skills / tools · prompt caching · Firestore · Cloud Tasks.

Este caso público incluye código original seleccionado y una muestra ejecutable aislada con datos sintéticos. Las integraciones de producción y los datos de clientes se mantienen privados. Las rutas originales, commits, hashes y modificaciones se registran en [provenance.json](../provenance.json).

## Probar el componente

Ejecuta localmente el constructor original de claves locales de caché de prompts con datos sintéticos. Requiere **Python 3.10 o posterior**, sin instalar dependencias ni conectar una cuenta. Ejecuta estos comandos desde la terminal:

```sh
git clone https://github.com/nasoler123/ai-agent-harness.git
cd ai-agent-harness
python3 -I demo.py
python3 verify.py
```

Resultados esperados:

- Repetir las entradas o cambiar el orden de las mismas skills conserva la clave.
- Cambiar las capacidades, el canal o el contenido del prompt cambia la clave.
- La muestra no llama a un modelo ni mide la tasa de aciertos de caché.

La muestra funciona sin conexión y rechaza conexiones de red y subprocesos externos. `verify.py` comprueba enlaces locales, igualdad de instrucciones, hash del código, patrones de credenciales y coincidencia con los resultados registrados de las comprobaciones del componente. [Resultados registrados](../verification.json).

## Más proyectos de Chals AI

Estos proyectos recogen mi trabajo en automatización de negocio, software financiero, agentes de IA e infraestructura de datos.

[Data Platform and MCP](https://github.com/nasoler123/data-platform-mcp) · [Financial Modeling SaaS](https://github.com/nasoler123/financial-modeling-saas) · [Invoice Automation](https://github.com/nasoler123/invoice-automation)

[Ignacio Soler](https://github.com/nasoler123) · [LinkedIn](https://www.linkedin.com/in/ignacio-soler-esteban/)

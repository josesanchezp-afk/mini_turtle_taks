# Mini Turtle Task

Un módulo simple en Python que simula dibujos de Turtle Graphics en la consola usando texto ASCII.

## Descripción

Este proyecto proporciona funciones básicas para dibujar patrones en la consola, simulando movimientos de una tortuga (turtle) con líneas horizontales y verticales. Es útil para aprender conceptos básicos de programación modular y gráficos simples.

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. Clona o descarga este repositorio en tu máquina local.

3. Navega al directorio del proyecto:
   ```
   cd mini_turtle_taks
   ```

## Uso

### Ejecutar el ejemplo

Para ver un ejemplo de uso, ejecuta el archivo `main.py`:

```
python main.py
```

Esto dibujará un patrón de escalones en la consola.

### Usar las funciones

Importa las funciones desde el módulo `mini_turtle_task`:

```python
from mini_turtle_task import derecha, abajo, reiniciar
```

#### Funciones disponibles:

- `derecha(n)`: Dibuja una línea horizontal de longitud `n` hacia la derecha, terminando con una flecha `>`.
- `abajo(n)`: Dibuja `n` líneas verticales hacia abajo, terminando con una flecha `V`. Cada llamada aumenta el nivel de indentación.
- `reiniciar()`: Reinicia el contador de escalones, volviendo a la posición inicial.

#### Ejemplo de uso personalizado:

```python
from mini_turtle_task import derecha, abajo, reiniciar

# Dibujar un cuadrado simple
derecha(5)
abajo(5)
derecha(5)
abajo(5)
reiniciar()
```

## Estructura del proyecto

- `main.py`: Archivo principal con un ejemplo de uso.
- `mini_turtle_task/`: Paquete del módulo.
  - `__init__.py`: Inicialización del paquete.
  - `drawer_logic.py`: Lógica de dibujo de las funciones.

## Licencia

Este proyecto está bajo la licencia especificada en el archivo `LICENSE`.

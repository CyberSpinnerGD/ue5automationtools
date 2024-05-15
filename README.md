# Scripts de Automatización para Unreal Engine 5.3

Este repositorio contiene scripts de automatización en UE5.3
Desarrollados durante  periodo formativo impartido por el artisa técnico Karol Kowalczyk (CD Projeck Red) 


## Índice

1. [fix_textures_compression.py](#fix_textures_compressionpy)
2. [instance_material_vector_set.py](#instance_material_vector_setpy)

---

## 🖼️ fix_textures_compression.py

**Validador de Compresión**

**Autor:** Daniel Dorado 2024

**Propósito:** Automatizar los ajustes de compresión para diferentes tipos de texturas en Unreal Engine 5.3.

| Función | Parámetros | Descripción |
| ------- | ---------- | ----------- |
| `validate_compression_settings` | `directory: str, apply_fix: bool = True` | Valida y opcionalmente corrige los ajustes de compresión de las texturas en el directorio especificado. |

### Detalles de la Función

- **validate_compression_settings(directory: str, apply_fix: bool = True):**
  - **Parámetros:**
    - `directory` (str): El directorio que contiene las texturas a validar.
    - `apply_fix` (bool): Si es `True`, la función aplicará los ajustes de compresión correctos a las texturas con configuraciones incorrectas.
  - **Descripción:** Lista todas las texturas en el directorio especificado, verifica si sus nombres coinciden con los sufijos de compresión predefinidos y asegura que sus ajustes de compresión sean correctos. Si los ajustes son incorrectos y `apply_fix` es `True`, corrige los ajustes.

---

## 🎨 instance_material_vector_set.py

**Configurador de Parámetros Vectoriales de Instancia de Material**

**Propósito:** Modificar los parámetros vectoriales de una instancia de material en Unreal Engine 5.3.

| Función | Parámetros | Descripción |
| ------- | ---------- | ----------- |
| `set_instance_mat_vtr` | `material_inst: unreal.MaterialInstanceConstant, param_name: unreal.Name, value` | Establece un parámetro vectorial en una instancia de material. |

### Detalles de la Función

- **set_instance_mat_vtr(material_inst: unreal.MaterialInstanceConstant, param_name: unreal.Name, value):**
  - **Parámetros:**
    - `material_inst` (unreal.MaterialInstanceConstant): La instancia de material a modificar.
    - `param_name` (unreal.Name): El nombre del parámetro vectorial a establecer.
    - `value` (list): El nuevo valor para el parámetro vectorial.
  - **Descripción:** Establece el parámetro vectorial especificado en la instancia de material dada y devuelve `True` si el cambio es exitoso.

- **Uso:**
  - Carga el asset de instancia de material especificado.
  - Restaura todos los parámetros de la instancia de material para evitar conflictos.
  - Establece nuevos valores para los parámetros vectoriales especificados.
  - Actualiza la instancia de material para aplicar los cambios.

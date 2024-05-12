# Compression Validator
# Author: Daniel Dorado 2024
# Proposito: Automatizar los settings de compresion de distintos tipos de texturas en UE5.3
# ===========================================================

import unreal

#Importamos la asset library
AssetLibrary = unreal.EditorAssetLibrary()

#Mapeamos sufijos de nombre de archivos de texturas con su correspondiente tipo de compresion
COMPRESSION_MAPPING = {
    "_N": unreal.TextureCompressionSettings.TC_NORMALMAP, # normalMap
    "_D": unreal.TextureCompressionSettings.TC_DEFAULT, # albedo/diffuse
    "_E": unreal.TextureCompressionSettings.TC_DEFAULT, # emissve
    "_M": unreal.TextureCompressionSettings.TC_GRAYSCALE, # metalness
    "_R": unreal.TextureCompressionSettings.TC_GRAYSCALE # roughness
}

def validate_compression_settings(directory: str, apply_fix: bool = True):
    

    #Listamos todas las texturas, desactivamos la recursividad
    asset_path_lst = AssetLibrary.list_assets(directory , recursive=False)

    #Por cada asset en la lista comprobamos si es una Textura2D
    for asset_path in asset_path_lst:

        #Dividimos cada asset_path  y nos quedamos solo con el nombre para evitar Warnings por deprecacion.
        package_name = asset_path.split('.')[0]


        #Carga del asset 
        texture = AssetLibrary.load_asset(package_name)
        
        #Obtengo el nombre de la textura
        textureName = str(texture.get_fname())
        
        #Comprobamos que no vamos a coger assets que no sean una Texture2D
        if not isinstance(texture , unreal.Texture2D):
            continue
        
        #Booleano para comprobar si el nombre coincide con el sufijo de compresion
        textureName_match = False
        #Objeto con el valor de compresion a aplicar
        correct_compression = None

        #Iteramos por cada sufijo definido
        #Si la textura concuerda ponemos el booleano a true y obtenemos el valor de compresion correcto para ese sufijo
        #Después salimos con break ya que no necesitamos seguir iterando (hay un solo valor correcto y ya ha sido encontrado)
        for suffix in COMPRESSION_MAPPING.keys():
            if textureName.endswith(suffix):
                textureName_match = True
                correct_compression = COMPRESSION_MAPPING[suffix]
                break
        if not textureName_match:
            continue
        
        
       
        #Sacamos por pantalla las texturas encontrads
        print(f"Textura encontrado: {textureName}")
        #Obtenemos la compresion actual de cada NormalMap (objeto)
        current_compression = texture.get_editor_property("compression_settings")
        #Checkeamos si la compresion actual de cada textura no corresponde a la que deberia tener (definido en COMPRESSION_MAPPING)
        if current_compression != correct_compression:
            print(f"Detectada Compresion Erronea: {textureName} -> {str(current_compression)}")
            
            #Seteamos el tipo de compresion a la adecuada si el parametro apply_fix es true
            if apply_fix:
                print(f"Corrigiendo compresion: {textureName} -> {str(correct_compression)}")
                texture.set_editor_property(name="compression_settings", value=correct_compression)

#MAIN
if __name__ == "__main__":
    validate_compression_settings(directory="/Game/StarterContent/Textures/")
    


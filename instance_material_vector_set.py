import unreal

#Cargamos EditorAssetLibrary
EAL = unreal.EditorAssetLibrary()
#Cargamos MaterialEditingLibrary
MEL = unreal.MaterialEditingLibrary()



#Wrapper para cambiar un parametro de instancia de material
def set_instance_mat_vtr(material_inst: unreal.MaterialInstanceConstant, param_name: unreal.Name, value) -> bool:

    assert param_name in MEL.get_vector_param_names(material_inst),  f"{param_name} no esta en {material_inst}"
    
    #En esta linea hacemos dos cosas, cambiamos el parametro de la instancia
    #y dado que funcion set_material_inst_vector_parameter_value
    #devuelve true o false en base a si el cambio se ha producido o no
    #obtenemos tambien el resultado, mejorando asi el control de cambios
    return MEL.set_material_inst_vector_parameter_value(instance=material_inst,
                                                            param_name=param_name,
                                                            value=value
                                                            )

#Cargamos el asset de tipo Constant (se procesa antes del runtime si fuese dinamica seria al reves)
#nota sobre tipado
#varName #type                           #content
asset: unreal.MaterialInstanceConstant = EAL.load_asset(
    "/Game/StarterContent/Materials/material_instance")
#Con esta funcion reseteamos a defualt los parametros del material, asi evitamos conflictos si alguien ha tocado el material.
MEL.clear_all_material_inst_parameters(asset)

#llamamos al wraper y le pasamos los parametros que necesita
set_instance_mat_vtr(material_inst=asset, param_name="Emissive color 01", value=[0.2, 0.1, 0.1, 0.4])
set_instance_mat_vtr(material_inst=asset, param_name="Emissive color 02", value=[0.2, 0.1, 0.1, 0.4])

#Tras realizar cualquier cambio en una instancia de material
#Llamamos a esta funcion porque es recomendable recompilar siempre el material
MEL.update_material_inst(asset)

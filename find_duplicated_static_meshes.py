#Encontrar actors duplicados con la misma malla y en una posicion similar

import unreal

# Cargar el subsistema del editor y obtener todos los actores del nivel
EAS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
actors = EAS.get_all_level_actors()

# Lista que almacenara groups, aqui un group es una lista que comparte la misma malla.
actors_list_group: list = []
# Lista para almacenar los grupos que tienen dos o más actores
# Los grupos que solo contengan 1, son correctos por lo que no es necesario almacenarlos para elminar duplicidades.
duplicated_actors_list_groups: list = []

# Iterar sobre cada actor
for actor in actors:
    # Filtrar solo los StaticMeshActor
    if not isinstance(actor, unreal.StaticMeshActor):
        continue
    
    print(f"Revisando actor: {actor.get_name()}")

    found = False
    # Buscar un grupo con la misma malla estática
    #Itero por cada sublista dentro de la lista principal
    #Si la malla de de ese actor coincide con la maya de alguna sublista ya creada, la agrego a la propia sublista.
    for sublist in actors_list_group:
        if actor.static_mesh_component.static_mesh.get_full_name() == \
                sublist[0].static_mesh_component.static_mesh.get_full_name():
            print(f"Actor {actor.get_name()} usa la misma malla que el grupo existente.")
            sublist.append(actor)
            found = True
            break
    
    # Si la malla es nueva, entonces creo una nueva sublista por la que iterar.
    if not found:
        print(f"Creando un nuevo grupo para el actor: {actor.get_name()}")
        actors_list_group.append([actor])

#Imprimimos informacion por pantalla
for i, sublist in enumerate(actors_list_group):
    print(f"\nSublista: {i + 1}:")
    for actor in sublist:
        print(f" - {actor.get_name()} (Malla: {actor.static_mesh_component.static_mesh.get_name()})")

#Ahora itero por cada sublista, y las que tienen 2 o mas elementos, son duplicadas.
#Por lo que las agrego a la lista: duplicated_actors_list_groups 
print(f"\nMeshes Duplicados:")
for sublist in actors_list_group:
    if len(sublist) >= 2:
        print(f"\nMesh: {sublist[0].static_mesh_component.static_mesh.get_full_name()}")
        duplicated_actors_list_groups.append(sublist)
        


#BLOQUE QUE ME CUESTA COMPRENDER
duplicate_groups: list = []

#Iteramos por cada grupo de acotores duplicados
for actors_groups in duplicated_actors_list_groups:
    matched_indexes = []


    for i in range(len(actors_groups) -1, -1, -1):
        if i in matched_indexes:
            continue

        current = actors_groups[i]
        nearby_actors = [current]
        actors_groups.pop(i)

        for j in range(len(actors_groups) -1, -1, -1):
            if j in matched_indexes:
                continue
            comparing_to = actors_groups[j]
            if current.get_actor_transform().is_near_equal(comparing_to.get_actor_transform()):
                nearby_actors.append(comparing_to)
                matched_indexes.append(j)

        if len(nearby_actors) > 1:
            duplicate_groups.append(nearby_actors)
#Print resultados
for actors_groups in duplicate_groups:
    print(20 * "-")
    for actor in actors_groups:
        print(f"Meshes Solapados: {actor.get_actor_label()}")
        print(20 * "-")
        print(f"Translation: {actor.get_actor_transform().translation}")
        print(20 * "-")
        

import unreal

#turning_deck = unreal.load_object(None, "/Game/NewWorld.NewWorld:PersistentLevel.Sphere_2")
#print (turning_deck)
#floor_binding = sequence.add_possessable(turning_deck)

'''
actors = unreal.EditorLevelLibrary.get_selected_level_actors()
print (actors[0].get_path_name())
'''



'''
https://docs.unrealengine.com/4.26/en-US/PythonAPI/class/_ObjectBase.html#unreal._ObjectBase
'''



            

# open widget
path = "/TechArtTool_TurnTableScene/EUW_TurnTableQuickConfig"
unreal.EditorUtilitySubsystem().spawn_and_register_tab(unreal.EditorAssetLibrary.load_asset(path))



#World'/TechArtTool_TurnTableScene/Version2/Version2.Version2'
#D:/p4/plugins/TechArtTools/Plugins/TechArtTool_TurnTableScene/Content/Version2/Version2.umap
#unreal.Paths.project_plugins_dir()


#binding = unreal.SequencerTools.get_object_bindings
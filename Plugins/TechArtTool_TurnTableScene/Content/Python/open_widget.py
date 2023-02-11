import unreal

# open widget
# path = "/TechArtTool_TurnTableScene/TurnTableQuickConfig"
path = "/TechArtTool_DecalAssistant/DecalAssistant"
if unreal.EditorAssetLibrary.does_asset_exist(path):
    unreal.EditorUtilitySubsystem().spawn_and_register_tab(unreal.EditorAssetLibrary.load_asset(path))
else:
    unreal.log_error("no widget!")
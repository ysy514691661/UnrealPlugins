import unreal

# open MASTER

sequencer = unreal.EditorAssetLibrary.load_asset('/TechArtTool_TurnTableScene/SequencerMaster.SequencerMaster')

print (sequencer)
unreal.log_warning("Sequencer opened :)")

editor_sys = unreal.AssetEditorSubsystem()
editor_sys.open_editor_for_assets([sequencer]) 


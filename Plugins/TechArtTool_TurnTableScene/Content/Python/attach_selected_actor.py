import unreal
import sequencer_examples

# model_ref = "/TechArtTool_TurnTableScene/Version2/TestLevel.TestLevel:PersistentLevel.SM_Chair_2"

#turning_deck_ref = "/TechArtTool_TurnTableScene/TurnTableLevel.TurnTableLevel:PersistentLevel.BP_TurningDeck"
#turning_deck = unreal.load_object(None, turning_deck_ref)

actors = unreal.EditorLevelLibrary.get_selected_level_actors()

if len(actors)  == 0:    
    unreal.log_warning("please select actor!")    
        
else:
    # open/refresh MASTER
    #sequencer = unreal.EditorAssetLibrary.load_asset('/TechArtTool_TurnTableScene/SequencerMaster.SequencerMaster')
    sequencer = unreal.LevelSequenceEditorBlueprintLibrary.get_current_level_sequence()

    # print (sequencer)
    editor_sys = unreal.AssetEditorSubsystem()
    editor_sys.open_editor_for_assets([sequencer])    
     

    model_ref = actors[0].get_path_name()
    model = unreal.load_object(None, model_ref)
    model_binding = sequencer.add_possessable(model)
    
    track = model_binding.add_track(unreal.MovieScene3DAttachTrack)
    #track.set_editor_property("track_tint", unreal.Color(b=1, g=1, r=1, a=1))
    sequencer_examples.populate_binding(sequencer, model_binding, 1, 1000)
    print(track)
    
    #section = unreal.MovieScene3DConstraintSection()            
    #print(section)
    
    section = track.add_section() 
    section.set_start_frame_bounded(0)
    section.set_end_frame_bounded(0)     
    print(section)    

    sequencer_bindings = sequencer.get_bindings()
    
    #for i in bindings:
    #    print (i.get_display_name())        
                 
    constraint_binding_id = unreal.MovieSceneObjectBindingID()


    constraint_binding_id.set_editor_property("guid", sequencer_bindings[1].get_id())


    section.set_constraint_binding_id(constraint_binding_id)
    
        

                                       

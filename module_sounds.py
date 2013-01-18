from header_sounds import *

sounds = [
 ("click", sf_2d|sf_priority_9|sf_vol_3, ["drum_3.ogg"]),
 ("tutorial_1", sf_2d|sf_priority_9|sf_vol_7, ["tutorial_1.ogg"]),
 ("tutorial_2", sf_2d|sf_priority_9|sf_vol_7, ["tutorial_2.ogg"]),
 ("gong", sf_2d|sf_priority_9|sf_vol_7, ["s_cymbals.ogg"]),
 ("quest_taken", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_completed", sf_2d|sf_priority_9|sf_vol_8, ["quest_completed.ogg"]),
 ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_6, ["quest_succeeded.ogg"]),
 ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, ["drum_3.ogg"]),
 ("quest_failed", sf_2d|sf_priority_9|sf_vol_7, ["quest_failed.ogg"]),
 ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, ["quest_cancelled.ogg"]),
 ("rain", sf_2d|sf_priority_2|sf_vol_4|sf_looping, ["rain_1.ogg"]),
 ("money_received", sf_priority_5|sf_vol_4, ["coins_dropped_1.ogg"]),
 ("money_paid", sf_priority_5|sf_vol_4, ["coins_dropped_2.ogg"]),
 ("sword_clash_1", 0, ["sword_clank_metal_09.ogg","sword_clank_metal_09b.ogg","sword_clank_metal_10.ogg","sword_clank_metal_10b.ogg","sword_clank_metal_12.ogg","sword_clank_metal_12b.ogg","sword_clank_metal_13.ogg","sword_clank_metal_13b.ogg"]),
 ("sword_clash_2", 0, ["drum_3.ogg"]),
 ("sword_clash_3", 0, ["drum_3.ogg"]),
 ("sword_swing", sf_priority_12|sf_vol_8, ["s_swordSwing.wav"]),

 ("footstep_grass", sf_priority_1|sf_vol_4, ["footstep_1.ogg","footstep_2.ogg","footstep_3.ogg","footstep_4.ogg"]),
 ("footstep_wood", sf_priority_1|sf_vol_6, ["footstep_wood_1.ogg","footstep_wood_2.ogg","footstep_wood_4.ogg"]),
 ("footstep_water", sf_priority_3|sf_vol_4, ["water_walk_1.ogg","water_walk_2.ogg","water_walk_3.ogg","water_walk_4.ogg"]),
 ("footstep_horse", sf_priority_3|sf_vol_8, ["drum_3.ogg"]),
 ("footstep_horse_1b", sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1f", sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
 ("footstep_horse_2b", sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav"]),
 ("footstep_horse_2f", sf_priority_3|sf_vol_8, ["s_footstep_horse_2f.wav"]),
 ("footstep_horse_3b", sf_priority_3|sf_vol_8, ["s_footstep_horse_3b.wav"]),
 ("footstep_horse_3f", sf_priority_3|sf_vol_8, ["s_footstep_horse_3f.wav"]),
 ("footstep_horse_4b", sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav"]),
 ("footstep_horse_4f", sf_priority_3|sf_vol_8, ["s_footstep_horse_4f.wav"]),
 ("footstep_horse_5b", sf_priority_3|sf_vol_8, ["s_footstep_horse_5b.wav"]),
 ("footstep_horse_5f", sf_priority_3|sf_vol_8, ["s_footstep_horse_5f.wav"]),
 ("jump_begin", sf_priority_9|sf_vol_7, ["jump_begin.ogg"]),
 ("jump_end", sf_priority_9|sf_vol_5, ["jump_end.ogg"]),
 ("jump_begin_water", sf_priority_9|sf_vol_4, ["jump_begin_water.ogg"]),
 ("jump_end_water", sf_priority_9|sf_vol_4, ["jump_end_water.ogg"]),
 ("horse_jump_begin", sf_priority_9|sf_vol_4, ["horse_jump_begin.ogg"]),
 ("horse_jump_end", sf_priority_9|sf_vol_4, ["horse_jump_end.ogg"]),
 ("horse_jump_begin_water", sf_priority_9|sf_vol_5, ["jump_begin_water.ogg"]),
 ("horse_jump_end_water", sf_priority_9|sf_vol_5, ["jump_end_water.ogg"]),

 ("release_bow", sf_priority_10|sf_vol_5, ["release_bow_1.ogg"]),
 ("release_crossbow", sf_priority_10|sf_vol_7, ["release_crossbow_1.ogg"]),
 ("throw_javelin", sf_priority_10|sf_vol_5, ["throw_javelin_2.ogg"]),
 ("throw_axe", sf_priority_10|sf_vol_7, ["throw_axe_1.ogg"]),
 ("throw_knife", sf_priority_10|sf_vol_5, ["throw_knife_1.ogg"]),
 ("throw_stone", sf_priority_10|sf_vol_7, ["throw_stone_1.ogg"]),

 ("reload_crossbow", sf_priority_8|sf_vol_3, ["reload_crossbow_1.ogg"]),
 ("reload_crossbow_continue", sf_priority_4|sf_vol_6, ["put_back_dagger.ogg"]),
 ("pull_bow", sf_priority_10|sf_vol_4, ["pull_bow_1.ogg"]),
 ("pull_arrow", sf_priority_4|sf_vol_5, ["pull_arrow.ogg"]),

 ("arrow_pass_by", sf_priority_9|sf_vol_10, ["arrow_pass_by_1.ogg","arrow_pass_by_2.ogg","arrow_pass_by_3.ogg","arrow_pass_by_4.ogg"]),
 ("bolt_pass_by", sf_priority_9|sf_vol_10, ["bolt_pass_by_1.ogg"]),
 ("javelin_pass_by", sf_priority_9|sf_vol_10, ["javelin_pass_by_1.ogg","javelin_pass_by_2.ogg"]),
 ("stone_pass_by", sf_priority_9|sf_vol_9, ["stone_pass_by_1.ogg"]),
 ("axe_pass_by", sf_priority_9|sf_vol_10, ["axe_pass_by_1.ogg"]),
 ("knife_pass_by", sf_priority_9|sf_vol_10, ["knife_pass_by_1.ogg"]),
 ("bullet_pass_by", sf_priority_9|sf_vol_10, ["arrow_whoosh_1.ogg"]),

 ("incoming_arrow_hit_ground", sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_bolt_hit_ground", sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_javelin_hit_ground", sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_stone_hit_ground", sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_axe_hit_ground", sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_knife_hit_ground", sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_bullet_hit_ground", sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.ogg"]),

 ("outgoing_arrow_hit_ground", sf_priority_6|sf_vol_7, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_bolt_hit_ground", sf_priority_6|sf_vol_7,  ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_javelin_hit_ground", sf_priority_6|sf_vol_10, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_stone_hit_ground", sf_priority_6|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_axe_hit_ground", sf_priority_6|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("outgoing_knife_hit_ground", sf_priority_6|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_bullet_hit_ground", sf_priority_6|sf_vol_7, ["incoming_bullet_hit_ground_1.ogg"]),

 ("draw_sword", sf_priority_8|sf_vol_4, ["draw_sword.ogg"]),
 ("put_back_sword", sf_priority_6|sf_vol_4, ["put_back_sword.ogg"]),
 ("draw_greatsword", sf_priority_9|sf_vol_4, ["draw_greatsword.ogg"]),
 ("put_back_greatsword", sf_priority_6|sf_vol_4, ["put_back_sword.ogg"]),
 ("draw_axe", sf_priority_8|sf_vol_4, ["draw_mace.ogg"]),
 ("put_back_axe", sf_priority_6|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_greataxe", sf_priority_9|sf_vol_4, ["draw_greataxe.ogg"]),
 ("put_back_greataxe", sf_priority_6|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_spear", sf_priority_7|sf_vol_4, ["draw_spear.ogg"]),
 ("put_back_spear", sf_priority_5|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_crossbow", sf_priority_7|sf_vol_4, ["draw_crossbow.ogg"]),
 ("put_back_crossbow", sf_priority_5|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_revolver", sf_priority_8|sf_vol_4, ["draw_from_holster.ogg"]),
 ("put_back_revolver", sf_priority_6|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_dagger", sf_priority_8|sf_vol_4, ["draw_dagger.ogg"]),
 ("put_back_dagger", sf_priority_6|sf_vol_4, ["put_back_dagger.ogg"]),
 ("draw_bow", sf_priority_7|sf_vol_4, ["draw_bow.ogg"]),
 ("put_back_bow", sf_priority_5|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_shield", sf_priority_4|sf_vol_3, ["draw_shield.ogg"]),
 ("put_back_shield", sf_priority_4|sf_vol_3, ["put_back_shield.ogg"]),
 ("draw_other", sf_priority_8|sf_vol_4, ["draw_other.ogg"]),
 ("put_back_other", sf_priority_6|sf_vol_4, ["draw_other2.ogg"]),

 ("body_fall_small", sf_priority_7|sf_vol_8, ["body_fall_small_1.ogg","body_fall_small_2.ogg"]),
 ("body_fall_big", sf_priority_9|sf_vol_9, ["body_fall_1.ogg","body_fall_2.ogg","body_fall_3.ogg"]),
 ("horse_body_fall_begin", sf_priority_9|sf_vol_10, ["horse_body_fall_begin_1.ogg"]),
 ("horse_body_fall_end", sf_priority_9|sf_vol_10, ["horse_body_fall_end_1.ogg","body_fall_2.ogg"]),

 ("hit_wood_wood", sf_priority_11|sf_vol_9, ["hit_wood_wood_1.ogg","hit_wood_wood_2.ogg","hit_wood_wood_3.ogg","hit_wood_wood_4.ogg","hit_wood_metal_4.ogg","hit_wood_metal_5.ogg","hit_wood_metal_6.ogg"]),
 ("hit_metal_metal", sf_priority_11|sf_vol_10, ["hit_metal_metal_3.ogg","hit_metal_metal_4.ogg","hit_metal_metal_5.ogg","hit_metal_metal_6.ogg","hit_metal_metal_7.ogg","hit_metal_metal_8.ogg","hit_metal_metal_9.ogg","hit_metal_metal_10.ogg","clang_metal_1.ogg","clang_metal_2.ogg"]),
 ("hit_wood_metal", sf_priority_11|sf_vol_10, ["hit_metal_metal_1.ogg","hit_metal_metal_2.ogg","hit_wood_metal_7.ogg"]),
 ("shield_hit_wood_wood", sf_priority_11|sf_vol_10, ["shield_hit_wood_wood_1.ogg","shield_hit_wood_wood_2.ogg","shield_hit_wood_wood_3.ogg"]),
 ("shield_hit_metal_metal", sf_priority_11|sf_vol_10, ["shield_hit_metal_metal_1.ogg","shield_hit_metal_metal_2.ogg","shield_hit_metal_metal_3.ogg","shield_hit_metal_metal_4.ogg"]),
 ("shield_hit_wood_metal", sf_priority_11|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg","shield_hit_cut_10.ogg"]),
 ("shield_hit_metal_wood", sf_priority_11|sf_vol_10, ["shield_hit_metal_wood_1.ogg","shield_hit_metal_wood_2.ogg","shield_hit_metal_wood_3.ogg"]),
 ("shield_broken", sf_priority_12|sf_vol_10, ["shield_broken.ogg"]),
 ("man_hit", sf_priority_11|sf_vol_8, ["man_hit_5.ogg","man_hit_6.ogg","man_hit_7.ogg","man_hit_8.ogg","man_hit_9.ogg","man_hit_10.ogg","man_hit_11.ogg","man_hit_12.ogg","man_hit_13.ogg","man_hit_14.ogg","man_hit_15.ogg","man_hit_17.ogg","man_hit_18.ogg","man_hit_19.ogg","man_hit_22.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg","man_hit_59.ogg"]),
 ("man_die", sf_priority_12|sf_vol_10,  ["man_death_1.ogg","man_death_8.ogg","man_death_8b.ogg","man_death_11.ogg","man_death_14.ogg","man_death_16.ogg","man_death_18.ogg","man_death_21.ogg","man_death_22.ogg","man_death_29.ogg","man_death_40.ogg","man_death_44.ogg","man_death_46.ogg","man_death_48.ogg","man_death_64.ogg"]),
 ("woman_hit", sf_priority_11|sf_vol_8, ["woman_hit_2.ogg","woman_hit_3.ogg","woman_hit_b_2.ogg","woman_hit_b_4.ogg","woman_hit_b_6.ogg","woman_hit_b_7.ogg","woman_hit_b_8.ogg","woman_hit_b_11.ogg","woman_hit_b_14.ogg","woman_hit_b_16.ogg"]),
 ("woman_die", sf_priority_12|sf_vol_10, ["woman_fall_1.ogg","woman_hit_b_5.ogg"]),
 ("woman_yell", sf_priority_9|sf_vol_8, ["woman_yell_1.ogg","woman_yell_2.ogg"]),
 ("hide", 0, ["s_hide.wav"]),
 ("unhide", 0, ["s_unhide.wav"]),
 ("neigh", sf_priority_1|sf_vol_1, []),
 ("gallop", sf_priority_10|sf_vol_3, ["horse_gallop_3.ogg","horse_gallop_4.ogg","horse_gallop_5.ogg"]),
 ("battle", sf_priority_10|sf_vol_4, ["battle.ogg"]),
 ("arrow_hit_body", sf_priority_9|sf_vol_10, ["arrow_hit_body_1.ogg","arrow_hit_body_2.ogg","arrow_hit_body_3.ogg"]),
 ("metal_hit_low_armor_low_damage", sf_priority_8|sf_vol_9, ["sword_hit_lo_armor_lo_dmg_1.ogg","sword_hit_lo_armor_lo_dmg_2.ogg","sword_hit_lo_armor_lo_dmg_3.ogg"]),
 ("metal_hit_low_armor_high_damage", sf_priority_10|sf_vol_9, ["sword_hit_lo_armor_hi_dmg_1.ogg","sword_hit_lo_armor_hi_dmg_2.ogg","sword_hit_lo_armor_hi_dmg_3.ogg"]),
 ("metal_hit_high_armor_low_damage", sf_priority_8|sf_vol_9, ["metal_hit_high_armor_low_damage.ogg","metal_hit_high_armor_low_damage_2.ogg","metal_hit_high_armor_low_damage_3.ogg"]),
 ("metal_hit_high_armor_high_damage", sf_priority_10|sf_vol_9, ["sword_hit_hi_armor_hi_dmg_1.ogg","sword_hit_hi_armor_hi_dmg_2.ogg","sword_hit_hi_armor_hi_dmg_3.ogg"]),
 ("wooden_hit_low_armor_low_damage", sf_priority_8|sf_vol_9, ["blunt_hit_low_1.ogg","blunt_hit_low_2.ogg","blunt_hit_low_3.ogg"]),
 ("wooden_hit_low_armor_high_damage", sf_priority_10|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("wooden_hit_high_armor_low_damage", sf_priority_8|sf_vol_9, ["wooden_hit_high_armor_low_damage_1.ogg","wooden_hit_high_armor_low_damage_2.ogg"]),
 ("wooden_hit_high_armor_high_damage", sf_priority_10|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("mp_arrow_hit_target", sf_2d|sf_priority_10|sf_vol_9, ["mp_arrow_hit_target.ogg"]),
 ("blunt_hit", sf_priority_9|sf_vol_9, ["punch_1.ogg","punch_4.ogg","punch_4.ogg","punch_5.ogg"]),
 ("player_hit_by_arrow", sf_priority_10|sf_vol_10, ["player_hit_by_arrow.ogg"]),
 ("release_crossbow_medium", sf_priority_4|sf_vol_7, ["release_crossbow_1.ogg"]),
 ("release_crossbow_far", sf_priority_3|sf_vol_7, ["release_crossbow_1.ogg"]),
 ("bullet_hit_body", sf_priority_6|sf_vol_7, ["player_hit_by_arrow.ogg"]),
 ("player_hit_by_bullet", sf_priority_10|sf_vol_10, ["player_hit_by_arrow.ogg"]),
 ("pistol_shot", sf_priority_12|sf_vol_10, ["fl_pistol.wav"]),
 ("man_grunt", sf_priority_6|sf_vol_4, ["man_excercise_1.ogg","man_excercise_2.ogg","man_excercise_4.ogg"]),
 ("man_breath_hard", sf_priority_7|sf_vol_8, ["man_ugh_1.ogg","man_ugh_2.ogg","man_ugh_4.ogg","man_ugh_7.ogg","man_ugh_12.ogg","man_ugh_13.ogg","man_ugh_17.ogg"]),
 ("man_stun", sf_priority_9|sf_vol_8, ["man_stun_1.ogg"]),
 ("man_grunt_long", sf_priority_7|sf_vol_7, ["man_grunt_1.ogg","man_grunt_2.ogg","man_grunt_3.ogg","man_grunt_5.ogg","man_grunt_13.ogg","man_grunt_14.ogg"]),
 ("man_yell", sf_priority_6|sf_vol_8, ["man_yell_4.ogg","man_yell_4_2.ogg","man_yell_7.ogg","man_yell_9.ogg","man_yell_11.ogg","man_yell_13.ogg","man_yell_15.ogg","man_yell_16.ogg","man_yell_17.ogg","man_yell_20.ogg","man_shortyell_4.ogg","man_shortyell_5.ogg","man_shortyell_6.ogg","man_shortyell_9.ogg","man_shortyell_11.ogg","man_shortyell_11b.ogg","man_yell_b_18.ogg","man_yell_22.ogg", "man_yell_c_20.ogg"]),
 ("man_warcry", sf_priority_8|sf_vol_10, ["man_insult_2.ogg","man_insult_3.ogg","man_insult_7.ogg","man_insult_9.ogg","man_insult_13.ogg","man_insult_15.ogg","man_insult_16.ogg"]),

 ("encounter_looters", sf_priority_8|sf_vol_8, ["encounter_river_pirates_5.ogg","encounter_river_pirates_6.ogg","encounter_river_pirates_9.ogg","encounter_river_pirates_10.ogg","encounter_river_pirates_4.ogg"]),
 ("encounter_bandits", sf_priority_8|sf_vol_8, ["encounter_bandit_2.ogg","encounter_bandit_9.ogg","encounter_bandit_12.ogg","encounter_bandit_13.ogg","encounter_bandit_15.ogg","encounter_bandit_16.ogg","encounter_bandit_10.ogg",]),
 ("encounter_farmers", sf_priority_8|sf_vol_8, ["encounter_farmer_2.ogg","encounter_farmer_5.ogg","encounter_farmer_7.ogg","encounter_farmer_9.ogg"]),
 ("encounter_sea_raiders", sf_priority_8|sf_vol_8, ["encounter_sea_raider_5.ogg","encounter_sea_raider_9.ogg","encounter_sea_raider_9b.ogg","encounter_sea_raider_10.ogg"]),
 ("encounter_steppe_bandits", sf_priority_8|sf_vol_8, ["encounter_steppe_bandit_3.ogg","encounter_steppe_bandit_3b.ogg","encounter_steppe_bandit_8.ogg","encounter_steppe_bandit_10.ogg","encounter_steppe_bandit_12.ogg"]),
 ("encounter_nobleman", sf_priority_8|sf_vol_8, ["encounter_nobleman_1.ogg"]),
 ("encounter_vaegirs_ally", sf_priority_8|sf_vol_8, ["encounter_vaegirs_ally.ogg","encounter_vaegirs_ally_2.ogg"]),
 ("encounter_vaegirs_neutral", sf_priority_8|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("encounter_vaegirs_enemy", sf_priority_8|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("sneak_town_halt", sf_priority_8|sf_vol_10, ["sneak_halt_1.ogg","sneak_halt_2.ogg"]),

 ("horse_walk", sf_priority_3|sf_vol_3, ["horse_walk_1.ogg","horse_walk_2.ogg","horse_walk_3.ogg","horse_walk_4.ogg"]),
 ("horse_trot", sf_priority_3|sf_vol_3, ["horse_trot_1.ogg","horse_trot_2.ogg","horse_trot_3.ogg","horse_trot_4.ogg"]),
 ("horse_canter", sf_priority_4|sf_vol_4, ["horse_canter_1.ogg","horse_canter_2.ogg","horse_canter_3.ogg","horse_canter_4.ogg"]),
 ("horse_gallop", sf_priority_5|sf_vol_4, ["horse_gallop_6.ogg","horse_gallop_7.ogg","horse_gallop_8.ogg","horse_gallop_9.ogg"]),
 ("horse_breath", sf_priority_1|sf_vol_4, ["horse_breath_4.ogg","horse_breath_5.ogg","horse_breath_6.ogg","horse_breath_7.ogg"]),
 ("horse_snort", sf_priority_1|sf_vol_1, ["horse_snort_1.ogg","horse_snort_2.ogg","horse_snort_3.ogg","horse_snort_4.ogg","horse_snort_5.ogg"]),
 ("horse_low_whinny", sf_priority_8|sf_vol_12, ["horse_whinny-1.ogg","horse_whinny-2.ogg"]),
 ("block_fist", sf_priority_9|sf_vol_10, ["block_fist_3.ogg","block_fist_4.ogg"]),
 ("man_hit_blunt_weak", sf_priority_9|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_blunt_strong", sf_priority_10|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_weak", sf_priority_9|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_strong", sf_priority_10|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_weak", sf_priority_9|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_strong", sf_priority_10|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_victory", sf_priority_5|sf_vol_10, ["man_victory_3.ogg","man_victory_4.ogg","man_victory_5.ogg","man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","man_victory_54.ogg","man_victory_57.ogg","man_victory_71.ogg"]),
 ("fire_loop", sf_priority_5|sf_vol_15|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("torch_loop", sf_priority_4|sf_vol_15|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("dummy_hit", sf_priority_6|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_5.ogg"]),
 ("dummy_destroyed", sf_priority_7|sf_vol_10, ["shield_broken.ogg"]),
 ("gourd_destroyed", sf_priority_7|sf_vol_10, ["shield_broken.ogg"]),
 ("cow_moo", sf_priority_6|sf_vol_12, ["cow_moo_1.ogg"]),
 ("cow_slaughter", sf_priority_9|sf_vol_12, ["cow_slaughter.ogg"]),
 ("distant_dog_bark", sf_priority_3|sf_vol_15|sf_stream_from_hd, ["d_dog1.ogg","d_dog2.ogg","d_dog3.ogg","d_dog7.ogg"]),
 ("distant_owl", sf_priority_3|sf_vol_15|sf_stream_from_hd, ["d_owl2.ogg","d_owl3.ogg","d_owl4.ogg"]),
 ("distant_chicken", sf_priority_3|sf_vol_15|sf_stream_from_hd, ["d_chicken1.ogg","d_chicken2.ogg"]),
 ("distant_carpenter", sf_priority_3|sf_vol_15|sf_stream_from_hd, ["d_carpenter1.ogg","d_saw_short3.ogg"]),
 ("distant_blacksmith", sf_priority_3|sf_vol_15|sf_stream_from_hd, ["d_blacksmith2.ogg"]),
 ("arena_ambiance", sf_2d|sf_priority_5|sf_vol_15|sf_looping|sf_stream_from_hd, ["arena_loop11.ogg"]),
 ("town_ambiance", sf_2d|sf_priority_5|sf_vol_15|sf_looping|sf_stream_from_hd, ["town_loop_3.ogg"]),
 ("tutorial_fail", sf_2d|sf_priority_10|sf_vol_7,["cue_failure.ogg"]),
 ("your_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_taken.ogg"]),
 ("enemy_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["enemy_flag_taken.ogg"]),
 ("flag_returned", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_returned.ogg"]),
 ("team_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["you_scored_a_point.ogg"]),
 ("enemy_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["enemy_scored_a_point.ogg"]),

 ("failure", sf_2d|sf_priority_6|sf_vol_5, ["cue_failure.ogg"]),
 ("man_yawn", sf_priority_6|sf_vol_10, ["man_yawn_1.ogg"]),
 ("man_cough", sf_priority_6|sf_vol_10, ["man_cough_1.ogg","man_cough_2.ogg","man_cough_3.ogg"]),
 ("man_drown", sf_priority_9|sf_vol_10, ["man_stun_1.ogg","man_ugh_7.ogg","man_ugh_13.ogg","man_ugh_17.ogg"]),
 ("woman_drown", sf_priority_9|sf_vol_10, ["woman_hit_b_2.ogg","woman_hit_2.ogg"]),
 ("cut_wood", sf_priority_9|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_5.ogg"]),
 ("cut_wood_break", sf_priority_10|sf_vol_10, ["shield_hit_cut_4.ogg"]),
 ("cut_wood_scratch", sf_priority_6|sf_vol_10, ["wooden_hit_high_armor_low_damage_1.ogg","wooden_hit_high_armor_low_damage_2b.ogg"]),
 ("mining_hit", sf_priority_9|sf_vol_10, ["hit_wood_metal_7.ogg","hit_metal_metal_1.ogg","hit_metal_metal_2.ogg","hit_metal_metal_4.ogg","hit_metal_metal_5.ogg"]),
 ("mining_scratch", sf_priority_6|sf_vol_10, ["hit_metal_metal_3.ogg","hit_metal_metal_6.ogg"]),
 ("repair_wood", sf_priority_9|sf_vol_10, ["hit_wood_wood_2.ogg","hit_wood_wood_3.ogg","hit_wood_wood_4.ogg","hit_wood_metal_4.ogg","hit_wood_metal_5.ogg"]),
 ("saw_wood", sf_priority_7|sf_vol_10, ["d_saw_short3.ogg"]),
 ("blacksmith", sf_priority_7|sf_vol_10, ["d_blacksmith2.ogg"]),
 ("damage_ship", sf_priority_9|sf_vol_10, ["shield_broken.ogg"]),
 ("lock", sf_priority_10|sf_vol_10, ["hit_wood_metal_6.ogg"]),
 ("pick_lock_fail", sf_priority_10|sf_vol_10, ["hit_wood_wood_1.ogg"]),
 ("fire", sf_priority_6|sf_vol_10, ["Fire_Small_Crackle_Slick_op.ogg"]),
 ("horse_neigh", sf_priority_8|sf_vol_10, ["horse_exterior_whinny_01.ogg","horse_exterior_whinny_02.ogg","horse_exterior_whinny_03.ogg","horse_exterior_whinny_04.ogg","horse_exterior_whinny_05.ogg","horse_whinny.ogg"]),
 ("pull_flax", sf_priority_6|sf_vol_3, ["draw_other.ogg"]),

 ("away_vile_beggar", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_nobleman_1.ogg"]),
 ("my_lord", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_farmer_7.ogg","encounter_farmer_9.ogg"]),
 ("almost_harvesting_season", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_farmer_2.ogg"]),
 ("whats_this_then", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_river_pirates_5.ogg"]),
 ("out_for_a_stroll_are_we", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_river_pirates_6.ogg"]),
 ("we_ride_to_war", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_ally.ogg"]),
 ("less_talking_more_raiding", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_sea_raider_10.ogg"]),
 ("you_there_stop", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["sneak_halt_1.ogg","sneak_halt_2.ogg"]),
 ("tear_you_limb_from_limb", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_river_pirates_9.ogg","encounter_river_pirates_10.ogg"]),
 ("better_not_be_a_manhunter", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_river_pirates_4.ogg"]),
 ("drink_from_your_skull", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_sea_raider_5.ogg"]),
 ("gods_will_decide_your_fate", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_sea_raider_9.ogg"]),
 ("nice_head_on_shoulders", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_sea_raider_9b.ogg"]),
 ("hunt_you_down", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_steppe_bandit_8.ogg","encounter_steppe_bandit_10.ogg"]),
 ("dead_men_tell_no_tales", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_steppe_bandit_3.ogg"]),
 ("stand_and_deliver", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_bandit_12.ogg"]),
 ("your_money_or_your_life", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_bandit_2.ogg","encounter_steppe_bandit_12.ogg"]),
 ("have_our_pay_or_fun", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_bandit_10.ogg"]),
 ("word_about_purse_belongings", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_bandit_13.ogg"]),
 ("easy_way_or_hard_way", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_bandit_15.ogg"]),
 ("everything_has_a_price", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_bandit_16.ogg"]),
 ("slit_your_throat", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["encounter_bandit_9.ogg"]),

 ("sounds_end", 0, []),
]

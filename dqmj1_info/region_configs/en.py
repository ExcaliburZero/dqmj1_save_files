from .region_configs import (
    RegionConfig,
    REGION_CONFIGS,
    StringTable,
    StringAddressTable,
)

import pathlib

REGION_CONFIGS["North America"] = RegionConfig(
    string_tables={
        pathlib.Path("arm9.bin"): (
            0x02000000,
            [
                StringTable("strings_a", 0x020735F0, 0x020749E8),
                StringTable("strings_b", 0x0207805C, 0x02083DE3),
                StringTable("strings_c", 0x02084B18, 0x0208A7B8),
                StringTable("strings_d", 0x0209072C, 0x02091753),
            ],
        ),
        pathlib.Path("overlay")
        / "overlay_0000.bin": (
            0x021A0A00,
            [
                StringTable("strings_h", 0x021F5950, 0x021F66EC),
                StringTable("strings_i", 0x021F678C, 0x021F6D6C),
                StringTable("strings_j", 0x021F6ED8, 0x021F78B8),
                StringTable("strings_k", 0x021F80C0, 0x021FC140),
                StringTable("strings_l", 0x021FC224, 0x021FC940),
                StringTable("strings_m", 0x021FCB10, 0x021FD2A0),
                StringTable("strings_n", 0x021FD2F8, 0x021FD45C),
                StringTable("strings_o", 0x021FD588, 0x021FD874),
                StringTable("strings_-17", 0x021F5F30, 0x021F66EC),
                StringTable("strings_-16", 0x021F678C, 0x021F6D6C),
                StringTable("strings_-15", 0x021F6ED8, 0x021F78B8),
                StringTable("strings_-14", 0x021F80C0, 0x021FC140),
                StringTable("strings_-13", 0x021FC224, 0x021FC940),
                StringTable("strings_-12", 0x021FCB10, 0x021FD2A0),
                StringTable("strings_-11", 0x021FD2F8, 0x021FD45C),
                StringTable("strings_-10", 0x021FD588, 0x021FD874),
                StringTable("strings_-9", 0x021FD8C0, 0x021FDAB0),
                StringTable("strings_-8", 0x021FDB78, 0x021FE024),
                StringTable("strings_-7", 0x021FE2D8, 0x02201E0C),
                StringTable("strings_-6", 0x02201EBC, 0x02202370),
                StringTable("strings_-5", 0x022025FC, 0x02203514),
                StringTable("strings_-4", 0x022035B8, 0x0220361C),
                StringTable("strings_-3", 0x022037E0, 0x02204060),
                StringTable("strings_-2", 0x022040F8, 0x02204398),
                StringTable("strings_-1", 0x022043B8, 0x0220441C),
                StringTable("strings_0", 0x02204458, 0x02204600),
                StringTable("strings_1", 0x0220468C, 0x02204990),
                StringTable("strings_2", 0x02204A70, 0x022050AC),
                StringTable("strings_3", 0x022050D4, 0x02205144),
                StringTable("strings_4", 0x02205174, 0x02205300),
                StringTable("strings_5", 0x0220533C, 0x02205444),
                StringTable("strings_6", 0x02205450, 0x02205498),
                StringTable("strings_7", 0x02205524, 0x022057D8),
                StringTable("strings_8", 0x02205814, 0x022059F4),
                StringTable("strings_9", 0x0220663C, 0x02207FB8),
            ],
        ),
    },
    string_address_tables={
        pathlib.Path("arm9.bin"): (
            0x02000000,
            [
                StringAddressTable("monster_species_names", 0x0207785C, 0x0207805C),
                StringAddressTable("skill_set_names", 0x020763E0, 0x020767E4),
                StringAddressTable("skill_names", 0x02076BE8, 0x0207705C),
                StringAddressTable("mnamemes", 0x02075FE0, 0x020763E0),
                StringAddressTable("unknown_a", 0x02074CE0, 0x02074DE0),
                StringAddressTable("tactic_names", 0x02074A88, 0x02074AA8),
                StringAddressTable("skill_descriptions", 0x02074FE0, 0x020753E0),
                StringAddressTable(
                    "skill_set_names_and_descriptions", 0x020753E0, 0x020757E0
                ),
                StringAddressTable("item_names", 0x020767E4, 0x02076BE8),
                StringAddressTable("trait_names", 0x020757E0, 0x02075BE0),
                StringAddressTable("enemy_scout_names", 0x02075BE0, 0x02075FE0),
                StringAddressTable("unknown_b", 0x0207705C, 0x0207785C),
                StringAddressTable("unknown_c", 0x02074A04, 0x02074A14),
                StringAddressTable("color_names", 0x02074A54, 0x02074A6C),
                StringAddressTable("day_and_night", 0x020749EC, 0x020749F4),
                StringAddressTable("nsbmd_filenames", 0x02074DE0, 0x02074FE0),
                StringAddressTable("unknown_d", 0x02074C60, 0x02074DDC),
                StringAddressTable("unknown_e", 0x02074B2C, 0x02074B74),
                StringAddressTable("unknown_f", 0x02074A6C, 0x02074A88),
                StringAddressTable(
                    "battle_and_field_and_anywhere", 0x020749F4, 0x02074A04
                ),
                StringAddressTable("unknown_g", 0x02074A3C, 0x02074A54),
                StringAddressTable("battle_targets", 0x02074A14, 0x02074A28),
                StringAddressTable("skill_targeting_types", 0x02074A28, 0x02074A3C),
                StringAddressTable("unknown_h", 0x02074AE8, 0x02074B2C),
                StringAddressTable("unknown_i", 0x02074BE0, 0x02074C60),
                StringAddressTable(
                    "unused_gun_minigame_battle_text", 0x02083E7C, 0x02083EBC
                ),
                StringAddressTable("unknown_6", 0x02083F48, 0x02083F98),
                StringAddressTable("unknown_7", 0x02083F98, 0x02084018),
                StringAddressTable("unknown_j", 0x02084018, 0x02084118),
                StringAddressTable("unknown_9", 0x02084118, 0x02084318),
                StringAddressTable("battle_messages", 0x02084318, 0x02084B18),
                StringAddressTable("unknown_k", 0x02083EBC, 0x02083EFC),
            ],
        ),
        pathlib.Path("overlay")
        / "overlay_0000.bin": (
            0x021A0A00,
            [
                StringAddressTable(
                    "monster_species_descriptions", 0x021F78C0, 0x021F80C0
                ),  # special case, they appear as two tables in ROM, but are actually one
                StringAddressTable("swear_words", 0x022059F8, 0x0220663C),
                StringAddressTable("unknown_w", 0x021F5E0C, 0x021F5F30),
                StringAddressTable("unknown_x", 0x021F66F0, 0x021F678C),
                StringAddressTable("unknown_y", 0x021F6D70, 0x021F6ED8),
                StringAddressTable("unknown_z", 0x021F78C0, 0x021F7CC0),
                StringAddressTable("unknown_aa", 0x021F7CC0, 0x021F80C0),
                StringAddressTable("unknown_ab", 0x021FC148, 0x021FC198),
                StringAddressTable("unknown_ac", 0x021FC198, 0x021FC224),
                StringAddressTable("unknown_ad", 0x021FC944, 0x021FCB10),
                StringAddressTable("unknown_ae", 0x021FD2A4, 0x021FD2F8),
                StringAddressTable("unknown_af", 0x021FD460, 0x021FD588),
                StringAddressTable("unknown_ag", 0x021FD878, 0x021FD8C0),
                StringAddressTable("main_quest_goals", 0x021FDAB4, 0x021FDB78),
                StringAddressTable("unknown_ai", 0x021FE030, 0x021FE054),
                StringAddressTable("unknown_aj", 0x021FE054, 0x021FE194),
                StringAddressTable("unknown_ak", 0x021FE194, 0x021FE2D8),
                StringAddressTable("unknown_al", 0x02201E10, 0x02201EBC),
                StringAddressTable("unknown_am", 0x02202374, 0x022025FC),
                StringAddressTable("unknown_an", 0x02203620, 0x022037E0),
                StringAddressTable("unknown_ao", 0x02204064, 0x022040F8),
                StringAddressTable("unknown_ap", 0x0220439C, 0x022043B8),
                StringAddressTable("unknown_aq", 0x02204420, 0x02204458),
                StringAddressTable("unknown_ar", 0x02204608, 0x0220468C),
                StringAddressTable("unknown_as", 0x02204994, 0x02204A70),
                StringAddressTable("unknown_at", 0x022050B4, 0x022050D4),
                StringAddressTable("unknown_au", 0x02205148, 0x02205174),
                StringAddressTable("unknown_av", 0x02205304, 0x0220533C),
                StringAddressTable("unknown_aw", 0x02205448, 0x02205450),
                StringAddressTable("unknown_ax", 0x0220549C, 0x02205524),
                StringAddressTable("unknown_ay", 0x0220549C, 0x02205524),
                StringAddressTable("unknown_az", 0x022057DC, 0x02205814),
            ],
        ),
    },
)

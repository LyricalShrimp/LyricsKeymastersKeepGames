from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class StrawberryJamArchipelagoOptions:
    strawberry_jam_include_lobbies: StrawberryJamIncludeLobbies
    strawberry_jam_include_heartsides: StrawberryJamIncludeHeartsides
    strawberry_jam_include_puzzle_maps: StrawberryJamIncludePuzzleMaps
    strawberry_jam_exclude_maps: StrawberryJamExcludeMaps

# Main Class
class StrawberryJamGame(Game):
    name = "Strawberry Jam"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = []

    is_adult_only_or_unrated = False

    options_cls = StrawberryJamArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete maps with all strawberries",
                data=dict()
            )
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete MAP",
                data={
                    "MAP": (self.maps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
        ]

    # "Template Include Hard Stuff" Option Property
    @property
    def heartsides(self) -> bool:
        return bool(self.archipelago_options.strawberry_jam_include_heartsides.value)
    
    @property
    def puzzles(self) -> bool:
        return bool(self.archipelago_options.strawberry_jam_include_puzzle_maps.value)

    # "Template DLC Owned" Option Properties
    @property
    def lobbies(self) -> Set[str]:
        return self.archipelago_options.strawberry_jam_include_lobbies.value
    
    @property
    def has_beginnerlobby(self) -> bool:
        return "Beginner" in self.lobbies
    
    @property
    def has_intermediatelobby(self) -> bool:
        return "Intermediate" in self.lobbies
    
    @property
    def has_advancedlobby(self) -> bool:
        return "Advanced" in self.lobbies

    @property
    def has_expertlobby(self) -> bool:
        return "Expert" in self.lobbies
    
    @property
    def has_grandmasterlobby(self) -> bool:
        return "Grandmaster" in self.lobbies
    
    @property
    def excludedmaps(self) -> List[str]:
        return self.archipelago_options.strawberry_jam_exclude_maps.value
    
    @functools.cached_property
    def maps_beginner(self) -> List[str]:
        return [
            "Forest Path",
            "Loopy Lagoon",
            "Azure Caverns",
            "Collapsing Skyline",
            "Over The City",
            "paint",
            "Switchtube Vista",
            "Strawberry Orchard",
            "Rose Garden",
            "If my 'driveway' almost did you in...",
            "The Squeeze",
            "Coresaken City",
            "Seeing Is Believing",
            "Cassette Cliffs",
            "Troposphere",
            "Potential for Anything",
            "Midnight Spire",
            "Treehive",
            "Soap"
        ]
    
    @functools.cached_property
    def maps_intermediate(self) -> List[str]:
        return [
            "Vertigo",
            "The Tower",
            "EAT GIRL",
            "Square the Circle",
            "Sea of Soup",
            "Midnight Monsoon",
            "In Filtration",
            "Fifth Dimension",
            "Pufferfish Transportation Co.",
            "Honeyzip Inc.",
            "Deep Blue",
            "Sleeping Under Stars",
            "Low-G Botany",
            "Temple of a Thousand Skies",
            "Frosted Fragments",
            "Supernautica",
            "Construction Conundrum"
        ]
    
    @functools.cached_property
    def maps_advanced(self) -> List[str]:
        return [
            "Sands of Time",
            "Slime Time!",
            "Lethal Laser Laboratory",
            "Starry Ruins",
            "Undergrowth",
            "Jellyfish Sanctum",
            "Tectonic Trenches",
            "Golden Dawn",
            "Forest Rush",
            "Attack of the Clone",
            "Bee Beserk",
            "Java's Crypt",
            "Raindrops on Roses",
            "Toggle Theory",
            "Superstructure",
            "Starlight Station",
            "Dusk City",
            "Synapse",
            "The Lab",
            "Belated Valentine's Day",
            "Thinking with Portals",
            "Rightside-Down Cavern",
            "Call of the Void"
        ]
    
    @functools.cached_property
    def maps_expert(self) -> List[str]:
        return [
            "Flying Battery",
            "The Core Problem",
            "Overgrown Linn",
            "Hydroshock",
            "Subway Neon",
            "Meaningless Contraptions",
            "Golden Alleyway",
            "System.InvalidMapException",
            "A Change in Direction",
            "Skyline Usurper",
            "Clockwork",
            "Plasma Reactor",
            "FLOATING POINT",
            "Storm Runner",
            "Time Trouble",
            "Hypnagogia",
            "Ethereal Ascension",
            "Vinculum",
            "Mosaic Garden",
            "Lunar Pagoda",
            "Caper Cavortion",
            "Chromatic Complex",
            "Fortress Fall",
            "Psychokinetic",
            "Garden of Khu'tara",
            "Narrow Hollow",
            "Summit Down-Side",
            "Polaris"
        ]
    
    @functools.cached_property
    def maps_grandmaster(self) -> List[str]:
        return [
            "Flipside Cliffside",
            "Lava Layer",
            "kevintechspam.bin",
            "Fractured Iridescence",
            "Superluminary",
            "Belly of the Beast",
            "Cycle Madness B-Side",
            "Cave of the Crimson Sky",
            "Drifting Deep",
            "World Abyss",
            "Stellar Odyssey",
            "74",
            "Shattersong",
            "summit",
            "Ivory",
            "Pinball Purgatory",
            "The Solar Express",
            "Nelumbo"
        ]
    
    @functools.cached_property
    def maps_beginner_puzzle_maps(self) -> List[str]:
        return [
            "Dropzle",
            "A Gift From the Stars"
        ]
    
    @functools.cached_property
    def maps_intermediate_puzzle_maps(self) -> List[str]:
        return [
            "Pointless Machines"
        ]
    
    @functools.cached_property
    def maps_advanced_puzzle_maps(self) -> List[str]:
        return [
            "The Tower XVI",
            "Lost Woods"
        ]

    def maps(self) -> List[str]:
        maps: List[str] = list()

        if self.has_beginnerlobby:
            maps.extend(self.maps_beginner)

        if self.has_intermediatelobby:
            maps.extend(self.maps_intermediate)
        
        if self.has_advancedlobby:
            maps.extend(self.maps_advanced)
        
        if self.has_expertlobby:
            maps.extend(self.maps_expert)
        
        if self.has_grandmasterlobby:
            maps.extend(self.maps_grandmaster)
        
        if self.has_beginnerlobby and self.puzzles:
            maps.extend(self.maps_beginner_puzzle_maps)
        
        if self.has_intermediatelobby and self.puzzles:
            maps.extend(self.maps_intermediate_puzzle_maps)

        if self.has_advancedlobby and self.puzzles:
            maps.extend(self.maps_advanced_puzzle_maps)

        if self.has_beginnerlobby and self.heartsides:
            maps.append("Blueberry Bay")

        if self.has_intermediatelobby and self.heartsides:
            maps.append("Raspberry Roots")

        if self.has_advancedlobby and self.heartsides:
            maps.append("Mango Mesa")

        if self.has_expertlobby and self.heartsides:
            maps.append("Starfruit Supernova")
        
        if self.has_grandmasterlobby and self.heartsides:
            maps.append("Passionfruit Pantheon")

        includedmaps = [x for x in maps if x not in self.excludedmaps]

        return sorted(includedmaps)
    
# Archipelago Options
class StrawberryJamIncludeLobbies(OptionSet):
    """
    Indicates which difficulties to include.
    """

    display_name = "Strawberry Jam Include Lobbies"
    valid_keys = [
        "Beginner",
        "Intermediate",
        "Advanced",
        "Expert",
        "Grandmaster"
    ]

    default = valid_keys

class StrawberryJamIncludeHeartsides(Toggle):
    """
    Indicates whether or not you want heartsides in. Applies to all lobbies.
    List for reference: Blueberry Bay, Raspberry Roots, Mango Mesa, Starfruit Supernova, Passionfruit Pantheon
    """

    display_name = "Strawberry Jam Include Heartsides"
    default = False

class StrawberryJamIncludePuzzleMaps(Toggle):
    """
    Indicates whether or not you want puzzle maps in. Includes Dropzle, A Gift From the Stars, Pointless Machines, Lost Woods, and The Tower XVI
    """

    display_name = "Strawberry Jam Include Puzzle Maps"
    default = True

class StrawberryJamExcludeMaps(OptionSet):
    """
    Use this if you would like to exclude very specific maps from the list of possible maps. 
    Best for if you would like to exclude specific difficulties within lobbies, specific heartsides, specific puzzle maps, or if you just really hate a certain map
    """

    valid_keys = [
        "Forest Path",
        "Loopy Lagoon",
        "Azure Caverns",
        "Collapsing Skyline",
        "Over The City",
        "paint",
        "Switchtube Vista",
        "Strawberry Orchard",
        "Rose Garden",
        "If my 'driveway' almost did you in...",
        "The Squeeze",
        "Coresaken City",
        "Seeing Is Believing",
        "Cassette Cliffs",
        "Troposphere",
        "Potential for Anything",
        "Midnight Spire",
        "Treehive",
        "Soap",
        "Dropzle",
        "A Gift From the Stars",
        "Vertigo",
        "The Tower",
        "EAT GIRL",
        "Square the Circle",
        "Sea of Soup",
        "Midnight Monsoon",
        "In Filtration",
        "Fifth Dimension",
        "Pufferfish Transportation Co.",
        "Honeyzip Inc.",
        "Deep Blue",
        "Sleeping Under Stars",
        "Low-G Botany",
        "Temple of a Thousand Skies",
        "Frosted Fragments",
        "Supernautica",
        "Construction Conundrum",
        "Pointless Machines",
        "Sands of Time",
        "Slime Time!",
        "Lethal Laser Laboratory",
        "Starry Ruins",
        "Undergrowth",
        "Jellyfish Sanctum",
        "Tectonic Trenches",
        "Golden Dawn",
        "Forest Rush",
        "Attack of the Clone",
        "Bee Beserk",
        "Java's Crypt",
        "Raindrops on Roses",
        "Toggle Theory",
        "Superstructure",
        "Starlight Station",
        "Dusk City",
        "Synapse",
        "The Lab",
        "Belated Valentine's Day",
        "Thinking with Portals",
        "Rightside-Down Cavern",
        "Call of the Void",
        "The Tower XVI",
        "Lost Woods",
        "Flying Battery",
        "The Core Problem",
        "Overgrown Linn",
        "Hydroshock",
        "Subway Neon",
        "Meaningless Contraptions",
        "Golden Alleyway",
        "System.InvalidMapException",
        "A Change in Direction",
        "Skyline Usurper",
        "Clockwork",
        "Plasma Reactor",
        "FLOATING POINT",
        "Storm Runner",
        "Time Trouble",
        "Hypnagogia",
        "Ethereal Ascension",
        "Vinculum",
        "Mosaic Garden",
        "Lunar Pagoda",
        "Caper Cavortion",
        "Chromatic Complex",
        "Fortress Fall",
        "Psychokinetic",
        "Garden of Khu'tara",
        "Narrow Hollow",
        "Summit Down-Side",
        "Polaris",
        "Flipside Cliffside",
        "Lava Layer",
        "kevintechspam.bin",
        "Fractured Iridescence",
        "Superluminary",
        "Belly of the Beast",
        "Cycle Madness B-Side",
        "Cave of the Crimson Sky",
        "Drifting Deep",
        "World Abyss",
        "Stellar Odyssey",
        "74",
        "Shattersong",
        "summit",
        "Ivory",
        "Pinball Purgatory",
        "The Solar Express",
        "Nelumbo",
        "Blueberry Bay",
        "Raspberry Roots",
        "Mango Mesa",
        "Starfruit Supernova",
        "Passionfruit Pantheon"
    ]

    default = valid_keys
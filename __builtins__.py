from typing import Any, Optional, Iterable, Tuple, Dict
from builtins import type, bool, int, float, str


# -------------------------------------------------------------------------------
class Item:
    """A member of the Items Class"""


class Items:
    Bone: Item
    """The bones of an ancient creature."""

    Cactus: Item
    """Obtained by harvesting sorted cacti."""

    Carrot: Item
    """Obtained by harvesting carrots."""

    Fertilizer: Item
    """Call `use_item(Items.Fertilizer)` to instantly remove 2s from the plants remaining grow time."""

    Gold: Item
    """Found in treasure chests in mazes."""

    Hay: Item
    """Obtained by cutting grass."""

    Piggy: Item
    """This item has been removed from the game but remains as a nostalgia trophy."""

    Power: Item
    """Obtained by harvesting sunflowers. The drone automatically uses this to move twice as fast."""

    Pumpkin: Item
    """Obtained by harvesting pumpkins."""

    Water: Item
    """Used to water the ground by calling `use_item(Items.Water)`."""

    Weird_Substance: Item
    """Call `use_item(Items.Weird_Substance)` on a bush to grow a maze, or on other plants to toggle their infection status."""

    Wood: Item
    """Obtained from bushes and trees."""


# -------------------------------------------------------------------------------
class Hat:
    """A member of the Hats class"""

class Hats:
    Brown_Hat: Hat
    """A brown hat."""

    Cactus_Hat: Hat
    """A hat shaped like a cactus."""

    Carrot_Hat: Hat
    """A hat shaped like a carrot."""

    Dinosaur_Hat: Hat
    """Equip it to start the dinosaur game."""

    Gold_Hat: Hat
    """A golden hat."""

    Gold_Trophy_Hat: Hat
    """A golden trophy hat."""

    Golden_Cactus_Hat: Hat
    """A golden hat shaped like a cactus."""

    Golden_Carrot_Hat: Hat
    """A golden hat shaped like a carrot."""

    Golden_Gold_Hat: Hat
    """A golden version of the gold hat."""

    Golden_Pumpkin_Hat: Hat
    """A golden hat shaped like a pumpkin."""

    Golden_Sunflower_Hat: Hat
    """A golden hat shaped like a sunflower."""

    Golden_Tree_Hat: Hat
    """A golden hat shaped like a tree."""

    Gray_Hat: Hat
    """A gray hat."""

    Green_Hat: Hat
    """A green hat."""

    Pumpkin_Hat: Hat
    """A hat shaped like a pumpkin."""

    Purple_Hat: Hat
    """A purple hat."""

    Silver_Trophy_Hat: Hat
    """A silver trophy hat."""

    Straw_Hat: Hat
    """The default hat."""

    Sunflower_Hat: Hat
    """A hat shaped like a sunflower."""

    The_Farmers_Remains: Hat
    """The remains of the farmer."""

    Top_Hat: Hat
    """A fancy top hat."""

    Traffic_Cone: Hat
    """A traffic cone hat."""

    Traffic_Cone_Stack: Hat
    """A stack of traffic cones as a hat."""

    Tree_Hat: Hat
    """A hat shaped like a tree."""

    Wizard_Hat: Hat
    """A magical wizard hat."""

    Wood_Trophy_Hat: Hat
    """A wooden trophy hat."""

# -------------------------------------------------------------------------------
class Leaderboard:
    """A member of the Leaderboards class"""

class Leaderboards:
    Cactus: Leaderboard
    """Farm 33554432 cacti with multiple drones."""

    Cactus_Single: Leaderboard
    """Farm 131072 cacti with a single drone on an 8x8 farm."""

    Carrots: Leaderboard
    """Farm 2000000000 carrots with multiple drones."""

    Carrots_Single: Leaderboard
    """Farm 100000000 carrots with a single drone on an 8x8 farm."""

    Dinosaur: Leaderboard
    """Farm 33488928 bones with multiple drones."""

    Fastest_Reset: Leaderboard
    """The most prestigious category. Completely automate the game from a single farm plot to unlocking the leaderboards again."""

    Hay: Leaderboard
    """Farm 2000000000 hay with multiple drones."""

    Hay_Single: Leaderboard
    """Farm 100000000 hay with a single drone on an 8x8 farm."""

    Maze: Leaderboard
    """Farm 9863168 gold with multiple drones."""

    Maze_Single: Leaderboard
    """Farm 616448 gold with a single drone on an 8x8 farm."""

    Pumpkins: Leaderboard
    """Farm 200000000 pumpkins with multiple drones."""

    Pumpkins_Single: Leaderboard
    """Farm 10000000 pumpkins with a single drone on an 8x8 farm."""

    Sunflowers: Leaderboard
    """Farm 100000 sunflowers with multiple drones."""

    Sunflowers_Single: Leaderboard
    """Farm 10000 sunflowers with a single drone on an 8x8 farm."""

    Wood: Leaderboard
    """Farm 10000000000 wood with multiple drones."""

    Wood_Single: Leaderboard
    """Farm 500000000 wood with a single drone on an 8x8 farm."""

# -------------------------------------------------------------------------------
class Entity:
    """A member of the Entities Class"""

class Entities:
    Apple: Entity
    """Dinosaurs love them apparently."""

    Bush: Entity
    """
    A small bush that drops `Items.Wood`.

    Average seconds to grow: 4
    Grows on: grassland or soil
    """

    Cactus: Entity
    """
    Cacti come in 10 different sizes (0-9). When harvested, adjacent cacti that are in sorted order will also be harvested recursively.
    You receive cactus equal to the number of harvested cacti squared.

    Average seconds to grow: 1
    Grows on: soil
    """

    Carrot: Entity
    """
    Carrots!

    Average seconds to grow: 6
    Grows on: soil
    """

    Dead_Pumpkin: Entity
    """
    One in five pumpkins dies when it grows up, leaving behind a dead pumpkin. Dead pumpkins are useless and disappear when something new is planted.
    `can_harvest()` always returns `False` on dead pumpkins.
    """

    Dinosaur: Entity
    """
    A piece of the tail of the dinosaur hat. When wearing the dinosaur hat, the tail is dragged behind the drone filling previously moved tiles.

    Average seconds to grow: 0.2
    Grows on: grassland or soil
    """

    Grass: Entity
    """
    Grows automatically on grassland. Harvest it to obtain `Items.Hay`.

    Average seconds to grow: 0.5
    Grows on: grassland or soil
    """

    Hedge: Entity
    """Part of the maze."""

    Pumpkin: Entity
    """
    Pumpkins grow together when they are next to other fully grown pumpkins. About 1 in 5 pumpkins dies when it grows up.
    When you harvest a pumpkin you get `Items.Pumpkin` equal to the number of pumpkins in the mega pumpkin cubed.

    Average seconds to grow: 2
    Grows on: soil
    """

    Sunflower: Entity
    """
    Sunflowers collect the power from the sun. Harvesting them will give you `Items.Power`.
    If you harvest a sunflower with the maximum number of petals (and there are at least 10 sunflowers) you get 5x bonus power.

    Average seconds to grow: 5
    Grows on: soil
    """

    Treasure: Entity
    """A treasure that contains gold equal to the side length of the maze in which it is hidden. It can be harvested like a plant."""

    Tree: Entity
    """
    Trees drop more wood than bushes. They take longer to grow if other trees grow next to them.

    Average seconds to grow: 7
    Grows on: grassland or soil
    """


# -------------------------------------------------------------------------------
class Ground:
    """A member of the Grounds Class"""


class Grounds:
    Grassland: Ground
    """The default ground. Grass will automatically grow on it."""

    Soil: Ground
    """Calling `till()` turns the ground into this. Calling `till()` again changes it back to grassland."""


# -------------------------------------------------------------------------------
class Unlock:
    """A member of the Unlocks Class"""


class Unlocks:
    Auto_Unlock: Unlock
    """Automatically unlock things."""

    Cactus: Unlock
    """
    Unlock: Cactus!
    Upgrade: Increases the yield and cost of cactus.
    """

    Carrots: Unlock
    """
    Unlock: Till the soil and plant carrots.
    Upgrade: Increases the yield and cost of carrots.
    """

    Costs: Unlock
    """Allows access to the cost of things."""

    Debug: Unlock
    """Tools to help with debugging programs."""

    Debug_2: Unlock
    """Functions to temporarily slow down the execution and make the grid smaller."""

    Dictionaries: Unlock
    """Get access to dictionaries and sets."""

    Dinosaurs: Unlock
    """
    Unlock: Majestic ancient creatures.
    Upgrade: Increases the yield and cost of dinosaurs.
    """

    Expand: Unlock
    """
    Unlock: Expands the farm land and unlocks movement.
    Upgrade: Expands the farm. This also clears the farm.
    """

    Fertilizer: Unlock
    """Reduces the remaining growing time of the plant under the drone by 2 seconds."""

    Functions: Unlock
    """Define your own functions."""

    Grass: Unlock
    """Increases the yield of grass."""

    Hats: Unlock
    """Unlocks new hat colors for your drone."""

    Import: Unlock
    """Import code from other files."""

    Leaderboard: Unlock
    """Join the leaderboard for the fastest reset time."""

    Lists: Unlock
    """Use lists to store lots of values."""

    Loops: Unlock
    """Unlocks a simple while loop."""

    Mazes: Unlock
    """
    Unlock: A maze with a treasure in the middle.
    Upgrade: Increases the gold in treasure chests.
    """

    Megafarm: Unlock
    """Unlocks multiple drones and drone management functions."""

    Operators: Unlock
    """Arithmetic, comparison and logic operators."""

    Plant: Unlock
    """Unlocks planting."""

    Polyculture: Unlock
    """Use companion planting to increase the yield."""

    Pumpkins: Unlock
    """
    Unlock: Pumpkins!
    Upgrade: Increases the yield and cost of pumpkins.
    """

    Senses: Unlock
    """The drone can see what's under it and where it is."""

    Simulation: Unlock
    """Unlocks simulation functions for testing and optimization."""

    Speed: Unlock
    """Increases the speed of the drone."""

    Sunflowers: Unlock
    """
    Unlock: Sunflowers and Power.
    Upgrade: Increases the power gained from sunflowers.
    """

    The_Farmers_Remains: Unlock
    """Unlocks the special hat 'The Farmers Remains'."""

    Timing: Unlock
    """Functions to help measure performance."""

    Top_Hat: Unlock
    """Unlocks the fancy Top Hat."""

    Trees: Unlock
    """
    Unlock: Unlocks trees.
    Upgrade: Increases the yield of bushes and trees.
    """

    Utilities: Unlock
    """Unlocks the `min()`, `max()` and `abs()` functions."""

    Variables: Unlock
    """Assign values to variables."""

    Watering: Unlock
    """Water the plants to make them grow faster."""


# -------------------------------------------------------------------------------
class Direction:
    """
    A direction, e.g. North.
    """


North = Direction()
"""
The direction north, i.e. up.
"""

East = Direction()
"""
The direction east, i.e. right.
"""
South = Direction()
"""
The direction south, i.e. down.
"""
West = Direction()
"""
The direction west, i.e. left.
"""


# -------------------------------------------------------------------------------
def harvest() -> bool:
    """
    Harvests the entity under the drone.
    If you harvest an entity that can't be harvested, it will be destroyed.

    returns `True` if an entity was removed, `False` otherwise.

    takes `200` ticks to execute if an entity was removed, `1` tick otherwise.

    example usage:
    ```
    harvest()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def can_harvest() -> bool:
    """
    Used to find out if plants are fully grown.

    returns `True` if there is an entity under the drone that is ready to be harvested, `False` otherwise.

    takes `1` tick to execute.

    example usage:
    ```
    if can_harvest():
        harvest()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def plant(entity: Entity) -> bool:
    """
    Spends the cost of the specified `entity` and plants it under the drone.
    It fails if you can't afford the plant, the ground type is wrong or there's already a plant there.

    returns `True` if it succeeded, `False` otherwise.

    takes `200` ticks to execute if it succeeded, `1` tick otherwise.

    example usage:
    ```
    plant(Entities.Bush)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def move(direction: Direction) -> bool:
    """
    Moves the drone into the specified `direction` by one tile.
    If the drone moves over the edge of the farm it wraps back to the other side of the farm.

    - `East `  =  right
    - `West `  =  left
    - `North`  =  up
    - `South`  =  down

    returns `True` if the drone has moved, `False` otherwise.

    takes `200` ticks to execute if the drone has moved, `1` tick otherwise.

    example usage:
    ```
    move(North)
    ```
    """
    ...

# -------------------------------------------------------------------------------
def can_move(direction: Direction) -> bool:
    """
    Checks if the drone can move in the specified `direction`.

    returns `True` if the drone can move, `False` otherwise.

    takes `1` tick to execute.

    example usage:
    ```
    if can_move(North):
        move(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def swap(direction: Direction) -> bool:
    """
    Swaps the entity under the drone with the entity next to the drone in the specified `direction`.
    - Doesn't work on all entities.
    - Also works if one (or both) of the entities are `None`.

    returns `True` if it succeeded, `False` otherwise.

    takes `200` ticks to execute on success, `1` tick otherwise.

    example usage:
    ```
    swap(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def till() -> None:
    """
    Tills the ground under the drone into soil. If it's already soil it will change the ground back to grassland.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    till()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_pos_x() -> int:
    """
    Gets the current x position of the drone.
    The x position starts at `0` in the `West` and increases in the `East` direction.

    returns a number representing the current x coordinate of the drone.

    takes `1` tick to execute.

    example usage:
    ```
    x, y = get_pos_x(), get_pos_y()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_pos_y() -> int:
    """
    Gets the current y position of the drone.
    The y position starts at `0` in the `South` and increases in the `North` direction.

    returns a number representing the current y coordinate of the drone.

    takes `1` tick to execute.

    example usage:
    ```
    x, y = get_pos_x(), get_pos_y()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_world_size() -> int:
    """
    Get the current size of the farm.

    returns the side length of the grid in the north to south direction.

    takes `1` tick to execute.

    example usage:
    ```
    for i in range(get_world_size()):
        move(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_entity_type() -> Entity | None:
    """
    Find out what kind of entity is under the drone.

    returns `None` if the tile is empty, otherwise returns the type of the entity under the drone.

    takes `1` tick to execute.

    example usage:
    ```
    if get_entity_type() == Entities.Grass:
        harvest()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_ground_type() -> Ground:
    """
    Find out what kind of ground is under the drone.

    returns the type of the ground under the drone.

    takes `1` tick to execute.

    example usage:
    ```
    if get_ground_type() != Grounds.Soil:
        till()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_time() -> float:
    """
    Get the current game time.

    returns the time in seconds since the start of the game.

    takes `1` tick to execute.

    example usage:
    ```
    start = get_time()

    do_something()

    time_passed = get_time() - start
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_tick_count() -> int:
    """
    Used to measure the number of ticks performed.

    returns the number of ticks performed since the start of execution.

    takes `0` tick to execute.

    example usage:
    ```
    do_something()

    print(get_tick_count())
    ```
    """
    ...


# -------------------------------------------------------------------------------
def use_item(item: Item, n: int = 1) -> bool:
    """
    Attempts to use the specified `item` `n` times. Can only be used with some items including `Items.Water`, `Items.Fertilizer` and `Items.Weird_Substance`.

    returns `True` if an item was used, `False` if the item can't be used or you don't have enough.

    takes `200` ticks to execute if it succeeded, `1` tick otherwise.

    example usage:
    ```
    if use_item(Items.Fertilizer):
        print("Fertilizer used successfully")
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_water() -> float:
    """
    Get the current water level under the drone.

    returns the water level under the drone as a number between `0` and `1`.

    takes `1` tick to execute.

    example usage:
    ```
    if get_water() < 0.5:
        use_item(Items.Water)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def do_a_flip() -> None:
    """
    Makes the drone do a flip! This action is not affected by speed upgrades.

    returns `None`

    takes 1s to execute.

    example usage:
    ```
    while True:
        do_a_flip()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def pet_the_piggy() -> None:
    """
    Pets the piggy! This action is not affected by speed upgrades.

    returns `None`

    takes 1s to execute.

    example usage:
    ```
    while True:
        pet_the_piggy()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def print(*something: Any) -> None:
    """
    Prints `something` into the air above the drone using smoke. This action is not affected by speed upgrades.
    Multiple values can be printed at once.

    returns `None`

    takes 1s to execute.

    example usage:
    ```
    print('ground:', get_ground_type())
    ```
    """
    ...


# -------------------------------------------------------------------------------
def set_execution_speed(speed: float) -> None:
    """
    Limits the speed at which the program is executed to better see what's happening.

    - A `speed` of `1` is the speed the drone has without any speed upgrades.
    - A `speed` of `10` makes the code execute `10` times faster and corresponds to the speed of the drone after `9` speed upgrades.
    - A `speed` of `0.5` makes the code execute at half of the speed without speed upgrades. This can be useful to see what the code is doing.

    If `speed` is faster than the execution can currently go it will just go at max speed.

    If `speed` is `0` or negative, the speed is changed back to max speed.
     The effect will also stop when the execution stops.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    set_execution_speed(1)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def set_world_size(size: float) -> None:
    """
    Limits the size of the farm to better see what's happening.
    Also clears the farm and resets the drone position.
    - Sets the farm to a `size` x `size` grid.
    - The smallest `size` possible is `3`.
    - A `size` smaller than `3` will change the grid back to its full size.
    - The effect will also stop when the execution stops.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    set_world_size(5)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def num_items(item: Item) -> float:
    """
    Find out how much of `item` you currently have.

    returns the number of `item` currently in your inventory.

    takes `1` tick to execute.

    example usage:
    ```
    if num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_cost(thing: Entity | Item | Unlock, level: Optional[int] = None) -> Dict[Item, float] | None:
    """
    Gets the cost of a `thing`

    If `thing` is an entity: get the cost of planting it.
    If `thing` is an unlock: get the cost of unlocking it at the specified level.

    - returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.
    - returns `None` for unlocks that are already unlocked (when no level specified).
    - The optional `level` parameter specifies the upgrade level for unlocks.

    takes `1` tick to execute.

    example usage:
    ```
    cost = get_cost(Unlocks.Carrots)
    for item in cost:
        if num_items(item) < cost[item]:
            print('not enough items to unlock carrots')
    ```
    """
    ...


# -------------------------------------------------------------------------------
def clear() -> None:
    """
    Removes everything from the farm, moves the drone back to position `(0,0)` and changes the hat back to the default.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    clear()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_companion() -> Tuple[Entity, Tuple[int, int]] | None:
    """
    Get the companion preference of the plant under the drone.

    returns a tuple of the form `(companion_type, (companion_x_position, companion_y_position))` or `None` if there is no companion.

    takes `1` tick to execute.

    example usage:
    ```
    companion = get_companion()
    if companion != None:
        plant_type, (x, y) = companion
        print(f"Companion: {plant_type} at ({x}, {y})")
    ```
    """
    ...


# -------------------------------------------------------------------------------
def unlock(unlock: Unlock) -> bool:
    """
    Has exactly the same effect as clicking the button corresponding to `unlock` in the research tree.

    returns `True` if the unlock was successful, `False` otherwise.

    takes `200` ticks to execute if it succeeded, `1` tick otherwise.

    example usage:
    ```
    unlock(Unlocks.Carrots)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def num_unlocked(thing: Unlock | Entity | Ground | Item) -> int:
    """
    Used to check if an unlock, entity, ground or item is already unlocked.

    returns `1` plus the number of times `thing` has been upgraded if `thing` is upgradable. Otherwise returns `1` if `thing` is unlocked, `0` otherwise.

    takes `1` tick to execute.

    example usage:
    ```
    if num_unlocked(Unlocks.Carrots) > 0:
        plant(Entities.Carrot)
    else:
        print("Carrots not unlocked yet")
    ```
    """
    ...


# -------------------------------------------------------------------------------
def measure(direction: Optional[Direction] = None) -> float | Tuple[int, int] | None:
    """
    Can measure some values on some entities. The effect of this depends on the entity.

    overloads:
    `measure()`: measures the entity under the drone.
    `measure(direction)`: measures the neighboring entity in the `direction` of the drone.

    Sunflower: returns the number of petals.
    Maze: returns the position of the current treasure from anywhere in the maze.
    Cactus: returns the size.
    Dinosaur: returns the number corresponding to the type.
    All other entities: returns `None`.

    takes `1` tick to execute.

    example usage:
    ```
    num_petals = measure()
    treasure_pos = measure()  # Works anywhere in maze
    ```
    """
    ...


# -------------------------------------------------------------------------------
def leaderboard_run(leaderboard: Leaderboard, file_name: str, speedup: float) -> None:
    """
    Starts a timed run for the `leaderboard` using the specified `file_name` as a starting point.
    `speedup` sets the starting speedup.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    leaderboard_run(Leaderboards.Fastest_Reset, "full_run", 256)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def simulate(filename: str, sim_unlocks: Dict[Unlocks, float] | Iterable[Unlocks] | type[Unlocks], sim_items: Dict[Item, float], sim_globals: Dict[str, Any], seed: float, speedup: float) -> float:
    """
    Starts a simulation for the leaderboard using the specified `file_name` as a starting point.

    `sim_unlocks`: A sequence containing the starting unlocks.

    `sim_items`: A dict mapping items to amounts. The simulation starts with these items.

    `sim_globals`: A dict mapping variable names to values. The simulation starts with these variables in the global scope.

    `seed`: The random seed of the simulation. Must be a positive integer.

    `speedup`: The starting speedup.

    returns the time it took to run the simulation.

    takes `200` ticks to execute.

    example usage:

    ```
    filename = "f1"
    sim_unlocks = Unlocks
    sim_items = {Items.Carrot : 10000, Items.Hay : 50}
    sim_globals = {"a" : 13}
    seed = 0
    speedup = 64
    run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def quick_print(*something: Any) -> None:
    """
    Prints a value just like `print()` but it doesn't stop to write it into the air so it can only be found on the output page.

    returns `None`

    takes `0` ticks to execute.

    example usage:
    ```
    quick_print('hi mom')
    ```
    """
    ...


# -------------------------------------------------------------------------------
def random() -> float:
    """
    Samples a random number between 0 (inclusive) and 1 (exclusive).

    returns the random number.

    takes `1` ticks to execute.

    example usage:
    ```
    def random_elem(list):
        index = random() * len(list) // 1
        return list[index]
    ```
    """
    ...


# -------------------------------------------------------------------------------
def str(obj: Any) -> str:
    """
    Converts an object to its string representation.

    returns the string representation of the object.

    takes `1` tick to execute.

    example usage:
    ```
    string = str(1000)
    print(string)  # prints "1000"
    ```
    """
    ...


# -------------------------------------------------------------------------------
def min(*args: Any) -> Any:
    """
    Gets the minimum of a sequence of elements or several passed arguments.
    Can be used on numbers and strings.

    `min(a,b,c)`: Returns the minimum of `a`, `b` and `c`.
    `min(sequence)`: Returns the minimum of all values in a sequence.

    returns the minimum value from the arguments.

    takes #comparisons ticks to execute.

    example usage:
    ```
    smallest = min(1, 5, 3, 2)
    smallest_from_list = min([3, 6, 34, 16])
    ```
    """
    ...


# -------------------------------------------------------------------------------
def max(*args: Any) -> Any:
    """
    Gets the maximum of a sequence of elements or several passed arguments.
    Can be used on numbers and strings.

    `max(a,b,c)`: Returns the maximum of `a`, `b` and `c`.
    `max(sequence)`: Returns the maximum of all values in a sequence.

    returns the maximum value from the arguments.

    takes #comparisons ticks to execute.

    example usage:
    ```
    largest = max(1, 5, 3, 2)
    largest_from_list = max([3, 6, 34, 16])
    ```
    """
    ...


# -------------------------------------------------------------------------------
def abs(x: float) -> float:
    """
    Returns the absolute value of a number.

    returns the absolute value of x.

    takes `1` tick to execute.

    example usage:
    ```
    positive = abs(-5)
    print(positive)  # prints 5
    ```
    """
    ...


# -------------------------------------------------------------------------------
def change_hat(hat: Hat) -> None:
    """
    Changes the hat of the drone to the specified `hat`.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    change_hat(Hats.Dinosaur_Hat)
    ```
    ...
    """
    ...


# -------------------------------------------------------------------------------
def spawn_drone(filename: str) -> Any:
    """
    Spawns a new drone in the same position as the drone that ran the `spawn_drone(function)` command. The new drone then begins executing the specified function. After it is done, it will disappear automatically.

    returns the handle of the new drone or `None` if all drones are already spawned.

    takes `200` ticks to execute if a drone was spawned, `1` otherwise.

    example:
    ```
    def harvest_column():
        for _ in range(get_world_size()):
            harvest()
            move(North)

    while True:
        if spawn_drone(harvest_column):
            move(East)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def wait_for(drone: Any) -> Any:
    """
    Waits until the given drone terminates.

    returns the return value of the function that the drone was running.

    takes `1` tick to execute if the awaited drone is already done.

    example:
    ```
    def get_entity_type_in_direction(dir):
        move(dir)
        return get_entity_type()

    def zero_arg_wrapper():
        return get_entity_type_in_direction(North)
    handle = spawn_drone(zero_arg_wrapper)
    print(wait_for(handle))
    ```
    """
    ...

# -------------------------------------------------------------------------------
def has_finished(drone: Any) -> Any:
    """
    Checks if the given drone has finished.

    returns `True` if the drone has finished, `False` otherwise.

    takes `1` tick to execute.

    example:
    ```
    drone = spawn_drone(function)
    while not has_finished(drone):
        do_something_else()
    result = wait_for(drone)
    ```
    """
    ...

# -------------------------------------------------------------------------------
def max_drones() -> int:
    """
    returns the maximum number of drones that you can have in the farm.

    takes `1` tick to execute.

    example:
    ```
    while num_drones() < max_drones():
        spawn_drone("some_file_name")
        move(East)
    ```
    """
    ...

# -------------------------------------------------------------------------------
def num_drones() -> int:
    """
    returns the number of drones currently in the farm.

    takes `1` tick to execute.

    example:
    ```
    while num_drones() < max_drones():
        spawn_drone("some_file_name")
        move(East)
    ```
    """
    ...

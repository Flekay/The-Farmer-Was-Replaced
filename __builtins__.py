from typing import Any, Optional, Iterable


# -------------------------------------------------------------------------------
class Item:
    """A member of the Items Class"""


class Items:
    Bone: Item
    """
    Obtained by the dinosaur minigame.\n
    Used for upgrades.
    """

    Cactus: Item
    """
    Obtained by harvesting sorted cacti.\n
    Used for upgrades.
    """

    Carrot: Item
    """
    Obtained by harvesting fully grown carrots.\n
    Used to plant `Entities.Pumpkin` and `Entities.Sunflower`. Also used for upgrades.
    """

    Fertilizer: Item
    """
    Obtained over time after unlocking the `Unlocks.Fertilizer` upgrade.\n
    Used to reduce the remaining growing time of the plant under the drone by 2 seconds.\n
    Note: Plants speed up with fertilizer will be infected with `Items.Weird_Substance`.
    """

    Gold: Item
    """
    Obtained by harvesting treasure chests in mazes.\n
    Used for upgrades.
    """

    Hay: Item
    """
    Obtained by harvesting grass.\n
    Used to plant `Entities.Carrot`. Also used for upgrades.
    """

    Power: Item
    """
    Obtained by harvesting sunflowers.\n
    Automatically used by the drone to speed up the execution by 100%.
    """

    Pumpkin: Item
    """
    Obtained by harvesting pumpkins.\n
    Used to plant `Entities.Cactus`. Also used for upgrades. Also used for Apples in the Dinosaur game.
    """

    Water: Item
    """
    Obtained over time after unlocking the `Unlocks.Watering` upgrade.\n
    Increases water level under the drone by 0.25 per use. The water level is capped at 1.
    """

    Weird_Substance: Item
    """
    Obtained by harvesting infected plants.\n
    Used on bushes to spawn a maze.\n
    e.g.\n
    `use_item(Items.Weird_Substance, n)` where `n` determines the size of the maze.
    """

    Wood: Item
    """
    Obtained by harvesting bushes and trees.\n
    Used to plant `Entities.Carrot`. Also used for upgrades.
    """


# -------------------------------------------------------------------------------
class Hat:
    """A member of the Hats class"""

class Hats:
    Straw_Hat: Hat
    """The default hat."""

    Dinosaur_Hat: Hat
    """Equip it to start the dinosaur game."""

# -------------------------------------------------------------------------------
class Leaderboard:
    """A member of the Leaderboards class"""

class Leaderboards:
    Cactus: Leaderboard
    """
    Goal: Farm 100000 cacti efficiently
    Success: num_items(Items.Cactus) >= 100000
    Starting Conditions:
    - All unlocks available
    - Required growing resources
    - Lots of power
    """

    Carrots: Leaderboard
    """
    Goal: Farm 100000 carrots efficiently
    Success: num_items(Items.Carrot) >= 100000
    Starting Conditions:
    - All unlocks available
    - Required growing resources
    - Lots of power
    """

    Dinosaur10x10: Leaderboard
    """
    Goal: Farm 98010 bones (fill 10x10 area with tail)
    Success: num_items(Items.Bone) >= 98010
    Starting Conditions:
    - All unlocks available
    - 1000000 Pumpkin
    - 1000000 Power
    """

    Fastest_Reset: Leaderboard
    """
    Goal: Automate game progression from start to unlocking Leaderboards
    Success: num_unlocked(Unlocks.Leaderboard) > 0
    Starting Conditions:
    - Empty farm
    - No unlocks
    - No items
    """

    Hay: Leaderboard
    """
    Goal: Farm 100000 hay efficiently
    Success: num_items(Items.Hay) >= 100000
    Starting Conditions:
    - All unlocks available
    - Required growing resources
    - Lots of power
    """

    Maze10x10: Leaderboard
    """
    Goal: Farm 300000 gold (equivalent to solving 300 mazes)
    Success: num_items(Items.Gold) >= 300000
    Starting Conditions:
    - All unlocks available
    - 1000000 Weird_Substance
    - 1000000 Power
    """

    Polyculture: Leaderboard
    """
    Goal: Farm 100000 of each polyculture resource
    Success: num_items() >= 100000 for all polyculture resources
    Starting Conditions:
    - All unlocks available
    - Required growing resources
    - Lots of power
    """

    Pumpkins: Leaderboard
    """
    Goal: Farm 100000 pumpkins efficiently
    Success: num_items(Items.Pumpkin) >= 100000
    Starting Conditions:
    - All unlocks available
    - Required growing resources
    - Lots of power
    """

    Sunflowers: Leaderboard
    """
    Goal: Farm 2400 power efficiently
    Success: num_items(Items.Power) >= 2400
    Starting Conditions:
    - All unlocks available
    - Required growing resources
    - No starting power
    """

    Wood: Leaderboard
    """
    Goal: Farm 100000 wood efficiently
    Success: num_items(Items.Wood) >= 100000
    Starting Conditions:
    - All unlocks available
    - Required growing resources
    - Lots of power
    """

# -------------------------------------------------------------------------------
class Entity:
    """A member of the Entities Class"""

class Entities:
    Apple: Entity
    """
    Food for dinosaurs

    Growth time: 0.2s fixed
    Grows on: Grassland or soil
    Plant cost: 2 Pumpkins
    Drops: None (consumed by dinosaurs)
    Note: Can be collected before fully grown
    """

    Bush: Entity
    """
    Basic wood source

    Growth time: 3.2-4.8s
    Grows on: Grassland or soil
    Plant cost: None
    Drops: Items.Wood
    """

    Cactus: Entity
    """
    Grows in 10 different sizes
    Must be harvested in sorted order for drops

    Growth time: 0.9-1.1s
    Grows on: Soil only
    Plant cost: 20 Pumpkins
    Drops: Items.Cactus
    """

    Carrot: Entity
    """
    Basic crop resource

    Growth time: 4.8-7.2s
    Grows on: Soil only
    Plant cost: 1 Wood + 1 Hay
    Drops: Items.Carrot
    """

    Grass: Entity
    """
    Base resource that grows automatically on grassland
    Can be manually planted on soil

    Growth time: 0.5s fixed
    Grows on: Grassland or soil
    Plant cost: None
    Drops: Items.Hay
    """

    Hedge: Entity
    """
    Maze wall. Created by fertilizing grown bush.

    Growth time: N/A
    Grows on: N/A
    Plant cost: N/A
    Drops: None
    """

    Pumpkin: Entity
    """
    Forms mega-pumpkins with adjacent ripe pumpkins
    20% chance to die when grown

    Growth time: 0.2-3.8s
    Grows on: Soil only
    Plant cost: 1 Carrot
    Drops: Items.Pumpkin
    """

    Sunflower: Entity
    """
    Power generator. Harvesting the sunflower with the most petals gives you bonus yield.

    Growth time: 5.6-8.4s
    Grows on: Soil only
    Plant cost: 1 Carrot
    Drops: Items.Power
    """

    Treasure: Entity
    """
    Found in mazes. Gold amount = maze size.

    Growth time: N/A
    Grows on: N/A
    Plant cost: N/A
    Drops: Items.Gold
    """

    Tree: Entity
    """
    Advanced wood source. Growth slowed by adjacent trees.

    Growth time: 5.6-8.4s (longer with adjacent trees)
    Grows on: Grassland or soil
    Plant cost: None
    Drops: Items.Wood
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
    """
    Unlock: Automatically unlock new abilities
    Upgrade: None
    """

    Cactus: Unlock
    """
    Unlock: Plant and harvest cacti
    Cost: 4000 Pumpkins
    Upgrade: Increases cactus yield and seed cost
    """

    Carrots: Unlock
    """
    Unlock: Till soil and plant carrots
    Cost: 100 Wood
    Upgrade: Increases carrot yield and cost
    """

    Costs: Unlock
    """
    Unlock: Access to get_cost() function
    Upgrade: None
    """

    Debug: Unlock
    """
    Unlock: Basic debugging tools
    Upgrade: None
    """

    Debug_2: Unlock
    """
    Unlock: Advanced debugging features
    Upgrade: None
    """

    Dictionaries: Unlock
    """
    Unlock: Use Python dictionaries and sets
    Upgrade: None
    """

    Dinosaurs: Unlock
    """
    Unlock: Dinosaur minigame access
    Cost: 4000 Pumpkins
    Upgrade: Increases dinosaur yield and costs
    """

    Expand: Unlock
    """
    Unlock: Larger farm and movement
    Cost: 30 Hay
    Upgrade: Increases farm size (clears farm)
    """

    Fertilizer: Unlock
    """
    Unlock: Speed up plant growth
    Cost: 1000 Wood
    Note: Creates Weird_Substance when used
    """

    Functions: Unlock
    """
    Unlock: Define custom functions
    Upgrade: None
    """

    Grass: Unlock
    """
    Unlock: Enhanced grass operations
    Cost: 300 Hay
    Upgrade: Increases grass yield
    """

    Leaderboard: Unlock
    """
    Unlock: Access to leaderboards
    Cost: 300000 Gold + 500000 Cactus + 400000 Bone
    Upgrade: None
    """

    Lists: Unlock
    """
    Unlock: Use Python lists
    Upgrade: None
    """

    Loops: Unlock
    """
    Unlock: Use while loops
    Upgrade: None
    """

    Mazes: Unlock
    """
    Unlock: Generate and solve mazes
    Cost: 3000 Pumpkins
    Upgrade: Increases treasure gold amounts
    """

    Operators: Unlock
    """
    Unlock: Use arithmetic/logic operators
    Upgrade: None
    """

    Plant: Unlock
    """
    Unlock: Basic planting ability
    Cost: 50 Hay
    Upgrade: None
    """

    Polyculture: Unlock
    """
    Unlock: Companion planting bonuses
    Cost: 800 Gold
    Upgrade: None
    """

    Pumpkins: Unlock
    """
    Unlock: Plant and harvest pumpkins
    Cost: 500 Wood + 350 Carrot
    Upgrade: Increases pumpkin yield
    """

    Senses: Unlock
    """
    Unlock: Drone position/tile awareness
    Upgrade: None
    """

    Simulation: Unlock
    """
    Unlock: Access to simulation mode
    Upgrade: None
    """

    Speed: Unlock
    """
    Unlock: Basic drone speed
    Cost: 20 Hay
    Upgrade: Further increases speed
    """

    Sunflowers: Unlock
    """
    Unlock: Power generation
    Cost: 200 Carrot
    Upgrade: Increases power yield
    """

    Timing: Unlock
    """
    Unlock: Performance measurement
    Upgrade: None
    """

    Trees: Unlock
    """
    Unlock: Tree farming
    Cost: 50 Wood + 70 Carrot
    Upgrade: Increases wood yield
    """

    Utilities: Unlock
    """
    Unlock: min(), max(), abs() functions
    Upgrade: None
    """

    Variables: Unlock
    """
    Unlock: Use variables
    Upgrade: None
    """

    Watering: Unlock
    """
    Unlock: Water plants
    Cost: 50 Wood
    Upgrade: None
    """



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
def get_tick_count() -> float:
    """
    Used to measure the number of ticks performed.

    returns the number of ticks performed since the start of execution.

    takes `1` tick to execute.

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
    Attempts to use the specified `item` `n` times. Can only be used with some items including `Items.Water`, `Items.Fertilizer` and `Items.Egg`.

    returns `True` if an item was used, `False` otherwise.

    takes `200` ticks to execute if it succeeded, `1` tick otherwise.

    example usage:
    ```
    use_item(Items.Fertilizer)
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
def set_farm_size(size: float) -> None:
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
    set_farm_size(5)
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
    if num_items(Items.Fertilizer) == 0:
        trade(Items.Fertilizer)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_cost(thing: Entity | Item | Unlock) -> dict[Item, float] | None:
    """
    Gets the cost of a `thing`

    If `thing` is an item: get the cost of buying it when using `trade(item)`.
    If `thing` is an entity: get the seed needed to plant it.
    If `thing` is an unlock: get the cost of unlocking it.

    - returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.
    - returns `None` when used on an upgradeable unlock that is already at the max level.

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
def get_companion() -> tuple[Entity, tuple[int, int]] | None:
    """
    Get the companion preference of the plant under the drone.

    returns a list of the form `(companion_type, (companion_x_position, companion_y_position))`

    takes `1` tick to execute.

    example usage:
    ```
    companion = get_companion()
    if companion != None:
        print(companion)
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
    if num_unlocked(Unlocks.Multi_Trade) > 0:
        trade(Items.Carrot_Seed, 10)
    else:
        for i in range(10):
            trade(Items.Carrot_Seed)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def measure(direction: Optional[Direction] = None) -> float | tuple[int, int] | None:
    """
    Can measure some values on some entities. The effect of this depends on the entity.

    overloads:
    `measure()`: measures the entity under the drone.
    `measure(direction)`: measures the neighboring entity in the `direction` of the drone.

    Sunflower: returns the number of petals.
    Treasure: returns the next position.
    Cactus: returns the size.
    Dinosaur: returns the number corresponding to the type.
    All other entities: returns `None`.

    takes `1` tick to execute.

    example usage:
    ```
    num_petals = measure()
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
def simulate(filename: str, sim_unlocks: dict[Unlocks, float] | Iterable[Unlocks], sim_items: dict[Items, float], sim_globals: dict[str, Any], seed: float, speedup: float) -> None:
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

    takes `1` ticks to execute.

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

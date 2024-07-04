from typing import Any, Optional


# -------------------------------------------------------------------------------
class Items:
    @property
    def Carrot(self):
        """Obtained by harvesting carrots."""
        ...

    @property
    def Carrot_Seed(self):
        """Used to grow carrots by calling `plant(Entities.Carrots)` on empty soil."""
        ...

    @property
    def Empty_Tank(self):
        """Empty tanks automatically turn into water tanks over time."""
        ...

    @property
    def Fertilizer(self):
        """Call `use_item(Items.Fertilizer)` to instantly grow the plant under the drone by 2s."""
        ...

    @property
    def Gold(self):
        """Found in treasure chests in mazes."""
        ...

    @property
    def Hay(self):
        """Obtained by cutting grass."""
        ...

    @property
    def Power(self):
        """Obtained by harvesting sunflowers. The drone automatically uses this to move twice as fast."""
        ...

    @property
    def Pumpkin(self):
        """Obtained when harvesting pumpkins."""
        ...

    @property
    def Pumpkin_Seed(self):
        """Used to grow pumpkins by calling `plant(Entities.Pumpkin)` on empty soil."""
        ...

    @property
    def Sunflower_Seed(self):
        """Used to grow sunflowers by calling `plant(Entities.Sunflower)` on empty soil."""
        ...

    @property
    def Water_Tank(self):
        """Used to water the ground by calling `use_item(Items.Water_Tank)`."""
        ...

    @property
    def Wood(self):
        """Obtained from bushes and trees."""
        ...

    @property
    def Cactus(self):
        """Obtained when harvesting sorted cacti."""
        ...

    @property
    def Cactus_Seed(self):
        """Used to grow cacti by calling `plant(Entities.Cactus)` on empty soil."""
        ...

    @property
    def Egg(self):
        """Call `use_item(Items.Egg)` to hatch a majestic dinosaur."""
        ...

    @property
    def Bones(self):
        """The bones of an ancient creature."""
        ...


# -------------------------------------------------------------------------------
class Entities:
    @property
    def Grass(self):
        """
        Grows automatically. Harvest it to obtain `Items.Hay`.

        Average seconds to grow: 0.5
        Grows on: turf or soil
        """
        ...

    @property
    def Bush(self):
        """
        A small bush that drops `Items.Wood`.

        Average seconds to grow: 4
        Grows on: turf or soil
        """
        ...

    @property
    def Tree(self):
        """
        Trees drop more wood than bushes. They take longer to grow if other trees grow next to them.

        Average seconds to grow: 7
        Grows on: turf or soil
        """
        ...

    @property
    def Carrots(self):
        """
        Carrots!

        Average seconds to grow: 6
        Grows on: soil
        """
        ...

    @property
    def Pumpkin(self):
        """
        Pumpkins grow together when they are next to other fully grown pumpkins. About 1 in 5 pumpkins dies when it grows up.
         When you harvest a pumpkin you get `Items.Pumpkin` equal to the number of pumpkins in the mega pumpkin cubed.

        Average seconds to grow: 2
        Grows on: soil
        """
        ...

    @property
    def Sunflower(self):
        """
        Sunflowers collect the power from the sun. Harvesting them will give you `Items.Power` equal to the number of sunflowers in the farm.
         If you harvest a sunflower that doesn't have the maximum number of petals all the sunflowers will die.

        Average seconds to grow: 5
        Grows on: soil
        """
        ...

    @property
    def Cactus(self):
        """
        Cacti come in 10 different sizes. When harvested, all cacti on the field will be harvested. Only those that are in sorted order will drop `Items.Cactus`.

        Average seconds to grow: 1
        Grows on: soil
        """
        ...

    @property
    def Hedge(self):
        """Part of the maze. Grow a maze by fertilizing a fully grown bush."""
        ...

    @property
    def Treasure(self):
        """A treasure that contains gold equal to the side length of the maze in which it is hidden. It can be harvested like a plant."""
        ...

    @property
    def Dinosaur(self):
        """
        A majestic dinosaur. It moves around randomly but won't move for a while after being measured. Harvesting it harvests all adjacent dinosaurs of the same type and makes them drop `Items.Bones`.

        Average seconds to grow: 0.2
        Grows on: turf or soil
        """
        ...


# -------------------------------------------------------------------------------
class Grounds:
    @property
    def Turf(self):
        """The default ground. Grass will automatically grow on it."""
        ...

    @property
    def Soil(self):
        """Calling `till()` turns the ground into this. Calling `till()` again changes it back to turf."""
        ...


# -------------------------------------------------------------------------------
class Unlocks:
    @property
    def Trees(self):
        """
        Unlock: Unlocks trees.
        Upgrade: Increases the yield of bushes and trees.
        """
        ...

    @property
    def Speed(self):
        """Increases the speed of the drone."""
        ...

    @property
    def Plant(self):
        """Unlocks planting."""
        ...

    @property
    def Loops(self):
        """Unlocks a simple while loop."""
        ...

    @property
    def Senses(self):
        """The drone can see what's under it and where it is."""
        ...

    @property
    def Expand(self):
        """
        Unlock: Expands the farm land and unlocks movement.
        Upgrade: Expands the farm. This also clears the farm.
        """
        ...

    @property
    def Operators(self):
        """Arithmetic, comparison and logic operators."""
        ...

    @property
    def Pumpkins(self):
        """
        Unlock: Pumpkins!
        Upgrade: Increases the yield of pumpkins and the cost of pumpkin seeds.
        """
        ...

    @property
    def Variables(self):
        """Assign values to variables."""
        ...

    @property
    def Functions(self):
        """Define your own functions."""
        ...

    @property
    def Watering(self):
        """Water the plants to make them grow faster."""
        ...

    @property
    def Carrots(self):
        """
        Unlock: Till the soil and plant carrots.
        Upgrade: Increases the yield of carrots and the cost of carrot seeds.
        """
        ...

    @property
    def Lists(self):
        """Use lists to store lots of values."""
        ...

    @property
    def Costs(self):
        """Allows access to the cost of things."""
        ...

    @property
    def Fertilizer(self):
        """Grow plants instantly."""
        ...

    @property
    def Mazes(self):
        """
        Unlock: A maze with a treasure in the middle.
        Upgrade: Increases the gold in treasure chests.
        """
        ...

    @property
    def Debug(self):
        """Tools to help with debugging programs."""
        ...

    @property
    def Debug_2(self):
        """Functions to temporarily slow down the execution and make the grid smaller."""
        ...

    @property
    def Benchmark():
        """Functions to help measure performance."""
        ...

    @property
    def Grass(self):
        """Increases the yield of grass."""
        ...

    @property
    def Multi_Trade(self):
        """Trade multiple items at once."""
        ...

    @property
    def Auto_Unlock(self):
        """Automatically unlock things."""
        ...

    @property
    def Polyculture(self):
        """Use companion planting to increase the yield."""
        ...

    @property
    def Sunflowers(self):
        """
        Unlock: Sunflowers and Power.
        Upgrade: Increases the power gained from sunflowers.
        """
        ...

    @property
    def Leaderboard(self):
        """Join the leaderboard for the fastest reset time."""
        ...

    @property
    def Dictionaries(self):
        """Get access to dictionaries and sets."""
        ...

    @property
    def Utilities(self):
        """Unlocks the `min()`, `max()` and `abs()` functions."""
        ...

    @property
    def Cactus(self):
        """
        Unlock: Cactus!
        Upgrade: Increases the yield of cactus and the cost of cactus seeds."""
        ...

    @property
    def Dinosaurs(self):
        """
        Unlock: Majestic ancient creatures.
        Upgrade: Increases the yield of dinosaurs and the cost of eggs.
        """
        ...


# -------------------------------------------------------------------------------
class North:
    """
    The direction north, i.e. up.
    """


# -------------------------------------------------------------------------------
class East:
    """
    The direction east, i.e. right.
    """


# -------------------------------------------------------------------------------
class South:
    """
    The direction south, i.e. down.
    """


# -------------------------------------------------------------------------------
class West:
    """
    The direction west, i.e. left.
    """


# -------------------------------------------------------------------------------
def harvest() -> bool:
    """
    Harvests the entity under the drone.
    If you harvest an entity that can't be harvested, it will be destroyed.

    returns `True` if an entity was removed, `False` otherwise.

    takes the time of `200` operations to execute if an entity was removed, `1` operation otherwise.

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

    takes the time of `1` operation to execute.

    example usage:
    ```
    if can_harvest():
        harvest()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def plant(entity: Entities) -> bool:
    """
    Plants the specified `entity` under the drone if it can be planted.
    Otherwise it just does nothing.

    returns `True` if it succeeded, `False` otherwise.

    takes the time of `200` operations to execute if it succeeded, `1` operation otherwise.

    example usage:
    ```
    plant(Entities.Bush)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def move(direction: North | East | South | West) -> None:
    """
    Moves the drone into the specified `direction` by one tile.
    If the drone moves over the edge of the farm it wraps back to the other side of the farm.

    - `East `  =  right
    - `West `  =  left
    - `North`  =  up
    - `South`  =  down

    returns `True` if the drone has moved, `False` otherwise.

    takes the time of `200` operations to execute if the drone has moved, `1` operation otherwise.

    example usage:
    ```
    move(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def swap(direction: North | East | South | West) -> None:
    """
    Swaps the entity under the drone with the entity next to the drone in the specified `direction`.
    - Doesn't work on all entities.
    - Also works if one (or both) of the entities are `None`.

    returns `None`

    takes the time of `200` operations to execute.

    example usage:
    ```
    swap(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def till() -> None:
    """
    Tills the ground under the drone into soil. If it's already soil it will change the ground back to turf.

    returns `None`

    takes the time of `200` operations to execute.

    example usage:
    ```
    till()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_pos_x() -> float:
    """
    Gets the current x position of the drone.
    The x position starts at `0` in the `West` and increases in the `East` direction.

    returns a number representing the current x coordinate of the drone.

    takes the time of `1` operation to execute.

    example usage:
    ```
    x, y = get_pos_x(), get_pos_y()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_pos_y() -> float:
    """
    Gets the current y position of the drone.
    The y position starts at `0` in the `South` and increases in the `North` direction.

    returns a number representing the current y coordinate of the drone.

    takes the time of `1` operation to execute.

    example usage:
    ```
    x, y = get_pos_x(), get_pos_y()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_world_size() -> float:
    """
    Get the current size of the farm.

    returns the side length of the grid in the north to south direction.

    takes the time of `1` operation to execute.

    example usage:
    ```
    for i in range(get_world_size()):
        move(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_entity_type() -> Entities | None:
    """
    Find out what kind of entity is under the drone.

    returns `None` if the tile is empty, otherwise returns the type of the entity under the drone.

    takes the time of `1` operation to execute.

    example usage:
    ```
    if get_entity_type() == Entities.Grass:
        harvest()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_ground_type() -> Grounds:
    """
    Find out what kind of ground is under the drone.

    returns the type of the ground under the drone.

    takes the time of `1` operation to execute.

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

    takes the time of `1` operation to execute.

    example usage:
    ```
    start = get_time()

    do_something()

    time_passed = get_time() - start
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_op_count() -> float:
    """
    Used to measure the number of operations performed.

    returns the number of operations performed since the start of execution.

    takes the time of `1` operation to execute.

    example usage:
    ```
    do_something()

    print(get_op_count())
    ```
    """
    ...


# -------------------------------------------------------------------------------
def trade(item: Items, n: Optional[float] = None) -> bool:
    """
    Tries to buy the specified `item`.
     If the `item` cannot be bought or you don't have the required resources it simply does nothing.

    overloads:
    `trade(item)`: Buy the `item` once.
    `trade(item, n)`: If `Unlocks.Multi_Trade` is unlocked, this will buy the `item` `n` times immediately. If you can't afford all `n` items, it won't buy any at all. If `Unlocks.Multi_Trade` is not unlocked, it throws an error.

    returns `True` if it was able to buy the item(s), `False` otherwise.

    takes the time of `200` operations to execute if it succeeded, `1` operation otherwise.

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
def use_item(item: Items) -> bool:
    """
    Attempts to use the specified `item`. Can only be used with some items including `Items.Water_Tank`, `Items.Fertilizer` and `Items.Egg`.

    returns `True` if an item was used, `False` otherwise.

    takes the time of `200` operations to execute if it succeeded, `1` operation otherwise.

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

    takes the time of `1` operation to execute.

    example usage:
    ```
    if get_water() < 0.5:
        use_item(Items.Water_Tank)
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

    takes the time of `200` operations to execute.

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
    Also clears the farm.
    - Sets the farm to a `size` x `size` grid.
    - The smallest `size` possible is `3`.
    - A `size` smaller than `3` will change the grid back to its full size.
    - The effect will also stop when the execution stops.

    returns `None`

    takes the time of `200` operations to execute.

    example usage:
    ```
    set_farm_size(5)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def num_items(item: Items) -> float:
    """
    Find out how much of `item` you currently have.

    returns the number of `item` currently in your inventory.

    takes the time of `1` operation to execute.

    example usage:
    ```
    if num_items(Items.Fertilizer) == 0:
        trade(Items.Fertilizer)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_cost(thing: Entities | Items | Unlocks) -> dict[Items, float] | None:
    """
    Gets the cost of a `thing`

    If `thing` is an item: get the cost of buying it when using `trade(item)`.
    If `thing` is an entity: get the seed needed to plant it.
    If `thing` is an unlock: get the cost of unlocking it.

    - returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.
    - returns `None` when used on an upgradeable unlock that is already at the max level.

    takes the time of `1` operation to execute.

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
    Removes everything from the farm, and moves the drone back to position `(0,0)`.

    returns `None`

    takes the time of `200` operations to execute.

    example usage:
    ```
    clear()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_companion() -> list[Entities, float, float] | None:
    """
    Get the companion preference of the plant under the drone.

    returns a list of the form `[companion_type, companion_x_position, companion_y_position]`

    takes the time of `1` operation to execute.

    example usage:
    ```
    companion = get_companion()
    if companion != None:
        print(companion)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def unlock(unlock: Unlocks) -> bool:
    """
    Has exactly the same effect as clicking the button corresponding to `unlock` in the research tree.

    returns `True` if the unlock was successful, `False` otherwise.

    takes the time of `200` operations to execute if it succeeded, `1` operation otherwise.

    example usage:
    ```
    unlock(Unlocks.Carrots)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def num_unlocked(thing: Unlocks | Entities | Grounds | Items) -> float:
    """
    Used to check if an unlock, entity, ground or item is already unlocked.

    returns `1` plus the number of times `thing` has been upgraded if `thing` is upgradable. Otherwise returns `1` if `thing` is unlocked, `0` otherwise.

    takes the time of `1` operation to execute.

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
def measure(direction: Optional[North | East | South | West] = None) -> float | None:
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

    takes the time of `1` operation to execute.

    example usage:
    ```
    num_petals = measure()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def timed_reset() -> None:
    """
    Starts a timed run for the leaderboard. Saves the game before the run and then loads that save afterwards so you can't gain any items during the run.

    returns `None`

    takes the time of `200` operations to execute.

    example usage:
    ```
    timed_reset()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def quick_print(*something: Any) -> None:
    """
    Prints a value just like `print()` but it doesn't stop to write it into the air so it can only be found on the output page.

    returns `None`

    takes the time of `1` operations to execute.

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

    takes the time of `1` operations to execute.

    example usage:
    ```
    def random_elem(list):
        index = random() * len(list) // 1
        return list[index]
    ```
    """
    ...

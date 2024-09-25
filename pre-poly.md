made by @placeholder



Farm 50 Hay
unlock Grass 1

Farm 20 Hay
unlock Speed 1

Farm 50 Hay
unlock Plant

Farm 30 Hay
unlock Expand 1

expected time: 1m 16.5s


Farm 20 Wood and roughly 108 Hay
unlock Expand 2

expected time: 1m 59.5s


Farm 10 Wood
unlock Speed 2

Farm Wood and Hay simultaneously, prioritizing Wood
at 300 Hay, unlock Grass 2
at 67 Hay and 202 Wood, unlock Carrots 1
trade for 67 Carrot Seed

(7 bushes are remaining on the farm; when harvested, the wood count will be 42.)

expected time: 4m 35.5s


Farm Carrots, Wood and Hay simultaneously, prioritized in that order
at 50 Wood, stop farming Wood and just farm Carrots and Hay
at 200 Carrot and 300 Hay, unlock Trees 1 and Trees 2 simultaneously

expected time: 5m 55s


Farm 101 Wood and 51 Hay
trade for 51 Carrot Seed
Farm Carrots until 50 Carrot
unlock Expand 3

(34 Carrot Seed left over)

expected time: 6m 35s


Farm 50 Wood and 100 Carrot
unlock Speed 3

Farm Wood and Hay until 386 Wood
trade for 86 Carrot Seed
unlock Carrots 2

expected time: 7m 35s


Farm Wood and Carrots simultaneously
buy Tanks whenever affordable, 16 at a time, until you have 80 total tanks

expected time: 8m 18s


Farm 500 Carrot
(with a few Carrots remaining on the farm to buy Sunflower seeds)
unlock Sunflowers 1

expected time: 8m 44s


do one round of Sunflowers

Farm 76 Wood and 76 Hay, watering Trees at 0.1 once 8 water tanks have stocked up
trade 38 Carrot Seed

Farm 100 Wood and 200 Carrots, watering Trees at 0.1
(once Wood target is met, switch to only farming Carrots)
unlock Speed 4
(some carrots remaining on the farm for sunflower seeds)

do two more rounds of Sunflowers

expected time: 9m 18s


Plant 10 Trees along the edges of the 4x4 farm
use the remaining 6 tiles to farm Hay in a loop
farm literally just Hay until:
    Grass 3
    Grass 4
    Trees 3
    Trees 4
    ~ 700 Hay saved up

the goal is to have at least 24 water tanks stocked up by the end of this phase

expected time: 10m 37s


Farm Wood and Hay, watering Trees to 0.7 at the start of the phase
buy Tanks, 20 at a time, until you have 180 total tanks
at 840 Hay and 840 Wood, trade for 420 Carrot Seed


Farm Wood and Carrots simultaneously,
watering Carrots at 85% of the Trees level, which starts at 0.65
and getting the following unlocks:
    Carrots 3
    expected time: 11m 04s
    Speed 5
        water level switches to 0.75
    Carrots 4
    Speed 6
        water level switches to 0.85
    Carrots 5
    Speed 7
        water level switches to 0.94
    expected time: 11m 40s

    do three Sunflower rounds just as you run out of power

    at 3340 Wood (minus the 160 Wood remaining on the farm), swap to farming only Carrots
    continue until 4000 Carrot (minus the 192 Carrot remaining on the farm)

    expected time: 12m 40s


Plant 8 Trees along the edges of the 4x4 farm
use the remaining 8 tiles to farm Hay in a loop
farm 3000 Hay
farm 160 Wood from the Trees remaining on the farm

unlock Pumpkins 1
unlock Polyculture 1

~ 10 to 14 Power remaining

expected time: 13m 20s




if anyone tries to implement this just know that you will have slightly different resources at every split based on your particular implementation and approach to managing your farm efficiently

you will have to tweak values and your timestamps will differ here and there

there is also more room for optimization in doing more passes of Trees during the two Grass phases, and changing up exactly when you do and don't buy and/or use Tanks

the unlock cost scaling in this game is designed to only allow subexponential growth as opposed to exponential growth. You can't really get a crazy runaway growth effect from any of the basic crops until you have Poly -- except for Watering. Water tanks allow for exponential growth and, when used in an incredibly specific manner, you can get away with keeping the farm watered at an ideal level with only a minimal number of Tanks

have fun exploring the even more complicated space of possibilities. I think I've hit my limit with prepoly optimization lol

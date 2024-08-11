BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
clear()
for i in range(0,1,0):
    plant(BUSH)
    while get_entity_type() == BUSH:
        use_item(FERTILIZER)
    harvest()

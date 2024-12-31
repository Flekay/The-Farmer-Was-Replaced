def update_available_resources(unlockment):
	link = {
		Unlocks.Plant:Items.Wood,
		Unlocks.Carrots:Items.Carrot,
		Unlocks.Pumpkins:Items.Pumpkin,
		Unlocks.Mazes:Items.Gold,
		Unlocks.Cactus:Items.Cactus,
		Unlocks.Dinosaurs:Items.Bone,
	}
	if unlockment in link:
		available_resources[link[unlockment]] = True
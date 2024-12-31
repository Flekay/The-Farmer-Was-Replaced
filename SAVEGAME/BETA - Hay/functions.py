
def init_run(x,y,i):
	coords = (x,y)
	if coords in companions:
		plant(companions.pop(coords))
		#move(dir)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, pos = get_companion()
		companions[pos] = companion
		#move(dir)
		
		
def default_run(x,y,i):
	coords = (x, y)
	if coords in companions:
		comp = companions.pop(coords)
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, pos = get_companion()
		companions[pos] = companion
# TODO
# global logging switch/formatted logs
# modules/seperate file imports

# global config
waterThreshold = 0.005 # needs to be small enough that we aren't constantly running out of water, but still water shit frequenty

#Functions
# reliably rotates thru available plants to give us something new to plant
# TODO utilize lookup tables once lists unlocked
def determine_next_plant(currentPlant) -> Entities:
	if currentEntity == Entities.Bush:
		return Entities.Grass
	elif currentEntity == Entities.Grass:
		return Entities.Carrot
	elif currentEntity == Entities.Carrot:
		# Trees grow slower right next to eachother
		# So only grow trees on even coords
		if (get_pos_x() % 2 == 0) and (get_pos_y() % 2 == 0):
			return Entities.Tree
		else:
			return Entities.Bush
	elif currentEntity == Entities.Tree:
		return Entities.Bush
	else:
		quick_print("Unrecognized entity!")

# encapsulates logic for planting
# TODO logging
# TODO build a mapping table once lists or a better data structure unlocked
def plant_next(toPlant):
	if toPlant == Entities.Bush:
		plant(toPlant)
	elif toPlant == Entities.Grass:
		till()
		plant(toPlant)
	elif toPlant ==  Entities.Carrot:
		till()
		plant(toPlant)
	elif toPlant == Entities.Tree:
		plant(toPlant)
	else:
		plant(Entities.Bush)

def water():
	currentWaterLevel = get_water()

	if (currentWaterLevel < waterThreshold):
		quick_print("water level less than threshhold, watering")
		quick_print(currentWaterLevel)
		use_item(Items.Water)

#Main loop
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			# vertical processing
			groundType = get_ground_type()
			currentEntity = get_entity_type()

			quick_print(groundType)
			quick_print(currentEntity)
			quick_print(get_water())

			# harvest if possible
			if can_harvest():
				harvest()

				# plant something new each time based on the last thing harvested.
				nextPlant = determine_next_plant(currentEntity)
				plant_next(nextPlant)

			else:
				# somehow something got removed and is no plant there. put a bush there
				if currentEntity == None:
					plant(Entities.Bush)
			
			# maintain a low level of water but water
			water()

			# when done, move north
			move(North)
				
			quick_print("___________")

		# horizontal processing
		move(East)
	# map processing done
	# lets set a hat
	change_hat(Hats.Tree_Hat)

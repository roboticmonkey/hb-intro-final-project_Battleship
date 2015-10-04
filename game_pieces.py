import ship


class Game_Pieces(ship.Ship):
	"""Creates a group of ship for game play. 
	Keeps track of all the players ships. 
	Methond all_sunk checks to see if all ships have been sunk.
	 """
	
	def __init__(self, player_name):
		#super(Game_Pieces, self).__init__()
		self.player_name = player_name
		self.carrier = ship.Ship(5, "Carrier")
		self.battleship = ship.Ship(4, "Battleship")
		self.cruiser = ship.Ship(3, "Cruiser")
		self.sub = ship.Ship(3, "Submarine")
		self.destroyer = ship.Ship(3, "Destroyer")
		self.fleet_sunk = False

	#changes Game_Pieces attribute fleet_sunk to True
	def all_sunk(self):
		if (self.carrier.sunk == True and (self.battleship.sunk == True and
			 (self.cruiser.sunk == True and (self.sub.sunk == True and 
			 	self.destroyer.sunk == True)))):
			self.fleet_sunk = True
		# print "im in a method about to do some shit"
		# print "self.carrier.sunk: ", self.carrier.sunk
		# if (self.carrier.sunk == True):
		# 	print "i made it in the if statement"
		# 	self.fleet_sunk = True
		# 	print "try to set the self.fleet_sunk to true", self.fleet_sunk



# computer = Game_Pieces("Computer")
# print computer.sub.ship_name
# print computer.sub.size
# print computer.sub.boat
# print computer.sub.sunk

# print computer.destroyer.ship_name
# print computer.carrier.ship_name
# print computer.cruiser.ship_name
# print computer.battleship.ship_name


# print "fleet sunk: ", computer.fleet_sunk

# computer.carrier.sunk = True
# print "sunk carrier", computer.carrier.sunk
# computer.all_sunk()
# print "fleet sunk: ", computer.fleet_sunk

# computer.battleship.sunk = True
# print "sunk battleship", computer.battleship.sunk 
# computer.all_sunk()
# print "fleet sunk: ",computer.fleet_sunk

# computer.sub.sunk = True
# print "sunk sub", computer.sub.sunk
# computer.all_sunk()
# print "fleet sunk: ",computer.fleet_sunk

# computer.cruiser.sunk = True
# print "sunk cruiser", computer.cruiser.sunk
# computer.all_sunk()
# print "fleet sunk: ",computer.fleet_sunk

# computer.destroyer.sunk = True
# print "sunk destroyer", computer.destroyer.sunk
# computer.all_sunk()
# print "fleet sunk: ",computer.fleet_sunk

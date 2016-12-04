#class and stuff for dwarves...
from race import Race

#pg 16 in pdf
def class Dwarf(Race):
	def __init__(self):
		#mature same rate as humans
			#considered young until 50
			#live about 350
		#size 
			#4ft to 5ft
			#~150lbs
			#medium
		Character.setMins()
		Character.setMaxs()
		self.speed = 25

		#hill dwarves, mountain dwarves, other for customization?
		self.subrace = None
		
		#ability score mods
			# con +2

			#hill
				#wis +1
			#mountain
				#str +2

		#alignment
			# most are lawful
			# lean towads good

		#traits
			#Darkvision
			#Dwarven Resilience
			#Dwarven Combat Training
			#tool proficiency
				#artisan's tools of choice:
			#Stonecunning
			#Hill Dwarves traits
				#Dwarven Toughness 
			#Mountain Dwarves traits
				#Dwarven Armor Training
		#languages
			#speak,read,write
				#Common
				#Dwarvish

#race code
from character import Character

#dwarf
#elf
#halfling
#human
#dragonborn
#gnome
#half-elf
#half-orc
#tiefling

def class Race(Character):
	def __init__(self):
		#ability mods

		#age range, pg 114
		self.minAge = 0
		self.maxAge = 0

		#typical alignment
		self.alignment = " "

		#size, pg 144
		self.minSize = 0
		self.maxSize = 0

		#speed
		self.speed = 0

		#traits - humans get "Variant Human Traits" pg 26
		#proficiencies
		#languages
		#subraces - humans get "Ethnicity"

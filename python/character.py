#character code
import dictionaries as dictionary

def class Character():
	def __init__(self):
		#details w/ no impact on other variables
		self.age = 0		#random setting in specific race
		self.height = 0		#random setting in specific race
		self.weight = 0		#random setting in specific race
		self.eyes = " " 	#random setting in specific race
		self.skin = " "		#random setting in specific race
		self.hair = " "		#random setting in specific race
		self.name = " "		#random setting in specific race
		self.alignment = " "	#random setting in specific race
		#background, pg 118

		
		#details w/ lots of impact
		self.race = None
		self.cclass = None


		#lowest for beginning character
		self.level = 1
		self.xp = 0
		self.ProficiencyBonus = 2
		self.station = 0 #for current campaign

		#other stuff
		self.inspiration = 0
		self.passiveWisdom = 0
		
		#combat stats
		self.ArmorClass = 0
		self.initiative = 0
		self.speed = 0
		self.hp = 0


		#abilities...
		self.stats = dictionary.Abilities

		#skills...
		self.numSkills = 0
		self.skills = dictionary.AllSkills

		#feats...
		self.numFeats = 0
		self.feats = dictionary.Feats

		#cantrips
		self.numCantrips = 0


		#spells
		self.numSpell1 = 0
		self.numSpell2 = 0
		self.numSpell3 = 0
		self.numSpell4 = 0
		self.numSpell5 = 0
		self.numSpell6 = 0
		self.numSpell7 = 0
		self.numSpell8 = 0

		#pg 163 for various other stats


	def setName(self, newName):
		self.name = newName

	def setAlignment(self, new):
		self.alignment = new

	



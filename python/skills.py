#skills code
def class Skill():
	def __init__(self, atype):
		self.ability = atype
		self.abilityMod = self.ability.totalBonus
		self.proficiencyMod = 0
		self.magicMod = 0
		self.otherMod = 0
		self.totalMod = 0
		self.proficient = False
		self.expertise = False

	def setAbilityMod(self):
		self.abilityMod = self.ability.totalBonus

	def setProficient(self, p):
		self.proficient = p

	def setExpertise(self, p):
		self.expertise = p

	def setProficiencyMod(self, number):
		if self.proficient == True:
			self.proficiencyMod = number
			if self.expertise == True:
				self.proficiencyMod *= 2
		else:
			self.proficiencyMod = 0

	#add/sub to current because could have mult magic mods
	def addMagicMod(self, number):
		self.magicMod += number

	#add/sub to current because could have mult mods
	def addOtherMod(self, number):
		self.otherMod += number

	def setTotalMod(self):
		self.totalMod =	self.abilityMod + self.proficiencyMod + self.magicMod +	self.otherMod


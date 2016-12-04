#ability score code

def class Ability():
	#strength
	#dexterity
	#constitution
	#intelligence
	#wisdom
	#charisma

	def __init__(self):
		self.value = 0
		self.raceMod = 0
		self.classMod = 0
		self.magicMod = 0
		self.otherMod = 0
		self.total = 0
		self.totalBonus = 0

	def setValue(self, number):
		self.value = number
		self.setTotal()

	def setRaceMod(self, number):
		self.raceMod = number
		self.setTotal()

	def setClassMod(self, number):
		self.classMod = number
		self.setTotal()

	def setMagicMod(self, number):
		self.magicMod = number
		self.setTotal()

	def setOtherMod(self, number):
		self.otherMod = number
		self.setTotal()

	def setTotal(self):
		self.total = self.value + self.raceMod + self.classMod + self.magicMod +	self.otherMod
		self.setTotalBonus()

	def setTotalBonus(self):
		#think the equation is (total-10)/2 and round down
		if (self.total - 10) mod 2 == 0:
			self.totalBonus = (self.total - 10)/2
		else:
			self.totalBonus = (self.total - 11)/2



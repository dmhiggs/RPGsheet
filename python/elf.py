#elf character
from character import Character

#pg 19 in pdf
def class Elf(Character):
	def __init__(self):
		#age, adult at ~100, dies at ~750
		#size, under 5ft to over 6ft, slender, Medium
		Character.setMins()
		Character.setMaxs()
		Character.setSpeed(30)		#walking speed

		#high elves, wood elves, dark elves (drow)
		self.subrace = None

		#ability score mod
			#dex +2
			#high
				#intelligence +1
			#wood
				#wis +1
			#dark
				#cha +1

		#alignment
			#chaotic
			#good
			#evil if drow

		#traits
			#Darkvision
			#Keen Senses
			#Fey Ancestry
			#Trance

			#high elf traits
				#Elf Weapon Training
					#proficiency w/
						#longsword
						#shortsword
						#shortbow
						#longbow
				#Cantrip
				#Extra Language
			#Wood elf traits
				#Elf Weapon Training
					#proficiency w/
						#longsword
						#shortsword
						#shortbow
						#longbow
				#Fleet of Foot
				#Mask of the Wild
			#dark elf traits
				#Superior Darkvision
				#Sunligh Sensitivity
				#Drow Magic
				#Drow Weapon Training
					#proficiency w/
						#rapiers
						#shortswords
						#hand crossbows

		#languages
			#c,r,w Common, Elvish

		

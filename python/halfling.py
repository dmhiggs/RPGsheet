#halflings

from character import Character
def class Halfling(Character):
	def __init__(self):
		#age, adult ~20, lives to ~150
		#size, ~3ft, ~40lbs, Small
		Character.setMins()
		Character.setMaxs()
		Character.setSpeed(25)		#walking speed

		#Lightfoot, stout
		self.subrace = None

		#ablity score mods
			#dex +2
			#lightfoot
				#cha +1
			#stout
				#con +1

		#alignment
			#most lawful good

		#traits
			#Lucky
			#Brave
			#Halfling Nimbleness
			#lightfoot traits
				#Naturally Stealthy
			#stout traits
				#Stout Resilience

		#languages
			#c,r,w Common, Halfling

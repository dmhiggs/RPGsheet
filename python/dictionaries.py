#dictionaries for abilities, skills, feats

from skills import Skill
from ability import Ability
from feats import Feat


#alignments
Alignment = ['Lawful Good','Neutral Good','Chaotic Good','Lawful Neutral','Neutral','Chaotic Neutral','Lawful Evil','Chaotic Evil']


#languages
StandardLanguages = ['Common','Dwarvish','Elvish','Giant','Gnomish','Goblin','Halfling','Orc']
ExoticLanguages = ['Abyssal','Celestial','Draconic','Deep Speech','Infernal','Primordial','Sylvan','Undercommon']
SecretLanguages = ["Thieves' Cant","Tongue of Druids"]


#abilities
Abilities = {'Strength': Ability(), 'Dexterity': Ability(), 'Constitution': Ability(), 'Intelligence': Ability(), 'Wisdom': Ability(), 'Charisma': Ability()}


#skills
Strength = {'Athletics': Skill(Abilities['Strength'])}

Dexterity = {'Acrobatics': Skill("Dexterity"),'Sleight of Hand': Skill("Dexterity"),'Stealth': Skill("Dexterity")}

Constitution = {}

Intelligence = {'Arcana': Skill("Intelligence"),'History': Skill("Intelligence"),'Investigation': Skill("Intelligence"),'Nature': Skill("Intelligence"),'Religion': Skill("Intelligence")}

Wisdom = {'Animal Handling': Skill("Wisdom"),'Insight': Skill("Wisdom"),'Medicine': Skill("Wisdom"),'Perception': Skill("Wisdom"),'Survival': Skill("Wisdom")}

Charisma = {'Deception': Skill("Charisma"),'Intimidation': Skill("Charisma"),'Performance': Skill("Charisma"),'Persuasion': Skill("Charisma")}


AllSkills = {'Strength': Strength, 'Dexterity': Dexterity, 'Constitution': Constitution, 'Wisdom': Wisdom, 'Charisma': Charisma}


#feats, pg 154
Feats = {
	'Alert': Feat(),
	'Athlete': Feat(),
	'Actor': Feat(),
	'Charger': Feat(),
	'Crossbow Exper': Feat(),
	'Defensive Duelist': Feat(),
	'Dual Wielder': Feat(),
	'Dungeon Delver': Feat(),
	'Durable': Feat(),
	'Elemental Adept': Feat(),
	'Grappler': Feat(),
	'Great Weapon Master': Feat(),
	'Healer': Feat(),
	'Heavily Armored': Feat(),
	'Heavy Armor Master': Feat(),
	'Inspiring Leader': Feat(),
	'Keen Mind': Feat(),
	'Lightly Armored': Feat(),
	'Linguist': Feat(),
	'Lucky': Feat(),
	'Mage Slayer': Feat(),
	'Magic Initiate': Feat(),
	'Martial Adept': Feat(),
	'Medium Armor Master': Feat(),
	'Mobile': Feat(),
	'Moderately Armored': Feat(),
	'Mounted Combatant': Feat(),
	'Observant': Feat(),
	'Polearm Master': Feat(),
	'Resilient': Feat(),
	'Ritual Caster': Feat(),
	'Savage Attacker': Feat(),
	'Sentinel': Feat(),
	'Sharpshooter': Feat(),
	'Shield Master': Feat(),
	'Skilled': Feat(),
	'Skulker': Feat(),
	'Spell Sniper': Feat(),
	'Tavern Brawler': Feat(),
	'Tough': Feat(),
	'War Caster': Feat(),
	'Weapon Master': Feat(),
}


#traits, 16, 19, 29, 32, 34, 36, 38, 
Traits = {
	'Darkvision':
	'Dwarven Resilience':
	'Dwarven Combat Training':
	'Stonecunning':
	'Dwarven Toughness':
	'Dwarven Armor Training':
	'Keen Senses':
	'Fey Ancestry':
	'Trance':
	'Elf Weapon Training':
	'Cantrip':
	'Extra Language':
	'Fleet of Foot':
	'Mask of the Wild':
	'Superior Darkvision':
	'Sunlight Sensitivity':
	'Drow Magic':
	'Drow Weapon Training':
	'Lucky':
	'Brave':
	'Halfling Nimbleness':
	'Naturally Stealthy':
	'Stout Resilience':
	'Draconic Ancestry':
	'Breath Weapon':
	'Damage Resistance':
	'Gnome Cunning':
	'Natural Illusionist':
	'Speak with Small Beasts':
	'Artificers Lore':
	'Tinker':
	'Skill Versatility':
	'Menacing':
	'Relentless Endurance':
	'Savage Attacks':
	'Hellish Resistance':
	'Infernal Legacy':
}


#proficiencies
#pg 136 -- toggle for wood or metal?
Armor = {
'Light': #padded,leather,studded leather
'Medium': #hide, chain shirt, scale mail, breastplate, half plate
'Heavy': #ring mail, chain mail, splint, plate
'Shields': 
}

#simple/martial, pg 140
SimpleWeapons = {
'Club':
'Dagger':
'Greatclub':
'Handaxe':
'Javelin':
'Light Hammer':
'Mace': 
'Quarterstaff':
'Sickle':
'Spear':
'Unarmed Strike':
'Light Crossbow':
'Dart':
'Shortbow':
'Sling':
}

MartialWeapons = {
'Battleaxe':
'Flail':
'Glaive':
'Greataxe':
'Greatsword':
'Halberd':
'Lance':
'Longsword':
'Maul':
'Morningstar':
'Pike':
'Rapier':
'Scimitar':
'Shortsword':
'Trident':
'War Pick':
'Warhammer':
'Whip':
'Blowgun':
'Hand Crossbow':
'Heavy Crossbow':
'Longbow':
'Net':
}


Weapons = {
'Simple':
'Martial':
}

Tools = {
'Disquise Kit':
'Forgery Kit':
'Gaming Set': #different types - dice set, dragonchess set, playing card set, three-dragon ante set
"Thieves' Tools":
'Musical Instrument': #different types - bagpipes, drum, dulcimer, flute, lute, lyre, horn, pan flute, shawm, viol
"Artisan's Tools": #different types - alchemist's supplies, brewer's supplies, calligrapher's supplies, carpenter's tools, cartographer's tools, cobbler's tools, cook's untensils, glassblower's tools, jeweler's tools, leatherworker's tools, mason's tools, painter's supplies, potter's tools, smith's tools, tinker's tools, weaver's tools, woodcarver's tools
'Vehicles(land)':
'Herbalism Kit':
"Navigator's Tools":
'Vehicles(water)':
"Poisoner's Kit":
}

Proficiencies = {
	'Armor':
	'Weapons':
	'Tools':
	'Skills': 
}


#Equipment lists, pg 141
Items = {
'Abacus':
'Acid (vial)':
"Alchemist's Fire (flask)":
'Arrow': #sold in 20 pack
'Blowgun Needle': #sold in 50 pack
'Crossbow Bolt': #sold in 20 pack
'Sling Bullet': #sold in 20 pack
'Antitoxin (vial)':
'Crystal':
'Orb':
'Rod':
'Staff':
'Wand':
'Backpack':
'Ball Bearing': #bag of 1,000
'Barrel':
'Basket':
'Bedroll':
'Bell':
'Blanket':
'Block and Tackle':
'Book':
'Glass Bottle':
'Bucket':
'Caltrop': #bag of 20
'Candle':
'Crossbow Bolt Case':
'Map Case':
'Scroll Case':
'Chain (10 feet)':
'Chalk (1 piece)':
'Chest':
"Climber's Kit": #special pitons, boot tips, gloves, harness
'Common Clothes':
'Costume Clothes':
'Fine Clothes':
"Traverler's Clothes":
'Component Pouch':
'Crowbar'
'Sprig of Mistletoe':
'Totem':
'Wooden Staff':
'Yew Wand':
'Fishing Tackle': #wooden rod, silken line, corkwood bobbers, steel hooks, icad sinkers, velvet lures, narrow netting
'Flask':
'Tankard':
'Grappling Hook':
'Hammer':
'Sledge Hammer':
"Healer's Kit": #leather pouch containing bandages, salves, splints -- 10 uses
'Amulet':
'Emblem':
'Reliquary':
'Holy Water (flask)':
'Hourglass':
'Hunting Trap':
'Ink (1 ounce bottle)':
'Ink Pen':
'Jug':
'Pitcher':
'Ladder (10-foot)':
'Lamp':
'Bullseye Lantern':
'Hooded Lantern':
'Lock':
'Magnifying Glass':
'Manacles':
'Mess Kit': #cup, cutlery
'Steel Mirror':
'Oil (flask)':
'Paper (one sheet)':
'Parchment (one sheet)':
'Perfume (vial)':
"Miner's Pick":
'Piton':
'Basic Poison (vial)':
'Pole (10-foot)':
'Iron Pot':
'Potion of Healing':
'Pouch':
'Quiver':
'Portable Ram':
'Rations (1 day)':
'Robes':
'Hempen Rope (50 feet)':
'Silk Rope (50 feet)':
'Sack':
"Merchant's Scale":
'Sealing Wax':
'Shovel':
'Signal Whistle':
'Signet Ring':
'Soap':
'Spellbook':
'Spyglass':
'Iron Spike': #sold in 10s
'Two-Person Tent':
'Tinderbox': #flint, fire steel, tinder
'Torch':
'Vial':
'Waterskin':
'Whetstone':
}

EquipmentPacks = {
"Burglar's Pack": #backpack, bag of 1000 ball bearings, 10 feet string, bell, 5 candles, crowbar, hammer, 10 pitons, hooded lantern, 2 flasks of oil, 5 days rations, tinderbox, waterskin, 50 feet hempen rope
"Diplomat's Pack": #chest, 2 cases for maps and scrolls, fine clothes, bottle of ink, ink pen, lamp, 2 flasks of oil, 5 sheets of paper, vial of perfume, sealing wax, soap
"Dungeoneer's Pack": #backpack, crowbar, hammer, 10 pitons, 10 torches, tinderbox, 10 days of rations, waterskin, 50 feet hempen rope
"Entertainer's Pack": #backpack, bedroll, 2 costumes, 5 candles, 5 days of rations, waterskins, disguise kit
"Explorer's Pack": #backpack, bedroll, mess kit, tinderbox, 10 torches, 10 days of rations, waterskin, 50 feet hempen rope
"Priest's Pack": #backpack, blanket, 10 candles, tinderbox, alms box, 2 blocks of incense, censer, vestments, 2 days of rations, waterskin
"Scholar's Pack": #backpack, book of lore, bottle of ink, ink pen, 10 sheets of parchment, little bag of sand, small knife
}


#mounts and animals, pg 147


#lifestyles, pg 148
Lifestyles = {
'Wretched':
'Squalid':
'Poor':
'Modest':
'Comfortable':
'Wealthy':
'Aristocratic':
}


#food drink lodging, pg 148


#trinkets, pg 150


#spells, pg 188


#conditions, pg 267
Conditions = {
'None':
'Blinded':
'Charmed':
'Deafened':
'Frightened':
'Grappled':
'Incapacitated':
'Invisible':
'Paralyzed':
'Petrified':
'Poisoned':
'Prone':
'Restrained':
'Stunned':
'Unconscious':
'Exhaustion':
}


#gods, pg 270


#pg 20, personality traits, ideals, bonds, flaws for random selection

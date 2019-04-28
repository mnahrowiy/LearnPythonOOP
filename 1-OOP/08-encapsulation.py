class Hero:

	def __init__(self, name, health, attackPower):
		self.__name = name
		self.__health = health
		self.__power = attackPower

	earthshaker = Hero ("earthshaker",50,5)

	print(earthshaker.__dict__)

	# game berjalan

	earthshaker.__name = "windruner"
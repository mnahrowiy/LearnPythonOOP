class Hero:

	def __init__(self, name, health, armor):
		self.name   = name
		self.__health = health
		self.__armor  = armor

	# def getHealth(self):
	# 	return self.__health


	# untuk membuat method info menjadi variabel.
	# menggunakan decorator
	@property 
	def info(self):
		return "name {} : \n\thealth: {}".format(self.name, self.__health)

	@property
	def armor(self):
		pass
	

	# getter
	@armor.getter # hanya untuk mengambil data
	def armor(self):
		return self.__armor

	# setter 
	@armor.setter
	def armor(self, input):
		self.__armor = input

sniper = Hero ("sniper",100,10)

# untuk mengambil file yang di encapsulasi
# print(sniper.getHealth())

# print(sniper.health)  ini error
# print(sniper.__health) in juga error

# @property
print('merubah info')
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info) 


print('getter dan setter untuk __armor:')
print(sniper.armor)
print(sniper.__dict__) # ketika di keluarkan , method info bukan bagia dari sniper, namun bisa dipakai sebagai methodnya
sniper.armor = 50 # tidak usah pakai sniper.armor(50) // INI SUDAH DI GANTI DENGAN SETTER
print(sniper.armor)
print(sniper.__dict__)
class Hero:

	def __init__(self,inputNama,inputDarah):
		self.nama   = inputNama
		self.darah = inputDarah

# class Hero_kuat(Hero): #
# 	pass



sniper = Hero("sniper",2)
budi   = Hero("budi",3)

print(budi.__dict__)
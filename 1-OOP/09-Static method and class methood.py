class Hero:

	# private class variable
	__jumlah = 0;

	def __init__(self, name):
		self.__name = name
		Hero.__jumlah += 1

	# method ini hanya berlaku untuk objek, karena pakai self
	def getJumlah(self):
		return Hero.__jumlah
	
	# method ini tidak berlaku untuk objek tapi berlaku untuk kelas	
	def getJumlah1():
		return Hero.__jumlah

	# method statics (decorator) nempel ke objek dan kelasnya
	@staticmethod # gak bisa mengambil argument
	def getJumlah2():
		return Hero.__jumlah

	@classmethod # nempel di kelas dan bisa pakai argument contoh cls (nama cls mah bebas)
	def getJumlah3(cls): # cls bebas aja namanya
		return cls.__jumlah



sniper = Hero("sniper")
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())
nahrowi = Hero("Nahrowi")
print(Hero.getJumlah2())
print(Hero.nahrowi())

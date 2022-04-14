#Написано для проекта друга

class Vizhener:

	def __init__(self, text, key, language):
		if language == "Rus":
			carriage = 33
			self.down, self.up = 1072, 1104
			self.alphabet = [chr(i) for i in range(self.down, self.up)]
			self.key = self.minusnotletters(self.minusyo(key.lower()))
			self.text = self.minusnotletters(self.minusyo(text.lower()))
		elif language == "Eng":
			carriage = 27
			self.down, self.up = 97, 123
			self.alphabet = [chr(i) for i in range(self.down, self.up)]
			self.key = self.minusnotletters(key.lower())
			self.text = self.minusnotletters(text.lower())
		else:
			return "Неверный язык!"
		table = []
		for i in range(carriage-1): #Составляем таблицу Виженера
			temp = []
			for j in range(self.up+1-carriage, self.up):
				temp.append(chr(j))
			for j in range(self.down, self.up+1-carriage):
				temp.append(chr(j))
			table.append(temp)
			carriage -= 1
		self.table = table
		oldkey = self.key
		while len(self.key) != len(self.text): #Циклически записываем ключевое слово, пока его длина не будет равна длине шифруемого текста
			if len(self.key) + len(oldkey) > len(self.text):
				temp = list(oldkey)
				for i in range(len(self.text) - len(self.key)):
					self.key += temp[i]
			else:
				self.key += oldkey

	def minusnotletters(self, words): #Убирает все не буквенные символы
		words = list(words)
		i = 0
		while i != len(words):
			if words[i] not in self.alphabet:
				del words[i]
			else:
				i += 1
		words = "".join(words)
		return words
	
	def minusyo(self, words): #Заменяет все "ё" на "е"
		words = list(words)
		for i in range(len(words)):
			if words[i] == "ё":
				words[i] = "е"
		words = "".join(words)
		return words

	def encrypt(self):
		text = self.text
		self.text = ""
		for i in range(len(list(text))): #Собственно шифруем текст
			self.text += self.table[ord(text[i])-self.down][ord(self.key[i])-self.down]
		return self.text
		
	def decrypt(self):
		text = self.text
		self.text = ""
		for i in range(len(list(text))): #А тут расшифровываем
			for j in range(len(list(self.table[0]))):
				if self.table[0][j] == self.key[i]:
					for k in range(len(self.table[j])):
						if self.table[j][k] == text[i]:
							ind = k
							break 
					break
			self.text += self.table[ind][0]
		return self.text 

a = Vizhener("Съешь ещё этих мягких французских булок, да выпей чаю.", "Абракадабра", "Rus")
print(a.encrypt())
print(a.decrypt())

a = Vizhener("The five boxing wizards jump quickly.", "Aligator", "Eng")
print(a.encrypt())
print(a.decrypt())

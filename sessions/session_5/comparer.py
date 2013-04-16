import hashlib

class Comparer():

	def __init__(self, thing1, thing2):
		self.thing1 = thing1
		self.thing2 = thing2

	def compareTwoHashCodes(self): 
		hash1 = HashGenerator(self.thing1).doHash()
		hash2 = HashGenerator(self.thing2).doHash()
		return hash1 == hash2

class HashGenerator():

	def __init__(self, thing):
		self.thing = thing

	def doHash(self):
		return hashlib.md5(self.thing).hexdigest()

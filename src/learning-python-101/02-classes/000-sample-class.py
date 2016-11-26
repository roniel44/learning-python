class Car():
	def __init__(self, type, color):
		self.type = type;
		self.color = color;
		
	def describe(self):
		print("I have a %s, color is %s" %(self.type, self.color));
		

car1 = Car("Hyundai", "Green");
car1.describe();
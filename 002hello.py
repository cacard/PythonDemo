# _*_ coding:utf-8 _*_

class App:

	# instance method
	def sayHello(self):
		print("hello python, in a method of a class.")

	# static method
	@staticmethod
	def sayHello1():
		print("hello, in static method.")

	# class method
	@classmethod
	def sayHello2(cls):
		print("hello, in class method.")


# invoke instance method
app = App();
app.sayHello()

# invoke static method
App.sayHello1()

# invoke class method
App.sayHello2()


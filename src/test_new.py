class MyClass:
    def __init__(self,name):
            self.name = name
            print("never called in this case")
    def __new__(cls):
            return name

obj = MyClass()
print(obj)
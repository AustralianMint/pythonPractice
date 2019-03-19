class person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print("Hello", self.name)

p = person("Thomas")
print(p.name)
print("Hello", p.name)

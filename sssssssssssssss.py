class ClassA:
    def method(self):
        return "Method class A"

class ClassB:
    def method(self):
        return "Method class B"

class ClassC:
    def method(self):
        return "Method class C"

obj = ClassC()
print(obj.method())
print(ClassC.mro())
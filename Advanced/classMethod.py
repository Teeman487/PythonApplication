class MyClass:
    class_variable=10
    def class_method(self,x):
        self.class_variable=x
        return x

obj=MyClass()
print(obj.class_method(4))
print(obj.class_variable)



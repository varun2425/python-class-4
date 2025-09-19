def verify(func):
    def inner(name):
        if name=="Modi":
            print("Modi is Prime Minister")
        else:
            return func(name)
    return inner

@verify
def greet(name):
    print("Hi -", name,"  GM")
greet("Varun")
greet("Annu")
greet("Renuka")
greet("Modi")
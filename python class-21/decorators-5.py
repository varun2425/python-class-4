def smart_div(func):
    def inner(a,b):
        if b==0:
            print("can't Divivde by Zero")
        else:
            return func(a,b)
        return inner
        
@smart_div 
def division (a,b):
    print(a,b)
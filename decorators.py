import time

# def mydecorator(function):
#     def Wrapper():
#          function()
#          print("This is a decoration")
       
    
#     return Wrapper


# @mydecorator
# def greeting():
#     print("Hi I am Mike")

# greeting()

#### Timing Function using decorator

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = function(*args, **kwargs)
        end = time.time()
        fname = function.__name__
        print(f"{fname} function took {end - start} seconds to execute")
        return value
    return wrapper



@timer
def random(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


random(100000)
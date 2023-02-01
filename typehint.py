def myfunction(param: list[int]) -> str:  #Here, type of parameter and return value is specified
    for i in param:
        print(f'{i} is in {param}')


myfunction([1, 2, 3, 4, 5])
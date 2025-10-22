n : int = 5

name: str = "Khushil"

def sum(a: int, b: int) -> int: #Why? This helps any programmer using your code
    #to know what type of variable a certain thing is
    return a + b 

print(sum(2, 3))
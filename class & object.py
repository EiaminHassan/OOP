# class creation
class Fruit:
    color = "red"

# object creation
apple = Fruit()
print(apple.color)  # Output: red

cherry = Fruit()
print(cherry.color)  # Output: red

# delete an object
del cherry
# print(cherry.color)  # This will raise an error since cherry has been deleted



# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Vehicle:
    pass  # This is a placeholder for future code

# creating an object of Vehicle class
car = Vehicle()
print(car)  # Output: <__main__.Vehicle object at 0x...>
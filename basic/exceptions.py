# try:
#     result = 2 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     result = 1
# print(result)

# try:
#     raise Exception("An error")
# except Exception as error:
#     print(error)


class DogNotFoundExceptiion(Exception):
    print("Inside")
    pass
try:
    raise DogNotFoundExceptiion()
except DogNotFoundExceptiion:
    print("Dog not found")
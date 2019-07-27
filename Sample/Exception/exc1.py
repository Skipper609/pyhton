# try:
#     num1 = int(input("Enter the number:"))
#     num = 100 / 0
# except ZeroDivisionError as z:
#     print(z)
# finally:
#     print("Finally block")

class UnderageException(Exception):

    def __init__(self):
        self.message = "Underage voting is not possible"

    def __str__(self):
        return self.message

def cast_vote(age):
    if age < 18:
        raise UnderageException
    else:
        print("Thank you for casting the vote")


try:
    age = int(input("Enter the age: "))
    cast_vote(age)
except UnderageException as u:
    print(u)
else:
    print("Thank you for voting")
finally:
    print("You can leave now")
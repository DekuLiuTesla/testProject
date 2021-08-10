i = 100
print("Type of " + str(i) + " is: " + str(type(i)))
new_string = "Try Python"
another_string = 'Come here'
print(new_string + " World!...")
print()
# Use List
print("Let's try the list: names.")
print("Now we don't use ;")
names = ["Saber", "Archer", 3]  # different data types are allowed in one list
print("names[0]: " + names[0])
print("names[1]: " + names[1])
print("names[2]: " + str(names[2]))
# print("names[3]: "+str(names[3])); Wrong! Out of range!
# If we pass negative value Python will start from the end.
print("names[-1]: " + str(names[-1]))
print("names[-2]: " + str(names[-2]))
print("names[-3]: " + str(names[-3]))
# print("names[-4]: "+str(names[-4])); Wrong! Out of range!
# print("names[3]: "+str(names[3])); #Wrong! Out of range!
L = len(names)
print("Length of names: ")
print(L)
print("Then we append Lancer.")
names.append('Lancer')
print(names)
print("Then we insert Rider.")
# Insert will insert the particular value to the appropriate position.
names.insert(2, 'Rider')
print(names)
print("Then we delete Rider.")
del names[2]
print(names)
# Pop will help you to remove the last element of an array
popped_element = names.pop()
print("The popped element: " + popped_element)
print(names)
print("Then we remove Archer.")
# Remove elements by value
names.remove('Archer')
print(names)

# Array, which uses []
alpha = ["z", "c", "a"]
print("List alpha is: ")
print(alpha)
# Sorting
print("After sorting: ")
print(sorted(alpha))
alpha.sort()
print(alpha)
# Reverse sorting
alpha.sort(reverse=True)
print("After reverse sorting: ")
print(alpha)
print("")

# Reversing an array
print("Let's create an array of numbers: ")
numbers = [156, 715, 23, 55]
print(numbers)
print("After reverse: ")
numbers.reverse()
print(numbers)
print("")

# Slicing elements
alpha = ['a', 'b', 'c', 'd', 'e']
print("Let's create an array of letters: ")
print(alpha)  # Or print(alpha[:])
print("Then alpha[0:3] are: ")
# The first element is the starting index. And Python stops in the item before the second index.
print(alpha[0:3])
print("Then alpha[:4] are: ")
print(alpha[:4])
print("Then alpha[2:] are: ")
print(alpha[2:])
print("Then we copy alpha to another_alpha")
another_alpha = alpha  # This is not copying the array. Any changes in alpha will affect another_alpha too.
print("And we append f to alpha")
alpha.append('f')
print("Now another_alpha is: ")
print(another_alpha)
print('')

# Tuple, which is immutable, use ()
print("Let's create Tuple 'nums': ")
nums = (5, 6, 7)
print(nums)
print("nums[2]: " + str(nums[2]))
print("Length: " + str(len(nums)))
# empty tuple. Length is zero.
empty_tuple = ()
# use trailing comma when defining a tuple with one element
print("Let's define a Tuple with only one element: ")
num = (1,)  # num = (1) is wrong
print("num: " + str(num))
print("Length: " + str(len(num)))
print(type(num))
# append new element
char = ('x',)
print("After concatenating a new tuple: ")
nums = nums + char
print(nums)
print('')

# Set, which is orderless and not callable, use {}
alphaSet = {'x', 'y', 'z', 'x'}
print("Let's create a set: ")
print(alphaSet)  # As you can see, duplicates are removed in sets. And also the output is not ordered.
# Accessing items in set
# You can't access by index because Sets are unordered.
# You can access it only by loop.
print("Let's access them by loop:")
for ele in alphaSet:
    print(ele)

print("Add one element by using add function: ")
# add one elements
alphaSet.add('s')
print(alphaSet)
print("Add multiple elements by using update function: ")
# add multiple elements
alphaSet.update(['a', 's', 'c'])
print(alphaSet)

print("Now length of alphaSet: ")
print(len(alphaSet))

print("Let's remove 'c': ")
# Remove the element from the set
alphaSet.remove('c')
print(alphaSet)
# It's safer to use discard than remove. Discard will never throw an error
# even if the element is not present in the set but remove will do.
alphaSet.discard('c')
print('')

# Dictionary, which is orderless as well
print("Let's create a dict: ")
user = {'id': 686, 'name': 'Jimmy Tesla', 'email': 'jimmy@gmail.com'}
print("ID is: " + str(user['id']))
print("Name is: " + user['name'])
print("Email is: " + user['email'])

print("Length of dict: ")
print(len(user))

# Add new key-value pair
print("Let's add sth new: ")
user['age'] = 35
print(user)

# To get all the keys
print("The keys are: ")
print(user.keys())
# To get all the values
print("The values are: ")
print(user.values())

# To delete a value
del user['age']
print("After deleting the 'age': ")
print(user)

# Example of nested dict.
user = {
    'id': 1,
    'name': 'John wick',
    'cars': ['audi', 'bmw', 'tesla'],
    'projects': [
        {
            'id': 10,
            'name': 'Project 1'
        },
        {
            'id': 11,
            'name': 'Project 2'
        }
    ]
}
print('')

print("Use if...else")
a = 5
b = 3
# This is the short-hand notation of if statement.
if a == 5: print("a equals to 5")
# Short-hand for if-else statement.
print("b equals to 5") if b == 5 else print("b equals to 3")
print('')

print("Use while")
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("End when i = " + str(i))
print("Now i = " + str(i))
print('')

print("Use for to print alpha")
# for ele in alpha:
#     print(ele)
for i in range(0, len(alpha)):  # inverse order
    print(alpha[len(alpha) - i - 1])
# for index, value in enumerate(alpha):
#     print(str(value) + " is presented in " + str(index))
word = "python"
print("Use for to print a word")
for char in word:
    print(char)
print("Use for to print a dictionary")
for key, value in user.items():
    print(str(key) + " is " + str(value))
print('')


def printsome(sth="Hello World"):
    return str(sth) + " from Python!"


def language(fav_lang, *names):
    print("My favorite language is: " + str(fav_lang))
    print("I will also learn: ")
    for var in names:
        print(str(var))
    return


def user_info(id, name, *names, **info):
    print("ID: " + str(id))
    print("Name: " + name)
    print(names)
    print(info)


print("Use function")
print(printsome())
print(printsome(201314))
language("Python", 'Ruby', 'JavaScript', 'C++')
user_info(1, 'Srebalaji', 'C', 'M', fav_language=['Python', 'Ruby'], twitter_handle='@srebalaji')
print('')

print("Use class")


class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " eats")

    def sleep(self):
        print(self.name + " sleeps")


# Inheritance
class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Dog eats")


class Person():
    def __init__(my_instance, name):
        # 'name' attribute is protected.
        my_instance._name = name

    def reads(my_instance):
        print(my_instance._name + " reads")

    def writes(my_instance):
        print(my_instance._name + " writes")


class newPerson():
    def __init__(self, name):
        # 'name' attribute is private.
        self.__name = name

    def reads(self):
        print(self.__name + " reads")

    def writes(self):
        print(self.__name + " reads")

    # This is a private method. This can't be accessed outside the class.
    def __some_helper_method(self):
        print('Some helper method.')


dog = Animal('harry')
print("The name of dog is: " + dog.name)
dog.sleep()

dog.name = 'Rosie'
print("Now the name of dog is: " + dog.name)

dog0 = Dog("Brown")
dog0.eat()
dog0.sleep()

person = Person("Jimmy")
person.writes()
person._name = "I can still change the name"
print(person._name)  # You can still access and change the protected members

person0 = newPerson("Ram")
person0.reads()
# print(person0.__name)  # Will throw an error. 'newPerson' object has no attribute '__name'
print(person0._newPerson__name)
person0._newPerson__name = 'Henry'  # You can even change the value
print(person0._newPerson__name)
print('')

x = ''
y = {}
z = []
w = ()

print(x is None)
print((y is None))
print(z is None)
print(w is None)

if not y:
    print("y is empty")
else:
    print("y is not empty")
print('')

print('Lets deal some exception ')
# ss = 10
# if ss > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

try:  # 执行代码
    1 / 0
except Exception as e:  # 发生异常时执行的代码
    print(e.__class__)
    print(e)
else:
    print('No error raised. You can resume your operation here')
finally:
    print('This code will run whether the code has error or not.')

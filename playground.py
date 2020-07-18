a = 1
print(a)

b = 'hello'
print(b)

if a == 1 and (a == 1 or a == 1):
    print('hi')
    print('test')
elif a == 2:
    print('a is 2')
else:
    print('else!')

if a is not None:
    print('a is not None')

if a:
    print('a')

if a is None:
    print('a is None')

def say():
    print('hi')

say()

# prefer this
def say1(number):
    print(f'hi {number}')

# not recommended
def say2(number: int):
    print('hi ' + str(number))

print(__name__)
class Sample:

    id = 10
    _name = "Hello"
    __email = "hello@gmail.com"
    def __init__(self):
        pass


s = Sample()

print(dir(s))

print(s.id)
print(s._name)
print(s._Sample__email)
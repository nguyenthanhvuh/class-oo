class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance    

s1 = Singleton(); s2 = Singleton()
assert(s1 is s2) # both refer to the same object 



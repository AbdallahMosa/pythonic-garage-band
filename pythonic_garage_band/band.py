from abc import ABC , abstractclassmethod


class Band():
    instances =[]
   
    def __init__(self,name,members=[] ) :
        self.name =name
        self.members=members
        self.__class__.instances.append(self)
    def play_solos(self):
        all=[]
        for bands in self.members:

             all.append(bands.play_solo())
        return all
            # if bands.play_solo()=="face melting guitar solo":
            #     return "face melting guitar solo"
            # if bands.play_solo()=="bom bom buh bom":
            #     return "bom bom buh bom"
            # if bands.play_solo()=="rattle boom crash":
            #     return "rattle boom crash"
    @classmethod
    def to_list(cls):
        return cls.instances
    def __str__(self) :
        return self.name
    def __repr__(self):
        return self.name
        


class Musician(ABC):
    '''
    Base Class
    '''
  
    def __init__(self, name):
        self.name = name

    def __str__(self) :
        pass

    def __repr__(self) :
        pass
    @abstractclassmethod
    def get_instrument(self):
        pass
    @abstractclassmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    '''
    Child Class
    '''
    def __init__(self, name):
        self.name = name
        super().__init__(name)
    def __str__(self) :
        return f"My name is {self.name} and I play guitar"
    def __repr__(self) :
        return f"Guitarist instance. Name = {self.name}"
    def play_solo(self):
        return "face melting guitar solo"
    def get_instrument(self):
        return "guitar"
class Drummer(Musician):

    '''
    Child Class
    '''
    def __init__(self, name):
        super().__init__(name)


    def __str__(self) :
        return f"My name is {self.name} and I play drums"
    def __repr__(self) :
        return f"Drummer instance. Name = {self.name}"
    def play_solo(self):
        return "rattle boom crash"
    def get_instrument(self):
        return "drums"

class Bassist(Musician):
    '''
    Child Class
    '''
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def play_solo(self):
        return "bom bom buh bom"
    def get_instrument(self):
        return "bass"



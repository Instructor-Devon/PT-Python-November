"""
Week 5 Day 1 - Object-Oriented Programming
"""

# class: globally define what a Person is/does
#   self => an instance of the class
#   self is like "this"
class Person():

    # Constructor Method
    # Attributes (data on the class)
        # first_name
        # last_name
        # email

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.num_jumps = 0
        
    def jump(self):
        print(f"I've jumped {self.num_jumps} times, time for another")
        print(f"My name is {self.first_name} and I am JUMPING!")
        self.num_jumps += 1

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # make printing easier...
    def __str__(self):
        return self.full_name
    
    # Methods (actions this class can perform)
        # greet
        # jump
        # eat
        # be birthed! AKA constructor

# objects: instances of the class

# inherritence: child classes
class Coder(Person):

    def __init__(self, first_name, last_name, email, hacker_name, skill_level):
        # required fields for parent class constructor
        super().__init__(first_name, last_name, email)
        # cool hacker name
        # programming skills (bt 1-100)
        self.hacker_name = hacker_name,
        self.skill_level = skill_level

    def code(self):
        if self.skill_level > 50:
            print("writing some LEET HAX04 codes....")
        else:
            print("just tring to get this feature done #UBER_N00B")

        # the act of coding can improve your skill
        self.skill_level += 1


class Party:

    def __init__(self, host, capacity):
        # host => Person
        # guests => [Person, Person...]
        # max_capacity => number
        self.host = host
        self.guests = []
        self.max_capacity = capacity

    def add_guest(self, guest):
        # check if we can even add a guest
        if self.max_capacity < len(self.guests) + 1:
            print(f"PARTY IS FULL (sorry {guest.first_name})")

        else:
            print(f"{guest.first_name} enters the party!")
            self.guests.append(guest)

josh = Coder("Josh", "Hernandez", "cooldude@sup.com", "h4x0r", 99)
devon = Person("Devon", "Newsom", "sup@sup.com")
claire = Coder("Claire", "Elliot", "whoisthis@sup.com", "MAXIMUM_OVERRIDE", 50)

the_party = Party(josh, 1)
the_party.add_guest(devon)
the_party.add_guest(claire)
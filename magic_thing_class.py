"""
jane = Thing('Jane')
jane.name # => 'Jane'

# can define boolean methods on an instance
jane.is_a.person
jane.is_a.woman
jane.is_not_a.man

jane.is_a_person # => True
jane.is_a_man # => False

# can define properties on a per instance level
jane.is_the.parent_of.joe
jane.parent_of # => 'joe'

# can define number of child things
# when more than 1, a tuple subclass is created
jane.has(2).legs
len(jane.legs) # => 2
isinstance(jane.legs[0], Thing) # => True

# can define single items
jane.has(1).head
isinstance(jane.head, Thing) # => True

# can define number of things in a chainable and natural format
>> Note: Python, unlike Ruby and Javascript, doesn't have a pretty syntax for blocks of expressions and a forEach method for iterables. So you should implement this behaviour yourself.
jane.has(2).arms.each.having(1).hand.having(5).fingers
len(jane.arms[0].hand.fingers) # => 5

# can define properties on nested items
jane.has(1).head.having(2).eyes.each.being_the.color.blue.having(1).pupil.being_the.color.black

# can define methods: thing.can.verb(method, past='')
method = lambda phrase: "%s says: %s" % (name, phrase)
# or
def method(phrase):
  return "%s says: %s" % (name, phrase)
jane.can.speak(method, "spoke")

jane.speak("hello") # => "Jane says: hello"

# if past tense was provided then method calls are tracked
jane.spoke # => ["Jane says: hello"]

"""


class Thing:
    def __init__(self, name) -> None:
        self.name = name
        self.set_attr_val = True

    def __getattr__(self, name: str):
        """Returns the attribute matching passed name."""
        if name.startswith('is_a_'):
            return bool(self.__dict__.get(name.replace('is_a_', '')))
        if name.startswith('is_not_a_'):
            return bool(self.__dict__.get(name.replace('is_not_a_', '')))

        value = self.__dict__.get(name)
        if not value:
            self.__dict__[name] = self.set_attr_val
        # Return attribute value.
        return value

    @property
    def is_a(self):
        self.set_attr_val = True
        # print(self.set_attr_val)
        return self

    @property
    def is_not_a(self):
        self.set_attr_val = False
        # print(self.set_attr_val)
        return self


jane = Thing('Jane')
print(jane.name)  # => 'Jane'
jane.is_a.person
jane.is_a.woman
jane.is_not_a.man

print(jane.is_a_person)  # => True
print(jane.is_a_man)  # => False

print(jane.__dict__)

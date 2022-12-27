class FancyTuple:

    def __init__(self, first=None, second=None, third=None, fourth=None, fifth=None):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth

    def __len__(self):
        length = 0
        if self.__first is not None: length += 1
        if self.__second is not None: length += 1
        if self.__third is not None: length += 1
        if self.__fourth is not None: length += 1
        if self.__fifth is not None: length += 1
        return length

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, first):
        self.__first = first

    @first.getter
    def first(self):
        if self.__first is None:
            raise AttributeError()
        return self.__first


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        self.__second = second

    @second.getter
    def second(self):
        if self.__second is None:
            raise AttributeError()
        return self.__second


    @property
    def third(self):
        return self.__third

    @third.setter
    def third(self, third):
        self.__third = third

    @third.getter
    def third(self):
        if self.__third is None:
            raise AttributeError()
        return self.__third


    @property
    def fourth(self):
        return self.__fourth

    @fourth.setter
    def fourth(self, fourth):
        self.__fourth = fourth

    @fourth.getter
    def fourth(self):
        if self.__fourth is None:
            raise AttributeError()
        return self.__fourth


    @property
    def fifth(self):
        return self.__fifth

    @fifth.setter
    def fifth(self, fifth):
        self.__fifth = fifth

    @fifth.getter
    def fifth(self):
        if self.__fifth is None:
            raise AttributeError()
        return self.__fifth


print(FancyTuple("dog", "cat").first)
# print(FancyTuple().first)
print(len(FancyTuple("dog", "cat")))

class FirstTest:
    def __init__(self, arg1, arg2):
        '''Try to define vars'''
        self.arg1 = arg1
        self.arg2 = arg2

    def test(self):
        message = (self.arg1 + " - this is arg1!")
        message2 = (self.arg2 + " - this is arg2")
        if self.arg2 != '':
            print("FirstTest class in runnging: " + message + " and " + message2)
        else:
            print("FirstTest class in runnging: " + message)

class SecondTest(FirstTest):
    def __init__(self, arg1, arg2, arg3):
        '''See on new arg3 parametr, I, add him in this new class, what was extended from parent FirstClass'''
        super().__init__(arg1, arg2)
        self.arg3 = arg3
    def test2(self):
        message3 = self.arg3

        print("New SecondTest class calling arg1: " + self.arg1 + ", arg2: " + self.arg2 + " from FirstClass from method test and arg3: "
              + message3 + "from SecondTest class , test2() method")
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
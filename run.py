import main

# Two = main.FirstTest("OnlyOneTestArgument")

First = main.FirstTest("TestArgument1", "TestArgument2")
Second = main.SecondTest("TestArgument1", "TestArgument2", "TestArgument3")

First.test()
Second.test2()
# Two.test()
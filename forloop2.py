"""
You are given a string s, you need to print its characters at even indices(index starts at 0).

Note: Please go through the range function to understand how to jump 2 steps.
"""
def stringJumper(s):
    for i in range(0,len(s),2):
        # from 0 to length of str and skip 2
        print(s[i], end="")
        #printing character and separating characters by nothing

#Given a number N. The task is to create an alphabetical string in lower case from that number and tell whether the string is palindrome or not. a = 0, b = 1….. and so on.

#For eg: If the number is 61 the substring “gb” will be printed till 7 (6+1) characters i.e. “gbgbgbg” and check if palindrome or not.

#Note: No number will start with zero. Consider alphabets ‘ a to j ‘ only i.e. single digit numbers from 0 to 9.

class Palindrome:
    def isPalindrome(self, str):
        for i in range (0, int(len(str)/2)):
            if str[i] != str[len(str) - i - 1]:
                return False
            else:
                return True

    def createString(self, N):
        s = str(N)
        sum = 0
        string = ''
        substr = ''
        letters = 'abcdefghij'

        for i in range(0, len(s)):
            digit = int(s[i])
            substr += letters[digit]
            sum += digit

        while(len(string) <= sum):
            string += substr

        return string[0:sum]

p = Palindrome()
mystr = p.createString(1998)
print(p.isPalindrome(mystr))

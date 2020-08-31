
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

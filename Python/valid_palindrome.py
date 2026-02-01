'''A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.'''

class valid_palindrome:
    def validation_palindrome(self,s:str)->bool:
        s=s.lower() #convert the string to lowercase
        str=""
        for i in s:
            if i.isalnum(): #remove the alphanumeric characters
                str+=i
        rev_str=str[::-1]
        if rev_str == str:
            return True
        else:
            return False

# s = "A man, a plan, a canal: Panama"
s = input("Enter a string:")
obj = valid_palindrome()
result = obj.validation_palindrome(s)
print(result)



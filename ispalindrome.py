def ispalindrome(string):
  if string[::-1] == string[:]:
    print(string + " is a palindrome")
  else:
    print(string + " is not a palindrome")

ispalindrome("navan")
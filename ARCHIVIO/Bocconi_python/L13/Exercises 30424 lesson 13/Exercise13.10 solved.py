def palindrome(wrd):

    rvs = wrd[::-1]  # string in reverse order

    if wrd == rvs:
        print('The word', '"' + wrd + '"', 'is a palindrome')
    else:
        print('The word', '"' + wrd + '"',
              'is not a palindrome, in fact it becomes',
              '"' + rvs + '"', 'if read in reverse order')

# Main program
palindrome("kajak")
palindrome("canoe")

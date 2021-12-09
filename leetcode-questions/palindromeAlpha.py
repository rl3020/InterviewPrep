
max_length = 0 
def palindrome(options): 
    

    def isPalindrome(string): 
        for i in range(len(string)): 
            if string[i] != string[len(string) - i - 1]: 
                print(string , "is not pal")
                return False
        else: 
            print(string , "IS pal")
            return True


    cache = { }
    # ["ck","kc","ho","kc"]
    def recurse(choices, curr_string, max_length): 
        if curr_string in cache: 
            return cache[curr_string]


        for letters in choices: 
            new_choices = [ c for c in choices if c != letters ]
            recurse(new_choices, curr_string + letters, max_length)


        if isPalindrome(curr_string): 
            if len(curr_string) > max_length:
                max_length = len(curr_string)
                cache[curr_string] =  max_length
                return max_length
        else: 
            cache[curr_string] = -1 
            return cache[curr_string]


    max_length = recurse(options, "", 0)
    return max_length

print( palindrome( [ "ck","kc","ho","kc" ] ) )




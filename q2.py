def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while True:
        new_s = ""
        i = 0
        while i < len(s):            
            if i + 1 < len(s) and s[i] == s[i+1]:
                i += 2
            else:
                new_s += s[i]
                i += 1               
        if new_s == s:
            return s        
        s = new_s
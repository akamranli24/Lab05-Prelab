def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    a=""
    for i in range(len(s)):
        for j in range(i, len(s)):
            empty_s = s[i:j+1]
            if empty_s == empty_s[::-1]:
                if len(empty_s)>len(a):
                    a=empty_s
    if len(a) > 1:
        return a
    else:
        return ''

                
            
def is_anagram(str1, str2):
    
    str1 = ''.join(sorted(str1.replace(' ', '').lower()))
    str2 = ''.join(sorted(str2.replace(' ', '').lower()))
    

    return str1 == str2
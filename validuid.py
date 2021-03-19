def validUID(num, uidlst):
    cap_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    sm_alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    digits = [0,1,2,3,4,5,6,7,8,9]
    word = []
    for case in uidlst:
        word = []
        # print(word)
        # print(case)
        if len(case) == 10:
            result = 'Valid'
            for letter in case:
                if (letter in cap_alphabet or sm_alphabet or digits):
                    if letter in word:
                        # return 'Invalid'
                        result = 'Invalid'
                        break
                    else:
                        word.append(letter)
                        # print(word)
                        continue
                else:
                    # return 'Invalid'
                      result = 'Invalid'  
                      break
            print(result)
        else:
            result = 'Invalid'
            print(result)


validUID(2,['B1CD102354', 'B1CDEF2354'])
validUID(2,['BQWAILU471', '115DEF2354'])
validUID(2,['5AW4F5SKRK', 'W45A55K455'])


# 2
# BQWAILU471
# 115DEF2354
# Expected Output
# Valid
# Invalid


# 5AW4F5SKRK
# W45A55K455
# Expected Output

# Download
# Invalid
# Invalid

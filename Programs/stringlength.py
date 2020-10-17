def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count

str1 = str(input("Enter any String: "))
print(string_length(str1))    

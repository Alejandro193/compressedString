# I found two ways to solve the exercise, using while and using for

# Using While
def compressedString(msg):
    compressed_msg = ""
    i = 0
    len_msg = len(msg)
    while i < len_msg:
        count = 1
        while i < len_msg - 1 and msg[i] == msg[i + 1]:
            count += 1
            i += 1
        if count > 1:
            compressed_msg += msg[i] + str(count)
        else:
            compressed_msg += msg[i]
        i += 1
    return compressed_msg


# Using for
def compressedString_for(msg):
    compressed_msg = ""
    count = 1
    len_msg = len(msg)
    for i in range(len_msg):
        if i < len_msg - 1 and msg[i] == msg[i + 1]:
            count += 1
        else:
            if count > 1:
                compressed_msg += msg[i] + str(count)
            else:
                compressed_msg += msg[i]
            count = 1
    return compressed_msg


# Using while
print(compressedString("abaabbbc"))  # output aba2b3c
print(compressedString("aabbabbbc"))  # output a2b2ab3c

# Using for
print(compressedString_for("aaabbcccc"))  # output a3b2c4
print(compressedString_for("aaababcccc"))  # output a3babc4

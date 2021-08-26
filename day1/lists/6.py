lista = [204, 120, 560, 204, 111, 120, 476, 382, 732]
listb = ["aa", "bb", "dd", "ww", "cc", "rr", "xx"]
listc = [158, "hello", 34.6, 219]
listd = ["hi", 306, [12, 13, 14], 28.9, listb]

print(listc)
listc[1] = "hi"
print("-----")
print(listc)

# error
listc[1][0] = "H"
print("-----")
print(listc)



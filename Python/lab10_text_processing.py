#  text processing tool

print("=======================")
print(" text processing tool")
print("=======================")
sec = input("enter scentence: ")
index=int(input("enter position for indexing: "))
print("character at position ",index,": ",sec[index])
slice1=int(input("enter index for slicing: "))
slice2=int(input("enter index for slicing: "))
print("sliced string: ",sec[slice1:slice2])
print("Uppercase: ",sec.upper())
print("Lowercase: ",sec.lower())
rep1=input("enter word to replace: ")
rep2=input("enter the replacing word: ")
print("after replacement: ",sec.replace(rep1,rep2))
print("length of the scentence: ",len(sec))



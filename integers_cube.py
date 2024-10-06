#for the size of array
print("Cubes of integers")
print("Hello User!\n")
size = float(input("Enter the size of the array: "))

#for inputing the integers of the array
elements = list(map(float, input("Enter the elements: ").split()))
if len(elements) != size:
    print(f"Invalid: You must enter exactly ({size}) elements. You entered ({len(elements)}) elements.")
else:
#display the cube of each integer
    print("The cube of each elements: ")
    for number in elements:
        print(number ** 3)
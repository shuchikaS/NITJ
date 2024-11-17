with open("file1.txt", "rb") as f:
    print("File1 Contents:")
    print(f.read())
    a = f.read(10)

with open("file2.txt", "wb+") as f2:
    # print("File2 contents:")
    print(f2.read())
    # f2.write(a)
    print("File2 contents after copying:")
    # print(f2.read())
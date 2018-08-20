with open("2b.png", "rb") as binary_file:
    
    data = binary_file.read(0x1F8734) # binary_file.seek(0x1F8734)
    data = binary_file.read()
    print(data)


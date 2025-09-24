def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as f:
            data = f.read()
        print(data)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
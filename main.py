from processor import data_handler

def main():
    user_input = input("Enter data: ")
    output = data_handler(user_input)
    print("Output:", output)

if __name__ == "__main__":
    main()

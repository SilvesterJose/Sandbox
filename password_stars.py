def get_password():
    password = input("Enter your password: ")
    return password

def print_password_stars(password):
    print('*' * len(password))

def main():
    password = get_password()
    print_password_stars(password)

if __name__ == "__main__":
    main()

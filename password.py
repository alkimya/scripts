import string
from secrets import choice

alphabet = string.printable

def pwd(len):
    while True:
        password = ''.join(choice(alphabet) for i in range(len))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    
    print(password)

if __name__ == "__main__":
    import sys
    pwd(int(sys.argv[1]))

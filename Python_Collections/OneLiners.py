print("Python One Liners")

txt = "One Liners"

print(txt[::-1])

print(''.join(reversed(txt)))

def check_length(x : str) -> str:
    return x.lower() if x.isupper() else x.upper()

print ( check_length('Subhash') )

# Password Generator
import random
#from secrets import choice
from string import ascii_letters, digits, punctuation

x: str = ''
for _ in range(5):
    x += random.choice(ascii_letters + digits + punctuation)

print(x)


def main() -> None:
    print('inside main')

if __name__ == '__main__':
    print('invoking main...')
    main()
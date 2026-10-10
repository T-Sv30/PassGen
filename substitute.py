from itertools import product
from lists import subDict
from lists import dummyCharacters
from lists import numbersOnly

#returns the cartesian product of all replaceable characters 
MAX_FULL_SUBSTITUTIONS = 1_000_000

def fullSub(password):
    """Generate substitutions, refusing empty input and excessive output."""
    if not isinstance(password, str) or not password:
        raise ValueError("password must be a non-empty string")

    letters = []
    for char in password:
        choices = subDict.get(char.lower(), [char]) if char.isupper() else subDict.get(char, [char])
        if char.isupper():
            choices = list(dict.fromkeys(
                item.upper() if item.isalpha() else item
                for item in choices
            ))
        letters.append(choices)
    count = 1
    for choices in letters:
        count *= len(choices)
        if count > MAX_FULL_SUBSTITUTIONS:
            raise ValueError(
                f"full substitution would generate more than "
                f"{MAX_FULL_SUBSTITUTIONS:,} candidates; use a shorter input"
            )

    return ["".join(item) for item in product(*letters)]

#returns a list of possible passwords by replacing the first letter with common substitutions and appending numbers and letters to the end.  If numbers flag is set then append numbers to end
def basicSub(password, numbers=False):
    if not isinstance(password, str) or not password:
        raise ValueError("password must be a non-empty string")

    if numbers:
        characterList = [
            ''.join(p)
            for n in range(1, 5)
            for p in product(numbersOnly, repeat=n)
        ]
    else:
        characterList = dummyCharacters
    passwords = []

    first = password[0]
    substitutions = subDict.get(first.lower(), [first])

    # Preserve uppercase when the original first character is uppercase.
    if first.isupper():
        substitutions = [item.upper() for item in substitutions]
    substitutions = list(dict.fromkeys(substitutions))

    middle = password[1:]
    replacements = product(substitutions, characterList)

    for val in replacements:
        passwords.append(val[0] + middle + val[1])

    return passwords

#same as basic substitution, but appends 0-9999 to the end 
def appendNumbers(password):
	return basicSub(password, True)

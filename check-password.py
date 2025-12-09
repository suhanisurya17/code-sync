# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def checkPassword(password):
    
    #rules
    #category 1
    #5 or more words (non-repeating_)
    #each word must be separated by a space
    #composite word must be at least 3 letteers
    #composed of only alphabetical characters
    
    #first I must turn the string into an array
    words = []
    words = password.split()
    if len(words) >= 5:
        for word in words:
            return len(word) >= 3 and word.isalpha():
                return True

    else:
        has_upper = False
        has_lower = False
        has_number = False
        has_symbol = False
        if len(password) >= 12:
            for char in password:
                if char.isupper():
                    has_upper = True
                if char.islower():
                    has_lower = True
                if char.isdigit():
                    has_number = True
                symbols = ["!","@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "="]
                if char in symbols:
                    has_symbol = True

                return has_upper and has_lower and has_number and has_symbol


                    
                
            
    #category 2
    #at least 12 char long
    #contains at least one upper case and one lowercase letter
    #contains at least one number
    #contains at least of of the following symbols: !@#$%^&*()_+=
    #no character may be used more than three times in a row


def main():
    test_cases = {
        # Category 1: Passphrase
        "apple banana cherry dragon eagle": True,
        "apple banana cherry dragon": False,
        "apple banana cherry apple eagle": False,
        "app ban cherry dragon eagle": True,
        "apple banana cherry123 dragon eagle": False,
        "applebananacherrydragoneagle": False,

        # Category 2: Complex password
        "Abcdef1@Ghij": True,
        "Ab1@Ghij": False,
        "abcdef1@ghij": False,
        "ABCDEF1@GHIJ": False,
        "Abcdef@Ghij": False,
        "Abcdef1Ghij": False,
        "Abc1111@Ghij": False,

        # Mixed edge cases
        "abc123": False,
        "äpple banåna chërry drägon eaglé": True,  # Depends on Unicode handling
        "apple  banana cherry dragon eagle": False,  # Double space
    }

    for pwd, expected in test_cases.items():
        result = checkPassword(pwd)
        print(f"Test: {pwd!r} → Expected: {expected}, Got: {result}, {'✅' if result == expected else '❌'}")


if __name__ == "__main__":
    main()
    

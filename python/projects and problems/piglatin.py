my_consonants = "bcdfghjklmnpqrstvwxyz"

def pig_latin(text, consonants):
    first_consonant = ''
    for char in text:
        if char in consonants:
            first_consonant = char
            break
    
    if not first_consonant:
        return text  # No consonants found in the text
    
    remaining_string = text.replace(first_consonant, '', 1)
    modified_string = remaining_string + '-' + first_consonant + 'ay'
    return modified_string

print(pig_latin("", my_consonants))






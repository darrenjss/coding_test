
letter_to_number = {
    # Uppercase letters
    'A': '0',
    'B': '1',
    'C': '2', 'D': '2',  # C and D both become 2
    'E': '3',
    'F': '4',
    'G': '5',
    'H': '6',
    'I': '7',
    'J': '8',
    'K': '9', 'L': '9', 'M': '9', 'N': '9', 'O': '9', 'P': '9',  # K through P become 9
    'Q': '2', 'R': '2', 'S': '2', 'T': '2', 'U': '2', 'V': '2',  # Q through V become 2
    'W': '2', 'X': '2', 'Y': '2', 'Z': '2',  # W through Z become 2
    
    # Lowercase letters
    'a': '9', 'b': '8', 'c': '7', 'd': '6',
    'e': '5', 'f': '4', 'g': '3', 'h': '3',
    'i': '2', 'j': '1',
    'k': '0', 'l': '0', 'm': '0', 'n': '0', 'o': '0', 'p': '0',  # k through p become 0
    'q': '7', 'r': '7', 's': '7', 't': '7', 'u': '7', 'v': '7',  # q through v become 7
    'w': '7', 'x': '7', 'y': '7', 'z': '7',  # w through z become 7
    
    # Space
    ' ': '0'
}

# This dictionary helps us convert numbers back to letters
number_to_letter = {
    '0': 'A',
    '1': 'B',
    '2': 'E',
    '3': 'F',
    '4': 'I',
    '5': 'J',
    '6': 'N',
    '7': 'O',
    '8': 'T',
    '9': 'Z'
}

# 1 Convert text to numbers
def convert_text_to_numbers(text):
    result = []
    
    
    for char in text:
        if char in letter_to_number:
            result.append(letter_to_number[char])
    
    return ' '.join(result)

# 2 Add and subtract numbers alternately
def add_subtract_numbers(number_string):
    numbers = number_string.split()
    
    numbers = [int(num) for num in numbers]
    
    result = numbers[0]
    
    for i in range(1, len(numbers)):
        if i % 2 == 1:
            result = result + numbers[i]
        else:
            result = result - numbers[i]

    return result

# 3 Convert number back to letters
def convert_number_to_letters(number):
    if number < 0:
        number = -number
    
    result = ""
    remaining = number
    
    while remaining > 0:
        for i in range(10):
            if remaining >= i:
                result += number_to_letter[str(i)]
                remaining -= i
                
        if len(result) > 20:
            break
    
    if result == "":
        return "A"
        
    return result

# 4 Transform letters in a pattern
def transform_letters(text):
    result = ""
    
    for i in range(len(text)):
        if i % 3 == 0:
            result += text[i]
        elif i % 3 == 1:
            result += 'B'
        else:
            result += 'E'
    
    return result

# 5 Convert final letters to numbers
def convert_final_letters(text):
    result = []
    
    
    for letter in text:
        if letter in ['A', 'B']:
            result.append('1')
        elif letter in ['E', 'F']:
            result.append('3')
        elif letter in ['I', 'J']:
            result.append('5')
        else:
            result.append('1')
    
    return ' '.join(result)

print("Welcome to Text Converter!")
print("This program will convert your text in 5 steps.")
print("Type 'quit' to exit the program")
print("-" * 50)

while True:
    
    text = input("\nPlease enter some text: ")
    
    if text.lower() == 'quit':
        print("Goodbye!")
        break
    
    print("\nConverting text to numbers:")
    step1_result = convert_text_to_numbers(text)
    print(step1_result)
    
    print("\nAdding and subtracting numbers:")
    step2_result = add_subtract_numbers(step1_result)
    print(step2_result)
    
    print("\nConverting number to letters:")
    step3_result = convert_number_to_letters(step2_result)
    print(step3_result)
    
    print("\nTransforming letters:")
    step4_result = transform_letters(step3_result)
    print(step4_result)
    
    print("\nFinal number conversion:")
    step5_result = convert_final_letters(step4_result)
    print(step5_result)
    
    print("\n" + "-" * 50)
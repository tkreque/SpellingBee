import string, yaml

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Wordle variables
required_letter = config['settings']['letters']['required']
optional_letters = config['settings']['letters']['optional']
letters_to_filter  = [letter for letter in list(string.ascii_lowercase) if letter not in optional_letters+list(required_letter)]

# File variables
fwords = open(config['settings']['files']['word'], "r")
fresult = open(config['settings']['files']['result'], "w")

# Initialize variables
output = [] 
words = []
count = 0

# Check for the words that contain the required letter
for word in fwords:
    word = word.lower()
    if required_letter.lower() in word:
        count += 1
        words.append(word)

# Remove words from the `letters_to_filter` variable
for word in words:
    if not any(letter.lower() in word for letter in letters_to_filter):
        output.append(word)

# Show some information
print(f"Words that have the letter '{required_letter.upper()}' are: {count}")
print(f"Total of filtered words {len(output)}")

# Save the result file
for line in output:
    fresult.write("".join(line)) 
fwords.close()
fresult.close()
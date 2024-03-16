import nltk
from nltk.stem import WordNetLemmatizer

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a dictionary mapping each keyword to a list of similar words or variables
keyword_mapping = {
    'pay': ['payment', 'salary', 'compensation','pay','pay range'],
    'site': ['location', 'place','workplace','site','remote','hybrid','home'],
    'level': ['position', 'rank', 'level'],
    'employees': ['staff', 'workers','strength','no of employees']
}

# Initialize lists to store extracted information
pay_list = []
site_list = []
time_list = []
level_list = []
employees_list = []

# Open the text file
with open("scrap_data.txt", "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Tokenize the line into words
        words = nltk.word_tokenize(line.lower())
        
        # Lemmatize each word
        lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
        
        # Iterate through each word in the line
        for i, word in enumerate(lemmatized_words):
            # Iterate through each keyword and its associated similar words or variables
            for keyword, similar_words in keyword_mapping.items():
                if word in similar_words:
                    # Extract the value next to or before the similar word or variable
                    if i < len(words) - 1:
                        value = words[i + 1]
                    else:
                        value = words[i - 1]
                    
                    # Append the value to the corresponding list based on the keyword
                    if keyword == 'pay':
                        pay_list.append(value)
                    elif keyword == 'site':
                        site_list.append(value)
                    elif keyword == 'time':
                        time_list.append(value)
                    elif keyword == 'level':
                        level_list.append(value)
                    elif keyword == 'employees':
                        employees_list.append(value)

# Display the extracted information
print("Pay List:", pay_list)
print("Site List:", site_list)
print("Time List:", time_list)
print("Level List:", level_list)
print("Employees List:", employees_list)

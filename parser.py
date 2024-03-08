from bs4 import BeautifulSoup

combined_content = content_2 + content_1

soup = BeautifulSoup(combined_content, 'html.parser')

# Find all text elements and print them
text_elements = soup.find_all(text=True)
for element in text_elements:
    if element.strip():
        print(element.strip())
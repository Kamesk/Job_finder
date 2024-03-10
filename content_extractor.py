from bs4 import BeautifulSoup

def token_extractor(content_1,content_2):
    combined_content = content_1 + content_2
    soup = BeautifulSoup(combined_content, 'html.parser')
    text_elements = soup.find_all(text=True)
    details = []
    for element in text_elements:
        if element.strip():
            details.append(element.strip())
    return details
import requests
from bs4 import BeautifulSoup

def get_passages(url):
    page = requests.get(url)
    matches = BeautifulSoup(page.content, "html.parser").find_all(title="Wikipedia:Citation needed")
    return [match.find_parent('p').text for match in matches]

def get_citations_needed_count(url):
    passages = get_passages(url)
    return len(passages)
    
def get_citations_needed_report(url):
    passages = get_passages(url)
    return '\n'.join([passage.strip() for passage in passages])

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Randall_Munroe"
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
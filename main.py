import requests
from colorama import Fore, Style, init
from cachetools import cached, LRUCache

init(autoreset=True)

headers = {
	"X-RapidAPI-Key": "fea76a78e2msh6ceeb99b809a476p150fb7jsn56411c2365be",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

@cached(cache=LRUCache(maxsize=10))
def getDefinition(word):
    
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"

    try:
        response = requests.get(url, headers=headers).json()
        return response
    except requests.exceptions.RequestException as e:
        return print(f'\n{Fore.RED}{e}{Style.RESET_ALL}')

@cached(cache=LRUCache(maxsize=10))
def getSyllables(word):

    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/syllables"

    try:
        response = requests.get(url, headers=headers).json()
        syllables = response["syllables"]
        return syllables
    except KeyError:
        return print(f'\n{Fore.RED}Word not found{Style.RESET_ALL}')
    except requests.exceptions.RequestException as e:
        return print(f'\n{Fore.RED}{e}{Style.RESET_ALL}')
    
@cached(cache=LRUCache(maxsize=10))
def getRhymes(word):

    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/rhymes"
     
    try:
        response = requests.get(url, headers=headers).json()
        rhymes = response["rhymes"]["all"]
        return rhymes
    except KeyError:
        return print(f'\n{Fore.RED}Word not found{Style.RESET_ALL}')
    except requests.exceptions.RequestException as e:
        return print(f'\n{Fore.RED}{e}{Style.RESET_ALL}')

def display_definitions(definitions):
    try:
        for definition in definitions['definitions']:
            print(f'\n{Fore.BLUE}Definition{Style.RESET_ALL} - ' + definition["definition"])
            return print(f'{Fore.RED}' + definition["partOfSpeech"] + f'{Style.RESET_ALL}', end="\n")
    except:
        return print(f'\n{Fore.RED}Word not found{Style.RESET_ALL}')

while True:
    print(f'\n{Fore.BLUE}1.{Style.RESET_ALL} Get definition')
    print(f'{Fore.BLUE}2.{Style.RESET_ALL} Get syllables')
    print(f'{Fore.BLUE}3.{Style.RESET_ALL} Get rhymes')
    
    choice = input(f"{Fore.BLUE}\nPick a choice:{Style.RESET_ALL} ")
    word = input(f"{Fore.BLUE}\nEnter a word:{Style.RESET_ALL} ")
        
    if choice == '1':
        definitions = getDefinition(word)
        display_definitions(definitions)
        
    elif choice == '2':
        syllables = getSyllables(word)
        print(f'{Fore.BLUE}Searched{Style.RESET_ALL} - {word.capitalize()}', end="\n")
        print(f'{Fore.BLUE}Syllables{Style.RESET_ALL} - {str(syllables["count"])} {str(syllables["list"])}')
    
    elif choice == '3':
        rhymes = getRhymes(word)
        print(f'{Fore.BLUE}Searched{Style.RESET_ALL} - {word.capitalize()}', end="\n")
        print(f'{Fore.BLUE}Rhymes{Style.RESET_ALL} - {str(rhymes)}')
    
    else:
        print(f'\n{Fore.RED}Invalid choice{Style.RESET_ALL}')
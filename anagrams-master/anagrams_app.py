from flask import Flask
from flask import request
import csv

app = Flask(__name__)


def load_dictionary_words():
    with open('dictionary.txt', newline='\n') as f:
        reader = csv.reader(f)
        dictionary_words = []
        for row in reader:
            dictionary_words.append(row[0])
        return dictionary_words

def get_anagrams_dict():
    anagrams_dict = {}
    dictionary_words = load_dictionary_words()
    for word in dictionary_words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams_dict:
            anagrams_dict[sorted_word] = [word]
        else:
            anagrams_dict[sorted_word].append(word)
    return anagrams_dict

def get_anagrams(word):
    sorted_word = "".join(sorted(word))
    anagrams = []
    anagrams_dict = get_anagrams_dict()
    if sorted_word in anagrams_dict:
        return str(anagrams_dict[sorted_word])
    if anagrams == []:
        return 'NOTHING WAS FOUND'



@app.route('/')
def hello_world():
    input_word = request.args.get('input_word')
    return get_anagrams(input_word)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

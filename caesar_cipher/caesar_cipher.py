import string
import nltk
nltk.download('words')
original_words_list = nltk.corpus.words.words()
words_list = [word.lower() for word in original_words_list]




def encrypt(string_, key):
    
    
    
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    result = ''

    for char in string_:
        alph = 0
        if not char.isalpha() : 
            if char ==' ' : 
                result += char
            continue

        char=char.lower()
        alph += alphabet_list.index(char) + key
        alph = alph % 26
        result += alphabet_list[alph]

    return result


def decrypt(string, key):
    return encrypt(string, -key)



def breack_code(string):
    trial_list = []
    for i in range(26):
        trial = decrypt(string,i)
        trial_list.append(trial)
    

    def count_words(sentence):
        sentence_words = sentence.split()
        en_word_count = 0

        for word in sentence_words:
            if word.lower() in words_list:
                en_word_count += 1

        return en_word_count

    def most_likely(sentences):
        _max = 0
        _max_sentence = ''

        for sentence in sentences:
            if count_words(sentence) > _max:
                _max_sentence = sentence
                _max = count_words(sentence)
        return _max_sentence

    return most_likely(trial_list)



if __name__ == "__main__":
    print( encrypt('majd mm', 30) )
    # print( encrypt('pdmg', -3) )
    # print(decrypt('pd@mg', 3))
    print(breack_code('Sd gkc dro locd yp dswoc sd gkc dro gybcd yp dswoc'))

# Assume that the comments are stored in file comments.txt
# assume that the profanity words are stored in file profanity.txt


from string import punctuation

profanity_words = ["stfu","bitch","wtf","gtfo","ass","stfu"]


def process_word(word):
    word = word.lstrip()
    word = word.strip()
    word = word.lower()
    return word


def process_sentence(sentence, line):
    profanity_counter = 0
    for p in list(punctuation):
        sentence = sentence.replace(p,'')
    words = sentence.split(' ')
    words_count = len(words)
    for word in words:
        word = process_word(word)
        if word in profanity_words:
            profanity_counter = profanity_counter+1
    print("Profanity in "+str(line)+" th sentence is "+str((profanity_counter/words_count)*100)+" %")


def divide_sentence(data):
    line = 0
    list_of_comments = data.split('.')
    for sentence in list_of_comments:
        sentence.strip()
        if sentence:
            line = line + 1
            process_sentence(sentence, line)


if __name__ == "__main__":

    with open("comments.txt","r") as f:
        data = f.read()
        divide_sentence(data)

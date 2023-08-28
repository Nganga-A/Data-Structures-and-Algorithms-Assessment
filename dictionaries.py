def word_frequency(sentence):
    content = sentence.split()
    result = [word.strip("?,!.") for word in content] #remove at beginning and end of sentence
    
    return {word: result.count(word) for word in result}

sentence = "This is a test sentence. This is a sentence test"
result = word_frequency(sentence)
print (result)

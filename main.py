def Tokenization(sentence):
    tokens = sentence.split()
    print("List of Tokens: ", tokens)
    return tokens

def RemoveStopWords(tokens):
    stopwords = [
        "a", "an", "the", "for", "of", "on", "at", "in", "to", "with", "by", 
        "and", "or", "but", "so", "from", "my", "your", "their", "our", 
        "this", "that", "these", "those", "is", "are", "was", "were", 
        "be", "been", "has", "have", "had", "do", "does", "did", "will", 
        "would", "can", "could", "should", "may", "might", "must", 
        "about", "up", "down", "under", "over", "as", "such", "into", 
        "out", "just", "like", "need", "required", "i", "am"
    ]

    tokens_set = set(tokens)
    print("set before filtering stopwords: ", tokens_set)
    
    filtered_tokens = {token for token in tokens if token.lower() not in stopwords}
    print("set after filtering stopwords: ", filtered_tokens)

    return filtered_tokens


if __name__ == "__main__":
    sentence = "I am a student and I am learning Python programming."
    tokens = Tokenization(sentence)
    tokens = RemoveStopWords(tokens)



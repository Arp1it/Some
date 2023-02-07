import time
init = time.time()

def search_engine():
    sentences = ["python is a good", "python is beggineer friendly", "python is a good programming language", "this is a good"]

    while True:
        matches = (yield)

        def matchingwords(sentence1, sentence2):
            words = sentence1.strip().split(" ")
            words2 = sentence2.strip().split(" ")
            score = 0

            for word in words:
                for word2 in words2:
                    if word.lower() == word2.lower():
                        score += 1

            return score

        scores = [matchingwords(matches, sentence) for sentence in sentences]

        sortedsetenscores = [sentscore for sentscore in sorted(zip(scores, sentences), reverse=True) if sentscore[0] != 0]

        print(f"{len(sortedsetenscores)} result found in ({time.time() - init}):-")
        for scor, item in sortedsetenscores:
            print(f" \"{item}\": with a score of {scor}")


while True:
    search = search_engine()
    querry = input("Enter: ")
    print("Search started")
    next(search)
    search.send(querry)

    i = input("continue or not: ")

    if i == "c":
        continue

    if i == "n":
        break
import pickle



with open("vectorizer.pkl", "rb") as file:
    cvectorizer = pickle.load(file)


def prepare_data(text):
    vectorized_text = cvectorizer.transform([text])
    return vectorized_text
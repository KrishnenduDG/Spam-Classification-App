import pickle
import string
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


def transform_text(text):
    ps = PorterStemmer()

    text = text.lower()  # Lower Case
    text = nltk.word_tokenize(text)  # Tokenise in Words

    text = list(filter(lambda x: x.isalnum(), text))  # Removing special characters

    text = list(
        filter(lambda x: x not in stopwords.words("english"), text)
    )  # Removing stop words

    text = list(
        filter(lambda x: x not in string.punctuation, text)
    )  # Removing punctuation

    text = [ps.stem(word) for word in text]  # Stemming

    return " ".join(text)


def predict_spam_or_ham(sentence):
    tfidf = pickle.load(open("vectorizer.pkl", "rb"))
    model = pickle.load(open("model.pkl", "rb"))

    vector_input = tfidf.transform([transform_text(sentence)])

    return model.get_model().predict(vector_input)

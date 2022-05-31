import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')

pac = joblib.load('fakenewsfinder.pkl')
cv = joblib.load('countvectorizer')
def newspredictor(input):
    token = word_tokenize(input)

    stop_words = set(stopwords.words('english'))
    filtered = []

    for i in token:
        if i not in stop_words:
            filtered.append(i)
    filtered = ' '.join(filtered)

    feature = [filtered]
    ftm = cv.transform(feature)
    #print(pac.predict(ftm))
    return(pac.predict(ftm))

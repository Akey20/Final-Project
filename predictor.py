import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

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
    print(pac.predict(ftm))


input = "TIRANA, Albania (AP) — Albania has offered NATO a naval base in an effort to highlight the small country’s value in the alliance “in these difficult times,” the prime minister’s office said Thursday. Prime Minister Edi Rama said Pashaliman naval base, 180 kilometers (110 miles) south of the capital Tirana, could be “an added value” to the alliance and they had prepared a project on its renovation. “In these dangerous times I believe the general may consider having a NATO’s naval base in Albania,” Rama said in a speech Wednesday. Albania, which became a NATO member in 2009, has joined the United States and the European Union in denouncing Russia’s war in Ukraine. The Pashaliman base located under the Vlora Bay was built in the 1950s when the Soviet Union brought 12 submarines, making it the only naval base they had in the Mediterranean. Following the breakdown of Tirana-Moscow ties in 1961, the Pashaliman remained as a naval base sheltering four remaining submarines and other small military ships. The base was looted, including material from the submarines, during the anarchic year of 1997 in Albania when Europe’s then-poorest population lost its life savings in failed pyramid investment schemes. Three of the submarines were sold for scrap while the fourth one remains, with the government considering whether to turn it into a museum. Pashaliman was renovated by Turkey and since has been used as a naval base for some military ships patrolling the Ionian and Adriatic Seas. NATO also has started work to upgrade Albania’s communist-era Kucove Air Base, 85 kilometers (53 miles) south of the capital Tirana, which will allow it to be used for alliance operations."
newspredictor(input)
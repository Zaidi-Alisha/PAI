#Tokenization
import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources (first time only)
nltk.download('punkt')

text = "This is an example sentence for tokenization."
tokens = word_tokenize(text)
print(tokens)


#Stemming and Lemitization
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

# Download necessary NLTK resources (first time only)
nltk.download('wordnet')

# Stemming
stemmer = PorterStemmer()
word = "running"
stemmed_word = stemmer.stem(word)
print(f"Stemmed word: {stemmed_word}")

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_word = lemmatizer.lemmatize(word, pos='v')  # 'v' for verb
print(f"Lemmatized word: {lemmatized_word}")


#Stop word removal
from nltk.corpus import stopwords

# Download stopwords list (first time only)
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
text = "This is an example sentence with stop words."
tokens = word_tokenize(text)
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print(filtered_tokens)

#Puctuation mark removal
import string

text = "This is an example sentence, with punctuation!"
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
print(cleaned_text)


#Convert Words to Vector (Count Vectorizer, TF-IDF)
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Example corpus
corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# Count Vectorizer
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(corpus)
print("Count Vectorizer Matrix:")
print(count_matrix.toarray())

# TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())


#Putting it all together
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Download necessary resources (first time only)
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "This is an example sentence, with punctuation and stopwords!"

# Tokenization
tokens = word_tokenize(text)

# Remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]

# Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word.lower() not in stop_words]

# Lemmatization
lemmatizer = nltk.WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(word) for word in tokens]

# Convert tokens back to a string for further processing or vectorization
processed_text = " ".join(tokens)

# Convert to TF-IDF vector
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([processed_text])

print(f"Processed Text: {processed_text}")
print(f"TF-IDF Matrix:\n{tfidf_matrix.toarray()}")


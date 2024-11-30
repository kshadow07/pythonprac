import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset 
train_data = ["This is a positive review", "This is a negative review", "I'm neutral about this product"] #will use bigger data sheet to train it.
train_labels = [1, 0, 1]  # 1 for positive, 0 for negative

# Tokenize the text data
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
tokenized_data = [sia.polarity_scores(text) for text in train_data]

# Convert tokenized data into a list of strings
tokenized_data_str = [' '.join(str(score) for score in scores.values()) for scores in tokenized_data]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(tokenized_data_str, train_labels, test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the training data and transform both the training and testing data
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a logistic regression model on the training data
lr_model = LogisticRegression()
lr_model.fit(X_train_tfidf, y_train)

# Evaluate the model on the testing data
accuracy = lr_model.score(X_test_tfidf, y_test)
print("Accuracy:", accuracy)
print('model',vectorizer.build_preprocessor)
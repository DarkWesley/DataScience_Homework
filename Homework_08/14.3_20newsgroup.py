from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
text_data = newsgroups.data
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(text_data)
print("第一个文本的结果向量:",tfidf_vectors[0].toarray())
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

docs=[ "the sky is blue",

"the sun is bright",

"the sun is in the sky is bright."]

vectorizer=Tfidfvectorizer()

tfidf_matrix=vectorizer.fit_transform(docs)

similarity=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix)

print("similarity scores:",similarity)
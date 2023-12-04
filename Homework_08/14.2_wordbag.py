from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()
text=['Can you get more interested in travelling',
    'One brings shadow',
    'One brings light',
    'Two-toned echoes tumbling through time']

v=cv.fit_transform(text)
print(v)
print(cv.get_feature_names_out())
print(v.toarray())
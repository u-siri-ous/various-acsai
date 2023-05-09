from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

data = [
    'problem of evil', 'evil queen', 'horizon problem'
]

# it works the same as the dictvectorizer
vec = CountVectorizer()     #Convert a collection of text documents to a matrix of token counts
X = vec.fit_transform(data)

# we aim to have a better visualization of data - use pandas
# convert the vec representation to a readable matrix with word occurrences (pandas dataframe)
vis_data = pd.DataFrame(X.toarray(), columns=vec.get_feature_names_out())

# weigh the words based on occurrences (TF-IDF; term frequency – inverse document frequency)
vec2 = TfidfVectorizer()
X2 = vec2.fit_transform(data)

# and visualize
vis_data2 = pd.DataFrame(X2.toarray(), columns=vec2.get_feature_names_out())


print(vis_data2)
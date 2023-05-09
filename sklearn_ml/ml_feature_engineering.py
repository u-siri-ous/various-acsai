from sklearn.feature_extraction import DictVectorizer   

data = [                            
    {'price': 12345, 'room': 4, 'neighborhood': 'Viale Ippocrate'},
    {'price': 26789, 'room': 6, 'neighborhood': 'Casilina'},
    {'price': 44444, 'room': 4, 'neighborhood': 'Appia'},
]

# the key is to uniformize the data by type (i.e. neigh becomes a number)
# {'Viale Ippocrate': 1, 'Casilina': 2, 'Appia': 3}   # this is not good, as the values are ordinal

# use one-hot-encoder for categorical/string-like values, transforming data in a binary string

vec = DictVectorizer(dtype=int)         #Transforms lists of feature-value mappings to vectors
new_feat = vec.fit_transform(data)      #Learn a list of feature name -> indices mappings and transform X

print(new_feat)
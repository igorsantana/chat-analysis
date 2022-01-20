import os
from gensim.models.doc2vec import Doc2Vec
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE

streamers = []
streamers_embeddings = {}


rootmodel = './src/models'
for subdir, dirs, files in os.walk(rootmodel):
    streamer = subdir.split('/')[-1]
    filtered_models = [file for file in files if file.endswith('_d2v.model')]
    if(len(filtered_models) == 0):
        continue
    model_file = filtered_models[0]
    to_save = os.path.join(rootmodel, streamer)
    model = Doc2Vec.load(to_save + '/' + model_file)
    streamers_embeddings[streamer] = model.dv.get_normed_vectors().mean(axis=0)
    streamers.append(streamer)
df = pd.DataFrame(data=streamers_embeddings)
tsne = TSNE(n_iter=1000)
embs = tsne.fit_transform(df)
x = embs[:, 0]
y = embs[:, 1]

plt.scatter(x, y)
labels = list(df.columns.values)
for i, label in enumerate(labels):
    plt.annotate(label, (x[i], y[i]))

plt.savefig('foo.png')

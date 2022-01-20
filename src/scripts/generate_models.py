# Import packages
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import os
import nltk
nltk.download('punkt')

rootdir = './src/logs'
rootmodel = './src/models'
for subdir, dirs, files in os.walk(rootdir):
    model = None
    streamer = subdir.split('/')[-1]
    filtered_files = [file for file in files if 'preprocessed' in file]
    if(len(filtered_files) == 0):
        continue
    to_save = os.path.join(rootmodel, streamer)
    for file in filtered_files:
        read_data = open(os.path.join(subdir, file), 'r')
        lines = read_data.readlines()
        tokenized_doc = []
        for line in lines:
            tokenized_doc.append(word_tokenize(line))
        read_data.close()
        tagged_data = [TaggedDocument(d, [i])
                       for i, d in enumerate(tokenized_doc)]
        if(model is not None):
            model.train(tagged_data, epochs=50,
                        total_examples=len(tagged_data),)
            print('Training again the model for ' + streamer)
        else:
            print('Generating the first model for ' + streamer)
            model = Doc2Vec(tagged_data, vector_size=50,
                            window=1, min_count=1, workers=4, epochs=50,)

    if not os.path.exists(to_save):
        os.makedirs(to_save)
    model.save(to_save + '/' + streamer + "_d2v.model")

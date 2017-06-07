print("loading vocab "+ str(datetime.datetime.now()))
    word2idx, idx2word = load_vocab('map.json')
    print("Done "+ str(datetime.datetime.now()))
    # cosine similarity model
    print("create input a and b "+ str(datetime.datetime.now()))
    input_a = Input(shape=(1,), dtype='int32', name='input_a')
    input_b = Input(shape=(1,), dtype='int32', name='input_b')
    print("Done "+ str(datetime.datetime.now()))
    print("create embedding layer "+ str(datetime.datetime.now()))
    embeddings = word2vec_embedding_layer('embeddings.npz')
    print("Done "+ str(datetime.datetime.now()))
    print("create embedding a and b "+ str(datetime.datetime.now()))
    embedding_a = embeddings(input_a)
    embedding_b = embeddings(input_b)
    print("Done "+ str(datetime.datetime.now()))
    print("merge for similarity "+ str(datetime.datetime.now()))
    similarity = merge([embedding_a, embedding_b],
                       mode='cos', dot_axes=2)
    print("Done "+ str(datetime.datetime.now()))
    print("compile model "+ str(datetime.datetime.now()))
    model = Model(input=[input_a, input_b], output=[similarity])
    model.compile(optimizer='sgd', loss='mse')
    print("Done "+ str(datetime.datetime.now()))
    while True:
        word_a = input('First word: ')
        if word_a not in word2idx:
            print('Word "%s" is not in the index' % word_a)
            continue
        word_b = input('Second word: ')
        if word_b not in word2idx:
            print('Word "%s" is not in the index' % word_b)
            continue
        output = model.predict([np.asarray([word2idx[word_a]]),
                                np.asarray([word2idx[word_b]])])
        print(output)
    
from gensim.models import word2vec


if __name__ == '__main__':
    '''
    sentences = word2vec.LineSentence('./sentences.txt')
    
    model_cbow = word2vec.Word2Vec(sentences, sg=0, vector_size=100, window=5, min_count=5, workers=3, epochs=20)
    model_skip_gram = word2vec.Word2Vec(sentences, sg=1, vector_size=100, window=5, min_count=5, workers=3, epochs=20)
    model_cbow.save('./cbow.model')
    model_skip_gram.save('./skip_gram.model')
    '''
    model_cbow = word2vec.Word2Vec.load('./cbow.model')
    model_skip_gram = word2vec.Word2Vec.load('./skip_gram.model')


    print(model_cbow.wv.most_similar('杨过', topn=10))
    print(model_cbow.wv.most_similar('郭靖', topn=10))
    print(model_cbow.wv.most_similar('韦小宝', topn=10))
    print(model_cbow.wv.most_similar('峨嵋派', topn=10))
    print(model_cbow.wv.most_similar('六脉神剑', topn=10))
    print(model_cbow.wv.most_similar('降龙十八掌', topn=10))

    print('\n')

    print(model_skip_gram.wv.most_similar('杨过', topn=10))
    print(model_skip_gram.wv.most_similar('郭靖', topn=10))
    print(model_skip_gram.wv.most_similar('韦小宝', topn=10))
    print(model_skip_gram.wv.most_similar('峨嵋派', topn=10))
    print(model_skip_gram.wv.most_similar('六脉神剑', topn=10))
    print(model_skip_gram.wv.most_similar('降龙十八掌', topn=10))






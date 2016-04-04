#encoding=utf-8

from zhcnSegment import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence

if __name__ == '__main__':
    # 读入训练集
    file_obj = FileObj(r"testSet/trainSet.txt")
    train_sentences = file_obj.read_lines()

    # 读入测试集1
    file_obj = FileObj(r"testSet/testSet1.txt")
    test1_sentences = file_obj.read_lines()

    # 读入测试集2
    file_obj = FileObj(r"testSet/testSet2.txt")
    test2_sentences = file_obj.read_lines()

    # 分词工具，基于jieba分词，我自己加了一次封装，主要是去除停用词
    seg = Seg()

    # 训练模型
    ss = SentenceSimilarity(seg)
    ss.set_sentences(train_sentences)
    ss.TfidfModel()         # tfidf模型
    # ss.LsiModel()         # lsi模型
    # ss.LdaModel()         # lda模型

    # 测试集1
    right_count = 0
    for i in range(0,len(train_sentences)):
        sentence = ss.similarity(test1_sentences[i])

        if i != sentence.id:
            print str(i) + " wrong! score: " + str(sentence.score)
        else:
            right_count += 1
            print str(i) + " right! score: " + str(sentence.score)

    print "正确率为: " + str(float(right_count)/len(train_sentences))

    # 测试集2
    # right_count = 0
    # for i in range(0,len(train_sentences)):
    #     sentence = ss.similarity(test2_sentences[i])
    #
    #     if i != sentence.id:
    #         print str(i) + " wrong! score: " + str(sentence.score)
    #     else:
    #         right_count += 1
    #         print str(i) + " right! score: " + str(sentence.score)
    #
    # print "正确率为: " + str(float(right_count)/len(train_sentences))
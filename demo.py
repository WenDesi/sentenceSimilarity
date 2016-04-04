#encoding=utf-8

from zhcnSegment import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence

if __name__ == '__main__':
    file_obj = FileObj(r"testSet/trainSet.txt")
    train_sentences = file_obj.read_lines()

    file_obj = FileObj(r"testSet/testSet1.txt")
    test1_sentences = file_obj.read_lines()

    file_obj = FileObj(r"testSet/testSet2.txt")
    test2_sentences = file_obj.read_lines()


    seg = Seg()
    ss = SentenceSimilarity(seg)
    ss.set_sentences(train_sentences)
    ss.TfidfModel()

    for i in range(0,len(train_sentences)):
        sentence = ss.similarity(test1_sentences[i])

        if i != sentence.id:
            print str(i) + " " + str(sentence.id)
            print train_sentences[i]
            print sentence.get_origin_sentence()
            print "#####################   score: " + str(sentence.score)

        else:
            print "ok:"+str(i)



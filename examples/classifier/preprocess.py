from tamil import utf8
import sys
import codecs
import csv

class Feature:
    def __init__(self):
        self.nletters = 0.0
        self.kurils = 0.0
        self.nedils = 0.0
        self.ayudhams = 0.0
        self.vallinams = 0.0
        self.mellinams = 0.0
        self.idayinams = 0.0
        self.granthams = 0.0
        self.first = 0.0
        self.last = 0.0 

    def __str__(self):
        return u"(n=%d,kurils=%g,nedils=%g,ayudhams=%g,vallinams=%g,mellinams=%g,idayinams=%g,granthams=%g,first=%g,last=%g)"%(self.nletters,self.kurils,self.nedils,self.ayudhams,self.vallinams,self.mellinams,self.idayinams,self.granthams,self.first,self.last)
    
    def data(self):
        return (self.nletters,self.kurils,self.nedils,self.ayudhams,self.vallinams,self.mellinams,self.idayinams,self.granthams,self.first,self.last)
    
    @staticmethod
    def get(word):
        word = word.strip()
        word = word.replace(u' ',u'')
        letters = utf8.get_letters(word)
        F = Feature()
        F.nletters = len(letters)*1.0
        for l in letters:
            kind = utf8.classify_letter(l)
            if kind == 'kuril':
                F.kurils += 1
            elif kind == 'nedil':
                F.nedils += 1
            elif kind == 'ayudham':
                F.ayudhams += 1
            elif kind == 'vallinam':
                F.vallinams += 1
            elif kind == 'mellinam':
                F.mellinams += 1
            elif kind == 'idayinam':
                F.idayinams += 1
            else:
                F.granthams += 1

        F.kurils /= F.nletters
        F.nedils /= F.nletters
        F.ayudhams /= F.nletters
        F.vallinams /= F.nletters
        F.vallinams /= F.nletters
        F.mellinams /= F.nletters
        F.idayinams /= F.nletters
        F.granthams /= F.nletters
        
        if letters[0] in utf8.uyir_letters:
            F.first += 0.1
        if letters[0] in utf8.mei_letters:
            F.first += F.first + 0.25
        if letters[0] in utf8.uyirmei_letters:
            F.first += F.first + 0.5

        if letters[-1] in utf8.uyir_letters:
            F.last += 0.1
        if letters[-1] in utf8.mei_letters:
            F.last += F.last + 0.25
        if letters[-1] in utf8.uyirmei_letters:
            F.last += F.last + 0.5
        return F

def process(fname):
    ofname = fname+".csv"
    ofp = csv.writer(codecs.open(ofname,"w","utf-8"))
    with codecs.open(fname,"r","utf-8") as fp:
        for idx,line in enumerate(fp.readlines()):
            w = line.strip()
            try:
                f = Feature.get(w)
            except Exception as ioe:
                print("SKIPPING => ",ioe.message)
                continue
            ofp.writerow(f.data())
    #ofp.close()
    
def run():
    for fname in sys.argv[1:]:
        process(fname)

if __name__ == u"__main__":
    run()

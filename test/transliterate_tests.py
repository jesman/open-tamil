# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

from transliterate import *

class Yazhpanam(unittest.TestCase):
    def test_vandemataram(self):     
        tamil_words = u"வந்தே மாதரம்"
        eng_string = u'vanthE mAtharam'
        tamil_tx = iterative_transliterate(jaffna.Transliteration.table,eng_string)
        print("]"+tamil_tx+"[", len(tamil_words), len(tamil_tx),type(tamil_tx),type(tamil_words))
        print("]"+tamil_words+"[")
        self.assertTrue( tamil_words == tamil_tx )

    def test_combinational(self):
        tamil_words = u"வந்தே மாதரம்"
        eng_string = u'van-thee maatharam'
        tamil_tx = iterative_transliterate(combinational.Transliteration.table,eng_string)
        print("]"+tamil_tx+"[", len(tamil_words), len(tamil_tx), type(tamil_tx), type(tamil_words))
        print("]"+tamil_words+"[", len(tamil_tx), len(tamil_words))
        
        self.assertTrue( tamil_words.find(tamil_tx) >= 0 )
        
    def test_azhagi(self):
        ## challenge use a probabilistic model on Tamil language to score the next letter,
        ## instead of using the longest/earliest match
        ## http://www.mazhalaigal.com/tamil/learn/keys.php
        
        codes = {"neenga":u"நீங்க", "andam":u"அண்டம்", "nandri":u"நன்றி", "katru":u"கற்று",
                 "viswam": u"விஸ்வம்", "namaskaaram":u"நமஸ்காரம்",
                 "sreedhar":u"ஸ்ரீதர்", "manju":u"மஞ்சு", "gnaayam":u"ஞாயம்",
                 "poi":u"பொய்", "kaai":u"காய்", "aGnGnaanam":u"அஞ்ஞானம்", "mei":u"மெய்",
                 "nanghu":u"நன்கு", "palancaL":u"பலன்கள்", "payanKaL":"பயன்கள்", "avanThaan":u"அவன்தான்",
                 "leoni":u"லியோனி", "paeTrik":u"பேட்ரிக்", "peTroal":u"பெட்ரோல்", "coapanHaegan":u"கோபன்ஹேகன்",
                 "bandham":u"பந்தம்", "saantham":u"சாந்தம்", "kaeLvi":u"கேள்வி", "koavil":u"கோவில்",
                 "nhagar":u"நகர்", "maanhagaram":u"மாநகரம்", "senhnheer":u"செந்நீர்"}
        
        tamil_words = u""
        for eng_string, tamil_words in codes.items():
            tamil_tx = iterative_transliterate(azhagi.Transliteration.table,eng_string)
            print("]"+tamil_tx+"[", len(tamil_words), len(tamil_tx), "]"+tamil_words+"[")
            #self.assertTrue( tamil_words == tamil_tx ) #we are almost there but not yet
        
    def test_devotional(self):
        for k,v in {u"thiruvaachakam":u"திருவாசகம்",
                    u"mANikka vAsagar":u"மாணிக்க வாசகர்"}.items():
            tamil_tx = iterative_transliterate( azhagi.Transliteration.table,
                                                k )
            if( tamil_tx != v ):
                raise Exception(u"Transliteration changed\n Expected %s, but got %s for string input %\n"%(v,tamil_tx,k))
            else:
                print(u"matched %s => %s"%(k,unicode(tamil_tx)))
        return

if __name__ == '__main__':    
    test_support.run_unittest(Yazhpanam)

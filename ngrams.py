## N-Gram Code  
## Outputs n-grams given output from 

import nltk
import string
import re
from unidecode import unidecode
import collections
import operator
import argparse

## Appearance limits in order to be printed in output files
one_gram_limit = 20
two_gram_limit = 10
three_gram_limit = 10
four_gram_limit = 5
five_gram_limit = 5

## Get filename, read it in
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='filename', action='store', required=True, help='filename')
flags = parser.parse_args()
filename = flags.filename

f = open(filename, 'r')
text = file.read(f)
f.close()

## Clean text
punct = re.sub('\'','',(string.punctuation))
text2 = unidecode(text.decode('utf-8'))
text3 = text2.translate(string.maketrans(punct,''.join(" " * len(punct))))
text4 = [word.strip(string.punctuation).lower() for word in text3.split(" ")]
text5 = filter(lambda a: a != '', text4)

## 1 Grams
c = collections.Counter(text4)
c2 = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
 
f = open('1grams.txt','w')
for a,b in c2:
    if b > one_gram_limit:
#         print '%s : %d\n' % (str.strip(a), b)
        f.write('%s : %d\n' % (str.strip(a), b))
f.close()
   
## 2 Grams
my_bigrams = list(nltk.bigrams(text5))
   
c = collections.Counter(my_bigrams)
c2 = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
   
f = open('2grams.txt','w')
for (a,b),c in c2:
    if c > two_gram_limit:
#         print '%s %s: %d\n' % (a, b, c)
        f.write('%s %s: %d\n' % (a, b, c))
f.close()
   
## 3 Grams
my_trigrams = list(nltk.trigrams(text5))
   
c = collections.Counter(my_trigrams)
c2 = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
   
f = open('3grams.txt','w')
for (a,b,c),d in c2:
    if d > three_gram_limit:
#         print '%s %s %s: %d\n' % (a, b, c, d)
        f.write('%s %s %s: %d\n' % (a, b, c, d))
f.close()
  
## 4 Grams
my_fourgrams = list(nltk.ngrams(text5,4))
  
c = collections.Counter(my_fourgrams)
c2 = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
  
f = open('4grams.txt','w')
for (a,b,c,d),e in c2:
    if e > four_gram_limit:
#         print '%s %s %s %s: %d\n' % (a, b, c, d, e)
        f.write('%s %s %s %s: %d\n' % (a, b, c, d, e))
f.close()
 
## 5 Grams
my_fivegrams = list(nltk.ngrams(text5,5))
 
c = collections.Counter(my_fivegrams)
c2 = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
 
f = open('5grams.txt','w')
for (a,b,c,d,e),g in c2:
    if g > five_gram_limit:
#         print '%s %s %s %s %s: %d\n' % (a, b, c, d, e, g)
        f.write('%s %s %s %s %s: %d\n' % (a, b, c, d, e, g))
f.close()
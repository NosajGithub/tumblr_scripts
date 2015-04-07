# tumblr_scripts

## tumblr_wordle
Given a tumblr blogname, this code produces a textfile with the body text for every text post on that blog that is not a reblog.
This can then be fed into wordle to make a nice visual representation of the author's posts.

*Requirements*:  
1) The tumblpy package (run "pip install python-tumblpy" if you don't have it)  
2) A tumblr API consumer and secret key, which you can get here: https://www.tumblr.com/oauth/apps  

*Usage*:  
Enter "python tumblr_wordle.py -b \<blog\> -c \<conusmer key\> -s \<secret key\>"  

Replace \<blog\> with the username to get, and \<consumer key\> with the consumer key and \<secret key\> with the secret key.  
When complete, it will create a text file called "<blog>.txt", which you can copy and enter on http://www.wordle.net/create.

## ngrams
Given the output of tumblr_wordle, this code produces textfiles with the most frequently occuring 1 through 5-grams.

*Requirements*:  
1) nltk ("sudo pip install -U nltk")   
2) unidecode (https://pypi.python.org/pypi/Unidecode)  

Usage:  
Enter "python ngrams.py -f \<filename\>"  

Just input the filename.

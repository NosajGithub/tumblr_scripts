## tumblr_wordle
## Spits out a text file containing the body of every non-reblogged text post 

from tumblpy import Tumblpy
import argparse

# Set up argument parser, read in username
parser = argparse.ArgumentParser()
parser.add_argument('-b', dest='blog', action='store', required=True, help='blog to check')
parser.add_argument('-c', dest='consumer', action='store', required=True, help='consumer key')
parser.add_argument('-s', dest='secret', action='store', required=True, help='secret key')

flags = parser.parse_args()
blog = flags.blog
blog_url = "http://" + blog + ".tumblr.com/"
consumer = flags.consumer
secret = flags.secret

# Authenticate on Tumblr
t = Tumblpy(consumer, secret)

auth_props = t.get_authentication_tokens()
auth_url = auth_props['auth_url']

OAUTH_TOKEN_SECRET = auth_props['oauth_token_secret']
print "You're into Tumblr!"

# Get the number of posts to evaluate
posts = t.get('info', blog_url=blog_url)
num_posts = posts['blog']['posts']
print "There are " + str(num_posts) + " posts to examine..."
 
# Iterate through posts, searching for self-text posts, saving body of each post
f = open((blog + '.txt'),'w')

count = 0
texts = []
for i in range(0,num_posts,20):
    # Only text posts, only raw text, and include reblog information
    posts = t.get('posts', blog_url=blog_url, params = {'offset':str(i),'type':'text','filter':'text','reblog_info':'true'})
    theposts = posts['posts']
    for j in theposts:
        body = j.get('body').encode('utf8')
        if body != None and j.get('reblogged_root_url') == None:
            texts.append(body)
            count += 1
            f.write(body)
    print "Checking out posts numbered " + str(i) + " to " + str(i+20)
f.close()

print "All done! There were a total of " + str(count) + " non-reblogged text posts collected."
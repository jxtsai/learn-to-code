from twitter import Twitter

aToken ='809491-HbR2j2Bj7E6fbZxl9RbutufysSGuRlnr7UEvADFZIEx' 
aTokenSec = 'M8N8Nbk7ypswR3fI3RveWFfy8PNaUc2HRDy6OuYTkSB52'
comsumerKey = 'e9Agxo4v3f4iOcdG6Cr6ArtPw'
comsumerSec = 'ia6SmBmTAPyLZwinN3GRcJEK3mqGOk7rONeVyqZJngnmPpTUHt'

t = Twitter(auth=OAuth(aToken,aTokenSec,comsumerKey,comsumerSec))

pythonTweets = t.search.tweets(q = "#python")

print(pythonTweets)
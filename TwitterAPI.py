import tweepy
import time
 
#auth = tweepy.OAuthHandler('d0g3B9Ausr3NRHTyMyWJH8EUa','Nu1SMvx0b4feUVHxR0aEDeP740ezTb0p83zcZQ0AM08994zwaV')
#auth.set_access_token('1353027768930340864-hSpi4M4J3iiu789if2bqihtlmGjC1s','uAB9w8tIxv6rKCy1Spdy8Ud1D2Bp5Xad6ZgyBal5xRFkc')

#rajas API keys
#auth = tweepy.OAuthHandler('evCzNKvLuRT4BeA0N10o6gWno','1lUl7MWzeNCLKyaEFYI9SAZo7gLaPEQ0CP1zm9NAMHEUL7hXdM')
#auth.set_access_token('1353027768930340864-vmZ5MubllljzytLu768ERxsmlrweVo','BAMHS7QaWTkBNULjne5rwH99l16kvcWS5IlHCmm9vQmrx')

#sneha API keys
auth = tweepy.OAuthHandler('rws1Ynh0zEAagYLhUye57C5gy','iJejuYnN16pYUlKrfvvSJdbK4GPrMctL28ov8jcxgbHVpBbG0u')
auth.set_access_token('772506753619496960-hD4fySzewXaE8x6PRiobCmmy2BG7nz2','r9rpJxHXWIyHFeKrbRXerP43vvYCBzvGEPVAoLPFHQpC0')


api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()

#print(user.screen_name)
#for follower in tweepy.Cursor(api.followers_ids).items():
#   print(follower)

search = ''
ntweets = 100
like_count = 0
rt_count = 0


for follower in tweepy.Cursor(api.followers).items():
    if follower.screen_name == 'Sagar Vishwakarma' or 'Ashish Mhatre' or 'Bhushan Devrukhkar' or 'HinduJagr utiOrg' or 'Sunil Ghanwat' or 'HinduJagrutiOrg':
        print('yay!')
        for tweet in tweepy.Cursor(api.search,search).items(ntweets):
            try:
                tweet.retweet()
                rt_count+=1
                time.sleep(5)
                
            except tweepy.TweepError as error:
                print(error.reason)
                tweet.favorite()
                like_count+=1    

            except StopIteration:
                break
    else:
        pass
    

liked = 'We have liked ' + str(like_count) + ' Tweets'
retweets = 'We have Retweeted ' + str(rt_count) + ' Tweets'

print(liked)
print(retweets)


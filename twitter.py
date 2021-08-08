import tweepy

# アクセスキー
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

# インスタンス作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 検索したいワードをqに入れる
# いいねしたいTweet数をcountに入れる
search_results = api.search(q="", count=)
for result in search_results:
	tweet_id = result.id
	user_id = result.user._json['id']
	try:
		api.create_favorite(tweet_id) # いいね
		#api.create_friendship(user_id) # フォロー
	except Exception as e:
		print(e)
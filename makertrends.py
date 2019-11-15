from __future__ import absolute_import, print_function
import os
from subprocess import call
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import MySQLdb

script_path = os.path.dirname(os.path.realpath(__file__))

#db connection

db = MySQLdb.connect(host= "localhost", user="", passwd="", db="")

conn = db.cursor()

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after

consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section

access_token=""
access_token_secret=""

# This is the string to search in the twitter feed
# May be  a word, an #hashtag or a @username

search_strings = ['makerspace','arduino','raspberry pi','raspberrypi','esp8266','robotics','robotica','microcontroller','microcontrolador','iot','tinkering','hackspace','hack','esp32','maker','lora']

class StdOutListener(StreamListener):
	"""
	A listener handles tweets are the received from the stream.
	This is a basic listener that just prints received tweets to stdout.
	"""

	def on_data(self, data):
		data  = json.loads(data)
		#print(data['text'])
		try:
			conn.execute("SELECT idCapture,points FROM capture where user='"+data['user']['screen_name']+"'")
			row = conn.fetchone()
			userfound = 0
			while row is not None:
				userfound = 1
				points=row[1]
				id=row[0]
				row = conn.fetchone()
			if userfound == 0:
				conn.execute("""INSERT INTO capture (nickname,user,geoLocation,lang,followers,friends,description,photo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(data['user']['name'].encode('utf-8'),data['user']['screen_name'].encode('utf-8'),data['user']['location'].encode('utf-8'),data['user']['lang'],data['user']['followers_count'],data['user']['friends_count'],data['user']['description'].encode('utf-8'),data['user']['profile_image_url']))
				db.commit()
			if userfound == 1:
				conn.execute("""UPDATE capture set followers=%s, friends=%s, points=%s, description=%s, photo=%s where idCapture=%s""", (data['user']['followers_count'],data['user']['friends_count'],points+1,data['user']['description'].encode('utf-8'),data['user']['profile_image_url'],id))
				db.commit()
		except:
			db.rollback()
		return True

	def on_error(self, status):
		return False

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(track=search_strings)

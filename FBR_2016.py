#!/bin/env python

#-----------------------------------------------------------------------
# twitter-authorize:
#  - step through the process of creating and authorization a
#    Twitter application.
#-----------------------------------------------------------------------

from twitter import *
import random
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=
consumer_secret=

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_key=
access_secret=

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter( auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

# Get a particular friend's timeline and a random number
number = random.randint(1, 15)
i= 0
kanye = twitter.statuses.user_timeline(screen_name = "kanyewest", count = 5)
for status in kanye:
	i= i +1	
	if i == number:
		quote= "%s" % (status["text"].encode("ascii", "ignore"))
trump = twitter.statuses.user_timeline(screen_name = "realDonaldTrump", count = 5)
for status in trump:
	i= i + 1
	if i == number:	
		quote= "%s" % (status["text"].encode("ascii", "ignore"))		
hoppus = twitter.statuses.user_timeline(screen_name = "markhoppus", count = 5)
for status in hoppus:
	i = i + 1
	if i == number:
		quote= "%s" % (status["text"].encode("ascii", "ignore"))

if len(quote) <= 131:
	post= quote + " #FBR2016"
else:
	post= quote

results = twitter.statuses.update(status = post)

print post
exit()

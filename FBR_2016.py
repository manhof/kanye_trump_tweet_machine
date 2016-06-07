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
consumer_key="jwin7Xc3SVaPqSZJ3PusrZc9n"
consumer_secret="4Cx4nsvGcL0KBi9XMFeqhl19f5YQwDSudZSOFP77zx86TqTJH1"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_key="740221558182973440-Jh0cIOKxMSCBDwlIpWZMzwTOazIkB6b"
access_secret="g0Dgs8pn1PCg1J6nHtWIHyDftAtt0kJgWqpVPBAdw4rLp"

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter( auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

# Get a particular friend's timeline and a random number
number = random.randint(1, 40)
i= 0
kanye = twitter.statuses.user_timeline(screen_name = "kanyewest", count = 20)
for status in kanye:
	i= i +1	
	if i == number:
		quote= "%s" % (status["text"].encode("ascii", "ignore"))
trump = twitter.statuses.user_timeline(screen_name = "realDonaldTrump", count = 20)
for status in trump:
	i= i + 1
	if i == number:	
		quote= "%s" % (status["text"].encode("ascii", "ignore"))		

if len(quote) <= 131:
	post= quote + " #FBR2016"
else:
	post= quote

results = twitter.statuses.update(status = post)

print post
exit()

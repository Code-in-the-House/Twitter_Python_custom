#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
query = twitter.search.tweets(q = "#at", lang= "tr", result_type="recent",count="150" )

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
ths = open("sonuc.txt", "w")


for result in query["statuses"]:
	print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
	ths.write('result["created_at"]')

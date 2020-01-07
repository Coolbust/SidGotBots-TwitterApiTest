import tweepy

# Code to Authenticate to Twiiter
auth = tweepy.OAuthHandler("Your_Handler")
auth.set_access_token("Your_Token")

# Create API object
api = tweepy.API(auth)

# Create a tweet
try:
    api.verify_credentials()
    print("Auth OK")
except:
    print("Error during auth")


try:
   # api.update_status("Auto Test Update 02: Lemme get a test")
    # print("Update succesful")
    print("test")
   #Print my followers
    print(api.followers(api.me()))
except:
    print("Update fail")


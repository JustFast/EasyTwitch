# EasyTwitch
This is a repository to make using the twitch IRC easier to use. It can shorten your code by a lot and allows you to view messages and send messages! Expect updates in the future this is my first python package!

EXAMPLE:

```py
from EasyTwitch import Twich

conn = Twich.connection("oauthToken", "TwitchUsername") #Make a connection to twitch go to https://twitchapps.com/tmi/ to get an oauth token

conn.join("#streamer") #Join a streamer who is currently streaming

conn.sendMSG("My message") #Send a message in the chat

conn.log() #Continuiously print out the twitch chat NOTE: This is a stopping function so BEWARE```


HOW TO INSTALL:

Go to your prefered place where you would like to use this package and clone the master directory into it. After doing that you should have a file that is your prefered program directory and inside the file there will be a file called EasyTwitch. Now all you need to do is follow the example!!

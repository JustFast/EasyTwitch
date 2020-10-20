# EasyTwitch
This is a repository to make using the twitch IRC easier to use. It can shorten your code by a lot and allows you to view messages and send messages! Expect updates in the future this is my first python package!

# DOCUMENTATION:

|Item                            | Type   | Disc.                                                     |
| -------------------------------|:------:|----------------------------------------------------------:|
|Connection(oauth, username)     |class   |Make a new connection to the Twitch server.                |
|Connection.join(#streamer)      |function|Join a Twitch streamer.                                    |
|Connection.log(file)            |function|Print out the Twitch chat (file logging is optional).      |
|Connection.sendMSG(message)     |function|Send a message to the selected Twitch streamer.            |


## HOW TO INSTALL:

Just run:
```
pip install EasyTwitch
```
After that you're set to go!! You can also view the Pypi at https://pypi.org/project/EasyTwitch/.

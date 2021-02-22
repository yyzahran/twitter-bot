# twitter-bot
Bot that tweets lyrics of Radiohead everyday


The bot is made using tweepy and I am using two types os schdeuling (but actively running on of them)

`TwitterBot_scheduled_cronjob.py` runs the bot locally using crontab, while `TwitterBot_scheduled.py` runs the bot using the schedule library every day, to do so I had to keep it running 24/7 on my machine, maybe I will look for a scheduler or a deployer to keep the file running all the time. At the moment, the cronjob seems to be doing the trick.



# twitter-bot
Bot that tweets lyrics of Radiohead everyday, the account is: https://twitter.com/radiohead_bot_

![radiohead](https://i.ibb.co/k8sJ3Fd/Screen-Shot-2021-02-21-at-8-57-31-PM.png)

The bot is made using tweepy and I am using two types os schdeuling (but actively running on of them):
- `TwitterBot_scheduled_cronjob.py` runs the bot locally using crontab.
- `TwitterBot_scheduled.py` runs the bot using the schedule library every day, to do so I had to keep it running 24/7 on my machine.

The tweets are taken from `radioheadLyrics.txt`, maybe I will look into getting parsed lyrics lines instead of having them 'hardcoded' in the reposiroty.

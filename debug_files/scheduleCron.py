from crontab import CronTab

my_cron = CronTab(user='')

for job in my_cron:
    print(job)
from crontab import CronTab
cron = CronTab(user = True)
job = cron.new(command = 'python3 /home/khoa/Documents/Test/Crontab/example.py', comment = 'test')
job.minute.every(1)
cron.write()

# for job in cron:
# 	print(job)
# 	cron.remove(job)
# 	cron.write()

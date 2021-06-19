from crontab import CronTab

cron = CronTab(user='root')
job = cron.new(command='D://data_pipeline//run_datapipeline.sh')
job.minute.on(0)
job.hour.on(1)

for item in cron:
    print(item)

cron.write()
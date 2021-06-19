# Data Engineering Technical Test
## Section 1: Data Pipelines

### Overview of folder architecture

    ├───data_pipeline
        ├───data
        │   ├───original
        │   └───processed
        └───pkg
        │   ├───common
        │       └───common_config.py
        │       └───setup_logger.py
        │   └───data_pipeline
        │       └───constants.py
        │       └───preprocess.py
        └───app.py
        └───cronjob.py
        └───requirements.txt
        └───installation.sh
        └───run_datapipeline.sh

### Getting Started
- Clone the repo and save it into to any location you prefer
- Assuming you store your repo right beneath D: drive
- Using gitbash or ubuntu terminal run the shellscript "installation.sh" to install the python libraries (For Example: run command "./data_pipeline/installation.sh" if your terminal is currently located at D: drive)
- Under ubuntu terminal, create a cron job for the project using "cronjob.py".
- Under assumption of the data file will be available at 1am everyday and store into "data/original" folder, 
        -   inside "cronjob.py" run the "app.py" file every 1am using cron expression "0 1 * * *"
        -   for the command inside "cronjob.py" set the <path> according to where you store your repo


### Notes
- "setup_logger.py" uses rotating logger that creates a new log file whenever the old file exceeds 10MB
- "preprocess.py" is meant to clean the Excel files into the appropriate format
        - add-on "price" have another new column "converted_price" that rounds up the "price" to 2 decimal place
- "app.py" is the main file to run the sub-folder ".py" files that utilises "main" function
- "cron" is utilised instead of Apache Airflow because since it only requires a single job it would be easily maintained and monitored.
        - Additionally, I failed to setup Apache Airflow locally through Docker and installing it directly into Window Subsystem for Linux, hence this would be the main reason why I use "cron".
        - I am aware that Airflow provide monitoring system and have feature that send alert to user. Moreover, providing an indepth outlook of the upstream and downstream pipelines.


## Section 2: Databases
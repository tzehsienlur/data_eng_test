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

## Section 3: System Design
![System Design](./system_design/system_design.png)

### Information
- The company also has a separate web application which provides a stream of images using a Kafka stream.
- The company’s software engineers have already some code written to process the images.
- The company would like to save processed images for a minimum of 7 days for archival purposes.
- Ideally, the company would also want to be able to have some Business Intelligence (BI) on key statistics including number and type of images processed, and by which customers.
### Assumption
- Company use Oracle SQL as a database to act as a data source.

### Cloud Tools
- Apache Kafka is used as a streaming engine that extract real-time data from the web application.
- Apache Airflow is used to automate the users tasks and manage the entire data pipeline. Moreover, providing alert to company's employee if failure of tasks.
- Amazon S3 meant to store the data into images or excel files and could be used to archive files.
        - As segregation of projects is using buckets, user can create a folder to archive images with the images name "YYYYMMDD_imagename"
- Amazon Redshift act as a data warehouse that store the data from the data lake (Amazon S3)
        - Can be utilised by company employees to provide data insights, reporting and data mining.

### Notes
- Above System Design image cannot be viewed, access "system_design/system_design.png"

## Section 4: Charts and APIs

### Overview of folder architecture
    ├───data_visualisation
        └───app.py
        └───data_visualisation.py
        └───preprocess_json.py
        └───requirements.txt
        └───installation.sh

### Getting Started
- Clone the repo and save it into to any location you prefer
- Assuming you store your repo right beneath D: drive
- Using gitbash or ubuntu terminal run the shellscript "installation.sh" to install the python libraries
- Run the entire python program using "python app.py"

### Notes
- "preprocess_json.py" is meant to clean the json data and produce it in a format that can be used for plotting graph
- "data_visualisation.py" is meant to plot the graphs and can be used as a package that showcase various types of graph
- "app.py" is the main file that combines "preprocess_json.py" and "data_visualisation.py" methods

## Section 5: Machine Learning

### Overview of folder architecture
    ├───machine_learning
        └───app.py
        └───create_model.py
        └───requirements.txt
        └───installation.sh
        
### Getting Started
- Clone the repo and save it into to any location you prefer
- Assuming you store your repo right beneath D: drive
- Using gitbash or ubuntu terminal run the shellscript "installation.sh" to install the python libraries
- Load the model "python app.py"
- "create_model.py" is meant to create model only.

### Information
- XGBoost model is used because is utilises extreme gradient boosting which improve model performance and computation speed
- Accuracy = 19% and Root Mean-squared Error = 1.935870
- After analysing the data, the multiple features that is utilised to gauge the buying price is ambiguous as same feature values is applied to a different buying price
- However, if given more time I could plot more graphs and determine the unique points and research further to determine the potential of the model accuracy.


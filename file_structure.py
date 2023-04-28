
import os

# define the directory path for the project
project_dir = "Time_Series_Analysis_Dashboard"

# create the project directory
os.mkdir(project_dir)

# create the data directory and subdirectories
data_dir = os.path.join(project_dir, "data")
os.mkdir(data_dir)

# create subdirectories for different data sources
sensor_data_dir = os.path.join(data_dir, "sensor_data")
os.mkdir(sensor_data_dir)

stock_data_dir = os.path.join(data_dir, "stock_data")
os.mkdir(stock_data_dir)

social_data_dir = os.path.join(data_dir, "social_data")
os.mkdir(social_data_dir)

web_traffic_dir = os.path.join(data_dir, "web_traffic")
os.mkdir(web_traffic_dir)

# create empty files for each subdirectory
sensor_data_file = os.path.join(sensor_data_dir, "sensor_data.csv")
open(sensor_data_file, 'w').close()

stock_data_file = os.path.join(stock_data_dir, "stock_data.csv")
open(stock_data_file, 'w').close()

social_data_file = os.path.join(social_data_dir, "social_data.csv")
open(social_data_file, 'w').close()

web_traffic_file = os.path.join(web_traffic_dir, "web_traffic.csv")
open(web_traffic_file, 'w').close()

# create the AWS directory and subdirectories
aws_dir = os.path.join(project_dir, "aws")
os.mkdir(aws_dir)

redshift_dir = os.path.join(aws_dir, "redshift")
os.mkdir(redshift_dir)

s3_dir = os.path.join(aws_dir, "s3")
os.mkdir(s3_dir)

# create empty files for each AWS subdirectory
redshift_file = os.path.join(redshift_dir, "redshift.txt")
open(redshift_file, 'w').close()

s3_file = os.path.join(s3_dir, "s3.txt")
open(s3_file, 'w').close()

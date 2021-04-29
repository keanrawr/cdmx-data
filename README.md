# About the project

This is a fun project to create some data pipelines for the [Mexico City Data Portal](https://datos.cdmx.gob.mx/pages/home/) using the available APIs.

This project is being archived on 2021-04-28, due to the Mexico City data API no longer existing as it was developed for this repo.

# What I learned

For this project I used:
- boto3 client to save the API output to s3
- aws lambda to execute the pipeline every hour
- aws IAM roles and JSON policies
- The Mexico City API for _metrobus_ data

# How to use

First you need to install the required python modules specified in `requirements.txt`. After that you need to set up the `BUCKET_NAME` environment variable in a `.env` file.
Depending on the way you have setup `boto3` you might want to add the necessary environment variables or use the aws CLI to manage your default profile. For more information check out the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

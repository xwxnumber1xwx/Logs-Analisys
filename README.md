## Logs Analysis Project - Udacity Full Stack Web Developer Nanodegree

#### DESCRIPTION
For this project, my task was to create a reporting tool that prints out reports( in plain text) based on the data in the given database. This reporting tool is a Python program using the `psycopg2` module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

#### RUNNING THE PROGRAM
1. To get started, I recommend the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer. You can download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.
Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login.

2. Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.

3. Load the database using `psql -d news -f newsdata.sql`.

4. Connect to the database using `psql -d news`.

5. Create the Views given below. Then exit `psql`.

6. Now execute the Python file - `python logs_analysis.py`.

7. Choose one SQL query and see the result


#### PROJECT REQUIREMENTS
Reporting tool should answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Project follows good SQL coding practices: Each question should be answered with a single database query.
The code is error free and conforms to the PEP8 style recommendations.
The code presents its output in clearly formatted plain text.

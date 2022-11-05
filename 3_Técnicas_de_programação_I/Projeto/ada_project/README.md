# ada_project

Repository for the essential files for the final project of the Programming Techniques course - Ada tech. The practical objective of this project is to develop a system for storing, maintaining and manipulating databases using pandas.

In this work, we want to create a system for organizing product sales data in a company. There are already two services that implement different blocks of a complete project.

## Part 1 - Data Acquisition
Initially, a web-server created in Javascript will serve as an entry point for the data, simulating the weekly acquisition of all products sold by the company. To run the server, you need to install [NodeJS](https://nodejs.org/en/). With the repository folder already cloned, you must use the following commands to install the packages.

`npm init`
`npm install`

Then just run the `node web-server.js` command. To request the data in JSON format, just use a GET request to localhost:3000/api/ep1

## Part 2 - Data Storage and Management

This is the necessary stage of the project. The student must be able to create a system that can update tables in the face of new data. Also, the formatting of dataframes must be in accordance with the project's specifications, so that communication with the dashboard can be stablished immediately and correctly, without any further adaptation. 

## Part 3 - Data visualization

Last step of the project pipeline. Using the aforementioned tables, this script generates a dashboard containing essential info for data visualization. The script uses the `streamlit` framework. In order to run locally, the student should install the package (either using `pip install streamlit` or `conda install streamlit`). To run the application, just type `streamlit run app.py` and access localhost:8501 to view the dashboard. If the second part of the project is done correctly, the dashboard should work like the image below.

![example](https://github.com/mdrs-thiago/ada_project/blob/492aafd0f66fdb37fec04a4e72c085ca7aba87f1/ada_project_dashboard.png)

from github import Github
import os
import time

def updateGit():
    while True:
        # Path to the CSV file
        csv_file_path = "E:/IOT projects/main application - LOCAL/check_in_data.csv"

        # Read the content of the CSV file
        with open(csv_file_path, 'r') as file:
            content = file.read()

        writing_path="E:/IOT projects/updated fiverr/dataset/check_in_data.csv"
        with open(writing_path, 'w') as file:
            file.write(content)
        


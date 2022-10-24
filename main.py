import pandas as pd
import csv

# Creating a new output csv file
with open("output.csv", 'w') as new_file:
    # creating a csv writer object
    csvwriter = csv.writer(new_file)
    fields = ['Sr No', 'Product Name', 'Flipkart Link - Clr 1', 'link']
    csvwriter.writerow(fields)

# Reading the Flipkart.csv file
with open("Flipkart.csv", mode='r') as file:
    csvfile = csv.reader(file)
    a = 0
    for rows in csvfile:
        a += 1
        if a > 1:           # Omitting the fields row
            # writing to csv file
            with open("output.csv", 'a') as new_file:
                # creating a csv writer object
                csvwriter = csv.writer(new_file)
                datarows = [rows[0], [rows[1], 'Flipkart Link - Clr 1', rows[2].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - Clr 2', rows[3].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - Clr 3', rows[4].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - Clr 4', rows[5].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - Clr 5', rows[6].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - RAM1', rows[7].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - RAM2', rows[8].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - RAM3', rows[9].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - RAM4', rows[10].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - Storage 1', rows[11].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - Storage 2', rows[12].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - Storage 3', rows[13].split("&lid=")[0]],
                            [rows[0], rows[1], 'Flipkart Link - Storage 4', rows[14].split("&lid=")[0]],
                            ]
                csvwriter.writerows(datarows)

data = pd.read_csv('output.csv')
# Droping the rows having the link value, NaN
data = data.dropna(subset=['link'])
# Dropping the duplicate rows
data = data.drop_duplicates(subset='link', keep="first")
data.to_csv('output.csv')

# Create List of RssFeeds Related to HT
jsonFiles = {
    1: {
        "date" : "20230208",
        "file" : "articles_20230208.json"
    },
    2: {
        "date" : "20230214",
        "file" : "articles_20230214.json"
    },
    3: {
        "date" : "20230215",
        "file" : "articles_20230215.json"
    },
    4: {
        "date" : "20230216",
        "file" : "articles_20230216.json"
    },
    5: {
        "date" : "20230217",
        "file" : "articles_20230217.json"
    },
    6: {
        "date" : "20230220",
        "file" : "articles_20230220.json"
    },
    7: {
            "date" : "20230221",
            "file" : "articles_20230221.json"
        },
    8: {
            "date" : "20230222",
            "file" : "articles_20230222.json"
        }
}
# Import JSON
import json
# Import MySql Connector
import mysql.connector
# Create MySQL Connection
cnx = mysql.connector.connect(user="python",password="@Clermont#2022$Casa",host="localhost",database="Articles")
cursor = cnx.cursor()
for file_id, file_info in jsonFiles.items():
    # Opening JSON file
    f = open(file_info['file'])
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    # Closing file
    f.close()
    # Loop through JSON File and add records to MySql
    for (k,v) in data.items():
        if k != 'Date':
            feed = v;
            for (i,value) in feed.items():
                if i == 'Subject':
                    subject = value

                if i != 'Subject' and i != 'Total Entries':
                    cursor.execute("INSERT INTO human_trafficking(topic,title,summary,url,date) VALUES (%s,%s,%s,%s,%s)",(subject, value['Title'], value['Summary'], value['Url'], value['Published']))
                    cnx.commit()

cursor.close()
cnx.close()
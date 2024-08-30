# This is a sample Python script.
# Create List of RssFeeds Related to HT
htRssFeeds = {
    1: {
        "alert" : "High School",
        "url" : "https://www.google.com/alerts/feeds/16496866187079825104/10015054984309650769"
    },
    2: {
        "alert": "Professional Sports",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/177254420229006693"
    },
    3: {
        "alert": "United States",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/12042937520084858969"
    },
    4: {
        "alert": "Africa",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/7028742816944007166"
    },
    5: {
        "alert": "Athletes",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/5673089392778127383"
    },
    6: {
        "alert": "Baseball",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/15423993847814923537"
    },
    7: {
        "alert": "Basketball",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/17400876314796697811"
    },
    8: {
        "alert": "Bitcoin",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/10728784591624863085"
    },
    9: {
        "alert": "Business",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/7980372463467550838"
    },
    10: {
        "alert": "Cheerleading",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/5673089392778128469"
    },
    11:{
        "alert": "Coach",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/9975456005604264084"
    },
    12: {
        "alert": "College Athletics",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/11592573615209202299"
    },
    13: {
        "alert": "Crypto",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/13247341685643952864"
    },
    14: {
        "alert": "Emoji",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/7112427900244901320"
    },
    15: {
        "alert": "Europe",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/9304247370931991164"
    },
    16: {
        "alert": "Facebook",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/11943188010964183349"
    },
    17: {
        "alert": "FIFA",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/8053622435815825117"
    },
    18: {
        "alert": "Football",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/7764202854300076174"
    },
    19: {
        "alert": "Instagram",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/15946377152558019828"
    },
    20: {
        "alert": "NBA",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/8460616856243124453"
    },
    21: {
        "alert": "NFL",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/4348394718398692573"
    },
    22: {
        "alert": "Snapchat",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/116618495033373067"
    },
    23: {
        "alert": "Soccer",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/8299378102514302573"
    },
    24: {
        "alert": "South America",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/4243396859131013206"
    },
    25: {
        "alert": "Sporting Event",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/15946866315839667724"
    },
    26: {
        "alert": "Sports",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/10855062532748619587"
    },
    27: {
        "alert": "TicTok",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/2869710621243659808"
    },
    28: {
        "alert": "Twitter",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/8933008975810794041"
    },
    29: {
        "alert": "University",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/7166803726064096450"
    },
    30: {
        "alert": "Modern Day Slavery",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/1174144090295073212"
    },
    31: {
        "alert": "Child Exploitation",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/10420291298657330565"
    },
    32: {
        "alert": "Fetanyl",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/6112558385753251016"
    },
    33: {
        "alert": "Human Trafficking",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/6315576169629939994"
    },
    34: {
        "alert": "Human Trafficking Task Force",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/13002961917882089963"
    },
    35: {
        "alert": "Human Smuggling",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/5888193635890171951"
    },
    36: {
        "alert": "Labor Trafficking",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/17356345081663601615"
    },
    37: {
        "alert": "Sex Trafficking",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/16031384764924176744"
    },
    38: {
        "alert": "Smuggling Southern Border",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/10142943357609642176"
    },
    39: {
        "alert": "Sports Trafficking",
        "url": "https://www.google.com/alerts/feeds/16496866187079825104/817387510601145395"
    }
}
# Import Date
from datetime import date
# Import RssFeed parser
import feedparser
# Import JSON
#import json
# Import Beautifulsoup to clean up HTML tags
from bs4 import BeautifulSoup
# Import MySql Connector
import mysql.connector
# Print Current Date & Time
today = date.today()
print(today)
total = 0
#create an empty dictionary
data = {
    "Date" : str(today)
}
# Create MySQL Connection
cnx = mysql.connector.connect(user="python",password="@Clermont#2022$Casa",host="localhost",database="Articles")
cursor = cnx.cursor()

for rss_id, rss_info in htRssFeeds.items():
    # Get rss feed
    NewsFeed = feedparser.parse(rss_info['url'])
    # Check which feed has news, if so print it
    if len(NewsFeed['entries']) > 0:
        data[rss_id] = {
            "Subject" : rss_info['alert'],
            "Total Entries" : len(NewsFeed['entries'])
        }
        for i, item in enumerate(NewsFeed['entries']):
            summary = BeautifulSoup(item.summary, "lxml").text
            summary = summary.encode("ascii", "ignore")
            summary = summary.decode()
            entry = {
                "Title" : BeautifulSoup(item.title, "lxml").text,
                "Url" : item.link,
                "Published" : item.published,
                "Summary" : summary
            }
            data[rss_id][i] = entry
            cursor.execute("INSERT INTO human_trafficking(topic,title,summary,url,date) VALUES (%s,%s,%s,%s,%s)",(rss_info['alert'], BeautifulSoup(item.title, "lxml").text, summary, item.link, item.published))
            cnx.commit()
            cursor.execute("INSERT INTO articles_article(topic,title,summary,url,date,featured, created_at) VALUES (%s,%s,%s,%s,%s,%s,%s)", (rss_info['alert'], BeautifulSoup(item.title, "lxml").text, summary, item.link, item.published,0,str(today)))
            cnx.commit()
        total = total + len(NewsFeed['entries'])
        print(str(rss_id) + " - " + rss_info['alert'] + " - " + str(len(NewsFeed['entries'])))
cursor.close()
cnx.close()
#Open a file for writing
#with open("articles_" + str(today).replace("-","") + ".json","w") as outfile:
    # Write the dictionary to a data file as a JSON Object
 #   json.dump(data,outfile)

print("Total articles today - " + str(today) + " : " + str(total))
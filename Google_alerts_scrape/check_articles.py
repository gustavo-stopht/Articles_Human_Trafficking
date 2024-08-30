
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Connect to the database
db = mysql.connector.connect(user="python",password="@Clermont#2022$Casa",host="localhost",database="Articles")
cursor = db.cursor()

# Get the list of links from the database
cursor.execute(
    "SELECT id, url FROM articles_article WHERE created_at >= CURDATE() ORDER BY created_at DESC"
)
links = cursor.fetchall()

# Loop through the links
for link in links:
    # Get the HTML page for the link
    page = requests.get(link[1])

    # Create a BeautifulSoup object for the HTML page
    soup = BeautifulSoup(page.content, "html.parser")

    # Get the text from the HTML page
    text = soup.get_text()

    # Define the list of words to be checked
    words = ["group", "of", "words"]

    # Check if the list of words is present in the text
    if all(word in text for word in words):
        # Update the featured column to 1
        cursor.execute(
            "UPDATE articles_article SET featured = 1 WHERE id = %s",
            (link[0],),
        )
        db.commit()

# Close the database connection
db.close()

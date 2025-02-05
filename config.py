# config.py
# This file contains the configuration for the web crawler.
#https://www.theknot.com/marketplace/wedding-reception-venues-atlanta-ga"

BASE_URL = "https://www.theknot.com/marketplace/wedding-reception-venues-albany-ny"
CSS_SELECTOR = "[class^='info-container']"

REQUIRED_KEYS = [
    "name",
    "price",
    "location",
    "capacity",
    "rating",
    "reviews",
    "description",
]

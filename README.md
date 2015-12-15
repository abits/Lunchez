# Lunchez - A lunch bot for Slack

This is **Lunchez**, a bot for Slack written in Python. Lunchez has one
job: provide a list of restaurants and post it on Slack. Slack users
can then vote on the restaurants with the help of reactions.

![Lunchez](https://github.com/frank-und-freunde/Lunchez/blob/master/lunchez.png)

##Dependencies

* Python 3
* requests
* slackweb
* bs4
* datetime

## Setup

Create slackkeys.py

    slackKeys = {
      'TEAM_NAME': 'https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxx'
    }

Create restaurantlist.py

    weeklySpots = [
      {
        # Required:
        "location": "https://www.google.com/maps/xxxxxxx/",  # Google Maps Link
        "restaurant": "Example Restaurant",                  # Name of the restaurant
        "number": "octocat",                                 # Slack emoji name. Will turn into :octocat:
        # Optional:
        "menu": "http://restaurant.com/weeklymenu"           # Link to the restaurant's weekly menu
      }
    ]
    
    staticSpots = [
      {
        # Required:
        "location": "https://www.google.com/maps/xxxxxxx/",  # Google Maps Link
        "restaurant": "Example Restaurant",                  # Name of the restaurant
        "number": "octocat",                                 # Slack emoji name. Will turn into :octocat:
        # Optional:
        "menu": "http://restaurant.com/weeklymenu",          # Link to the restaurant's menu
        "credit": "yes",                                     # Accepts non-cash payments
        "dayoff": "Monday",                                  # One day off during the week
        "vacationFrom": "2016-01-01",                        # Beginning of vacation
        "vacationTo": "2016-10-10"                           # End of vacation
      }
    ]

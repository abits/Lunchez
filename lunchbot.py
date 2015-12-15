# Lunch-Bot 2.0

import slackweb
# Additional files
import functions
import slackkeys
import restaurantlist
# import preview

slack = slackweb.Slack(url=slackkeys.slackKeys['codinggoat'])

bot_text = 'This is a sample text. Please replace me before you use this bot.'

weekly_content = functions.restaurants(restaurantlist.weeklySpots)
static_content = functions.restaurants(restaurantlist.staticSpots)
additional_content = ":new: I want to go somewhere else (please suggest an alternative)\n:x: I don't want to/I brought my own lunch to work"
legend_content = "<https://127.0.0.1|Txt> `menu`\n:octocat: `google maps link`\n:credit_card: `card payment possible`"

weekly = {"title": "Restaurants (with an alternating menu)", "value": weekly_content, "short": True}
static = {"title": "Restaurants (with a fixed menu)", "value": static_content, "short": True}
additional = {"title": "Additional Options", "value": additional_content, "short": False}
legend = {"title": "Legend", "value": legend_content, "short": True}
pretext = ""  # "*Suggestions:*" + preview.firstToday + preview.secondToday + preview.thirdToday

attachments = []
attachment = {"pretext": pretext, "color": "orange", "fields": [weekly, static, additional, legend], "mrkdwn_in": ["fields", "pretext"]}
attachments.append(attachment)

slack.notify(text=bot_text, channel="#general", username="Lunchez", icon_emoji=":fork_and_knife:", attachments=attachments)

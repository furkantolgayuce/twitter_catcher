import sys
import os
sys.path.append(os.path.join(sys.path[0], '../'))
from twitter_catcher.twitter_catcher import twitter_catcher

bot = twitter_catcher()
api = bot.login()
search = bot.search(api,"#pazartesi",200)
df = bot.dataframe(search)
bot.to_sql(df)
bot.to_excel(df)

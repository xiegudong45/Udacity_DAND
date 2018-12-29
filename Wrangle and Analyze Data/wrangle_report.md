# Wrangle Act Report

Wrangling this data was very challenging and time-consuming as it requires me to gather, assess and clean the data before investigating them. I need to think of what kind of data is necessary and how to get new data based on existing information.

Gathering data is comparably the easiest of the three. However, it took some time when I tried to grab the data from Twitter API. Collecting data from API is far more different than transferring a CSV file into a data frame. I had to understand what data I was getting from the API once it was retrieved.

As there're a lot of quality issues and tidiness issues in these datasets, I listed all the problem I found and then solved them one by one. New problems will appear in the cleaning process. Some of them are easy to find, such as missing data, wrong data types while others are not. Not all the tweets listed in `twitter-archive-enhanced-2.csv` file is original tweets. Therefore, I needed to remove retweets when I cleaned the data.

Cleaning the data is always the most time-consuming part in wrangling data. It is common to find new problems when you started to clean them. For example, when I saw there's a 0 in `rating_denominator` column, I noticed that there're some value is not divisible by 10. I collect these weird data, searched the tweet page and found that these data were dates or some number which were irrelevant to rating score. So I had to go back and re-document the issue before going on to my original efforts.

Above all, I think I tried my best in this project and got a good result.

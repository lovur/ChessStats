## Chess Statistics Tableau Dashboard

[Tableau Public](https://public.tableau.com/profile/logan.van.vuren#!/vizhome/ChessStudy/Ratingvs_AgeStory)

**Project description:** Inspired by the recent boom in chess players from the popularity of the Queen's Gambit on Netflix, I decided to see for myself what insights I could gather from data currently available from the FIDE, the international governing body for chess regulations and rankings. After parsing through this XML data using Python, I was able to view how players and countries related to each other in terms of chess rankings. 

**Skills:** 
* Data analysis
* Python
* XML
* Statistical insights

### 1. Rating vs. Age

Age seems to have a smaller role to play in the distribution of titles than I thought. Of course, lower titles tended to be younger audiences, but after 1750 the distribution is relatively flat. I included the average for both rating and age to show the data is skewed slightly right. This is probably a result of chess reaching a much more global audience through Netflix and therefore has a larger, younger playerbase. 

<img src="rating_vs_age.PNG?raw=true"/>

### 2. Top Players per Country

One pattern to notice here is the popularity of chess among Europe in comparison to the rest of the world. Even in countries with smaller populations than that of Russia, China, and India, there are many top players represented. I included parameter slide to see how this changes depending on how many top players we include on the map. Chess is definitely a global phenomenon!

<img src="top_players_per_country.PNG?raw=true"/>

### 3. Country Median vs. Max Ratings

The third visualization shows how median rating varies per country. This also shows how much higher rating the best players are compared to their own countries. Overall, most of the countries hover within 400 points of the average, and it should be interesting how chess's new popularity with the Queen's Gambit being released on Netflix may change this data in the near future.

<img src="country_median_vs_max_ratings.PNG?raw=true"/>

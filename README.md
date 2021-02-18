# Classify food desert status and predict food insecurity prevalence of areas in the US based on social media data

## Directory name
[food_desert_social_media](https://github.com/michen00/)
## Application
Food deserts — areas with poor access to healthy and affordable food — exist mostly in socioeconomically disadvantaged areas associated with poor diet and related health outcomes. Because food deserts may contribute to social disparities, there is growing interest in identifying places that are likely to be food deserts. [Prior research](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/cscw_fooddeserts.pdf) has used the food-related hashtags of geotagged Instagram posts to predict whether different areas are food deserts. Ostensibly, classification accuracy could be improved if the images and captions of each Instagram post or food-related Tweets were also incorporated into the dataset.
## Data
Twitter and Instagram APIs may provide access to food-related Instagram posts and tweets. [Food vocabulary lists](https://www.enchantedlearning.com/wordlist/food.shtml) have been useful in [prior research](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/cscw_fooddeserts.pdf) for topic modeling of text data and could be expanded. The [Food Environment Atlas](https://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads/) and the [Food Access Research Atlas](https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data/) contain information about food access and security at the county and census tract levels (respectively) based on 2010 and 2015 US Census data.
## Data gathered for project submission
* Geotagged Instagram and Twitter posts filtered for food words gathered via API (forthcoming)
* [Food words corpora](https://github.com/michen00/)
  * [DiscoverTheMenu](https://github.com/michen00/)
    * New York Public Library, *Discover The Menu.* 2017. Distributed by data.world. Accessed Feb. 10, 2021. [Online]. Available: https://data.world/data-society/discover-the-menu
  * [demonymic_adjectivals]()
    * EnglishClub.com. "Countries and Nationality Vocabulary." 1997. The EnglishClub Group. https://www.englishclub.com/vocabulary/world-countries-nationality.php (accessed Feb. 17, 2021).
    * Government Publishing Office Style Board. "U.S. Government Publishing Office Style Manual." Jan. 12, 2017. United States Government Publishing Office. https://www.govinfo.gov/content/pkg/GPO-STYLEMANUAL-2016/pdf/GPO-STYLEMANUAL-2016.pdf (accessed Feb. 17, 2021).
    * MyEnglishPages.com. "Nationalities, Countries and the People." 2021. MyEnglishPages.com. https://www.myenglishpages.com/site_php_files/vocabulary-lesson-countries-nationalities.php (accessed Feb. 17, 2021).
    * National Institutes of Health. "Racial and Ethnic Categories and Definitions for NIH Diversity Programs and for Other Reporting Purposes." Apr. 8, 2015. United States Department of Health and Human Services. https://grants.nih.gov/grants/guide/notice-files/not-od-15-089.html (accessed Feb. 17, 2021).
    * The Peoples of the World Foundation. "Indigenous Peoples of the World Listed by Names and Aliases (Ethnonyms)." 1999. PeoplesOfTheWorld.org. http://www.peoplesoftheworld.org/bypeople (accessed Feb. 17, 2021).
    * Wikipedia contributors. "List of adjectival and demonymic forms for countries and nations." Feb. 1, 2021. Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=List_of_adjectival_and_demonymic_forms_for_countries_and_nations&oldid=1004165249 (accessed Feb. 17, 2021).
    * Wikipedia contributors. "List of adjectival and demonymic forms of place names." Feb. 14, 2021. Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=List_of_adjectival_and_demonymic_forms_of_place_names&oldid=1006793392#Continents (accessed Feb. 17, 2021).
    * Wikipedia contributors. "List of states and territories of the United States." Feb. 2, 2021. Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=List_of_states_and_territories_of_the_United_States&oldid=1004472264 (accessed Feb. 17, 2021).
    * Wikipedia contributors. "List of United States cities by population." Jan. 29, 2021. Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=List_of_United_States_cities_by_population&oldid=1003478087 (accessed Feb. 17, 2021).
  * [enes](https://github.com/michen00/) (English-Spanish)
    * Lawlwess Spanish. "Spanish Food Vocabulary and Verbs - Lawless Spanish Lesson." 2020. https://www.lawlessspanish.com/vocabulary/food/ (accessed Feb. 11, 2021).
    * Lingolex. "Glossary of English-Spanish food words." https://www.lingolex.com/spanishfood/a-b.htm (accessed Feb. 11, 2021).
    * Wikibooks contributors. "Spanish/Vocabulary/Food." Sep. 29, 2020. Wikibooks, the Free Textbook Project. https://en.wikibooks.org/w/index.php?title=Spanish/Vocabulary/Food&oldid=3743870 (accessed Feb. 11, 2021).
    * US Institute of Languages. "Food Words in Spanish." 2019. LearnALanguage.com. https://www.learnalanguage.com/learn-spanish/spanish-words/food-I.php (accessed Feb. 11, 2021).
  * [food_vocab](https://github.com/michen00/)
    * Enchanted Learning. "Food Vocabulary Word List." 2009. EnchantedLearning.com. https://www.enchantedlearning.com/wordlist/food.shtml (accessed Feb. 10, 2021).
  * [foodbase](https://github.com/michen00/)
    * G. Popovski, B. K. Seljak, and T. Eftimov, "FoodBase corpus: A new resource of annotated food entitites," *Database,* vol. 2019, Nov. 4, 2019, doi: https://doi.org/10.1093/database/baz121.
  * [hashtag_research](https://github.com/michen00/)
    * M. C. Buckley. "A collection of the best Instagram food hashtags." Dec. 2, 2019. HangryWoman.com. https://hangrywoman.com/a-collection-of-the-best-instagram-food-hashtags/ (accessed Feb. 10, 2021).
    * Best-Hashtags. "Hashtags for #food on Instagram, Twitter, Facebook, Tumblr." Feb. 4, 2021. Best-Hashtags.com. https://best-hashtags.com/hashtag/food/ (accessed Feb. 10, 2021).
    * Top-Hashtags.com. "Hashtags for #food in 2021 to be popular and trending in Instagram, TikTok." 2021. Top-Hashtags. https://top-hashtags.com/hashtag/food/ (accessed Feb. 10, 2021).
  * [Large_US_grocers]()
    * FoodIndustry.com. "Who Are the Top 10 Grocers in the United States?" Nov. 2019. FoodIndustry.com. https://www.foodindustry.com/articles/top-10-grocers-in-the-united-states-2019/ (accessed Feb. 12, 2021).
    * FoodIndustry.com. "A List of the Top Ten Grocery Chains in the United States." Nov. 2020. FoodIndustry.com. https://www.foodindustry.com/articles/a-list-of-the-top-ten-grocery-chains-in-the-united-states/ (accessed Feb. 16, 2021).
  * [Large_US_restaurant_chains]()
    * O. Tarantino. "50 Largest Restaurant Chains in America." Aug. 26, 2020. Eat This, Not That! https://www.eatthis.com/largest-restaurant-chains-america/ (accessed Feb. 12, 2021).
  * [MenuStat](https://github.com/michen00/)
    * Department of Health and Mental Hygiene, *DOHMH MenuStat. V20200207.* 2020. Distributed by City of New York. Accessed Feb. 10, 2021. [Online]. Available: https://data.cityofnewyork.us/Health/DOHMH-MenuStat/qgc5-ecnb
  * [national_dishes]()
    * Wikipedia contributors. "National dish." Feb. 10, 2021. Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=National_dish&oldid=1005897722 (accessed Feb. 17, 2021).
  * [popular_brands]()
    * YouGov PLC. "The most popular food & snack brands in America." 2018. YouGov.com. https://today.yougov.com/ratings/food/popularity/food-snack-brands/all (accesssed Feb. 16, 2021).
  * [state_foods]()
    * Wikipedia contributors. "List of U.S. state foods." Feb. 1, 2021. Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=List_of_U.S._state_foods&oldid=1004266086 (accessed Feb. 17, 2021).
* US Census food access and security
  * [Food_Access_Research_Atlas](https://github.com/michen00/)
    * United States Department of Agriculture, *Food Access Research Atlas. V2017.05.18.* 2017. Distributed by Economic Research Service. Accessed Feb. 10, 2021. [Online]. Available: https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data/
  * [Food_Environment_Atlas](https://github.com/michen00/)
    * United States Department of Agriculture, *Food Environment Atlas. V2020.09.10.* 2020. Distributed by Economic Research Service. Accessed Feb. 10, 2021. [Online]. Available: https://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads/
* FoodData Central
 * United States Department of Agriculture, *FoodData Central. V2020.10.30.* 2020. Distributed by Agricultural Research service. Accessed Feb. 12, 2021. [Online]. Available: https://fdc.nal.usda.gov/download-datasets.html

## Related resources
* M. de Choudhury, S. Sharma, and E. Kiciman, "Characterizing dietary choices, nutrition, and language in food deserts via social media," in *Proc. 19th ACM Conf. Comput.-Supported Cooperative Work and Social Comput.,* San Francisco, California, USA, Feb. 27–Mar. 2, 2016, pp. 1157–1170. doi: https://doi.org/10.1145/2818048.2819956.
* M. J. Widener and W. Li, "Using geolocated Twitter data to monitor the prevalence of healthy and unhealthy food references across the US," *Appl. Geopgrahy,* vol. 54, pp. 189–197, Oct. 2014, doi: https://doi.org/10.1016/j.apgeog.2014.07.017.
* United States Federal Communincations Commission. "API Documentation for Developers." FCC.gov. https://geo.fcc.gov/api/census/#!/block/get_block_find (accessed Feb. 12, 2021).
* Federal Financial Institutions Examination Council. "FFIEC Online Census Data System." 2020. FFIEC.gov. https://www.ffiec.gov/census/default.aspx (accessed Feb. 12, 2021).

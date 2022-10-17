# kvanme01_proj2

[![Python application test with Github Actions](https://github.com/nogibjj/proj2_cltool/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/proj2_cltool/actions/workflows/main.yml)

For this project, I wanted to create an easy way to access an online database 
that is updated with some regularity as well as a method to easily query it
using keywords. I like to stay updated on current life science research, so 
I utilized the the 'Most Downloaded Articles' list on Elsevier found at 
https://www.journals.elsevier.com/journal-of-advanced-research/most-downloaded-articles .


![IMG_0013](https://user-images.githubusercontent.com/112578194/196303166-53a0492f-494d-4df3-9cef-ab2a93190336.jpg)

I used the beautifulsoup and pandas packages to scrape the dataset from the 
Elsevier website and format it in a dataframe. I then created a bash script to 
with a help functionality and the ability to call three functions. Function
get_data, called with ./main.sh run_scrape, scrapes the dataset from the 
website without printing it. Function print_df, called with ./main.sh run_scrape, 
scrapes the dataset from the website and prints it to the terminal. Function
run_search, called with ./ main.sh keyword_search, prompts the user for a 
keyword. If the keyword is in any of the article titles, the title of the article, 
its rank in the dataset, and the hyperlink to the article is printed to the 
terminal. 


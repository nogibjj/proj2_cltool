import pandas as pd
import requests
from bs4 import BeautifulSoup

# scrapes site for data, returns df
def get_data():
    website = "https://www.journals.elsevier.com/journal-of-advanced-research/most-downloaded-articles"
    website_url = requests.get(website).text
    soup = BeautifulSoup(website_url, "html.parser")

    # make a list of titles
    titles = []
    for title in soup.find("ul", class_="sc-9zxyh7-0 ffmPq"):
        titles.append(title.get_text())

    # make a list of hyperlinks
    hyper = []
    for link in soup.find("ul", class_="sc-9zxyh7-0 ffmPq").find_all("a", href=True):
        hyper.append(link["href"])

    # create a dataframe from the lists
    df = pd.DataFrame({"Title": titles, "Hyperlink": hyper})
    return df


# searches df for keyword input by user in CL, returns list with any matching values
def search_df(df, keyword):
    search = df[df["Title"].str.contains(keyword, case=False)]
    if df["Title"].str.contains(keyword, case=False).any():
        return search


def run_search(keyword):
    df = get_data()
    results = search_df(df, keyword)
    print(results)


def print_df():
    df = get_data()
    print(df)


# def test():
#    run_search("plant")


# test()

# Import statements.
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction import text
import datetime


def main():
    create_log('Main function starts executing')
    # my_stop_words contains default english stop words and extra stop words related to story.
    my_stop_words = text.ENGLISH_STOP_WORDS.union(
        ["gutenberg", "ebook", "online", "distributed", "transcriber", "etext", "note", "copyright", "start",
            "project", "end", "produced", "proofreading", "team", "http", "www", "pgdp", "net", "illustrated", ]
    )
    # Reading the dataset into stories_df
    create_log('Reading dataset starts.')
    stories_df = pd.read_csv('files/stories.csv')
    create_log('Reading dataset ends.')
    create_log('Creating a object of TfidfVectorizer with stopwords starts.')
    vectorizer = TfidfVectorizer(stop_words=my_stop_words)
    create_log('Creating a object of TfidfVectorizer with stopwords ends.')
    create_log('Running vectorizer.fit starts.')
    vectorizer.fit(stories_df["content"])
    create_log('Running vectorizer.fit ends.')
    create_log('Running vectorizer.transform starts.')
    X_vector = vectorizer.transform(stories_df["content"])
    create_log('Running vectorizer.transform ends.')
    create_log('Running cosine_similarity starts.')
    similarity_matrix = cosine_similarity(X_vector)
    create_log('Running cosine_similarity ends.')
    create_log('Main function ends executing\n')
    

def create_log(data):
    global log
    log = open("logs.txt", "a")
    log.write(str(datetime.datetime.now()) + "\t" + data + "\n")


main()

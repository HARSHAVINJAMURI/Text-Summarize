from flask import Flask, render_template, request
import bs4 as bs
import urllib.request as url
import re
import nltk
import heapq
import os
from string import punctuation
# import nltk
# nltk.download('all')

# Download required nltk packages
nltk.download("punkt")
nltk.download("stopwords")
nltk.download('averaged_perceptron_tagger') 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)

def summarize_article(article_url):
    try:
        # Scrape the article
        scraped_data = url.urlopen(article_url)
        article = scraped_data.read()
        parsed_article = bs.BeautifulSoup(article, "lxml")
        paragraphs = parsed_article.find_all("p")

        article_text = ""
        for p in paragraphs:
            article_text += p.text

        # Clean text
        article_text = re.sub(r"\s+", " ", article_text)
        formatted_article_text = re.sub("[^a-zA-Z]", " ", article_text)
        formatted_article_text = re.sub(r"\s+", " ", formatted_article_text)

        # Tokenization
        sentence_list = sent_tokenize(article_text)
        stop_words = set(stopwords.words("english"))

        # Calculate word frequency
        word_frequencies = {}
        for word in word_tokenize(formatted_article_text):
            if word.lower() not in stop_words and word not in punctuation:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1

        # Normalize frequency
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] /= max_frequency

        # Score sentences
        sentence_scores = {}
        for sent in sentence_list:
            for word in word_tokenize(sent.lower()):
                if word in word_frequencies:
                    if len(sent.split(" ")) < 30:  # Limit sentence length
                        sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

        # Get the top 7 sentences for summary
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = " ".join(summary_sentences)

        return summary

    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        article_url = request.form["article_url"]
        summary = summarize_article(article_url)
        return render_template("summary.html", article_url=article_url, summary=summary)

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)

# Article Summarizer  

A Flask-based web application that scrapes an article from a given URL and generates a concise summary using NLP techniques.  

## Features  
✅ Extracts text content from any article URL  
✅ Cleans and processes text for summarization  
✅ Uses NLP techniques like tokenization, stopword removal, and frequency-based scoring  
✅ Web-based interface for input and output  
✅ Deployed with configurable port support  

## Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/article-summarizer.git
cd article-summarizer
```
2. Set Up a Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the Application
```
python app.py
  ```
By default, the app runs on http://localhost:5000.

# Usage
1. Open the web app in a browser.
2. Enter a valid article URL.
3. Click submit to generate a summary.
# Environment Variables
To configure the application, you can set the following environment variables:  

| Variable | Description | Default |
|----------|------------|---------|
| `PORT`   | The port number to run the app | `5000` |
# Deployment
For deployment on Render, Heroku, or any cloud platform, ensure the PORT environment variable is set.

## Tech Stack
- Python (Flask)
- BeautifulSoup (Web Scraping)
- NLTK (Natural Language Processing)
  
# Contributing
- Feel free to contribute! Open an issue or submit a pull request.

# License
This project is licensed under the MIT License.

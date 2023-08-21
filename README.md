# NLPApp

NLPApp is a graphical user interface (GUI) application built using Python's Tkinter library. It provides users with various natural language processing (NLP) functionalities, including sentiment analysis, named entity recognition (NER), and emotion prediction. The application uses the ParallelDots API for NLP tasks and stores user data in a JSON file.

Link for API - https://komprehend.io/api-wrappers
## Features

- User Registration and Login: Users can register with their name, email, and password. Registered users can log in to access the application's features.

- Sentiment Analysis: Users can perform sentiment analysis on provided text. The application uses the ParallelDots API to analyze and determine the sentiment of the input text.

- Named Entity Recognition (NER): The application can recognize named entities in the provided text using the ParallelDots API for NER analysis.

- Emotion Prediction: Users can predict emotions associated with provided text using the ParallelDots API.

- User Interface: The application has a clean and user-friendly interface built using Tkinter, making it easy for users to interact with the various features.

## Installation

1. Clone the repository to your local machine:

2. Install the required dependencies. 

3. Run the application:


## Configuration

Before running the application, make sure to set up your ParallelDots API key in the `api.py` file.

```python
# api.py

import paralleldots

class API:
 def __init__(self):
     paralleldots.set_api_key('YOUR_PARALLELDOTS_API_KEY')
 # Replace 'YOUR_PARALLELDOTS_API_KEY' with your actual ParallelDots API key.
```

## Usage

1. Launch the application by running main.ipynb.

2. Register or log in using your credentials.

3. Use the provided buttons to access different NLP functionalities: Sentiment Analysis, NER, and Emotion Prediction.

4. Enter the required text and click on the respective buttons to perform the analysis/prediction.

5. The results will be displayed on the GUI interface.

import paralleldots  # Import the paralleldots module for accessing the ParallelDots API

class API:

    def __init__(self):
        """
        Initializes the API class with the ParallelDots API key.
        """
        paralleldots.set_api_key('YOUR_PARALLELDOTS_API_KEY')
        
    def sentiment_analysis(self, text):
        """
        Performs sentiment analysis on the provided text.
        """
        response = paralleldots.sentiment(text)
        return response
    
    def ner(self, text):
        """
        Performs named entity recognition (NER) analysis on the provided text.
        """
        response = paralleldots.ner(text)
        return response
        
    def emotion_prediction(self, text):
        """
        Performs emotion prediction on the provided text.
        """
        response = paralleldots.emotion(text)
        return response

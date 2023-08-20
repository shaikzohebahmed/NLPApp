import paralleldots

class API:
    
    def __init__(self):
        paralleldots.set_api_key('8mxbRbNTQPRb4hRIaDwmPRDPWkogspOpXMhSv2Cz2ok')
        
        
    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response
    
    def ner(self,text):
        response = paralleldots.ner(text)
        return response
        

    def emotion_prediction(self,text):
        response = paralleldots.emotion(text)
        return response
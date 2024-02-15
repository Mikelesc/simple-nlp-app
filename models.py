from transformers import pipeline


class SentimentModel():
    model = None

    def load_model(self):
        model_name = "fgaim/tielectra-small-sentiment"
        self.model = pipeline("sentiment-analysis", model = model_name)

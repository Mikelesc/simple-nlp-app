from transformers import pipeline


class SentimentModel():
    model = None

    def load_model(self):
        model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
        self.model = pipeline(model = model_name)

import json
import os

class FAQDataLoader:
    @staticmethod
    def load_faqs(filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"FAQ Dataset not found at {filepath}")
            
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        if not isinstance(data, list):
            raise ValueError("FAQ dataset must be a list of objects containing 'question' and 'answer'.")
            
        return data

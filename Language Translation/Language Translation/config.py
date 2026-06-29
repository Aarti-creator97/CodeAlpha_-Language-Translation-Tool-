import os

class Config:
    # Application configuration
    DEBUG = True
    PORT = 5000
    
    # Basedir
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Path to FAQ dataset
    FAQ_DATA_PATH = os.path.join(BASE_DIR, 'data', 'faqs.json')

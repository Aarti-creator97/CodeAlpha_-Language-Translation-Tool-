from flask import Flask
from flask_cors import CORS
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS for frontend requests
    CORS(app)
    
    # Initialize the NLP Engine and Data Loader upon startup
    # We load it globally once to avoid reloading on every request
    from data.data_loader import FAQDataLoader
    from core.nlp_engine import NLPEngine
    from core.matcher import FAQMatcher

    try:
        faq_data = FAQDataLoader.load_faqs(app.config['FAQ_DATA_PATH'])
        app.nlp_engine = NLPEngine()
        app.faq_matcher = FAQMatcher(nlp_engine=app.nlp_engine, faqs=faq_data)
        print("FAQ Dataset and NLP Engine loaded successfully.")
    except Exception as e:
        print(f"Error loading NLP components: {e}")
        
    # Register API blueprints
    from api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])

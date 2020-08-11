import os

# Sélectionnez la configuration en fonction de l'environnement
env = os.environ.get('FLASK_ENV', 'development')
if env == 'production':
    from config.production import ProductionConfig
    config = ProductionConfig
else:
    from config.development import DevelopmentConfig
    config = DevelopmentConfig

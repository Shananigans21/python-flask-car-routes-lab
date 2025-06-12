from flask import Flask
app = Flask(__name__)

# Array of existing model names
existing_models = ['beedle', 'crossroads', 'm2', 'panique']

# Default route for the homepage
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

# Dynamic route for model lookup
@app.route('/<model>')
def get_model(model):
    # Normalize input and compare
    if model.lower() in existing_models:
        return f"Flatiron {model.capitalize()} is in our fleet!"
    else:
        return f"No models called {model.capitalize()} exist in our catalog"

if __name__ == '__main__':
    app.run(debug=True)

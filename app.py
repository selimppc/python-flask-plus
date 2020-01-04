from flask import Flask
from apis import api

app = Flask(__name__) # flask uses the import name to know where to look up resources
api.init_app(app)  # initiate app

# Debug
app.run(debug=True)

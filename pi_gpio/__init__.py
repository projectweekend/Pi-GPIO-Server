import os
from flask import Flask


app = Flask(__name__)
app.config['HOST'] = os.getenv('HOST', '0.0.0.0')
app.config['PORT'] = os.getenv('PORT', 3000)
app.config['DEBUG_MODE'] = os.getenv('DEBUG_MODE', True)

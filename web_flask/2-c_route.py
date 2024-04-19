#!/usr/bin/python3
"""Script to start flask application"""

app = Flask(__name__)

app.route('/', strict_slashes=False)
def root():
    """Display text"""
    return 'Hello HBNB!'

app.route('/hbnb', strick_slashes=False)
def hbnb():
    """Diplay text"""
    return 'HBNB'

app.route('/c/<text>', strict_slashes=False)
def text():
    """Display text"""
    t_text = text.replace('_', ' ')
    return 'C {}'.format(t_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

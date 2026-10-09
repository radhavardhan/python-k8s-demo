from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My Application</h1>
    <a href="/">Home/contactContact Us</a>
    <p>Hello Kubernetes!</p>
    """

@app.route('/contact')
def contact():
    return """
    <h1>Contact Us</h1>
    <aome</a> |
    <a href="/contact">Contact <p>Email: support@example.com</p>
    <p>Phone: +91-9876543210</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
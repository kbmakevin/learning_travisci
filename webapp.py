"""
Simple web app to test TravisCI mechanism
"""
from flask import Flask

HTML = """
<!DOCTYLE html>
<html lang="en">
    <head>
        <title>Home | TravisCI</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="description" content="Social media analytic tool">
        <meta name="author" content="Kevin Ma">
    </head>
    <body>
        <h1>Home Page</h1>
    </body>
</html>
"""

app = Flask(__name__) # pylint: disable=invalid-name

@app.route('/')
def home():
    """Main route to the web app
    """
    return HTML

if __name__ == '__main__':
    app.run()

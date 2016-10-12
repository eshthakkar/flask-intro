from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely', 'balloonicorny']

DISS = ['so-meh', 'not-so-balloonicorny', 'regular', 'not-Py']

@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>Hi! This is the home page.
    <a href="/hello">Go to Hello!</a>
    <html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
           <label>What's your name? <input type="text" name="person"></label>
           <label>Select your compliment: </label> 
           <select name="compliment">
            <option value="awesome">awesome</option>
            <option value="brilliant">brilliant</option>
            <option value="balloonicorny">balloonicorny</option>
            <option value="incredible">incredible</option>
            <option value="wonderful">wonderful</option>
          </select><br>
          <input type="submit">
        </form>


      </body>
    </html>
    """




@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)

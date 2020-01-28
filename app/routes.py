from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'DCurrey'}
    return '''
<html>
    <head>
        <title>Index - LearningFlask</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''.</h1>
    </body>
</html>'''

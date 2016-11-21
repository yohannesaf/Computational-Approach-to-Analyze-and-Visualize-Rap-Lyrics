from flask import Flask, request
# from mcl_clustering import mcl
from TextAssemble import TextAssemble
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Page Title</title>
            </head>
          <body>
            <!-- page content -->
            <h1>Rap Lyric Visualization</h1>

            <form action="/test" method='POST' >

            <textarea
            name="user_input_lyrics"
            style="width:50%; height:90px; padding:2%">
            Copy and paste rap lyrics
            </textarea>
            <input type="submit" value="Visualize"/>
            <p> Click the "Visualize" to visualize rap lyrics.</p>
            </form>

          </body>
        </html>
        '''


@app.route('/test', methods=['POST'] )
def test():
    user_input = str(request.form['user_input_lyrics']).upper()
    # text = TextAssemble(text)
    # check =
    return user_input



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

from flask import Flask, request, render_template
# from mcl_clustering import mcl
from TextAssemble import TextAssemble
from ScoreMechanism import ScoreMechanism
from PrepareText import PrepareText
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
            <head>
                <div align="center">
                <meta charset="utf-8">
                <title>Page Title</title>
            </head>
          <body>
            <!-- page content -->
            <h1>Rap Lyric Visualization</h1>

            <div align="center">
            <form action="/test" method='POST' >
            <textarea
                name="user_input_lyrics"
                rows = "7" cols = "80" wrap="soft">
                Copy and paste rap lyrics
            </textarea>
            <br>
                <input type="submit" value="Visualize" />
            </br>
            <p>
                Click the "Visualize" to analyze rap lyrics
            </p>
            </form>

          </body>
        </html>
        '''


@app.route('/test', methods=['POST'] )
def test():
    user_input = str(request.form['user_input_lyrics'])
    text = TextAssemble(user_input)
    return text.original



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

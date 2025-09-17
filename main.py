from generator import generate_captions
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
    captions = ""
    if request.method == 'POST':
        description = request.form.get('description')
        tone = request.form.get('tone')
        length = request.form.get('length')
        social_media_platform = request.form.get('social_media_platform')

        captions = generate_captions(description, tone, length, social_media_platform)

    return render_template('index.html', captions= captions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
cors = CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = [
    '.jpg', '.png', '.gif', '.txt', '.text', 'plain']
app.config['UPLOAD_PATH'] = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['CORS_HEADERS'] = "Content-Type"


def validate_image(stream):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)


@app.route('/', methods=['POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        # check if the post request has the files part
        if 'files[]' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        for file in files:
            if file:  # and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        #flash('File(s) successfully uploaded')
    # return redirect(url_for('index'))
        return redirect('/')


@app.route('/uploads/list')
def list():
    # Implement!
    return json.dumps(

        os.listdir(
            os.path.join(
                os.path.dirname(__file__), "uploads"
            ))
    )


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route('/app/assets/<filename>')
def get_app_asset(filename):
    return send_from_directory(os.path.join(
                os.path.dirname(__file__), "dist","assets"
            ),filename)

@app.route('/app/<filename>')
def get_app(filename):
    return send_from_directory(os.path.join(
                os.path.dirname(__file__), "dist"
            ),filename)


if __name__ == '__main__':
    app.run(debug=True)

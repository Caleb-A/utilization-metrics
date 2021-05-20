import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.txt', '.text', 'plain']
app.config['UPLOAD_PATH'] = '/home/zero/workspace/python_code/uploads'

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

"""@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
           file_ext != validate_image(uploaded_file.stream):
           abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))"""

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			#flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file: #and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
		#flash('File(s) successfully uploaded')
        #return redirect(url_for('index'))
		return redirect('/')


@app.route('/uploads/list')
def list():
    # Implement!
    return "not yet implemented"

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)



if __name__ == '__main__':
   app.run(debug = True)
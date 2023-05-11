# import cv2
# from flask import Flask, render_template
#
# from opencv import grey_filter
#
# app = Flask(__name__)
#
#
# # Render the template with the filtered image
# @app.route('/hello')
# def index():
#     # Get the path to the image file
#     image_path = 'static/lena.jpg'
#     # Apply the gray filter
#     filtered_image = grey_filter(image_path)
#     # Save the filtered image to the static directory
#     cv2.imwrite('static/filtered_image.jpg', filtered_image)
#     # Render the template with the filtered image
#     return render_template('index.html', image_url='filtered_image.jpg')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# #####################################################################
#with upload
import os
import cv2
from flask import Flask, render_template, request

from opencv import grey_filter

app = Flask(__name__)

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Render the template with the uploaded and filtered images
@app.route('/hello', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', message='No file selected')

        file = request.files['file']

        # Check if the file has an allowed extension
        if not allowed_file(file.filename):
            return render_template('index.html', message='Invalid file type')

        # Save the uploaded file to the uploads directory
        file.save(os.path.join('uploads', file.filename))

        # Apply the gray filter to the uploaded file
        image_path = os.path.join('uploads', file.filename)
        filtered_image = grey_filter(image_path)

        # Save the filtered image to the static directory
        filtered_image_path = os.path.join('static', 'filtered_image.jpg')
        cv2.imwrite(filtered_image_path, filtered_image)

        # Render the template with the uploaded and filtered images
        return render_template('index.html', image_url='filtered_image.jpg', upload_url=file.filename)

    # Render the template with the Lena image
    return render_template('index.html', image_url='lena.jpg')

@app.route("/uploadImg")
def upload():
    if 'image' not in request.files:
        return "No image uploaded."

    file=request.files['image']
    file_name=file.filename

    file.save('static/'+file_name)

    return "File uploaded successfully."


if __name__ == '__main__':
    app.run(debug=True)


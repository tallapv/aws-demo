from flask import Blueprint, render_template, request
import os

careers_blueprint = Blueprint('careers', __name__)

# Ensure the 'data' folder exists to store uploaded files
os.makedirs('data', exist_ok=True)

@careers_blueprint.route('', methods=['GET', 'POST'])
def careers():
    if request.method == 'POST':
        # Handle file upload
        if 'file' not in request.files:
            return "No file part", 400
        
        file = request.files['file']
        
        if file.filename == '':
            return "No selected file", 400
        
        # Save the file in the 'data' folder
        file_path = os.path.join('data', file.filename)
        file.save(file_path)
        return f"File '{file.filename}' uploaded successfully to {file_path}"

    # Render the careers page template
    return render_template('careers.html')

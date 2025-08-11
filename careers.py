from flask import Blueprint, render_template, request
import os

careers_blueprint = Blueprint('careers', __name__)

# Ensure the 'data' folder exists to store uploaded files
os.makedirs('data', exist_ok=True)

@careers_blueprint.route('', methods=['GET', 'POST'])
def careers():
    if request.method == 'POST':
        # Get the user name from the form
        user_name = request.form.get('name')

        # Handle file upload
        if 'file' not in request.files:
            return "No file part", 400
        
        file = request.files['file']
        
        if file.filename == '':
            return "No selected file", 400
        
        # Extract file extension and save the file with the user's name and original extension
        file_extension = os.path.splitext(file.filename)[1]  # Get the file extension
        file_name = f"{user_name}{file_extension}"  # Combine user name with the file extension

        # Save the file in the 'data' folder with the new name
        file_path = os.path.join('data', file_name)
        file.save(file_path)

        return f"File '{file_name}' uploaded successfully to {file_path}"

    # Render the careers page template
    return render_template('careers.html')

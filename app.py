import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Configuration for file uploads
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Admin credentials (in production, use proper authentication)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'  # Change this to a secure password

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_profile_data():
    """Load profile data from JSON file"""
    try:
        with open('profile_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            'name': 'Your Name',
            'profile_picture': 'https://via.placeholder.com/150',
            'resume_file': None
        }

def save_profile_data(data):
    """Save profile data to JSON file"""
    with open('profile_data.json', 'w') as f:
        json.dump(data, f)

@app.route('/')
def home():
    profile_data = load_profile_data()
    return render_template('home.html', profile_data=profile_data)

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/job-support')
def job_support():
    return render_template('job_support.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin/login', methods=['POST'])
def admin_authenticate():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return redirect(url_for('admin_dashboard'))
    else:
        flash('Invalid credentials. Please try again.', 'error')
        return redirect(url_for('admin_login'))

@app.route('/admin/dashboard')
def admin_dashboard():
    profile_data = load_profile_data()
    return render_template('admin_dashboard.html', profile_data=profile_data)

@app.route('/admin/upload', methods=['POST'])
def admin_upload():
    if 'profile_picture' in request.files:
        file = request.files['profile_picture']
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename('profile_picture.' + file.filename.rsplit('.', 1)[1].lower())
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            profile_data = load_profile_data()
            profile_data['profile_picture'] = f'/static/uploads/{filename}'
            save_profile_data(profile_data)
            
            flash('Profile picture updated successfully!', 'success')
        else:
            flash('Invalid file type. Please upload an image file.', 'error')
    
    if 'resume' in request.files:
        file = request.files['resume']
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename('resume.' + file.filename.rsplit('.', 1)[1].lower())
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            profile_data = load_profile_data()
            profile_data['resume_file'] = f'/static/uploads/{filename}'
            save_profile_data(profile_data)
            
            flash('Resume updated successfully!', 'success')
        else:
            flash('Invalid file type. Please upload a PDF or DOC file.', 'error')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/update-name', methods=['POST'])
def admin_update_name():
    name = request.form.get('name')
    if name:
        profile_data = load_profile_data()
        profile_data['name'] = name
        save_profile_data(profile_data)
        flash('Name updated successfully!', 'success')
    else:
        flash('Name cannot be empty.', 'error')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/resume')
def download_resume():
    profile_data = load_profile_data()
    if profile_data.get('resume_file'):
        return send_from_directory(app.config['UPLOAD_FOLDER'], 
                                 profile_data['resume_file'].split('/')[-1])
    else:
        flash('Resume not found.', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) 
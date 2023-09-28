from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)

# Define Partner Model
class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Define JobOpening model
class JobOpening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

# Define Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create Inquiry model (for adding inquiries)
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)

# Define API endpoints

# Get business partners
@app.route('/partners', methods=['GET'])
def get_partners():
    partners = Partner.query.all()
    partner_list = [{'id': partner.id, 'name': partner.name} for partner in partners]
    return jsonify(partner_list)

# Get job openings
@app.route('/job-openings', methods=['GET'])
def get_job_openings():
    job_openings = JobOpening.query.all()
    job_opening_list = [{'id': job.id, 'title': job.title} for job in job_openings]
    return jsonify(job_opening_list)

# Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    project_list = [{'id': project.id, 'name': project.name} for project in projects]
    return jsonify(project_list)

# Add inquiry
@app.route('/inquiries', methods=['POST'])
def add_inquiry():
    data = request.get_json()
    if 'message' not in data:
        return jsonify({'error': 'Message is required'}), 400
    message = data['message']
    inquiry = Inquiry(message=message)
    db.session.add(inquiry)
    db.session.commit()
    return jsonify({'message': 'Inquiry added successfully'}), 201

if __name__ == '__main__':
    with app.app_context():  # Create an application context
        db.create_all() # Perform database operations within the context
        app.run(debug=True) # Run app

from flask import Blueprint, render_template, current_app
import csv



bp = Blueprint('main', __name__)

def read_csv_file(filename):
    data = []
    filepath = current_app.root_path + '/static/csv_folder/' + filename
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@bp.route('/')
def index():
    data = read_csv_file('students.csv')[0:3]  #1st 3 students
    return render_template('index.html', toppers=data)

@bp.route('/about')
def about():
    return render_template('about.html')


#@bp.route('/toppers')
#def toppers():
   # return render_template('toppers.html')



@bp.route('/toppers')
def toppers():
    data = read_csv_file('students.csv')  # Ensure 'toppers.csv' is the correct filename
    return render_template('toppers.html', toppers=data)
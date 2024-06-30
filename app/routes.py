from flask import Blueprint, render_template, current_app, request
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

@bp.route('/map')
def map():
    return render_template('map.html')

@bp.route('/guidelines')
def guidelines():
    semester_id = request.args.get('semester_id')
    if not semester_id:
        return "Semester ID not provided", 400

    courses = read_csv_file('course.csv')
    online_courses = [course for course in courses if course['semester_id'] == semester_id and course['Course_Type'] == 'Online']
    offline_courses = [course for course in courses if course['semester_id'] == semester_id and course['Course_Type'] == 'Offline']
    total_online = calculate_total_price(online_courses)
    total_offline = calculate_total_price(offline_courses)

    return render_template('guidelines.html', semester_id=semester_id, online_courses=online_courses, total_online=total_online )


def calculate_total_price(courses):
    total = sum(float(course['Price']) for course in courses)
    if(course==0):
        return "Free"
    else:
        return total
    
    
@bp.route('/course')
def course():
    semester_id = request.args.get('semester_id')
    courses = read_csv_file('course.csv')
    
    online_courses = [course for course in courses if course['semester_id'] == semester_id and course['Course_Type'] == 'Online']
    offline_courses = [course for course in courses if course['semester_id'] == semester_id and course['Course_Type'] == 'Offline']
    total_online = calculate_total_price(online_courses)
    total_offline = calculate_total_price(offline_courses)
    
    return render_template('course.html', semester_id=semester_id, online_courses=online_courses, offline_courses=offline_courses,total_online=total_online,total_offline=total_offline)

@bp.route('/toppers')
def toppers():
    data = read_csv_file('students.csv')  # Ensure 'students.csv' is the correct filename
    return render_template('toppers.html', toppers=data)

from flask import Blueprint, current_app, request, jsonify
import csv
import os

admin_bp = Blueprint('admin', __name__)

def get_csv_file_path(filename):
    return os.path.join(current_app.root_path, 'static/csv_folder', filename)

def read_csv_file(filename):
    data = []
    filepath = get_csv_file_path(filename)
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


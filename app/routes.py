from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/quiz')
def quiz():
    return render_template('quiz.html')

@bp.route('/result')
def result():
    return render_template('result.html')

@bp.route('/characters')
def characters():
    return render_template('characters.html')

@bp.route('/relationships')
def relationships():
    return render_template('relationships.html')

@bp.route('/history')
def history():
    return render_template('history.html')

@bp.route('/mbti/<type>')
def mbti_type(type):
    return render_template('mbti_type.html', type=type)

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/careers')
def careers():
    return render_template('careers.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

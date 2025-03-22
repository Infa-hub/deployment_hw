from flask import Flask, render_template
from gitlab_api import get_user_info, get_user_projects

app = Flask(__name__)

@app.route('/')
def index():
    user_info = get_user_info()
    if user_info:
        projects = get_user_projects(user_info['id'])
        return render_template('resume.html', user=user_info, projects=projects)
    else:
        return "Ошибка: не удалось получить данные о пользователе"

@app.route('/update')
def update():
    user_info = get_user_info()
    if user_info:
        projects = get_user_projects(user_info['id'])
        return render_template('resume.html', user=user_info, projects=projects)
    else:
        return "Ошибка: не удалось обновить данные"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/list_prof/<ol_ul>')
def index(ol_ul):
    if ol_ul == "ol":
        return render_template("ol.html")
    elif ol_ul == "ul":
        return render_template("ul.html")


@app.route("/answer")
def answer():
    answer_dict = {"surname": "Watny", "Watnyname": "Mark", "education": "выше среднего",
                   "profession": "штурман марсохода", "sex": "male", "motivation": "всегда хотел", "ready": "True"}

    return render_template("auto_answer.html", title="Анкета", answer_dict=answer_dict)


@app.route('/training/<one>')
def training(one):
    if one == "doc":
        return render_template("training_doc.html")
    elif one == "eng":
        return render_template("training_eng.html")


@app.route('/distribution')
def distribution():
    list = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандрес", "Шон Бин"]
    return render_template('rooms.html', title='Расселение', users=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

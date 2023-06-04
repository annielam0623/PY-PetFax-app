from flask import ( Blueprint, render_template, request, redirect)
from . import models


bp = Blueprint('/', __name__, url_prefix="/facts")

@bp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        author = request.form['author']
        fact = request.form['fact']

        new_fact = models.Fact(author=author, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')
    
    results = models.Fact.query.all()
    # for result in results:
    #     print(result)
    
    return render_template('facts/index.html', facts=results)

@bp.route('/new')       
def new():
    return render_template('facts/new.html')

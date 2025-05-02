from app import app, models
from flask import render_template, url_for, request, jsonify

@app.route('/')
@app.route('/Accueil')
def accueil():
    return render_template('accueil.html', title="Nate's Library : déjà plus de 20 livres disponibles !")



@app.route('/Books')
def show_all_books():
    list_books = models.View_books_with_authors_and_categories.query.all()
    return render_template('all_books.html', title='All our books', books=list_books)

@app.route('/Categories')
def categories():
    liste_categories_books = models.View_books_with_authors_and_categories.query.distinct('category_name')
    return render_template('categories.html', title="Categories", categories=liste_categories_books)

@app.route('/Authors')
def authors():
    liste_authors_books = models.View_books_with_authors_and_categories.query.distinct('author_name')
    return render_template('authors.html', title="Authors", authors=liste_authors_books)

@app.route('/books_category')
def books_category():
    cat_name = request.args.get('category_name')
    list_books = models.View_books_with_authors_and_categories.query.filter_by(category_name=cat_name)
    return render_template('books_category.html', title='Nos produits', books=list_books, typeprod=type(list_books))

@app.route('/books_author')
def books_author():
    auth_name = request.args.get('author_name')
    list_books = models.View_books_with_authors_and_categories.query.filter_by(author_name=auth_name)
    return render_template('books_author.html', title='Nos produits', books=list_books, typeprod=type(list_books))

@app.route('/books_search')
def books_search():
    search = request.args.get('search')
    list_books = models.View_books_with_authors_and_categories.query.filter(models.View_books_with_authors_and_categories.title.ilike(f'%{search}%'))
    return render_template('books_search.html', title='Nos produits', books=list_books, typeprod=type(list_books))
"""
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('search', '')  # Récupère la saisie utilisateur
    suggestions = models.View_books_with_authors_and_categories.query.filter(
        models.View_books_with_authors_and_categories.title.ilike(f'%{search}%')
    ).limit(5).all()  # Limite les résultats à 5 suggestions

    # Retourne les titres des livres sous forme de JSON
    return jsonify([book.title for book in suggestions])"""
    
@app.route('/search', methods=['GET'])
def search():
    search_type = request.args.get('type')  # Get the selected search type (books, categories, authors)
    query = request.args.get('query')  # Get the search query

    if search_type == 'books':
        results = models.View_books_with_authors_and_categories.query.filter(models.View_books_with_authors_and_categories.title.ilike(f'%{query}%'))
    elif search_type == 'categories':
        results = models.View_books_with_authors_and_categories.query.filter(models.View_books_with_authors_and_categories.category_name.ilike(f'%{query}%')).distinct()
    elif search_type == 'authors':
        results = models.View_books_with_authors_and_categories.query.filter(models.View_books_with_authors_and_categories.author_name.ilike(f'%{query}%')).distinct()
    else:
        results = []

    return render_template('search_results.html', query=query, results=results, search_type=search_type)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search_type = request.args.get('type')
    query = request.args.get('query', '')

    if search_type == 'books':
        suggestions = models.View_books_with_authors_and_categories.query.filter(
            models.View_books_with_authors_and_categories.title.ilike(f'%{query}%')
        ).limit(5).all()
        return jsonify([book.title for book in suggestions])
    elif search_type == 'categories':
        suggestions = models.View_books_with_authors_and_categories.query.filter(
            models.View_books_with_authors_and_categories.category_name.ilike(f'%{query}%')
        ).limit(5).all()
        return jsonify([category.category_name for category in suggestions])
    elif search_type == 'authors':
        suggestions = models.View_books_with_authors_and_categories.query.filter(
            models.View_books_with_authors_and_categories.author_name.ilike(f'%{query}%')
        ).limit(5).all()
        return jsonify([author.author_name for author in suggestions])
    else:
        return jsonify([])
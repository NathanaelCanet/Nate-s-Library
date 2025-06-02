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
    search_type = request.args.get('type')  # Récupère le type de recherche (books, categories, authors)
    query = request.args.get('query', '')  # Récupère la saisie utilisateur

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
""" 
   
@app.route('/search', methods=['GET'])
def search():
    search_type = request.args.get('type')  # Récupère le type de recherche (books, categories, authors)
    query = request.args.get('query')  # Récupère la saisie utilisateur

    if search_type == 'books':
        # Recherche par titre de livre
        results = models.View_books_with_authors_and_categories.query.filter(
            models.View_books_with_authors_and_categories.title.ilike(f'%{query}%')
        ).all()
    elif search_type == 'categories':
        # Recherche par catégorie
        results = models.View_books_with_authors_and_categories.query.filter(
            models.View_books_with_authors_and_categories.category_name.ilike(f'%{query}%')
        ).all()
    elif search_type == 'authors':
        # Recherche par auteur
        results = models.View_books_with_authors_and_categories.query.filter(
            models.View_books_with_authors_and_categories.author_name.ilike(f'%{query}%')
        ).all()
    else:
        # Si aucun type valide n'est fourni, renvoyer une liste vide
        results = []

    # Rendre les résultats dans le template
    return render_template('search_results.html', query=query, results=results, search_type=search_type)
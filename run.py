from app import app  # On importe l'app depuis ton package "app"

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
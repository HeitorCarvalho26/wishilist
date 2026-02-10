from flask import Flask, render_template, request, redirect, url_for
from models.obra import Obra

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo = "Lista de desejos")

@app.route('/wishlist', methods=['GET', 'POST'])
def list():
    obra = None

    if request.method == 'POST':
        titulo_obra = request.form['titulo_obra']
        indicacao = request.form['indicacao']
        obra = Obra(titulo_obra, indicacao)
        obra.salvar_obra()

    obras = Obra.obter_obra()
    return render_template('wishlist.html', titulo='Lista', obra=obras)

@app.route('/update/<int:idObra>', methods = ['GET', 'POST'])
def update(idObra):
    if request.method == 'POST':
        titulo = request.form['titulo-obra']
        indic = request.form['indicacao']
        obra = Obra(titulo, indic, idObra)
        obra.atualizar_obra()
        return redirect(url_for)
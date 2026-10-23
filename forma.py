from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)
@app.route("/")
def início():

    return render_template("formulario.html")

@app.route("/cadastrar", methods=['POST'])
def cadastrar():
   
    nome = request.form["nome"]
    cpf = request.form["cpf"]    
    descricao_cliente = request.form["descricao_cliente"]
    
    banco = sqlite3.connect("banco.db")
    cursor = banco.cursor()
    cursor.execute("INSERT INTO registros (nome, cpf, descricao_cliente) VALUES (?, ?, ?)", (nome, cpf, descricao_cliente))
    banco.commit()
    banco.close()
    
    return render_template("ok.html")
    
@app.route("/clientes", methods=['GET'])
def clientes():

    banco = sqlite3.connect("banco.db")
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM registros")
    registros = cursor.fetchall()
    banco.close()
    
    return render_template("clientes.html", registros=registros)

@app.route("/procurar", methods=['GET', 'POST'])
def procurar():
    registros = []
    if request.method == "POST":
        nome = request.form["pesquisa"]
    
        banco = sqlite3.connect("banco.db")
        cursor = banco.cursor()
        cursor.execute("SELECT nome, cpf, descricao_cliente FROM registros WHERE nome LIKE ?", 
        ("%" + nome + "%",))
        registros = cursor.fetchall()
        banco.close()
    
    return render_template("procurar.html", registros=registros)

@app.route("/excluir_cadastro", methods=["GET", "POST"])
def excluir_cadastro():
    registros = []
    if request.method == "POST":
        nome = request.form["excluir_cadastro"]
        
        banco = sqlite3.connect("banco.db")
        cursor = banco.cursor()
        cursor.execute ("DELETE FROM registros WHERE nome = ?", (nome,))
        banco.commit()
        banco.close()
    return render_template("excluir_cadastro.html")
if __name__ == "__main__":
    app.run(debug=True)
    
    
    

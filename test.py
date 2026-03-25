@app.route("/")
def hello_world():
    return "<h1> Pagina inicial </h1>" + "<a href='/random_fact'>Veja um fato aleatório!</a>"
@app.route("/random_fact")
def random_fact():
    fato = random.choice(fatos_aleátorios)
    return f"<h1>Fato aleatório: {fato}</h1>"
app.run(debug=True)

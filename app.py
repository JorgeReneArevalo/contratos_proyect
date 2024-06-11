from flask import Flask, render_template,request, send_file

app = Flask(__name__)


@app.route('/generar_docx', methods=['POST'])
def generar_docx():
    print("Todo OKAY")
    datos = request.json  # Recibimos los datos desde el frontend
    # generar_docx_modificado(datos)
    return "Documento generado correctamente"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

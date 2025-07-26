from flask import Flask, render_template, redirect, url_for
from db.extensoes import db
from routes.fazenda_routes import fazenda_bp
from routes.cultura_routes import cultura_bp
from routes.projeto_routes import projeto_bp
from routes.api_routes import api_bp
from routes.irrigacao_routes import irrigacao_bp
from routes.dashboard_routes import dashboard_bp
from routes.relatorios_routes import relatorios_bp
import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__)
app.template_folder = "templates"

app.secret_key = "irrigacao2025@flask!"

# ✅ Aqui usamos o valor da variável de ambiente do Render
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return 'Bem-vindo ao sistema Irrigação Flask + Render!'

@app.route("/home")
def home():
    return redirect(url_for('dashboard.dashboard'))

# Blueprints
app.register_blueprint(fazenda_bp)
app.register_blueprint(cultura_bp)
app.register_blueprint(projeto_bp)
app.register_blueprint(api_bp)
app.register_blueprint(irrigacao_bp)
app.register_blueprint(relatorios_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run()


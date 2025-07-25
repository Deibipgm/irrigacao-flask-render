# 🌱 Irriga+ - Sistema de Gestão de Irrigação

Este sistema Flask permite cadastrar fazendas, pivôs, parâmetros técnicos e registrar irrigação diária com controle completo via web.

---

## 🚀 Como Publicar no Render

### ✅ 1. Pré-requisitos
- Conta GitHub e projeto versionado
- Estrutura de pastas organizada com `app.py`, `requirements.txt`, `Procfile`, `.env`

### ✅ 2. Deploy no Render
1. Acesse [https://render.com](https://render.com) e crie um novo **Web Service**
2. Conecte seu repositório GitHub
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Production
   - **Python Version**: 3.11+

4. Adicione variáveis de ambiente (Environment Variables):
```
FLASK_ENV=production
DATABASE_URL=mysql+pymysql://usuario:senha@host/db_irrigacao
```

5. Clique em **Deploy** e o Render gerará um domínio como:
```
https://irriga.onrender.com
```

---

## 🗃️ Como Migrar o Banco de Dados MySQL para a Nuvem

### 💡 Opção 1 - PlanetScale (Recomendado)
1. Acesse [https://planetscale.com](https://planetscale.com) e crie um banco
2. Vá em `Settings > Connection Strings` e copie a conexão
3. Adicione no `.env` ou no Render como `DATABASE_URL`

### 💡 Opção 2 - ClearDB
1. Acesse [https://www.cleardb.com/store/](https://www.cleardb.com/store/)
2. Crie um plano gratuito
3. Copie e adapte a string de conexão para SQLAlchemy

### 💡 Opção 3 - Servidor Próprio
1. Use MySQL em VPS, CPANEL ou DigitalOcean
2. Libere porta 3306 e crie usuário/senha
3. Use string: `mysql+pymysql://usuario:senha@host/db`

---

## 🛠️ Como Migrar os Dados (Opcional)
1. Exporte localmente:
```bash
mysqldump -u root -p db_irrigacao > backup.sql
```

2. Importe remotamente:
```bash
mysql -h host.com -u user -p -D db_irrigacao < backup.sql
```

---

## ✅ Pronto!
Acesse `https://irriga.onrender.com` e comece a usar seu sistema online!
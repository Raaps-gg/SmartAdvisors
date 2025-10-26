from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug True for local development
    app.run(host="127.0.0.1", port=5000, debug=True)

# Running the python script on a virtual enviormnet backend
# python3 -m venv venv
# pip install flask flask-cors flask_sqlalchemy python-dotenv pdfplumber psycopg2-binary
# python run.py
# deactivate

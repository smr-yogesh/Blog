from flask import render_template
from routes.admin import admin
from routes.user import B_user
from routes import app

app.register_blueprint(admin)
app.register_blueprint(B_user)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8002)
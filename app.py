from flask import render_template
from routes.admin import admin_B
from routes.user import B_user
from routes.posts import posts_B
from routes import app
from datetime import datetime

app.register_blueprint(admin_B)
app.register_blueprint(B_user)
app.register_blueprint(posts_B)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8002)

def db(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/hsm"

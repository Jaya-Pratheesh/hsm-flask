from Controller.employeeController import employee

def serve(app, PyMongo):
    @app.route("/")
    def welcome():
        return "Hello World!"
    
    @app.route("/get-employee")
    def gt_emp():
        emp = employee(app, PyMongo)
        return emp.get_emp()

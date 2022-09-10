from flask import Flask,render_template
from flask import jsonify
from flask import request
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/mapping/")
def mapping():
    data = [{"banner_id": "1", 
             "value": "https://cdn.sanity.io/images/r21q6f3r/cms/7371703666592ff66cc1d29525b1a8f53ea4b6bb-1500x938.jpg?w=1920&q=75&fit=clip&auto=format"},
            {"banner_id": "2",
             "value": "https://cdn.sanity.io/images/r21q6f3r/cms/0ed7230874e77157e32e85c5a749738b6bc45c2c-1500x936.jpg?w=1920&q=75&fit=clip&auto=format"}]
    message = "Mapping fetched successfully"
    return jsonify(data), 200

@app.route('/mapping/<banner_id>/')
def show_results(banner_id):
    data =   [{"banner_id": "1", 
             "value": "https://cdn.sanity.io/images/r21q6f3r/cms/7371703666592ff66cc1d29525b1a8f53ea4b6bb-1500x938.jpg?w=1920&q=75&fit=clip&auto=format"},
            {"banner_id": "2",
             "value": "https://cdn.sanity.io/images/r21q6f3r/cms/0ed7230874e77157e32e85c5a749738b6bc45c2c-1500x936.jpg?w=1920&q=75&fit=clip&auto=format"}]
    res = list(filter(lambda person: person['banner_id'] == banner_id, data))
    if res:
        return jsonify(res[0]), 200
    return jsonify("Not Found"), 404
    
if __name__ == "__main__":
    app.run()#(debug=False,host='0.0.0.0')

from flask import Flask, send_file, request, render_template

#app.config["CACHE_TYPE"] = "null"

import os

app = Flask(__name__)

@app.route("/")

def home_func():
    return render_template("filename.html")

@app.route("/filesearch", methods=["GET", "POST"])

def file_search():
    if request.method == 'POST':
       fn = request.form['filename']

      # return "filename: "+request.method+" "+fn

   # else:
       # return "not get method"

       path = os.path.join('/home/ubuntu/flaskapp', fn)

       #return send_file(path, as_attachment=True)

       return render_template("filedisplay.html", myfile=path)



@app.route("/filedownload", methods=["GET", "POST"])

def file_download():
    if request.method == 'POST':
      fn = request.form['filename']

      # return "filename: "+request.method+" "+fn

   # else:
       # return "not get method"

      # path = os.path.join('/home/ubuntu/flaskapp', fn)

       return send_file(path, as_attachment=True)

#       return render_template("filedisplay.html", myfile=path)




@app.route("/downloads")

def download_file():
    path = "./downloads/sample1.txt"

    return send_file(path, as_attachment=True)



if __name__ == "__main__":

   app.run()




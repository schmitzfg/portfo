from flask import Flask, request, render_template, redirect  # redirect - modul pentru redirectiona pagina
import csv

## #  * Running on http://127.0.0.1:5000/ 
app = Flask(__name__)

@app.route("/")     
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")     
def html_page(page_name):
    return render_template(page_name)

# @app.route("/about.html")             # accesam pagina about.html
# def about():
#     return render_template('about.html')

def write_to_file(data):            # salvam in .txt file
    with open('database.txt','a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},\t{subject},\t{message}')

def write_to_csv(data):            # salvam in .csv file
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # write_to_file(data)
            return redirect('/thankyou.html')       # cind dam submit la forma ne redirectioneaza pe pagina thankyou.html cu modulul redirect
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'
from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)
# flask --app serv.py --debug run
@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)

def write_file(data):
    with open('database.txt',mode='a') as database:
        email =data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email =data['email']
        subject = data['subject']
        message = data['message']
        csv_w = csv.writer(database2,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_w.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
       try:
        data = request.form.to_dict()
        write_csv(data)
        return redirect('/thankyou.html')
       except:
           return 'Did not save to database'
    else:
        return 'something went wrong!'

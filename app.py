from flask import Flask,render_template,request
app1=Flask(__name__)
@app1.route('/')
def index():
    # return render_template('index.html')
    personal_info={'name':'Annamdas Rajeshwari',
                   'bio':'I am a passionate Python developer currently pursuing an internship focused on backend web development.',
                   'skills':['Python','Flask','HTML','CSS']
                   }
    return render_template('index.html',personal_info=personal_info)
@app1.route('/contact', methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')
        return f"{name}, Thank you for your message!"
    return render_template('contact.html')

app1.run(debug=True,port=5002)



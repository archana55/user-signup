from flask import Flask, request,redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True

#form = """

#"""

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()
# return form.format(username_error='',password_error ='',
 #   verify_error = '',email_error = '',name ='',emailname='')


@app.route("/", methods=['POST'])
def validate():
    username = request.form['user_name_input']
    error_username = validateusername(username)

    password = request.form['pass_word_input']
    error_password = validatepassword(password)

    verify_pwd = request.form['verify_pass_word_input']
    error_verifypwd = validateverifypwd(verify_pwd,password)

    email_input = request.form['email_input']
    error_email = validateemail(email_input)

    if not error_username and not error_password and not error_verifypwd and not error_email :
        return redirect('/hello?name={0}'.format(username))
    else:
        template = jinja_env.get_template('index.html')
        return template.render(username_error = error_username,
        password_error =error_password,
        verify_error = error_verifypwd , email_error = error_email ,
        name = username , emailname = email_input)

def validateusername(username):
    error_message = ''
    if len(username) == 0:
       error_message = "Blank is not valid"
    elif len(username)<3 or len(username)>20:
        error_message = "Invalid input"
    elif  (' ' in username) == True:
         error_message = "Invalid input"


    return error_message

def validatepassword(password):
    error_message = ''
    if len(password) == 0:
       error_message = "Blank is not valid"
    elif len(password)<3 or len(password)>20:
         error_message = "Invalid input"
    elif  (' ' in password) == True:
        error_message = "Invalid input"

    return error_message

def validateverifypwd(verifypwd,password):
    error_message = ''
    if len(verifypwd) == 0:
       error_message = "Blank is not valid"
    elif password != verifypwd:
        error_message = " Passwords do not match!"
    return error_message

def validateemail(email):   
    error_message = ''
    if len(email) == 0:
       error_message = '' 
    elif email.count("@") != 1 or email.count(".") != 1:
         error_message = "Invalid Email"
    elif (' 'in email) ==True or len(email)<3 or len(email)>20:
        error_message = "Invalid Email"  
    return error_message


@app.route("/hello")
def hello():
    username = request.args.get('name')
    template = jinja_env.get_template('welcome.html')
    return template.render(username = cgi.escape(username))
#    return '<h1>Welcome, ' +cgi.escape(username)+ '!</h1>'





app.run() 
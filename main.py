# from crypt import methods
import os
from flask import Flask, render_template, redirect, url_for, make_response, session, request, abort, flash
import yaml
from zipfile import ZipFile
from private_key import encryption

app =Flask(__name__)
app.secret_key = 'p26b5LZUEGuPkvekv6ZzkwInufEDyjf'

bank_info = ['fname', 'lname', 'bname', 'address', 'acc', 'ifsc', 'micr', 'bcode']
personal_info = ['fname', 'mname', 'lname', 'gender', 'dob', 'address', 'mobile', 'email', 'addhar', 'pan']


def save_bank(data):
    with open(f"{data}.yaml", "w") as f:
        yaml.dump(data, f)

def save_personal(data):
    with open(f"P_{data}.yaml", "w") as f:
        yaml.dump(data, f)

@app.route("/bank", methods=["GET", "POST"])
def result_bank():
    if request.method == 'POST':
        full_name = request.form['fname'] + request.form['lname']
        with open(f"{full_name}.yaml", "a") as f:
            yaml.dump(full_name, f)
        for i in bank_info:
            data = request.form[i]
            with open(f"{full_name}.yaml", "a") as f:
                yaml.dump({ i:data}, f)
        return render_template('services.html')
    return render_template('store_bank_details.html')

@app.route("/personal", methods=["GET", "POST"])
def result_personal():
    if request.method == 'POST':
        full_name = request.form['fname'] + request.form['lname']
        full_name.lower()
        with open(f"P_{full_name}.yaml", "a") as f:
            yaml.dump(full_name, f)
        for i in personal_info:
            p_data = request.form[i]
            with open(f"P_{full_name}.yaml", "a") as f:
                yaml.dump({ i:p_data}, f)
        return render_template('services.html')
    return render_template('store_personal_details.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['userid']
        key = request.form['key']
        try:
            with open(f"{username}.yaml", "r") as f:
                data = yaml.safe_load(f)
                data_new = data.get(username)
                if data_new == key:
                    return redirect(url_for('home_page', success='true'))
                    # resp = make_response(render_template('home.html'))
                    # resp.set_cookie('Username', username)
                    # return resp
        except FileNotFoundError:
            pass  # If file doesn't exist, continue to error handling below
        
        # Flash an error message if login fails
        flash("Invalid UserID or Key. Please try again.")
    
    return render_template('login_page.html')

@app.route("/sign_in", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form['userid']
        key = request.form['userid'] + request.form['password']
        enkey = encryption(key, username)
        with open(f'{username}.yaml', 'w') as file: 
            yaml.dump({request.form['userid'] : enkey}, file)
        with open(f'{username}.yaml', "r") as f:
            data = yaml.safe_load(f)
            data_new = data.get(username)
       
        resp = make_response(render_template('generate_qr.html', variable=[username, data_new]))
        resp.set_cookie('Username', username)
        return resp
    return render_template('sign_in_page.html')


@app.route("/services", methods=["GET", "POST"])
def services():
    return render_template('services.html') 


@app.route("/fetch_data", methods=["GET", "POST"])
def fetch_data():
    if request.method == "POST":
        username = request.form['userid']
        print(username)
        key = request.form['private_key']
        full_name = request.form['fname'] + request.form['lname']
        full_name = full_name.lower()
        p = 'P_' + full_name
        print(p)
        with open(f'{username}.yaml', 'r') as f:
            data = yaml.safe_load(f)
            data_new = data.get(username)
        if data_new == key:
            if request.form['data_type'] == 'bank':
                input_file = f"{full_name}.yaml"
                output_file = f"{full_name}.zip"
                password = key.encode()

                # Create a password-protected zip file
                with ZipFile(output_file, 'w') as zipf:
                    zipf.write(input_file)
                    zipf.setpassword(password)

                return render_template('download.html', variable=full_name)
            if request.form['data_type'] == 'personal':
                input_file = f"P_{full_name}.yaml"
                output_file = f"P_{full_name}.zip"
                password = key.encode()

                # Create a password-protected zip file
                with ZipFile(output_file, 'w') as zipf:
                    zipf.write(input_file)
                    zipf.setpassword(password)

                return render_template('download.html', variable=p)
        else:
            return render_template('home.html')
    return render_template('fetch_data.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/pages")
def pages():
    return render_template('pages.html') 


# move back to home page
@app.route("/logout")
def logout():
    resp = make_response(render_template('home.html'))
    resp.delete_cookie('Username')
    return resp


# redirecting to home page
@app.route("/")
def home_page():
    return render_template('home.html')


# run flask app
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_amount_on_form = request.form['strawberry']
    raspberry_amount_on_form = request.form['raspberry']
    apple_amount_on_form = request.form['apple']
    blackberry_amount_on_form = request.form['blackberry']
     # Grab Logan and see if she can help you figureo how to convert the fruit into integers for numbers so we can keep count and display the count back to the person.
     # Also can she help you display the propper time?

    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id_from_form = request.form['student_id']
    count = int(strawberry_amount_on_form) + int(raspberry_amount_on_form) + int(apple_amount_on_form) + int(blackberry_amount_on_form)


   
    
    return render_template("checkout.html", strawberry_amount_on_template=strawberry_amount_on_form, raspberry_amount_on_template=raspberry_amount_on_form, apple_amount_on_template=apple_amount_on_form, blackberry_amount_on_template=blackberry_amount_on_form, first_name_from_template=first_name_from_form, last_name_from_template=last_name_from_form, student_id_from_template=student_id_from_form, count=count)

@app.route('/fruits')         
def fruits():
    
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
from flask import Flask, render_template, redirect, request
import time
from form import *

numb_of_canned_beans = 0

items = ["numberOfSackedBeans", "numberOfCannedBeans"]
item_prises = [1.5, 2.0]
item_count = []
total = 0.0

app = Flask(__name__)
app.config['SECRET_KEY'] = "UHvfbihjdfhj jnlvfdhgu r ikgd vd 45y egb gfjjfn wr"

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   print(form.validate())
   print(form.validate_on_submit())
   print(form.errors)
   if form.validate_on_submit():
      return redirect('/')
   return render_template('login.html', title='Sign In', form=form)

@app.route("/", methods=['GET', 'POST'])
def home():
   global total
   global item_count
   global item_prises
   form = HomeForm()
   if request.method == "POST":
      item_count = []
      total = 0
      for i in range(len(items)):
         count = request.form.get(items[i])
         total += (int(count) * item_prises[i]) * 1.21
         item_count.append(count)
      total = "%.2f" % round(total,2)
      return redirect("cart")
   return render_template('home.html', title='Buy', form=form, item_prises=item_prises)

@app.route("/cart", methods=['GET', 'POST'])
def cart():
   global total
   global item_count
   form = CartForm()
   print(item_count)
   if request.method == "POST":
      if "order" in request.form:
         return redirect("pay")
      item_count = []
      total = 0
      for i in range(len(items)):
         count = request.form.get(items[i])
         total += (int(count) * item_prises[i]) * 1.21
         item_count.append(count)
      total = "%.2f" % round(total,2)
      return render_template("cart.html", form=form, total=total, item_count=item_count)
   return render_template("cart.html", form=form, total=total, item_count=item_count)

@app.route("/pay", methods=['GET', 'POST'])
def pay():
   global total
   if request.method == "POST":
      return redirect("")
   return render_template("pay.html", total=total)

app.run(debug=True)

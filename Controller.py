from flask import Flask , render_template , url_for, flash, redirect
from forms import RegistrationForm

app = Flask(__name__)

sentences = ['hello my name is taehee' , 'Arsenal fuck you']
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

@app.route('/')
def home():
    return render_template('list.html' , template_var = sentences)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        return redirect(url_for('home'))
    return render_template('register.html', form = form)



if __name__ == '__main__':
    app.run(debug=True)
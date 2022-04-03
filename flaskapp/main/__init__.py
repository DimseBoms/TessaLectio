from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flaskapp.main.utils import save_image, create_token, valid_token, process_image, img_to_text


main = Blueprint('main', __name__)

current_year = datetime.now().year


@main.route("/")
def welcome():
    return render_template('main/welcome.html', title='Welcome', current_year=current_year)


@main.route("/ocr")
def ocr():
    return render_template("main/index.html", title='Home', current_year=current_year, token=create_token())


@main.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        if valid_token():
            option = request.form.get('option')
            image = request.files.get('image')
            if image:
                img_name = save_image(image)
                if img_name:
                    img_path = process_image(img_name, arg=option)
                    img_text = img_to_text(img_path)[:-1]
                    if not img_text or img_text.isspace():
                        flash('Was not able to detect any text.', 'warning')
                        return redirect(url_for('main.ocr'))
                    flash('Text has been extracted!', 'success')
                else:
                    flash("File type not supported, try again.", 'warning')
                    return redirect(url_for('main.ocr'))
            else:
                flash("Need an image.", 'danger')
                return redirect(url_for('main.ocr'))
        else:
            flash('Not a valid token, try again.', 'info')
            return redirect(url_for('main.ocr'))

        return render_template("main/result.html", title='Result', current_year=current_year, text=img_text)
    else:
        flash("No result found, try again.", 'warning')
        return redirect(url_for('main.ocr'))


@main.route('/about')
def about():
    return render_template("main/about.html", title='About', current_year=current_year)


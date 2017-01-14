from app import app
from flask import render_template
from flask import request
from flask import flash
import os
@app.route('/')
@app.route('/index',  methods=['GET', 'POST'])

def index():
    #########DEFAULT variables#######
    adocdir='/path/to/asciidoctor-auto-run/adoc/'
    f=''
    req=''
    display=''
    fileContent=''
    filename=''
    debug=''
    update=''
    emptyFileError=False
    successMessage=False
    #################################
    filelist = os.listdir(adocdir)
    if request.method == 'POST':
       #If the save button was clicked
        if "Save" in request.form['submit']:
             #Keep the text area displayed
             display=True
             filename=request.form.get('hidden', "")
             req=filename
             #If we do have a filename 
             if filename != "":
                 update=request.form.get('text', "")
                 wf = open(adocdir+filename, 'w')
                 wf.write(update)
                 f=update
                 successMessage=True
             else:
                 #Probably not possible.. Give them an error
                 emptyFileError=True
        else:
            req=request.form['submit']
            display=True
            f = open(adocdir+req)
            f=f.read()
            update=request.form
    return render_template('index.html', 
    title="Home", 
    filelist=filelist,
    buttonclick=req,
    displayTextArea=display,
    fileContents=f, debug=debug,
    emptyFileError=emptyFileError, 
    successMessage=successMessage)


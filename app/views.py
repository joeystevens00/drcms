from app import app
from flask import render_template
from flask import request
from flask import flash
import os
@app.route('/')
@app.route('/index',  methods=['GET', 'POST'])

def index():

    #Setup vars
    dir='/home/zen/dev/web/asciidoctor-auto-run/adoc/'
    #These don't need editing
    f=""
    req=""
    #Displays the textarea
    display=""
    fileContent=""
    filename=""
    debug=""
    #Value of the textarea
    update=""
    emptyFileError=False
    filelist = os.listdir(dir)	
    if request.method == 'POST':
       #If the save button was clicked
        if "Save" in request.form['submit']:
             #Keep the text area displayed
             display=True
             filename=request.form.get('hidden', "")
             #If we do have a filename 
             if filename != "":
                 update=request.form.get('text', "")
                 wf = open(dir+filename, 'w')
                 wf.write(update)
             else:
                 #User probably clicked save with no file open so show them an error
                 emptyFileError=True
        else:
            req=request.form['submit']
            display=True
            f = open(dir+req)
            f=f.read()
            update=request.form
    return render_template('index.html', title="Home", filelist=filelist, \
    buttonclick=req, displayTextArea=display, fileContents=f, debug=debug, \
    emptyFileError=emptyFileError)


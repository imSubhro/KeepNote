from flask import Flask,jsonify

app= Flask(__name__)

Full_content=[]

@app.route('/')
def home():
    return jsonify({"example_route":[
        "/note/view-all",
        "/note/create/note1/Mycontentnote1",
        "/note/view/note1",
        "/note/update/note1/extracontent",
        "/note/delete/note1"
    ]})


@app.route('/note/view-all')
def view_all():
    return str(Full_content)



@app.route('/note/create/<title>/<content>')
def create_note(title,content):
    mylist= {"title":title, "content":content}
    Full_content.append(mylist)
    return "saved"


@app.route('/note/view/<title>')
def view_note(title):
    for i in Full_content:
        if title==i["title"]:
            return str(i["content"])
        
    return "not found"


@app.route('/note/update/<title>/<content>')
def update_note(title,content):
    for i in Full_content:
        if title==i["title"]:
            old_content=i["content"]
            Total_content= old_content+content
            i.update({"content":Total_content})

            return "update successful"
        
    return "couldnot find"


@app.route('/note/delete/<title>')
def delete_note(title):
    for i in Full_content:
        if title==i["title"]:
            Full_content.remove(i)
            return "delete sucessful"
        
    return "not found"


app.run(debug=True)

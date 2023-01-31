from flask import Flask,render_template,request
import pickle, json
import numpy as np

with open('Log_model.pkl','rb') as file:
    log_reg = pickle.load(file)

with open('project_data.json') as file:
    data = json.load(file)



app = Flask(__name__)

@app.route('/')


@app.route('/Homepage')
def Homepage():
    return render_template('home.html')

@app.route('/submit',methods=['GET'])
def submit():

    Clump_Thickness = request.args.get('Clump_Thickness')
    Uniformity_of_Cell_Size = request.args.get('Uniformity_of_Cell_Size')
    Uniformity_of_Cell_Shape = request.args.get('Uniformity_of_Cell_Size')
    Marginal_Adhesion = request.args.get('Marginal_Adhesion')
    Single_Epithelial_Cell_Size = request.args.get('Single_Epithelial_Cell_Size')
    Bare_Nuclei = request.args.get('Bare_Nuclei')
    Bland_Chromatin = request.args.get('Bland_Chromatin')
    Normal_Nucleoli = request.args.get('Normal_Nucleoli')
    Mitoses = request.args.get('Mitoses')
    

    

    array = np.zeros(len(data['columns']))
    array[0] = Clump_Thickness
    array[1] = Uniformity_of_Cell_Size
    array[2] = Uniformity_of_Cell_Shape
    array[3] = Marginal_Adhesion
    array[4] = Single_Epithelial_Cell_Size
    array[5] = Bare_Nuclei
    array[6] = Bland_Chromatin
    array[7] = Normal_Nucleoli
    array[8] = Mitoses
    
    

    pred = log_reg.predict([array])[0]
    return render_template('after.html', data=pred)

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080)


    

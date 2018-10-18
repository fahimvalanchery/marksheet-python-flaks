from flask import Flask,render_template,request


app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')



@app.route('/result',methods=['GET','POST'])
def reg():
    if(request.method=='POST'):
        rStudDetails=[request.form['name'],request.form['reg_no'],request.form['sem']]
        rSub_Name=[request.form['S1_N'],request.form['S2_N'],request.form['S3_N'],request.form['S4_N']]
        rMarks_Obtained=[int(request.form['S1_M_O']),int(request.form['S2_M_O']),int(request.form['S3_M_O']),int(request.form['S4_M_O'])]
        rTotal_Marks=[int(request.form['S1_T_M']),int(request.form['S2_T_M']),int(request.form['S3_T_M']),int(request.form['S4_T_M'])]
        rPerc=[((rMarks_Obtained[0]/rTotal_Marks[0])*100),((rMarks_Obtained[1]/rTotal_Marks[1])*100),((rMarks_Obtained[2]/rTotal_Marks[2])*100),((rMarks_Obtained[3]/rTotal_Marks[3])*100)]
        
        Grades=[]
        for p in rPerc:
            
            if(p>=90):
                Grades.append("A")
                
                
            elif(p>=80 and p<=89):
                Grades.append("B")
                
                
            elif(p>=70 and p<=79):
                Grades.append("C")
                
                
            elif(p>=60 and p<=69):
                Grades.append("D")
                
                
            else:
                Grades.append("F")
                
        if "F" in Grades:
            status="Failed"
        else:
            status="Passed"

        return render_template('result.html',StudentDetails=rStudDetails,Subjects=rSub_Name,ObtainedMarks=rMarks_Obtained,TotalMarks=rTotal_Marks,resGrade=Grades,res_status=status)
        




if(__name__=='__main__'):
    app.run(debug=True)
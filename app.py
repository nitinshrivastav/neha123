#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def nitin():
    return render_template('mobile.html')
@app.route('/info',methods=['GET','POST'])
def fkjfkjf():
    if(request.method=='POST'):
        num1=int(request.form['a'])
        num2=int(request.form['b'])
        total=num1+num2
        return render_template('mobile.html',nitin=total) 
if __name__=='__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





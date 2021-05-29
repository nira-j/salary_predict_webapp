import joblib
 
model=joblib.load('salary_predict.pk1')
print("\t\tWelcome to my Machine Learning docker app\n")
print("About app:- Application is based on linear regression model of Machine Learning, used to predict ")
print("\t\tsalary of employee based on his/her working experience. ")
print()
out=int(model.predict([[inp]]))
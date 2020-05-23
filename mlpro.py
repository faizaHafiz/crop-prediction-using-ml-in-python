from tkinter import *
root=Tk()
root.title("crop prediction")
root.geometry("600x500+0+0")
def f1():
    import pandas as pd
    d = pd.read_csv('D:/cpdata.csv')
    import numpy as np
    label = np.array(d['labels'])
    d= d.drop('labels', axis = 1)
    d_list = list(d.columns)
    d = np.array(d)
    from sklearn.model_selection import train_test_split
    train_features, test_features, train_labels, test_labels = train_test_split(d, label, test_size = 0.25, random_state =42)
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(train_features, train_labels)
    temp= enttemp.get()
    humid= enthumid.get()
    rain= entrain.get()
    ph= entph.get()
    testfeatures = [[temp,humid,rain,ph]]
    predictions = rf.predict(testfeatures)
    entres = Entry(root, bd=5)
    entres.insert(INSERT, predictions[0])
    entres.place(x=240, y=400)

lblhead = Label(root, text="CROP PREDICTION",font="italic")
lbltemp = Label(root, text="Enter temperature:")
enttemp = Entry(root, width=20)
lblhumid = Label(root, text="Enter Humidity:")
enthumid = Entry(root,width=20)
lblrain = Label(root, text="Enter rainfall in mm:")
entrain = Entry(root, width=20)
lblph = Label(root, text="Enter ph of soil:")
entph = Entry(root, width=20)
btn = Button(root, text="Predict crop",width=20,command=f1)
res = Label(root, text="predicted crop")



lblhead.pack(pady=20)
lbltemp.place(x=10,y=80)
enttemp.pack(pady=20)
lblhumid.place(x=10,y=150)
enthumid.pack(pady=20)
lblrain.place(x=10,y=200)
entrain.pack(pady=20)
lblph.place(x=10,y=260)
entph.pack(pady=20)
btn.pack(pady=30)
res.place(x=10,y=400)

root.mainloop()


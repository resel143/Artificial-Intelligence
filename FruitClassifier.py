from sklearn import tree
features = [[140,1], [130,1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
# claiming 
clf = clf.fit(features, labels)
# making predictions 
print(clf.predict([[150, 0]]))

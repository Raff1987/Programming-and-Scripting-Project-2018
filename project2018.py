import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
    # importing the numpy & matplot libraries to help manipulate the data, and giving them shorthand names
    # Alternately I could import these into iPython while testing. Remember I'm working on a multivariate dataset
data = np.genfromtxt('Data/Iris.csv', delimiter=',')# importing the iris dataset as a csv file using numpy
    
col1 = (data[:,0])    
col2 = (data[:,1])  
col3 = (data[:,2])  
col4 = (data[:,3])  

# Mean,Min,Max and Standard diviation calulation rounded up to one decimal place
def mean(col):
    meancol = (np.mean(data[:,col]))
    return meancol    

print("Sepal Length Mean is:",'{:0.1f}'.format(mean(0)))
print("Sepal Width Mean is:",'{:0.1f}'.format(mean(1)))
print("Petal Length Mean is:",'{:0.1f}'.format(mean(2)))
print("Petal Width Mean is:",'{:0.1f}'.format(mean(3)))

def colmin(col):
    mincol = (np.min(data[:,col]))
    return mincol    

print("Sepal Length min is:",'{:0.1f}'.format(colmin(0)))
print("Sepal Width min is:",'{:0.1f}'.format(colmin(1)))
print("Petal Length min is:",'{:0.1f}'.format(colmin(2)))
print("Petal Width min is:",'{:0.1f}'.format(colmin(3)))   

def colmax(col):
    maxcol = (np.max(data[:,col]))
    return maxcol    

print("Sepal Length Max is:",'{:0.1f}'.format(colmax(0)))
print("Sepal Width Max is:",'{:0.1f}'.format(colmax(1)))
print("Petal Length Max is:",'{:0.1f}'.format(colmax(2)))
print("Petal Width Max is:",'{:0.1f}'.format(colmax(3)))


def colstd(col):
    stdcol = (np.std(data[:,col]))
    return stdcol    

print("Sepal Length std dev is:",'{:0.1f}'.format(colstd(0)))
print("Sepal Width std dev is:",'{:0.1f}'.format(colstd(1)))
print("Petal Length std dev is:",'{:0.1f}'.format(colstd(2)))
print("Petal Width std dev is:",'{:0.1f}'.format(colstd(3)))

# Plotting Histograms using Numpy:
plt.hist(col1) # Histogram showing the sepal length
plt.title('Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('No. of Samples')
plt.show()

plt.hist(col2) # Histogram showing the sepal widths
plt.title('Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('No. of Samples')
plt.show()

plt.hist(col3) # Histogram showing the petal length
plt.title('Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('No. of Samples')
plt.show()

plt.hist(col4) # Histogram showing the petal widths
plt.title('Petal Width')
plt.xlabel('Petal Width(cm)')
plt.ylabel('No. of Samples')
plt.show()

# Scatter plot using matplotlib & seaborn
# Scatter plots show how much one variable is affected by another. The relationship between two variables is called their correlation 
# https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
x=[data[:,0]]
y=[data[:,1]]

plt.scatter(x,y,label='flow',s=30,marker='*')
plt.xlabel('Pepal length (cm)')
plt.ylabel('Sepal width in (cm)')
plt.title('Scatter plot of Sepal')
plt.show()

x=[data[:,2]]
y=[data[:,3]]

plt.scatter(x,y,label='flow',s=30,marker='*')
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.title('Scatter plot of petal')
plt.show()


iris = sns.load_dataset("iris")

ratio = iris["sepal_length"]/iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()

iris = sns.load_dataset("iris")

ratio = iris["petal_length"]/iris["petal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()


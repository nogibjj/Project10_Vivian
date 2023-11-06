import pandas as pd
import matplotlib.pyplot as plt

def f():
    df=pd.read_csv("california_housing_train.csv")

    print(df.shape)
    print(df.shape[0])
    print(df.describe())

    # Bottom 3 house price
    sorted_by_value=df.sort_values('median_house_value', ascending = True)[:3]
    # Calculate the median/mean/standard deviation for the 2022 numbers
    median=df['median_house_value'].dropna().median()
    mean=df['median_house_value'].dropna().mean()
    sd=df['median_house_value'].dropna().std()
    print("Bottom 3 house price: "+str(sorted_by_value))
    print("median is: "+ str(median))
    print("mean is: "+str(mean))
    print("standard deviation is: "+str(sd))

    # Plot a histogram for the house value
    data = df['median_house_value'].dropna()

    # Create histogram
    plt.hist(data, bins=5, edgecolor="k")

    # Add labels and title
    plt.xlabel('median_house_value')
    plt.ylabel('Frequency')
    plt.title('Histogram of median house price')

    # Show plot
    plt.show()
    return 0
    

if __name__ == "__main__":
    f()

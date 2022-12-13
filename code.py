import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def splitting_dataset(path):
    '''
    The function takes Input path of the dataset as returns two dataframes with country name and year as columns
    Parameters
    ----------
    path : String
        The path of the dataset is given here.

    Returns
    -------
    df : dataframe
        dataset with years as the column names
    df2 : dataframe
        dataset with countries as the column names

    '''
    df = pd.read_csv(path)
    df=df.drop(columns=['Indicator Code','Country Code'])
    df2 = pd.DataFrame.transpose(df)
    header = df2.iloc[0].values.tolist()
    df2.columns = header
    df2=df2.iloc[1:]
    return df, df2

country,year=splitting_dataset('dataset.csv')
indicators=year.iloc[0].unique()

country_select=year[['China','India','Canada','United States','United Kingdom']]

def bar(datah,indi):
    '''
    The function plots bar plots for the 5 countries from 2005 to 2019.

    Parameters
    ----------
    datah : dataframe
        dataframe from which data needs to be used
    indi : Numeric values
        indicator to plot

    '''
    l=[]
    s=indi
    for i in range(5):
        l.append(datah.iloc[:,s])
        i=i+1
        s=s+76
    data= pd.DataFrame(l)
    data=data.iloc[:,1:]
    data=data.transpose()
    data.iloc[45:60].plot(kind='bar',figsize=(15,8),xlabel='Years',ylabel=indicators[indi],title=indicators[indi]+' from 2005 to 2019')
    plt.show()
bar(country_select,4) #plotting population growth
bar(country_select,41)#plotting Co2 emission


uk=year[['United Kingdom']] # change to India for other graph

l=[]
s=[4,8,33,49]
for i in s:
    l.append(uk.iloc[:,i])
data= pd.DataFrame(l)
data=data.transpose()
data.columns=data.iloc[0]
data=data[31:60]
data=data[1:]
data=data.fillna(data.mean())

corr = data.corr()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
plt.title(" UK indicators correlation")
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);



def line(datah,indi):
    '''
    The function plots line plots for the 5 countries from 2005 to 2019.

    Parameters
    ----------
    datah : dataframe
        dataframe from which data needs to be used
    indi : Numeric values
        indicator to plot

    '''
    l=[]
    s=indi
    for i in range(5):
        l.append(datah.iloc[:,s])
        i=i+1
        s=s+76
    data= pd.DataFrame(l)
    data=data.iloc[:,1:]
    data=data.transpose()
    data.iloc[45:62].plot(kind='line',figsize=(15,8),xlabel='Year',ylabel=indicators[indi],title=indicators[indi]+' from 2005 to 2019')
    plt.show()
line(country_select,52)
line(country_select,60)










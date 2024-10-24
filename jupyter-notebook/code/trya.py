import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('creditcard.csv')

print(df.shape)
df.head()

df['Class'].hist()
plt.title('Histogram of Fraudulent Transactions')
plt.xlabel('Fraud');
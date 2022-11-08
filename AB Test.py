import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp,shapiro,levene,ttest_ind,pearsonr,mannwhitneyu,spearmanr,kendalltau,f_oneway,kruskal
from statsmodels.stats.proportion import proportions_ztest

df_control = pd.read_excel("Datasets/ab_testing.xlsx",sheet_name="Control Group")
df_test = pd.read_excel("Datasets/ab_testing.xlsx",sheet_name="Test Group")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",10)
pd.set_option("display.float_format",lambda x : "%.5f"%x)

df_control.head()
df_test.head()

def check(dataframe):
    print("#########head#############")
    print(dataframe.head())
    print("#########isnull#############")
    print(dataframe.isnull().sum())
    print("#########shape#############")
    print(dataframe.shape)
    print("#########DESCRİBE#############")
    print(dataframe.describe().T)
check(df_control)
check(df_test)

df = pd.concat([df_test,df_control],ignore_index=True)

#Hipotezlerin oluşturulması
#H0 : M1 = M2 (anlamlı fark yoktur)
#H1 : M1 != M2 (anlamlı fark vardır)

df_test["Purchase"].mean()
df_control["Purchase"].mean()


#Varsayım kontrolleri
#H0 : Varsayım sağlanıyor
#H1 : Varsayım sağlanmıyor

# (1) normalllik varsayımı:
test_stat,pvalue = shapiro(df_test["Purchase"])
print(pvalue)
test_stat,pvalue = shapiro(df_control["Purchase"])
print(pvalue)
#Reddedilir

# (2) Varyans homojenliği:
test_stat,pvalue = levene(df_test["Purchase"],
                           df_control["Purchase"])
print(pvalue)
#Reddedilir

#Nonparametrik test
test_stat,pvalue = mannwhitneyu(df_test["Purchase"],
                           df_control["Purchase"])
print(pvalue)
#H0 hipotezi reddedilir (test ve kontrol verileri arasında anlamlı bir fark vardır.)

#GÖREV 4
#Varsayım kontrollerine göre normallik ve varyans homogenliği sağlanamadığı için nonparametrik test kullanılır.
#Test verisetindeki alım sayıları ortalaması daha yüksektir ve istatistiksel olarak iki veri seti arasında anlamlı bir fark vardır
#Bu anlamda AverageBidding yönteminin daha başarılı bir yöntem olduğunu bilimsel olarak söyleyebiliriz.
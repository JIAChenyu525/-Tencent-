import pandas as pd

titanic = pd.read_excel("D:/wenjian/titanic.xlsx")

print(titanic.head())

# 平均数
a = titanic['Age'].mean()

# Age和Fare的中位数
b = titanic[['Age', 'Fare']].median()

# 计算聚合统计量
c = titanic[['Age', 'Fare']].describe()

# 泰坦尼克号男性和女性乘客的平均年龄分别是多少
d = titanic[['sex', 'Age']].groupby('sex').mean()

# mean 方法将通过传递 numeric_only=True 应用于每个包含数值数据的列
e = titanic.groupby("Sex").mean(numeric_only=True)

# 在分组数据上支持列的选择（像往常一样使用方括号 []）
f = titanic.groupby('Sex')['Age'].mean()

# 每个性别和客舱等级组合的平均票价是多少？
g = titanic.groupby(['Sex', 'Pclass'])['Fare'].mean()

# 用.value_counts()方法统计列中每个类别的记录数
h = titanic['Pclass'].value_counts()
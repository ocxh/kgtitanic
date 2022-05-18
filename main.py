import pandas as pd

#데이터 읽어오기
train = pd.read_csv("./train.csv")
test = pd.read_csv("./test.csv")

#데이터 프레임 확인
#train_head()
#test.head()
#train.describe()

#누락된 값 확인
#train.isnull().sum()
#test.isnull().sum()

#전처리(sex, embarked, name, age, cabin, fare, sibsp, parch, ticket)

#Cabin
#누락값이 많기때문에 지운다
train=train.drop(columns='Cabin')
test=test.drop(columns='Cabin')

#sex
#성별을 숫자로 매핑
sex_map = {"male": 0, "female": 1}
train['Sex'] = train['Sex'].map(sex_map)
test['Sex'] = test['Sex'].map(sex_map)

#Age
#누락된 값 평균으로 채우기
train["Age"] = train["Age"].fillna(train["Age"].mean())
test["Age"] = test["Age"].fillna(test["Age"].mean())

# Pclass
#hot encoding 적용
train['Pclass_3']=(train['Pclass']==3)
train['Pclass_2']=(train['Pclass']==2)
train['Pclass_1']=(train['Pclass']==1)

test['Pclass_3']=(test['Pclass']==3)
test['Pclass_2']=(test['Pclass']==2)
test['Pclass_1']=(test['Pclass']==1)

train=train.drop(columns='Pclass')
test=test.drop(columns='Pclass')

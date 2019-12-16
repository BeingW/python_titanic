import pandas as pd
import matplotlib as plt

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

print(train.shape)
print(test.shape)

# def pie_chart(feature):
#     #들어온 값에 대한 정보를 셋팅한다 ex) female 314, male 577 / Name: Sex, dtype: int6
#     feature_ratio = train[feature].value_counts(sort=False)
#     # print(feature_ratio)
#
#     #들어온 값의 종류에 대한 size 를 구한다. ex) female, male -> 2
#     feature_size = feature_ratio.size
#     # print(feature_size)
#
#     #들어온 값의 종류에 대한 index or key? 를 구한다 ex) Index(['female', 'male'])
#     feature_index = feature_ratio.index
#     # print(feature_index)
#
#     print(train['Survived'])
#     #산사람들 중 feature 값에 대한 데이터를 구한다 ex) female 233, male 109
#     survived = train[train['Survived'] == 1][feature].value_counts()
#     print(survived)
#     #죽은사람 중 feature 값에 대한 데이터를 구한다 ex) female x, male y
#     dead = train[train['Survived'] == 0][feature].value_counts()
#
#     #메인 다이어그램을 나타낸다.
#     plt.plot(aspect='auto')
#     plt.pie(feature_ratio, labels=feature_index, autopct='%1.1f%%')
#     plt.title(feature + ' total')
#     plt.show()
#
#     #feature_index 만큼 enumerate 를 실행한다 ex) Sex -> i = [0, 1], index = ['female', 'male']
#     for i, index in enumerate(feature_index):
#         #feature_index 만큼 다이어그램을 그린다.
#         plt.subplot(1, feature_size + 1, i + 1, aspect='equal')
#         plt.pie([survived[index], dead[index]], labels=['Survived', 'Dead'], autopct='%1.1f%%')
#         plt.title(str(index) + ' ratio')
#     plt.show()
#
# pie_chart('Sex')

# def bar_chart(feature):
#    #train 의 feature 값중 살아있는 사람들의 데이터를 셋팅한다.
#    survived = train[train['Survived']==1][feature].value_counts()
#    #train 의 feature 값중 죽어있는 사람들의 데이터를 셋팅한다.
#    dead = train[train['Survived']==0][feature].value_counts()
#    #살아있는 사람, 죽은 사람의 DataFrame 을 만든다.
#    df = pd.DataFrame([survived,dead])
#    print(df)
#    df.index = ['Survived','Dead']
#    df.plot(kind='bar',stacked=True, figsize=(10,5))
#
# print(bar_chart('Pclass'))




#encoding=utf8
import pandas as pd
import datetime as dt

action_train = pd.read_csv('/home/jdwang/PycharmProjects/tianchi/tianchi_song_data/mars_tianchi_user_actions.csv',header=0)

song_train = pd.read_csv('/home/jdwang/PycharmProjects/tianchi/tianchi_song_data/mars_tianchi_songs.csv',header=0)

# print action_train.head()
# print action_train.describe()
print action_train.info()

# ds_strptime = action_train['Ds'].apply(lambda x: dt.datetime.strptime(x,'%Y%m%d'))
# print ds_strptime
# print dt.datetime.strptime('20150501','%Y%m%d')
# action_train[ ds_strptime < dt.datetime.strptime('20150501','%Y%m%d')]
# print action_train['Ds'].value_counts(sort=False)
# print train[train[0]=='023406156015ef87f99521f3b343f71f'][1].value_counts()
# print train[train[0]=='023406156015ef87f99521f3b343f71f'][3].value_counts()
# print song_train.head()

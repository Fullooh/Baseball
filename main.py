import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#loading the csv data
batting_data = pd.read_csv('batting_stats.cs')
pitching_data = pd.read_csv('pitching_stats.csv')

combined_data = pd.merge(batting_data, pitching_data, on='player_id')

#loading in data
features = combined_data[['last_name', 'first_name', 'player_id', 'year', 'player_age', 'ab', 'pa', 'hit', 'single', 'double', 'triple','home_run', 'strikeout', 'walk', 'k_percent', 'bb_percent', 'batting_avg', 'slg_percent', 'on_base_percent', 'on_base_plus_slg', 'woba' ]]
#target data to predict
target = combined_data[ 'pa','ab','hit','single','double','triple','home_run','strikeout','walk','k_percent','bb_percent','batting_avg','slg_percent','on_base_percent','on_base_plus_slg','woba']

X_train, X_test, y_train, y_test, = train_test_split(features, target, test_size=0.2, random_state= 42)

#x train, this variable 
#x_test, 


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report
from xgboost.sklearn import XGBClassifier
import xgboost as xgb
import numpy as np
import pickle

# Read the data file and convert into a dataframe
def read_csv(path):
    df =  pd.read_csv(path, sep=",")
    return df

# Clean the data by changing the column name and merging multiple features into a single feature
def clean_data(df):
    column_dict = {'vhigh': 'buying', 'vhigh.1': 'maint', '2': 'doors', '2.1': 'persons', 'small': 'lug_boot', 'low': 'safety', 'unacc': 'class_value'}
    df = df.rename(columns=column_dict)
    cols = ['maint', 'doors', 'persons', 'lug_boot', 'safety', 'class_value']
    clean_df = pd.DataFrame()
    clean_df['x_combined'] = df[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
    clean_df['label'] = df['buying']

    return clean_df

# Vectorize the words into numerics using Count Vectorizer and encode the label using LabelEncoder
def preprocess_data(clean_df):
    word_list = clean_df['x_combined'].to_list()
    label_list = clean_df['label'].to_list()

    cv = CountVectorizer()
    label_encoder = LabelEncoder()

    x = cv.fit_transform(word_list)
    y = label_encoder.fit_transform(label_list)

    return x,y

# Create model using XGBClassifier for boosting model performance and computational speed
def create_model(x_train, y_train, x_test, y_test):
    model = XGBClassifier(learning_rate=0.1,
                        n_estimators=1000,
                        max_depth=5,
                        min_child_weight=1,
                        gamma=0,
                        subsample=0.8,
                        colsample_bytree=0.8,
                        objective='multi:softmax',
                        nthread=4,
                        num_class=9,
                        seed=27)
    model.fit(x_train, y_train)

    train = xgb.DMatrix(x_train, label=y_train)
    val = xgb.DMatrix(x_test, label=y_test)
    params = model.get_xgb_params()
    evallist = [(val, 'val'),(train,'train')]
    store = {}
    epochs = 300
    xgb_model = xgb.train(params, train, epochs, evallist,evals_result=store,verbose_eval=100)

    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    
    print("Accuracy: " + str(accuracy))
    print("RMSE: %f" % (rmse))
    print(classification_report(y_test, predictions))
    return model


def main(path):
    df = read_csv(path)
    clean_df = clean_data(df)
    x,y = preprocess_data(clean_df)
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)
    model = create_model(x_train, y_train, x_test, y_test)
    pickle.dump(model, open('./model/car_prediction_model.hdf5', 'wb'))

if __name__ == "__main__":
    path = './data/car.data'
    main(path)
import pickle



if __name__=="__main__":
    filename = './model/car_prediction_model.hdf5'
    loaded_model = pickle.load(open(filename, 'rb'))
    print("Loaded Model: ")
    print(loaded_model)
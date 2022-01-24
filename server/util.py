import json
import pickle
import numpy as np

__location = None
__dataColumns = None
__model = None

def getEstimatedPrice(location, sqft, bath, bhk):
    try:
        loc_index = __dataColumns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__dataColumns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def getLocationName():
    return __location

def loadSavedArtifacts():
    print("Loading saved artifacts...")
    global __location
    global __dataColumns
    global __model

    with open("columns.json", "r") as f:
        __dataColumns = json.load(f)['data_columns']
        __location = __dataColumns[3:]
        # print("Loaded artfacts: " + str(__dataColumns))
    
    with open('D:\Ready\Project\house_pred\house-pred-sc-yt\server\Artifacts\Banglore_home_prices.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("Loaded model: " + str(__model))



if __name__ == '__main__':
    loadSavedArtifacts()
    # print (getLocationName())
    
    print(getEstimatedPrice('1st Phase JP Nagar', 1000, 3, 2))
    print(getEstimatedPrice('kalhalli', 1000, 3, 2))
import json
import pickle

__location = None
__dataColumns = None
__model = None


def getLocationName():
    pass

def loadSavedArtifacts():
    print("Loading saved artifacts...")
    global __location
    global __dataColumns

    with open("./artifacts/columns.json", "r") as f:
        __dataColumns = json.load(f)
        data = json.load(f)
        __location = __dataColumns[3:]
        print("Loaded artfacts: " + str(data))
    
    with open('./artifacts/banglore_home_prices.pickle', 'rb') as f:
        __model = pickle.load(f)
        print("Loaded model: " + str(__model))



if __name__ == '__main__':
    loadSavedArtifacts()
    print (getLocationName())
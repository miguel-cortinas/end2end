import joblib

def predict(data):
    
    model = joblib.load('random_forest_model.pkl')

    pipeline = joblib.load("full_pipeline.pkl")
    data = pipeline.transform(data)
    
    return model.predict(data)
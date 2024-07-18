from app.main import SKLearnModel

if __name__ == '__main__':
    model = SKLearnModel(model_dir='model/', name='test_model')
    model.load()

    # Test with sample input
    test_payload = {
        "instances": [
            {
                "cylinders": 6,
                "displacement": 304.0,
                "horsepower": 150,
                "weight": 3504,
                "acceleration": 10.5,
                "model year": 80,
                "origin": 1
            }
        ]
    }

    prediction = model.predict(test_payload)
    print(prediction)
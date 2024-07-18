import pandas as pd
import kserve
import logging
from joblib import load
import os


class SKLearnModel(kserve.Model):
    def __init__(self, name, model_dir):
        logging.info('Initializing model')
        super().__init__(name)
        self.name = name
        self.model_dir = model_dir
        self.ready = False
        self.model = None
        logging.info('Initializing model done')

    def load(self):
        try:
            logging.info('Loading model')
            self.model = load(os.path.join(self.model_dir, 'linear_regression_model.pkl'))
            logging.info(f'Model {self.model_dir} loaded')
            self.ready = True

        except FileNotFoundError:
            logging.info('File not found')
            self.ready = False

    def predict(self, payload: dict, headers: dict[str, str] = None) -> dict:
        data_df = pd.DataFrame(payload['instances'])
        probabilities = self.model.predict(data_df)
        return {'predictions': probabilities.tolist()}


def main():
    model_path = 'model/'

    model = SKLearnModel(model_dir=model_path, name='test_model')

    model.load()

    kserve.ModelServer(http_port=8082, workers=1).start([model])


if __name__ == '__main__':
    main()

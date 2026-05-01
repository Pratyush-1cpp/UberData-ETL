import pandas as pd


class Extract:
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        data = pd.read_csv(self.file_path)
        return data
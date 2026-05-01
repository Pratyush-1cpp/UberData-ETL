from src.extract import Extract
from src.transform import Transform
from src.load import Load

def run_pipeline():

    extractor = Extract("data/uber.csv")
    transformer = Transform()
    loader = Load()

    df = extractor.run()
    df = transformer.run(df)
    loader.run(df)

if __name__ == "__main__":
    run_pipeline()
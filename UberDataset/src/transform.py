class Transform:

    def run(self, df):
        import pandas as pd

        df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
        df = df.dropna(subset=['pickup_datetime'])

        df['year'] = df['pickup_datetime'].dt.year
        df['month'] = df['pickup_datetime'].dt.month

        print("Transform ✅")
        return df
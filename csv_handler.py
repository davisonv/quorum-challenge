import pandas as pd

class CSVHandler:
    def __init__(self, ):
        pass
    
    def read_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df
    
    def supported_and_opposed_bills_per_legislator(self, vote_results_file_path, legislators_file_path):
        vote_results = self.read_csv(vote_results_file_path)
        legislators = self.read_csv(legislators_file_path)
        combined_df = vote_results.merge(legislators, left_on='legislator_id', right_on='id')

        num_supported_bills = combined_df[combined_df['vote_type'] == 1].groupby('legislator_id').size()
        num_opposed_bills = combined_df[combined_df['vote_type'] == 2].groupby('legislator_id').size()

        summary_df = legislators[['id', 'name']].copy()
        summary_df['num_supported_bills'] = summary_df['id'].map(num_supported_bills).fillna(0).astype(int)
        summary_df['num_opposed_bills'] = summary_df['id'].map(num_opposed_bills).fillna(0).astype(int)

        # Exibir o DataFrame resultante
        summary_df.to_csv('results/legislators-support-oppose-count.csv', index=False)

csv_handler = CSVHandler()

csv_handler.supported_and_opposed_bills_per_legislator("./models/vote_results.csv", "./models/legislators.csv")
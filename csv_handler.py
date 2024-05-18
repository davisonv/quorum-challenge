import pandas as pd

class CSVHandler:
    def __init__(self,):
        self.support_vote = 1
        self.oppose_vote = 2
    
    def read_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df
    
    def supported_and_opposed_bills_per_legislator(self, vote_results_file_path, legislators_file_path):
        # Read CSV files
        vote_results_df = self.read_csv(vote_results_file_path)
        legislators_df = self.read_csv(legislators_file_path)

        # Merge dataframes to get legislators details and vote results
        combined_df = vote_results_df.merge(legislators_df, left_on='legislator_id', right_on='id')

        # Calculate supported and opposed bills per legislator
        num_supported_bills = combined_df[combined_df['vote_type'] == self.support_vote].groupby('legislator_id').size()
        num_opposed_bills = combined_df[combined_df['vote_type'] == self.oppose_vote].groupby('legislator_id').size()


        # Create the summary dataframe by coping id and name columns from legislator's dataframe and adding the counting columns above
        summary_df = legislators_df[['id', 'name']].copy()
        summary_df['num_supported_bills'] = summary_df['id'].map(num_supported_bills).fillna(0).astype(int)
        summary_df['num_opposed_bills'] = summary_df['id'].map(num_opposed_bills).fillna(0).astype(int)

        summary_df.to_csv('results/legislators-support-oppose-count.csv', index=False)

    def process_bills_and_votes(self, bills_file_path, votes_file_path, vote_results_file_path, legislators_file_path):
        # Read CSV files
        bills_df = self.read_csv(bills_file_path)
        votes_df = self.read_csv(votes_file_path)
        vote_results_df = self.read_csv(vote_results_file_path)
        legislators_df = self.read_csv(legislators_file_path)

        # Merge dataframes to get bill details and vote results
        merged_df = bills_df.merge(votes_df, left_on='id', right_on='bill_id', suffixes=('_bill', '_vote'))
        merged_df = merged_df.merge(vote_results_df, left_on='id_vote', right_on='vote_id')

        # Calculate supporter and opposer counts per bill
        supporter_counts = merged_df[merged_df['vote_type'] == self.support_vote].groupby('bill_id').size().reset_index(name='supporter_count')
        opposer_counts = merged_df[merged_df['vote_type'] == self.oppose_vote].groupby('bill_id').size().reset_index(name='opposer_count')

        # Merge counts with bill details
        summary_df = bills_df.merge(supporter_counts, left_on='id', right_on='bill_id', how='left')
        summary_df = summary_df.merge(opposer_counts, left_on='id', right_on='bill_id', how='left')
        
        # Get primary sponsor names
        summary_df = summary_df.merge(legislators_df, left_on='sponsor_id', right_on='id', how='left')
        summary_df.fillna({'name': 'Unknown'}, inplace=True)

        # Drop unnecessary columns and rename columns
        summary_df = summary_df.drop(columns=['sponsor_id', 'bill_id_x', 'bill_id_y' ,'id_y'])
        summary_df = summary_df.rename(columns={'id_x': 'id'})

        summary_df.to_csv('results/bills.csv', index=False)

        

csv_handler = CSVHandler()

csv_handler.supported_and_opposed_bills_per_legislator("./models/vote_results.csv", "./models/legislators.csv")
csv_handler.process_bills_and_votes("./models/bills.csv", "./models/votes.csv", "./models/vote_results.csv", "./models/legislators.csv")
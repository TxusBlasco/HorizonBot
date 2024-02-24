import pandas as pd


def raw_to_df(raw: list[dict]) -> pd.DataFrame:
	df = pd.DataFrame(raw)
	return df


def df_to_csv(df: pd.DataFrame, file_path: str) -> None:
	df.to_csv(file_path, index=False)


def csv_to_df(file_path: str) -> pd.DataFrame:
	df = pd.read_csv(file_path)
	return df


def compare_df(last_df: pd.DataFrame, new_df: pd.DataFrame) -> dict[str, pd.DataFrame]:
	"""
	Compares the last and new dataframes containing grant details. If some grants are unique to the last_df,
	they are added as the value to the 'deleted' key. I some grants are unique to the new_df, they are added to 'added'.
	:param last_df: old dataframe containing grant info
	:param new_df: new df containing grant info
	:return: a dictionary of two dataframes, one for deleted grants and other one for newly added grants
	"""
	merged_df = pd.merge(
		last_df,
		new_df,
		how='outer',
		on=['title', 'id', 'funding_type', 'program', 'status', 'grant_or_tender', 'topic', 'deadline_model',
		    'opening_date', 'closing_date'],
		indicator=True)
	deleted = merged_df[merged_df['_merge'] == 'left_only'].copy()
	deleted.drop(columns=['_merge'], inplace=True)
	added = merged_df[merged_df['_merge'] == 'right_only'].copy()
	added.drop(columns=['_merge'], inplace=True)
	diff = {'deleted': deleted, 'added': added}
	return diff

def cleaning(df):
    """
    This is what this function is for
    """
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
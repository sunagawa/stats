def cleanse_dataframe(df, Y=None, drops=[], dummies=[]):
    """automatically converts a dataframe to a scikit-learn analizable format (for the prototyping purpose)"""
    df = pd.concat([
        df.drop(np.concatenate([drops, dummies]), axis=1),
        *[pd.get_dummies(df[dummy], drop_first=True) for dummy in dummies]
    ], axis=1)
    return df.drop(Y, axis=1), df.get(Y)

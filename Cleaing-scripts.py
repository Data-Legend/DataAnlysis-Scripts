import pandas as pd


def drop_duplicates(df):
    return df.drop_duplicates()


def drop_missing(df, missing_value=None, missing_threshold=0, axis=1):
    if missing_value is not None:
        df = df.replace(missing_value, pd.NA)

    missing_percent = df.isna().sum() / len(df) * 100
    if axis == 1:
        return df.loc[:, missing_percent <= missing_threshold]
    else:
        return df.loc[missing_percent <= missing_threshold, :]


def fill_missing(df, method='mean', fill_value=None):
    if method == 'mean':
        return df.fillna(df.mean(), inplace=True)
    elif method == 'median':
        return df.fillna(df.median(), inplace=True)
    elif method == 'mode':
        return df.fillna(df.mode().iloc[0], inplace=True)
    elif method == 'value':
        return df.fillna(fill_value, inplace=True)
    else:
        raise ValueError("Invalid method. Use 'mean', 'median', or 'mode'.")


def remove_special_characters(df):
    for column in df.columns:
        if df[column].dtype == object:
            df[column] = df[column]._str.replace('[^A-Za-z0-9\s]+', '')

    return df


def rename_columns(df, rename_dict):
    return df.rename(columns=rename_dict, inplace=True)


def replace_values(df, replace_dict):
    return df.replace(replace_dict, inplace=True)


def lowercase_column_names(df):
    return df.rename(columns=lambda x: x.lower(), inplace=True)


def clean_dataset(df, drop_duplicate_rows=True, drop_duplicate_columns=True, 
                  drop_high_missing_columns=True, missing_column_threshold=90,
                  missing_value=None, fill_method='mean', fill_value=None,
                  replace_dict=None, rename_dict=None, remove_special_chars=True,
                  lowercase_columns=True):
    
    if drop_duplicate_rows:
        df = drop_duplicates(df)

    if drop_duplicate_columns:
        df = df.T.drop_duplicates().T
        
    if drop_high_missing_columns:
        df = drop_missing(df, missing_value=missing_value, missing_threshold=missing_column_threshold, axis=1)
    
    fill_missing(df, method=fill_method, fill_value=fill_value)
    
    if rename_dict is not None:
        rename_columns(df, rename_dict)
    
    if replace_dict is not None:
        replace_values(df, replace_dict)

    if remove_special_chars:
        df = remove_special_characters(df)

    if lowercase_columns:
        lowercase_column_names(df)

    return df


if __name__ == '__main__':
    dt = pd.read_csv("your_dataset.csv")

    cleaned_data = clean_dataset(dt)
    cleaned_data.to_csv("cleaned_dataset.csv", index=False)

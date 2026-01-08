def transform(legacy_data):
    data = {i.lower(): num for num in legacy_data.keys() for i in legacy_data[num]}

    return data
    
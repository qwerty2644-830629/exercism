def transform(legacy_data):
    return {i.lower(): num for num in legacy_data.keys() for i in legacy_data[num]}
    
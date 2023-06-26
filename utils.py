# from sklearn.preprocessing import MinMaxScaler

# feature_ranges = {
#     'Air temperature [K]': (295, 310),
#     'Process temperature [K]': (300, 320),
#     'Rotational speed [rpm]': (1150, 2890),
#     'Torque [Nm]': (2, 80),
#     'Tool wear [min]': (10, 260),
#     'Power': (2*10, 80*260)
#     }

# scaler = MinMaxScaler(feature_range=(0, 1))

# Preprocessing function
def preprocess_input(input_data):
    # Map 'Type' column
    input_data['Type'] = input_data['Type'].map({
        'L - Lower Grade': 0,
        'M - Medium Grade': 1,
        'H - High Grade': 2
    })

    # # Scale numerical features using the defined feature ranges
    # for feature, (min_val, max_val) in feature_ranges.items():
    #     input_data[feature] = (input_data[feature] - min_val) / (max_val - min_val)

    # # Apply scaling to the input data
    # scaled_input_data = scaler.transform(input_data)

    # return scaled_input_data
    return input_data

columns = ['Type', 'Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Power']

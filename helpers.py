#preprocessing helper function
def preprocess(data):
    nested_features = ['video', 'author', 'music', 'stats', 'authorStats', 'challenges','duetInfo', 'textExtra', 'stickersOnItem']
    skip_features = ['challenges','duetInfo', 'textExtra', 'stickersOnItem' ]

    #creating blank dictionary
    flattened_data = {}
    #looping through each data
    for idx, value in enumerate(data):
        flattened_data[idx] = {}
        #looping through each value in each data
        for feat_idx, feat_value in value.items():
            #checking if feature in data is nested
            if feat_idx in nested_features:
                #checking if its a needed feature
                if feat_idx in skip_features:
                    pass
                else:
                    #looping nested features
                    for nested_idx, nested_value in feat_value.items():
                        flattened_data[idx][feat_idx+'_'+nested_idx] = nested_value
            #adding non nested features back to the flattened dictionary       
            else:
                flattened_data[idx][feat_idx] = feat_value

    return flattened_data
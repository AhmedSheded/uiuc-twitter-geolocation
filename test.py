import pickle


with open('data/user_states_train.pickle', 'rb') as handle:
    states_train = pickle.load(handle)

with open('data/user_states_test.pickle', 'rb') as handle:
    states_test = pickle.load(handle)

with open('data/user_states_dev.pickle', 'rb') as handle:
    states_dev = pickle.load(handle)
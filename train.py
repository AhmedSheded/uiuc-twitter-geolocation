import argparse
from data import twus

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--training_data", help="Path to training data set.", default='./na/user_info.dev')
    parser.add_argument("-e", "--epochs", type=int, default=5)
    parser.add_argument("--max_words", type=int, help="Max number of words to analyze per user.", default=500)
    parser.add_argument("--vocab_size", type=int, help="Use the top N most frequent words.", default=50000)
    parser.add_argument("-b", "--batch_size", type=int, help="Batch size.", default=32)
    parser.add_argument("--tensorboard", action="store_true", help="Track training progress using Tensorboard.")
    args = parser.parse_args()

    from models.twitter_geomodel import Model

    x_train, y_train, x_dev, y_dev, x_test, y_test = twus.load_state_data()

    geoModel = Model(num_outputs=53, epochs=args.epochs, batch_size=args.batch_size, time_steps=args.max_words,
                     vocab_size=args.vocab_size, use_tensorboard=args.tensorboard)


    geoModel.train(x_train, y_train, x_dev, y_dev)
    # geoModel.save_model()

def get_confusion(data_iter, model):
    # Reset data iter so that it starts from batch 0
    data_iter.reset()
    samples = ((data_iter.samples//data_iter.batch_size))*32
    prog = tf.keras.utils.Progbar(target=samples)
    # Initialize empty arrays to store values
    y_true = np.empty(shape=(samples, OUTPUT_SHAPE[0]), dtype=np.float32)
    y_predict = np.empty(shape=(samples, OUTPUT_SHAPE[0]), dtype=np.float32)
    X = np.empty(shape=((data_iter.batch_size,) + INPUT_SHAPE[:]), dtype=np.float32)
    # For every batch,
    a, b = (0, 0,)
    for i in range((samples//data_iter.batch_size)-2):
        try:
            # Get X and y_true
            X[:], y_temp = data_iter.next()
            b += y_temp.shape[0]
            prog.update(b)
            y_true[a : b] = y_temp
            # predict X and y
            y_predict[a : b] = model.predict(X, verbose=0)
            a = b
        except ValueError:
            return y_predict, y_true, a, b
    return y_predict, y_true, a, b#, #sklearn.metrics.confusion_matrix(y_true, y_predict)
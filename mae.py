def MAE(true_labels, pred_labels):
    n = len(true_labels)
    tot = 0
    for i in range(n):
       tot += abs(true_labels[i] - pred_labels[i])
    mae = tot/ n   
    return mae
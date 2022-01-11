import numpy as np


def calculate(lst: list):
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    a = np.array(lst)
    am = a.reshape(3, 3)
    res = dict()
    funcdict = {
        "mean": np.mean,
        "var": np.var,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
        "std": np.std
    }
    for key in funcdict.keys():
        res[key] = [funcdict[key](am, axis=0), funcdict[key](am, axis=1), funcdict[key](a)]
    res["variance"] = res.pop("var")
    res["standard deviation"] = res.pop("std")

    return res

from datetime import datetime, timedelta


def to_cst(dt: datetime):
    return dt + timedelta(hours=8)


def exp_calc(x, y, x1, power=1.5):
    z = x ** power
    r = y / z
    z1 = x1 ** power
    y1 = z1 * r
    return y1

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sqr_k(x, k, yp=1.0, eps=1.0e-5):
    yc = yp + (x / yp ** (k-1) - yp) / k
    if abs(yc - yp) <= eps:
        return yc
    else:
        return sqr_k(x, k, yc)


if __name__ == '__main__':
    x1 = float(input("Введите x - "))
    k1 = int(input("Введите степень k - "))
    sqr = sqr_k(x1, k1)
    print("Корень степени", k1, "из", x1, "=", sqr)
    print("Проверка -", sqr, "**", k1, "=", sqr ** k1)


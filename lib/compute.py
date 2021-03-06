import math
import statistics


def compute_average_and_stdev(list):
    return (statistics.mean(list), statistics.stdev(list))


def compute_u_from_delta_p(delta_p, rho):
    return math.sqrt(float(delta_p)*2/float(rho))


def turbulence_intensity_from_u(u, stdev_u):
    return float(stdev_u)/float(u)

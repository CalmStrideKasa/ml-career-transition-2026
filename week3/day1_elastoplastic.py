def compute_stress_elastoplastic(strain: float, E: float, sigma_y: float, H: float = 0.0) -> float:
    epsilon_y = sigma_y / E
    sigma_elastic = E * strain

    if abs(sigma_elastic) <= sigma_y:
        sigma = sigma_elastic
    else:
        sign = 1 if strain > 0 else -1
        sigma = sign * sigma_y + H * (strain - sign * epsilon_y)

    return sigma
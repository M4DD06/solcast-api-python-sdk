from .api import Client, Response
from .urls import (
    base_url,
    forecast_rooftop_pv_power,
    forecast_radiation_and_weather,
    forecast_advanced_pv_power,
)


def radiation_and_weather(
    latitude: float, longitude: float, output_parameters: str, **kwargs
) -> Response:
    """
    Get irradiance and weather forecasts from the present time up to 14 days ahead
    for the requested location, derived from satellite (clouds and irradiance
    over non-polar continental areas, nowcasted for approx. four hours ahead)
    and numerical weather models (other data and longer horizons).
    """
    client = Client(base_url=base_url, endpoint=forecast_radiation_and_weather)

    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "output_parameters": output_parameters,
            "format": "json",
            **kwargs,
        }
    )


def rooftop_pv_power(
    latitude: float, longitude: float, output_parameters: str, **kwargs
) -> Response:
    """
    Get basic rooftop PV power forecasts from the present time up to 14 days ahead
    for the requested location, derived from satellite (clouds and irradiance
    over non-polar continental areas, nowcasted for approx. four hours ahead)
    and numerical weather models (other data and longer horizons).

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=forecast_rooftop_pv_power)

    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "output_parameters": output_parameters,
            "format": "json",
            **kwargs,
        }
    )


def advanced_pv_power(resource_id: int, **kwargs) -> Response:
    """
    Get high spec PV power forecasts from the present time up to 14 days ahead
    for the requested site, derived from satellite (clouds and irradiance over
    non-polar continental areas, nowcasted for approx. four hours ahead) and
    numerical weather models (other data and longer horizons).

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=forecast_advanced_pv_power)

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})

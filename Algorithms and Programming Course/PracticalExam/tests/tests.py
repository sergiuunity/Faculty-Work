from repository.station import Station
from domain.measurement import Measurement


def test_validation():
    try:
        test_station = Station([Measurement(12, 30, 70), Measurement(13, 30, 20), Measurement(13, 45, 50)])
        test_station.add_measurement(Measurement(-5, 10, 6))
        assert False
    except ValueError:
        assert True
    try:
        test_station = Station([Measurement(12, 30, 70), Measurement(13, 30, 20), Measurement(13, 45, 50)])
        test_station.add_measurement(Measurement(1, 61, 590))
        assert False
    except ValueError:
        assert True

    try:
        test_station = Station([Measurement(12, 30, 70), Measurement(13, 30, 20), Measurement(13, 45, 50)])
        test_station.add_measurement(Measurement(0, 14, 2))
        assert True
    except ValueError:
        assert False

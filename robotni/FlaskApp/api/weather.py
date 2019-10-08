from pyowm import OWM
import apiconfig

api_token = apiconfig.owm_token
owm = OWM(api_token)


def get_weather_info():
    obs = owm.weather_at_place('Claremont,CA')
    # time = obs.get_reception_time(timeformat='iso')
    # date = obs.get_reception_time(timeformat='date')

    # w = obs.get_weather()
    # fc = owm.daily_forecast('Claremont,CA', limit=5)
    # f = fc.get_forecast()
    return obs

info = get_weather_info()

if info is not None:
    print('Info: ')
    print(info)
    print()
else:
    print('[!] Request Failed')

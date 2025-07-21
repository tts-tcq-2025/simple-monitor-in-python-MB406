
def temperature_is_ok(temperature):
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False
    return True

def soc_is_ok(soc):
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False
    return True

def charge_rate_is_ok(charge_rate):
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    if not temperature_is_ok(temperature):
        return False
    if not soc_is_ok(soc):
        return False
    if not charge_rate_is_ok(charge_rate):
        return False
    return True

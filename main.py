import ru_local as ru

print(ru.WRITE_THE_COUNT_OF_DAYS)

count_days = float(input())
dist_miles = 16_637_000_000
spd_miles = 38_241
waves_spd_meter = 299_792_458
au_in_meters = 149_597_870_700

current_dist = count_days * 24 * spd_miles + dist_miles
number_miles = current_dist
numbers_km = number_miles * 1.61
numbers_au = numbers_km * 1000 / au_in_meters
delay_seconds = numbers_km * 1000 / waves_spd_meter
delay_hours = delay_seconds / 3600

print(ru.NUMBER_MILES, number_miles)
print(ru.NUMBER_KM, numbers_km)
print(ru.NUMBER_AU, numbers_au)
print(ru.DELAY_HOURS, delay_hours)

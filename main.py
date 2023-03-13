import ru_local as ru
print(ru.WRITE_THE_COUNT_OF_DAYS)
count_days = float(input())
distance_miles = 16637000000
speed_miles = 38241
radio_waves_speed_meter = 299792458
au_in_meters = 149597870700
current_distance = count_days * 24 * speed_miles + distance_miles
number_of_miles = current_distance
numbers_of_kilometers = number_of_miles * 1.61
numbers_of_au = numbers_of_kilometers * 1000 / au_in_meters
delay_in_seconds = numbers_of_kilometers * 1000 / radio_waves_speed_meter
delay_in_hours = delay_in_seconds / 3600
print(ru.NUMBER_OF_MILES, number_of_miles)
print(ru.NUMBER_OF_KILOMETERS, numbers_of_kilometers)
print(ru.NUMBER_OF_AU, numbers_of_au)
print(ru.DELAY_IN_HOURS, delay_in_hours)
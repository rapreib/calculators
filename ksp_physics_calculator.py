import math

TONS_TO_KG = 1000
GRAVITY = 9.8
AIR_DENSITY = 1.3
Cd = 1.0

mass0 = 0
mass1 = 0
fuel = 0
velocity = 0
duration = 0
avg_velocity = 0

mass0 = float(raw_input("Mass0 in tons: "))
fuel = float(raw_input("Mass of fuel in tons: "))
velocity = float(raw_input("Change in velocity: "))
duration = float(raw_input("Duration of flight in seconds: "))
area = float(raw_input("Area: "))

mass1 = mass0 - fuel
avg_accel = velocity / duration
mass0 = mass0 * TONS_TO_KG
mass1 = mass1 * TONS_TO_KG

mass0_str = "{:,}".format(mass0)
mass1_str = "{:,}".format(mass1)
print("\nMasses in kg: %s, %s" % (mass0_str, mass1_str))

#-----EXHAUST VELOCITY (V_e)-----
# Exhaust velocity = delta v / ln(mass0 / mass1)
# Rocket Equation: delta v = v_e * ln(mass0 / mass1)
ve = velocity / math.log((mass0 / mass1))
ve_str = "{:,}".format(ve)
print("Exhaust Velocity (Ve) = %s m/s" % ve_str)

#-----MASS FLOW RATE (M_fr)-----
# Mfr = total fuel mass / time of burn
massfr = fuel / duration
massfr_str = "{:,}".format(massfr)
print("Mass Flow Rate = %s kg/s" % massfr_str)

#-----THRUST (T)-----
# Thrust = mass flow rate * exhaust velocity
thrust = ve * massfr
thrust_str = "{:,}".format(thrust)
print("Thrust = %s N" % thrust_str)

#-----GRAVITY (F_g)-----
# Fg = mass * gravity
fg = mass0 * GRAVITY
fg_str = "{:,}".format(fg)
print("Fg = %s N" % fg_str)

#-----AIR RESISTANCE (F_d)-----
# Fd = 1/2 * air density * area * drag coefficient * velocity^2
fd = 0.5 * AIR_DENSITY * area * Cd * avg_velocity * avg_velocity
fd_str = "{:,}".format(fd)
print("Fd = %s N" % fd_str)

'''
#-----THRUST-----
thrust = mass0 * avg_accel
thrust_str = "{:,}".format(thrust)
print("Thrust = %s N" % thrust_str)

#-----TOTAL FORCE-----
ftotal = thrust - fg - fd
ftotal_str = "{:,}".format(ftotal)
print("Ftotal = %s N" % ftotal_str)

#-----MASS FLOW RATE-----
massfr = thrust / ve
massfr_str = "{:,}".format(massfr)
print("Mass Flow Rate = %s kg/s" % massfr_str)

#-----SANITY CHECK (CALCULATE FUEL BURNED)-----
fuel_mass_check = massfr * duration / TONS_TO_KG
fuel_mass_check_str = "{:,}".format(fuel_mass_check)
check_result = "FAILED"
if fuel_mass_check == fuel:
    check_result = "PASSED"
print("Sanity check: Fuel Mass = %s t\tCheck %s" % (fuel_mass_check_str, check_result))
'''

#-----TOTAL FORCE (F_total)-----
# Ftotal = thrust - Fg - Fd
ftotal = thrust - fg - fd
ftotal_str = "{:,}".format(ftotal)
print("Ftotal = %s N" % ftotal_str)

#-----SANITY CHECK (CALCULATE AVG ACCEL)-----
# Thrust = mass0 * average acceleration
avg_accel_check = thrust / mass0
check_str = "{:,}".format(avg_accel_check)
print("Sanity check: Avg Acceleration = %s" % (check_str))

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

#----EXHAUST VELOCITY----
ve = velocity / math.log((mass0 / mass1))
ve_str = "{:,}".format(ve)
print("Exhaust Velocity (Ve) = %s m/s" % ve_str)

#-----GRAVITY------
fg = mass0 * GRAVITY
fg_str = "{:,}".format(fg)
print("Fg = %s N" % fg_str)

#----AIR RESISTANCE------
fd = 0.5 * AIR_DENSITY * area * Cd * velocity * velocity
fd_str = "{:,}".format(fd)
print("Fd = -%s N" % fd_str)

#----THRUST--------
thrust = mass0 * avg_accel
thrust_str = "{:,}".format(thrust)
print("Thrust = %s N" % thrust_str)

#-----TOTAL FORCE-----
ftotal = thrust - fg - fd
ftotal_str = "{:,}".format(ftotal)
print("Ftotal = %s N" % ftotal_str)

#-----MASS FLOW RATE----
massfr = thrust / ve
massfr_str = "{:,}".format(massfr)
print("Mass Flow Rate = %s kg/s" % massfr_str)

#----SANITY CHECK (CALCULATE FUEL BURNED)-----
fuel_mass_check = massfr * duration / TONS_TO_KG
fuel_mass_check_str = "{:,}".format(fuel_mass_check)
check_result = "FAILED"
if fuel_mass_check == fuel:
    check_result = "PASSED"
print("Sanity check: Fuel Mass = %s t\tCheck %s" % (fuel_mass_check_str, check_result))

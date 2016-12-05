import math

TONS_TO_KG = 907.18474000000008192
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
velocity = float(raw_input("Maximum velocity: "))
duration = float(raw_input("Duration of flight in seconds: "))
length = float(raw_input("Length: "))
width = float(raw_input("Width: "))

mass1 = mass0 - fuel
avg_accel = velocity / duration
mass0 = mass0 * TONS_TO_KG
mass1 = mass1 * TONS_TO_KG

print("Masses %d %d" % (mass0, mass1))

ve = velocity / math.log((mass0 / mass1))
ve_str = "{:,}".format(ve)
print("\nExhaust Velocity (Ve) = %s m/s" % ve_str)

fg = mass0 * GRAVITY
fg_str = "{:,}".format(fg)
print("Fg = %s N" % fg_str)

fd = -0.5 * AIR_DENSITY * (length * width) * Cd * velocity * velocity
fd_str = "{:,}".format(fd)
print("Fd = %s N" % fd_str)

thrust = mass0 * avg_accel
thrust_str = "{:,}".format(thrust)
print("Thrust = %s N" %thrust_str)

ftotal = thrust - fg - fd
ftotal_str = "{:,}".format(ftotal)
print("Ftotal = %s N" % ftotal_str)


# Idea Gas Law
# PV = nRT
def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    R = 0.082
    temp += 273.15
    p1 = n1 * R * temp / volume
    p2 = n2 * R * temp / volume
    return p1 + p2

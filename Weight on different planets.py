"""
                         Weight on Earth 
 Weight on any planet =  --------------- x Gravitational force on that planet
                           9.81 m/s^2

<---- Gravitational forces of different planets, dwarf planets and moons ---->

Mercury has gravitational force of 3.7 m/s^2
Venus has gravitational force of 8.87 m/s^2
Earth has gravitational force of 9.81 m/s^2
Mars has gravitational force of 3.721 m/s^2
Jupiter has gravitational force of 24.79 m/s^2
Saturn has gravitational force of 10.44 m/s^2
Uranus has gravitational force of 8.87 m/s^2
Neptune has gravitational force of 11.15 m/s^2

------------- Dwraf Planets --------------

Pluto has gravitational force of 0.62 m/s^2
Eris has gravitational force of 0.82 m/s^2
Ceres has gravitational force of 0.27 m/s^2

------------------ Moons -----------------

Moon has gravitational force of 1.622 m/s^2
Encelaedus has gravitational force of 0.113 m/s^2
Titan has gravitational force of 1.352 m/s^2
Europa has gravitational force of 1.315 m/s^2
IO has gravitational force of 1.796 m/s^2
Ganymede has gravitational force of 1.428 m/s^2
Callisto has gravitational force of 1.236 m/s^2
Cyllene has gravitational force of 0.001 m/s^2

"""

w = float(input("Enter Your Weight in KGs: "))

mer_w = w * 0.377
ven_w = w * 0.904
ear_w = w * 1.000
mar_w = w * 0.379
jup_w = w * 2.527
sat_w = w * 1.064
ura_w = w * 0.904
nep_w = w * 1.136

plu_w = w * 0.063
eri_w = w * 0.083
cer_w = w * 0.0275

tit_w = w * 0.1378
eur_w = w * 0.134
io_w = w * 0.1830
gan_w = w * 0.1455
cal_w = w * 0.1259
cyl_w = w * 0.000010
enc_w = w * 0.0113
moon_w = w * 0.165

print('Your weight on Mercury planet: ', mer_w)
print('Your weight on Venus planet: ', ven_w)
print('Your weight on Earth planet: ', ear_w)
print('Your weight on Mars planet: ', mar_w)
print('Your weight on Jupiter planet: ', jup_w)
print('Your weight on Saturn planet: ', sat_w)
print('Your weight on Uranus planet: ', ura_w)
print('Your weight on Neptune planet: ', nep_w)

print('Your weight on Pluto dwarf planet: ', plu_w)
print('Your weight on Eris dwarf planet: ', eri_w)
print('Your weight on Ceres dwarf planet: ', cer_w)

print('Your weight on Moon: ', moon_w)
print('Your weight on saturn\'s moon Encelaedus: ', enc_w)
print('Your weight on jupiter\'s moon Titan: ', tit_w)
print('Your weight on jupiter\'s moon Europa: ', eur_w)
print('Your weight on jupiter\'s moon IO: ', io_w)
print('Your weight on jupiter\'s moon Ganymede: ', gan_w)
print('Your weight on jupiter\'s moon Callisto: ', cal_w)
print('Your weight on jupiter\'s moon Cyllene: ', cyl_w)

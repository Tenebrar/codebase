# Adapted to be in 1 file and ran via https://www.jdoodle.com/execute-ada-online

# with Ada.Text_IO; use Ada.Text_IO;
# with Ada.Float_Text_IO; use Ada.Float_Text_IO;
# with Ada.Text_IO, Calendar;
# use Ada.Text_IO, Calendar;
#
# procedure jdoodle is
#     X_initial : FLOAT := 0.0;
#     M         : FLOAT := 1.0;
#     A         : FLOAT := 7.0;
#     C         : FLOAT := 13.0 / 31.0;
#     Temp         : FLOAT;
#     Natural_Temp : NATURAL;
# begin
#     X_Initial := 0.1;
#
#     Temp := A * X_Initial + C;
#     Natural_Temp := NATURAL(Temp - 0.5);
#     Temp := Temp - FLOAT(Natural_Temp);
#     X_Initial := Temp;
#     Put(Temp, 2, 6, 0);
#
#     Temp := A * X_Initial + C;
#     Natural_Temp := NATURAL(Temp - 0.5);
#     Temp := Temp - FLOAT(Natural_Temp);
#     X_Initial := Temp;
#     Put(Temp, 2, 6, 0);
# end jdoodle;

# Result: '0.119355 0.254839'

# Converted from Ada

X_initial = 0.0
M = 1.0
A = 7.0
C = 13.0 / 31.0


def set_seed():
    global X_Initial
    X_Initial = 0.1


def random_number():
    global A
    global X_Initial
    global C
    Temp = A * X_Initial + C
    Natural_Temp = int(Temp - 0.5)
    Temp = Temp - float(Natural_Temp)
    X_Initial = Temp
    return Temp


set_seed()
print(f' {random_number():.7} {random_number():.7}')

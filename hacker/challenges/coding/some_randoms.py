# Adapted to be in 1 file and ran via https://www.jdoodle.com/execute-ada-online

# with Ada.Text_IO; use Ada.Text_IO;
# with Ada.Float_Text_IO; use Ada.Float_Text_IO;
# with Ada.Text_IO, Calendar;
# use Ada.Text_IO, Calendar;
#
# procedure jdoodle is
#     X_initial : FLOAT := 0.0;
#     M         : FLOAT := 1.0;
#     a         : FLOAT := 7.0;
#     c         : FLOAT := 13.0 / 31.0;
#     Temp         : FLOAT;
#     Natural_Temp : NATURAL;
# begin
#     x_initial := 0.1;
#
#     Temp := a * x_initial + c;
#     Natural_Temp := NATURAL(Temp - 0.5);
#     Temp := Temp - FLOAT(Natural_Temp);
#     x_initial := Temp;
#     Put(Temp, 2, 6, 0);
#
#     Temp := a * x_initial + c;
#     Natural_Temp := NATURAL(Temp - 0.5);
#     Temp := Temp - FLOAT(Natural_Temp);
#     x_initial := Temp;
#     Put(Temp, 2, 6, 0);
# end jdoodle;

# Result: ' 0.119355 0.254839'


# Converted from Ada (Unused parts of code removed)
class Random:
    def __init__(self):
        self.a = 7.0
        self.c = 13.0 / 31.0
        self.x_initial = 0.0  # The Ada code has X_initial and X_Initial (capitalization differs), but only 1 is used

    def set_seed(self, value):
        # The Ada code does a lot of things with the time which are then ignored
        self.x_initial = value

    # The Ada code makes a function force_seed which is never called

    def random_number(self):
        temp = self.a * self.x_initial + self.c
        natural_temp = round(temp - 0.5)  # int conversion in Ada rounds
        temp = temp - float(natural_temp)
        self.x_initial = temp
        return temp


def put(item, fore, aft, exp):
    if exp != 0:
        raise NotImplementedError('Only functionality with exp 0 is currently implemented')
    aft = aft or 1

    base = f'{item:.{aft}}'
    print(' ' * (max(0, fore - base.index('.'))) + base, end='')


# Result: ' 0.119355 0.254839'
r = Random()
r.set_seed(0.1)
for index in range(2):
    put(r.random_number(), 2, 6, 0)

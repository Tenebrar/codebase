from hacker.hackvm.hackvm import HackVm

value = '79+3>111++<9+3>0<1+0>999**0<:6?084*-g1111++*<p'

result = HackVm(max_iterations=100000).run(value)

print(result)

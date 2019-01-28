from hacker.hackvm.hackvm import HackVm

program = '0<0<1</1<*-p'

result = HackVm().run(program, [21, 8])

print(result)

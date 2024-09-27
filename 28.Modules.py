# module = a file containing code you want to include in your program. Use "import" to include a module (built-in or your own)
# useful to break up a large program reusuable separate files

# print(help("modules")) # common ones include math and time module

import math
import math as m #changes math.pi to m.pi
from math import pi # import something specific. no longer need to do math.pi and can just use pi. becareful for name conflicts

print(m.pi)
print(pi)


#created my own module called "ModulesPractice28"
import ModulesPractice28

result = ModulesPractice28.pi
print(result)
result = ModulesPractice28.square(3)
print(result)


from idautils import *
from idaapi import *

ea = ScreenEA()
calls = [0x416d13,0x403a1e,0x4030d6,0x4031b6,0x40648f,0x4028ea,0x40652f,0x40667b,0x4065c3,0x403776,0x40336e,0x40383a,0x40670f,0x407826,0x41470d,0x411edc,0x411f35,0x40a7a7,0x40114e,0x4155f4,0x415636,0x415600,0x415606,0x415630,0x40112b,0x414101,0x4120db]
for call in calls:
    print "%08x %s"%(call, GetFunctionName(call))

print "-----"
calls2 = [0x00411F35,0x00416d13,0x00403A1e,0x0043F49C,0x0043F4A6,0x004030D6,0x0043F4D8,0x004031B6,0x0043F4Ec,0x0040648F,0x0043F500,0x004028EA,0x0041470D,0x00411EDC,0x00411F35,0x0043F604,0x0040A7A7]
for call in calls2:
    print "%08x %s"%(call, GetFunctionName(call))

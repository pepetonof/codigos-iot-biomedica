# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import uos
uos.dupterm(None, 1)#disable REPL on UART(0)

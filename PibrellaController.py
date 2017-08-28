import pibrella
import time

var = 1

while var == 1 :

	time.sleep(1) 

	buttonstatus = pibrella.button.read() 

	if (buttonstatus == 0) :

		print 'Button State Is ', buttonstatus
		pibrella.light.off()

	if (buttonstatus == 1) :
   		print 'Button State Is ', buttonstatus
		print 'GOTCHA'
		pibrella.light.green.on()


import pibrella
import time

# commented this out, not sure why I had it on
# pibrella.output.g.on()

var = 1

while var == 1 :

	time.sleep(.05) 

	print 'Input Read'
	print pibrella.input.a.read()

	buttonstatus = pibrella.button.read() 

	if (buttonstatus == 0) :

		print 'Button State Is ', buttonstatus
		pibrella.light.off()
		pibrella.light.red.on()
		pibrella.output.h.off()

	if (buttonstatus == 1) :
   		print 'Button State Is ', buttonstatus
		print 'GOTCHA'
		pibrella.light.off()
		pibrella.light.green.on()
		pibrella.output.h.on()


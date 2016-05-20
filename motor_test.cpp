#include <iostream>
#include <unistd.h>
#include "GPIO.h"
#include "PWM.h"
#include "eqep.h"
//#include "DCMotor.h"
using namespace std;
using namespace geeBBB;



int main(){
   if(getuid()!=0){
      cout << "You must run this program as root. Exiting." << endl;
      return -1;
   }
   
   cout << "Starting Motor Test" << endl;
   GPIO enableGPIO(27), brakeGPIO(22), directionGPIO(23);  //Set GPIOs for Enable, Brake, and Direction
   //DCMotor bbb(new PWM("48304000.epwmss/48304200.ehrpwm/pwm/pwm5"), 70); //Vref (PWM) line
   PWM pwm("48304000.epwmss/48304200.ehrpwm/pwm/pwm5"); //Vref pwm line
   enableGPIO.setDirection(OUTPUT);
   cout << "enableGPIO27 set direction" << endl;
   brakeGPIO.setDirection(OUTPUT);
   cout << "brakeGPIO22 set direction" << endl;
   directionGPIO.setDirection(OUTPUT);
   cout << "directionGPIO23 set direction" << endl;
   enableGPIO.setValue(HIGH);
   cout << "enableGPIO27 set value high" << endl;
   brakeGPIO.setValue(HIGH);
   cout << "brakeGPIO22 set value low" << endl;
   directionGPIO.setValue(HIGH);
   cout << "directionGPIO23 set value high...to set pwm period" << endl;
   
   pwm.setPeriod(100000);
   cout << "pwm period ..to set duty cycle" << endl;
   pwm.setDutyCycle(25.0f);
   cout << "duty cycle to set polarity" << endl;
   pwm.setPolarity(PWM::ACTIVE_HIGH);
   cout << "polarity" << endl;
   pwm.run();

   eQEP eqep2("/sys/devices/ocp.3/48304000.epwmss/48304180.eqep", eQEP::eQEP_Mode_Absolute); 
   eqep2.set_period(1000000000L); 
   std::cout << "[eQEP] Period = " << eqep2.get_period() << " ns" << std::endl;
      
   while(1)
    {
        std::cout << "[eQEP]  Position = " << eqep2.get_position() << std::endl;
        if (eqep2.get_position() == 0)
          {
           pwm.stop();
          }
    }


   
   // This code uses DCMotor.h and DCMotor.cpp and not currently in use to control the motor 
   //bbb.setDirection(DCMotor::ANTICLOCKWISE);
   //bbb.setSpeedPercent(25.0f);   //make it clear that a float is passed
   //bbb.go();
   //cout << "Rotating clockwise at 25% speed" << endl;
   //usleep(5000000);    //sleep for 5 seconds
   //bbb.reverseDirection();
   //cout << "Rotating clockwise at 50% speed" << endl;
   //usleep(5000000);
   //bbb.setSpeedPercent(100.0f);
   //cout << "Rotating clockwise at 100% speed" << endl;
   //usleep(5000000);
   //bbb.stop();
   //cout << "End of EBB DC Motor Example" << endl;
   //usleep(10000000); //10 seconds
   pwm.stop();
   
   return 0;
}

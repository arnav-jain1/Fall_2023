#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Stuff we added in as well as stdlib
#include "eecs388_lib.h"
#define SERVO_PULSE_MAX 2400    /* 2400 us */
#define SERVO_PULSE_MIN 544     /* 544 us */
#define SERVO_PERIOD    20000   /* 20000 us (20ms) */


void steering(int gpio, int pos)
{
    // Task-3: 
    // Your code goes here (Use Lab 05 for reference)
    // Check the project document to understand the task



    int onTime = SERVO_PULSE_MIN + pos*(SERVO_PULSE_MAX-SERVO_PULSE_MIN)/180; //Add min to pos*(max-min)/180 to get onTime
    int offTime = SERVO_PERIOD - onTime; // Off time is full period - on time

    gpio_write(gpio, ON); // turn on the gpio
    delay_usec(onTime); //Add min to pos*(max-min)/180

    gpio_write(gpio, OFF); // turn off the gpio
    // delay_usec(offTime); // Off time is full period - on time

}

int read_from_pi(int devid)
{
    // Task-2: 
    //after performing Task-2 at dnn.py code, modify this part to read angle values from Raspberry Pi
    // You code goes here (Use Lab 09 for reference)
    
    char line[16]; // create a char array to store the line
    static int read = 0; // create a static int to store the read value
    if (ser_isready(1)) { // if the serial is ready
        ser_readline(devid, sizeof(line), line); // read the line and store it in the line array

        
        read = atoi(line); // convert the line to an int and store it in read and then return read
    
        
    }
    return read;

}

void auto_brake(int devid)
{
    // Task-1: 
    // Your code here (Use Lab 02 - Lab 04 for reference)
    // You must use the directions given in the project document to recieve full credit

    //Counter to flash every 10 cycles (one cycle is 10ms so 10 cycles is 100ms)
    static int counter = 0;

    // printf(ser_read(0));
    if ('Y' == ser_read(devid) && 'Y' == ser_read(devid)) {
        int total_dist = (ser_read(devid) | (ser_read(devid) << 8)); // read the lower 8 bits and then read again to get the higher 8 bits. Then do an 8 bit shift left for the higher bit and Then or the 2 vars together to get the total distance

        // printf("Distance: %d\n", total_dist); // print the distance  to the console

        //If the distance is greater than 200, turn on the green LED and turn off the red LED
        if (total_dist > 200) {
            
            gpio_write(RED_LED, OFF);
            gpio_write(GREEN_LED, ON);
        } else if (total_dist > 100) {
            //If the distance is greater than 100, turn on both LED (Yellow)
            gpio_write(RED_LED, ON); 
            gpio_write(GREEN_LED, ON);
        } else if (total_dist > 60) {
            //If the distance is greater than 60, turn on the red LED and turn off the green LED
            gpio_write(GREEN_LED, OFF);
            gpio_write(RED_LED, ON);

        } else {
            //If the distance is less than 60, flash the red LED do this by having a counter that counts to 10 and then flashes the LED
            counter++;
            // Turn off the green LED
            gpio_write(GREEN_LED, OFF);
            if (counter >= 10) {
                //if the flashing counter is greater than 10, flash the LED and reset the counter
                flashing();
                counter = 0;
            }           

        }
    }
        
}

volatile int led_state = OFF;
// Timer interrupt service routine
void flashing() {
    // If the LED is on, turn it off and vice versa
    if (led_state == ON) {
        gpio_write(RED_LED, OFF);
        led_state = OFF;
    } else {
        gpio_write(RED_LED, ON);
        led_state = ON;
    }
}

int main()
{
    // initialize UART channels
    ser_setup(0); // uart0
    ser_setup(1); // uart1


    int pi_to_hifive = 1; //The connection with Pi uses uart 1
    int lidar_to_hifive = 0; //the lidar uses uart 0
    
    printf("\nUsing UART %d for Pi -> HiFive", pi_to_hifive);
    printf("\nUsing UART %d for Lidar -> HiFive", lidar_to_hifive);
    
    //Initializing PINs
    gpio_mode(PIN_19, OUTPUT);
    gpio_mode(RED_LED, OUTPUT);
    gpio_mode(BLUE_LED, OUTPUT);
    gpio_mode(GREEN_LED, OUTPUT);

    printf("Setup completed.\n");
    printf("Begin the main loop.\n");

    while (1) {

        auto_brake(lidar_to_hifive); // measuring distance using lidar and braking
        int angle = read_from_pi(pi_to_hifive); //getting turn direction from pi
        printf("angle: %d \n", angle);
        int gpio = PIN_19; 
        // for (int i = 0; i < 10; i++){
            // Here, we set the angle to 180 if the prediction from the DNN is a positive angle
            // and 0 if the prediction is a negative angle.
            // This is so that it is easier to see the movement of the servo.
            // You are welcome to pass the angle values directly to the steering function.
            // If the servo function is written correctly, it should still work,
            // only the movements of the servo will be more subtle
            if(angle>0){
                steering(gpio, 180);
            }
            else {
                steering(gpio,0);
            }
        // }

    }
    return 0;
}

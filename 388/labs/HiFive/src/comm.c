#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "eecs388_lib.h"

void steering(int gpio, int pos)
{
    // Task-3: 
    // Your code goes here (Use Lab 05 for reference)
    // Check the project document to understand the task
}

int read_from_pi(int devid)
{
    // Task-2: 
    //after performing Task-2 at dnn.py code, modify this part to read angle values from Raspberry Pi
    // You code goes here (Use Lab 09 for reference)

}

void auto_brake(int devid)
{
    // Task-1: 
    // Your code here (Use Lab 02 - Lab 04 for reference)
    // You must use the directions given in the project document to recieve full credit
    static int counter = 0;
    if ('Y' == ser_read(0) && 'Y' == ser_read(0)) {
        int total_dist = (ser_read(0) | (ser_read(0) << 8)); // read the lower 8 bits and then read again to get the higher 8 bits. Then do an 8 bit shift left for the higher bit and Then or the 2 vars together to get the total distance

        printf("Distance: %d\n", total_dist); // print the distance  to the console
        if (total_dist > 200) {
            gpio_write(RED_LED, OFF);
            gpio_write(GREEN_LED, ON);
        } else if (total_dist > 100) {
            gpio_write(RED_LED, ON); 
            gpio_write(GREEN_LED, ON);
        } else if (total_dist > 60) {
            gpio_write(GREEN_LED, OFF);
            gpio_write(RED_LED, ON);

        } else {
            counter++;
            gpio_write(GREEN_LED, OFF);
            if (counter >= 10) {
                flashing();
                counter = 0;
            }           

        }
    }
        
}

volatile int led_state = OFF;
// Timer interrupt service routine
void flashing() {
    // This function is called every time the timer interrupt occurs
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
        // int angle = read_from_pi(pi_to_hifive); //getting turn direction from pi
        // printf("\nangle=%d", angle) 
        // int gpio = PIN_19; 
        // for (int i = 0; i < 10; i++){
        //     // Here, we set the angle to 180 if the prediction from the DNN is a positive angle
        //     // and 0 if the prediction is a negative angle.
        //     // This is so that it is easier to see the movement of the servo.
        //     // You are welcome to pass the angle values directly to the steering function.
        //     // If the servo function is written correctly, it should still work,
        //     // only the movements of the servo will be more subtle
        //     if(angle>0){
        //         steering(gpio, 180);
        //     }
        //     else {
        //         steering(gpio,0);
        //     }
        // }

    }
    return 0;
}

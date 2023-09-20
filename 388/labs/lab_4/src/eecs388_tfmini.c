/**
 * This program reads the distance data from the TFmini lidar sensor,  
 * prints the read data and controls an LED depending on the measured distance.
 */
#include <stdint.h>
#include <stdio.h>

#include "eecs388_lib.h"

int main()
{
    gpio_mode(RED_LED, OUTPUT);
    gpio_mode(GREEN_LED, OUTPUT);
    ser_setup();

    ser_printline("Setup completed.\n"); //ser_printline() can be used to print to the serial monitor

    /* 
        LIDAR distance data is 16 bits.
    */
    uint16_t dist = 0;

    while (1) {
        /* 
            Task 2.1: 
            - read a data frame from the TFmini sensor
            
            - from Table 6, we know each LIDAR measurement sends 9 bytes
            - the function `ser_read()` can process 1 byte per function call

            - This if-statement below will read (and check) the first two bytes of a valid data frame
            - You will need to write code to read the subsequent bytes to get the distance data
            - You will need to process the data received from the sensor to get the correct distance value
        */
        if ('Y' == ser_read() && 'Y' == ser_read()) {
            int total_dist = (ser_read() | (ser_read() << 8)); // read the lower 8 bits and then read again to get the higher 8 bits. Then do an 8 bit shift left for the higher bit and Then or the 2 vars together to get the total distance
            printf("Distance: %d\n", total_dist); // print the distance  to the console
            if (total_dist < 50) {
                gpio_write(GREEN_LED, OFF); //If the distance is less than 50 cm, turn off the green LED and turn on the red LED
                gpio_write(RED_LED, ON);
            } else {
                gpio_write(RED_LED, OFF); //Otherwise, turn off the red LED and turn on the green LED
                gpio_write(GREEN_LED, ON);
            }
        /* 
            Task 2.2: 
            - turn on the red LED if the distance measured is less than 50 cm. 
            - otherwise turn on the green LED 

            - print the measured value to the console (i.e. the serial monitor) 
            - You can use printf() or ser_printline() or ser_write()
            
            - Helpful guide for printing with printf()
            - https://en.cppreference.com/w/cpp/io/c/fprintf
        */
        
        }
    }
}

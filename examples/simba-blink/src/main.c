/*******************************************************************************
****版本：V1.0.0
****平台：esp8266
****日期：2021-05-20
****作者：Qitas
****版权：OS-Q
*******************************************************************************/
#include "simba.h"

int main()
{
    struct pin_driver_t led;

    /* Start the system. */
    sys_start();

    /* Initialize the LED pin as output and set its value to 1. */
    pin_init(&led, &pin_led_dev, PIN_OUTPUT);
    pin_write(&led, 1);

    while (1) {
        /* Wait half a second. */
        thrd_sleep_us(500000);

        /* Toggle the LED on/off. */
        pin_toggle(&led);
    }

    return (0);
}

/*---------------------------(C) COPYRIGHT 2021 OS-Q -------------------------*/

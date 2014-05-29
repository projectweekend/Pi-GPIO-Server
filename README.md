A Raspberry Pi powered API server providing a RESTful interface to the GPIO pins.

NOTE: This is no where close to being finished. The documented routes listed here are not ready yet. For now, this is just a roadmap.


## Getting Started

A config file named `pins.yml` is used to define the initial setup for pins that will be accessible to the API. If a pin is not defined here it will not have a URL route in the API. For full documentation about available GPIO input pin configurations see the [documentation](http://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/).

```yaml
- pin: 1
  mode: IN
  initial: HIGH
  resistor: PUD_UP
- pin: 2
  mode: OUT
  initial: LOW
  resistor: PUD_DOWN
```

* `pin` - This is the number of the pin to configure. (Required)
* `mode` - This controls whether the pin will be used for input or output. Accepted values are: `IN`, `OUT`. (Required)
* `initial` - This controls the starting value of the pin. Accepted values are: `LOW`, `HIGH`. (Optional - defaults to `LOW`)
* `resistor` - This controls the software defined pull up/pull down resistor available in the Broadcom SOC. Accepted values are: `PUD_UP`, `PUD_DOWN`. (Optional - defaults to none)

**TODO:** At some point this configuration file should support mapping a custom callback and switch debouncing.

### List enabled GPIO pins and configuration

**GET:** `/api/v1/pin`

**Response**

```json
[
    {
        pin: 1,
        mode: "GPIO.INPUT",
        initial: "GPIO.HIGH",
        resistor: "GPIO.PUD_UP"
    },
    {
        pin: 2,
        mode: "GPIO.OUTPUT",
        initial: "GPIO.LOW",
        resistor: "GPIO.PUD_DOWN"
    },
    ...
]
```

### Read a pin's value (includes configuration)

**GET:** `/api/v1/pin/:pin`

**Response**

```json
{
    pin: 1,
    mode: "GPIO.INPUT",
    initial: "GPIO.HIGH",
    resistor: "GPIO.PUD_UP",
    value: 1
}
```

### Write to a pin

**PUT:** `/api/v1/pin/:pin`

**Body**

```json
{
    value: 0
}
```

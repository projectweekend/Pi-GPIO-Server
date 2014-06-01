A Raspberry Pi powered API server providing a RESTful interface to the GPIO pins.

NOTE: This is no where close to being finished. The documented routes listed here are not ready yet. For now, this is just a roadmap.


## Getting Started

A config file named `pins.yml` is used to define the initial setup for pins that will be accessible to the API. If a pin is not defined here it will not have a URL route in the API. For full documentation about available GPIO input pin configurations see the [documentation](http://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/).

```yaml
1:
  mode: IN
  initial: HIGH
  resistor: PUD_UP
2:
  mode: OUT
  initial: LOW
  resistor: PUD_DOWN
```
* Add a numbered element for each pin number you want to enable
* `mode` - This controls whether the pin will be used for input or output. Accepted values are: `IN`, `OUT`. (Required)
* `initial` - This controls the starting value of the pin. Accepted values are: `LOW`, `HIGH`. (Optional - defaults to `LOW`)
* `resistor` - This controls the software defined pull up/pull down resistor available in the Broadcom SOC. Accepted values are: `PUD_UP`, `PUD_DOWN`. (Optional - defaults to none)

------------------------------------------------------------------------------

#### List enabled GPIO pins and configuration

**GET:** `/api/v1/pin`

**Response**

```json
[
    {
        "num": 1,
        "mode": "IN"
    },
    {
        "num": 2,
        "mode": "OUT"
    },
    ...
]
```

#### Read a pin's value (includes configuration)

**GET:** `/api/v1/pin/:pin`

**Response**

```json
{
    "num": 1,
    "mode": "IN",
    "value": 1
}
```

#### Write to a pin

**PUT:** `/api/v1/pin/:pin`

**Body**

```json
{
    "value": 0
}
```

**Response**

```json
{
    "num": 1,
    "mode": "IN",
    "value": 0
}
```

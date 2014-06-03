This is a server that provides access to the Raspberry Pi's GPIO pins using both a RESTful JSON API and [socket.io](http://socket.io/).

NOTE: This is no where close to being finished. The documented routes listed here are not ready yet. For now, this is just a roadmap.


## Getting Started

A config file `pins.yml` is used to define the initial setup for pins that will be accessible to the API. If a pin is not defined here it will not have a URL route in the API. For full documentation about available GPIO input pin configurations see the [documentation](http://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/).

```yaml
18:
  mode: IN
  initial: HIGH
  resistor: PUD_UP
23:
  mode: OUT
  initial: LOW
  resistor: PUD_DOWN
24:
  mode: IN
  event: RISING
  bounce: 200
```

* Add a numbered element that corresponds to each pin to enable
* `mode` - This controls whether the pin will be used for input or output. Accepted values are: `IN`, `OUT`. (Required)
* `initial` - This controls the starting value of the pin. Accepted values are: `LOW`, `HIGH`. (Optional - defaults to `LOW`)
* `resistor` - This controls the software defined pull up/pull down resistor available in the Broadcom SOC. Accepted values are: `PUD_UP`, `PUD_DOWN`. (Optional - defaults to none)
* `event` - This can only be used in combination with a pin set to input mode (`mode: IN`). If defined, the pin will use a socket.io connection to push data to the client when the event is detected. Accepted values are: `RISING`, `FALLING`, `BOTH`.
* `bounce` - This can be used when an `event` is defined to prevent multiple callbacks being fired accidentally. The value is the number of milliseconds to wait before detecting another `event`.

------------------------------------------------------------------------------

### JSON API

------------------------------------------------------------------------------

#### List enabled GPIO pins

**GET:** `/api/v1/pin`

**Response**

```json
[
    {
        "num": 1,
        "mode": "IN",
        "value": 0
    },
    {
        "num": 2,
        "mode": "OUT",
        "value": 1
    },
    ...
]
```

#### Read a single pin

**GET:** `/api/v1/pin/:pin`

**Response**

```json
{
    "num": 1,
    "mode": "IN",
    "value": 1
}
```

#### Write to a single pin

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

------------------------------------------------------------------------------

### Events

------------------------------------------------------------------------------

Each pin `event` defined in `pins.yml` will push inormation to the client via socket.io. Data is sent on a named socket corresponding to the pin where it was triggered. For example, if an event was attached to pin 23, the named socket is `pin:23`.

##### Example Socket.io Payload
```json
{
  "num": 23,
  "mode": "IN",
  "value": 1
}
```

##### Example Client JavaScript

```javascript
var socket = io.connect('http://your_raspberry_pi.local');
socket.on('pin:23', function (data) {
  // do something with data
  console.log(data);
});
```

## TODO

* Add support for I2C

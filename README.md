![GPIO server page](http://i.imgur.com/FEOoPHj.png)


------------------------------------------------------------------------------

### Installation & Setup

------------------------------------------------------------------------------

#### Step 1: Clone this repository

```
git clone https://github.com/projectweekend/Pi-GPIO-Server.git
```

#### Step 2: Run install script

From the project directory `Pi-GPIO-Server/`, run the following command:

```
./install.sh
```

**NOTE:** This step will probably take several minutes to complete. When the script starts to install [Upstart](http://upstart.ubuntu.com/), you will receive a warning message. It will prompt you to type the following message to confirm the installation: `Yes, do as I say!`. You must type it exactly.

#### Step 3: Reboot

```
sudo reboot
```


------------------------------------------------------------------------------

### Getting Started

------------------------------------------------------------------------------

### Pin Configuration

A config file `config/pins.yml` is used to define the initial setup for pins that will be accessible to the API. If a pin is not defined here it will not have a URL route in the API. For full documentation about available GPIO input pin configurations see the [documentation](http://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/).

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

* Add a numbered element for each pin enabled
* `mode` - This controls whether the pin will be used for input or output. Accepted values are: `IN`, `OUT`. (Required)
* `initial` - This controls the starting value of the pin. Accepted values are: `LOW`, `HIGH`. (Optional - defaults to `LOW`)
* `resistor` - This controls the software defined pull up/pull down resistor available in the Broadcom SOC. Accepted values are: `PUD_UP`, `PUD_DOWN`. (Optional - defaults to none)
* `event` - This can only be used in combination with a pin set to input mode (`mode: IN`). If defined, the pin will use a socket.io connection and push data to the client when an event is detected. Accepted values are: `RISING`, `FALLING`, `BOTH`.
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
        "initial": null,
        "value": 0,
        "resistor": null,
        "num": 18,
        "mode": "OUT",
        "event": null,
        "bounce": 0
    },
    {
        "initial": null,
        "value": 0,
        "resistor": null,
        "num": 23,
        "mode": "IN",
        "event": "RISING",
        "bounce": 200
    },
    ...
]
```

#### Read a single pin

**GET:** `/api/v1/pin/:num`

**Response**

```json
{
    "initial": null,
    "value": 0,
    "resistor": null,
    "num": 18,
    "mode": "OUT",
    "event": null,
    "bounce": 0
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
    "initial": null,
    "value": 0,
    "resistor": null,
    "num": 18,
    "mode": "OUT",
    "event": null,
    "bounce": 0
}
```


------------------------------------------------------------------------------

### Socket.io

------------------------------------------------------------------------------

#### List enabled GPIO pins

**Name:** `pin:list`

**Example Client JavaScript**

~~~javascript
var socket = io.connect( 'http://your_raspberry_pi.local' );

socket.on( 'pin:list', function ( data ) {
  // do something with data
  console.log( data );
} );

socket.emit( 'pin:list' );
~~~

#### Read a single pin

**Name:** `pin:read`

**Example Client JavaScript**

~~~javascript
var socket = io.connect( 'http://your_raspberry_pi.local' );

socket.on( 'pin:read', function ( data ) {
  // do something with data
  console.log( data );
} );

socket.emit( 'pin:read', { num: 1 } );
~~~

#### Write to a single pin

**Name:** `pin:write`

**Example Client JavaScript**

~~~javascript
var socket = io.connect( 'http://your_raspberry_pi.local' );

socket.on( 'pin:write', function ( data ) {
  // do something with data
  console.log( data );
} );

socket.emit( 'pin:write', { num: 1, value: 0 } );
~~~


------------------------------------------------------------------------------

### Events

------------------------------------------------------------------------------

Each pin `event` defined in `pins.yml` will push inormation to the client via socket.io. Data is sent on a named socket: `pin:event`.

##### Example Socket.io Payload

```json
{
  "num": 23,
  "event": "RISING"
}
```

##### Example Client JavaScript

```javascript
var socket = io.connect( 'http://your_raspberry_pi.local' );

socket.on( 'pin:event', function ( data ) {
  // do something with data
  console.log( data );
} );
```


------------------------------------------------------------------------------

### TODO

------------------------------------------------------------------------------

* Add support for I2C

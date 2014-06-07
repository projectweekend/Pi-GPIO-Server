'use strict';

/* Services */


var sModule = angular.module( 'myApp.services', [] );

sModule.factory( 'socket', function ( socketFactory ) {
    return socketFactory();
} );


sModule.factory( 'API', function ( $http, $location, $window ) {

    var apiRequest = function ( method, path, requestData, callback ) {

        var headers = {
            "Content-Type": "application/json"
        };

        var options = {
            method: method,
            url: path,
            headers: headers,
            data: requestData
        };

        $http( options )
            .success( function ( data, status, headers, config ) {
                callback( null, data );
            } )
            .error( function ( data, status, headers, config ) {
                callback( data, null );
            } );
    };


    return {
        get: function ( path, callback ) {
            return apiRequest( 'GET', path, {}, callback );
        },
        post: function ( path, requestData, callback ) {
            return apiRequest( 'POST', path, requestData, callback );
        },
        put: function ( path, requestData, callback ) {
            return apiRequest( 'PUT', path, requestData, callback );
        },
        patch: function ( path, requestData, callback ) {
            return apiRequest( 'PATCH', path, requestData, callback );
        },
        delete: function ( path, callback ) {
            return apiRequest( 'DELETE', path, {}, callback );
        }
    };

} );


sModule.factory( 'Pin', function ( API, socket ) {

    var url = "/api/v1/pin";

    return {
        error: {},
        list: [],
        getList: function () {
            var self = this;
            API.get( url, function ( err, data ) {
                if ( err ) {
                    self.error = err;
                }
                self.list = data;
            });
        },
        setValue: function ( pin_num, value ) {
            var self = this;
            API.patch( url + "/" + pin_num, { value: value }, function ( err, data ) {
                if ( err ) {
                    self.error = err;
                }
                for ( var i = 0; i < self.list.length; i++ ) {
                    if ( self.list[ i ].num === pin_num ) {
                        self.list[ i ] = data;
                    }
                }
            } );
        },
        turnOn: function ( pin_num ) {
            var self = this;
            this.setValue( pin_num, 1 );
        },
        turnOff: function ( pin_num ) {
            var self = this;
            this.setValue( pin_num, 0 );
        }
    };

} );


sModule.factory( 'Events', function ( socket ) {
    return {
        error: {},
        list: [],
        listen: function () {
            var self = this;
            socket.on( 'pin:event', function ( data ) {
                data.date = new Date();
                self.list.push( data );
            } );
        }
    };
} );

'use strict';

/* Services */


var sModule = angular.module( 'myApp.services', [] );


sModule.factory( 'API', function ( $http, $location, $window ) {

    var apiRequest = function ( method, path, requestData, callback ) {

        var headers = {
            "Authorization": "Bearer " + $window.sessionStorage.token,
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
                if ( status === 401 || status === 403 ) {
                    $window.sessionStorage.token = "";
                    $location.path( "/login" );
                    return;
                }
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


sModule.factory( 'Pin', function ( API ) {

    var url = "/api/v1/pin";

    return {
        error: {},
        list:[],
        getList: function () {
            var self = this;
            API.get( url, function ( err, data ) {
                if ( err ) {
                    self.error = err;
                }
                self.list = data;
            });
        }
    };

} );

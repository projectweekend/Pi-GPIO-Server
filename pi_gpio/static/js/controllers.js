'use strict';

/* Controllers */

var cModule = angular.module( 'myApp.controllers', [] );


cModule.controller( 'AppCtrl', function ( $scope ) {

} );


cModule.controller( 'PinsCtrl', function ( $scope, Pin, socket ) {

    $scope.Pin = Pin;
    $scope.Pin.getList();

    $scope.events = [];

    socket.on( 'test', function ( data ) {
        console.log( data );
    } );

    socket.on( "pin:list", function ( data ) {
        console.log( data );
    } );

    socket.emit( "pin:list" );



} );


cModule.controller( 'MyCtrl2', function ( $scope ) {

});

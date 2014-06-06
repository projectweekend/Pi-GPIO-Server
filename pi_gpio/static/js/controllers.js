'use strict';

/* Controllers */

var cModule = angular.module( 'myApp.controllers', [] );


cModule.controller( 'AppCtrl', function ( $scope ) {

} );


cModule.controller( 'PinsCtrl', function ( $scope, Pin, socket ) {

    $scope.Pin = Pin;
    $scope.Pin.getList();

    socket.on( 'pin:event', function ( data ) {
        console.log( data );
    } );

    socket.emit( 'pin:list' );

} );


cModule.controller( 'MyCtrl2', function ( $scope ) {

});

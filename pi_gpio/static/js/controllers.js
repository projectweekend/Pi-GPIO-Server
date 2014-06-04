'use strict';

/* Controllers */

var aModule = angular.module( 'myApp.controllers', [] );

aModule.controller( 'AppCtrl', function ( $scope, socket ) {

} );


aModule.controller( 'PinsCtrl', function ( $scope, socket, Pin ) {

    $scope.Pin = Pin;
    $scope.Pin.getList();

    // socket.on( 'pin:list', function ( data ) {
    //     $scope.pinsEnabled = data;
    // } );

} );


aModule.controller( 'MyCtrl2', function ( $scope ) {

});

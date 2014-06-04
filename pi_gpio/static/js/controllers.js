'use strict';

/* Controllers */

var aModule = angular.module( 'myApp.controllers', [] );

aModule.controller( 'AppCtrl', function ( $scope ) {

} );


aModule.controller( 'PinsCtrl', function ( $scope, Pin ) {

    $scope.Pin = Pin;
    $scope.Pin.getList();

    // socket.on( 'pin:list', function ( data ) {
    //     $scope.pinsEnabled = data;
    // } );

} );


aModule.controller( 'MyCtrl2', function ( $scope ) {

});

'use strict';

/* Controllers */

var cModule = angular.module( 'myApp.controllers', [] );


cModule.controller( 'AppCtrl', function ( $scope ) {

} );


cModule.controller( 'PinsCtrl', function ( $scope, Pin, Events, socket ) {

    $scope.Pin = Pin;
    $scope.Pin.getList();

    $scope.Events = Events;
    $scope.Events.listen();

    socket.emit( 'pin:list' );

} );


cModule.controller( 'MyCtrl2', function ( $scope ) {

});

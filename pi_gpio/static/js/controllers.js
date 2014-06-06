'use strict';

/* Controllers */

var cModule = angular.module( 'myApp.controllers', [] );


cModule.controller( 'AppCtrl', function ( $scope ) {

} );


cModule.controller( 'PinsCtrl', function ( $scope, Pin, socket ) {

    $scope.Pin = Pin;
    $scope.Pin.getList();
    $scope.Pin.listenForEvents();

} );


cModule.controller( 'MyCtrl2', function ( $scope ) {

});

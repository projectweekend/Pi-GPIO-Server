'use strict';

/* Controllers */

var cModule = angular.module( 'myApp.controllers', [] );

cModule.controller( 'AppCtrl', function ( $scope ) {

} );


cModule.controller( 'PinsCtrl', function ( $scope, Pin ) {

    $scope.Pin = Pin;
    $scope.Pin.getList();

} );


cModule.controller( 'MyCtrl2', function ( $scope ) {

});

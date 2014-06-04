'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('AppCtrl', function ($scope, socket) {
    $scope.app_test = "APP TEST";

    alert("TEST");

  }).
  controller('PinsCtrl', function ($scope, socket) {

    $scope.test = "TESTING!!!";

    socket.emit( 'pin:list' );
    socket.on( 'pin:list', function ( data ) {
        $scope.socket_data = data;
    } );

  }).
  controller('MyCtrl2', function ($scope) {

  });

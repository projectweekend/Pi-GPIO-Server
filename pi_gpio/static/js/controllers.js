'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('AppCtrl', function ($scope, socket) {

  }).
  controller('PinsCtrl', function ($scope, socket) {

    $scope.test = "TESTING!!!";

    socket.on( 'pin:list', function ( data ) {
        $scope.socket_data = data;
    } );

    socket.emit( 'pin:list' );

  }).
  controller('MyCtrl2', function ($scope) {

  });

'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('AppCtrl', function ($scope, socket) {
    $scope.app_test = "APP TEST";
  }).
  controller('PinsCtrl', function ($scope, socket) {

    $scope.test = "TESTING!!!";

  }).
  controller('MyCtrl2', function ($scope) {

  });

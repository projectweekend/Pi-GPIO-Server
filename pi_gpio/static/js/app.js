'use strict';

// Declare app level module which depends on filters, and services

angular.module( 'myApp', [
  'ngRoute',

  'myApp.controllers',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',

  // 3rd party dependencies
  'btford.socket-io'
] ).
config( function ( $routeProvider, $locationProvider ) {
  $routeProvider.
    when('/pins', {
      templateUrl: 'static/partials/pins.html',
      controller: 'PinsCtrl'
    }).
    otherwise({
      redirectTo: '/pins'
    });

  $locationProvider.html5Mode( true );
} );

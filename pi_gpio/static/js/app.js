'use strict';

// Declare app level module which depends on filters, and services

var appModule = angular.module( 'myApp', [
    'ngRoute',

    'myApp.controllers',
    'myApp.services',
    'myApp.directives',

    // 3rd party dependencies
    'btford.socket-io'
] );

appModule.config( function ( $routeProvider, $locationProvider ) {
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

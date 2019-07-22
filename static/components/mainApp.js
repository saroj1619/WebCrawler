angular.module('mainApp',[
    'ui.router',
    'dashboardApp',
    'ui.bootstrap',
])

.config(['$stateProvider','$urlRouterProvider', function($stateProvider, $urlRouterProvider){
    $urlRouterProvider.otherwise('/dashboard');

    $stateProvider
    .state('dashboard',{
        url: '/dashboard',
        templateUrl: '/static/components/dashboard/views/dashboard.html',
        controller: 'dashboardController',
        controllerAs: 'dashboardScope',
    })

    .state('urlList',{
        url: '/urlList',
        templateUrl: '/static/components/dashboard/views/urlList.html',
//        controller: 'urlListController',
//        controllerAs: 'urlListScope',
    })

}])
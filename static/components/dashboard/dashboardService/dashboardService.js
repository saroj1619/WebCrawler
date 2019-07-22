angular.module('dashboardServiceApp',[])

.service('dashboardService', function($http){

    service = {}

    service.crawl = function(data){
        return $http.post('api/wc/', data)
    }

    return service;
})
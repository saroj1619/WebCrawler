angular.module('dashboardControllerApp',[])

.controller('dashboardController', function(dashboardService, $state){
    var dashboardScope = this;

    dashboardScope.crawl = function(flag){

        var data = {
            "url": dashboardScope.url,
            "depth": dashboardScope.depth,
            "flag": flag
        }
        console.log(data)
        console.log(data)

        dashboardScope.loadingMsg = "Loading..."

        var success = function(response){
            console.log(response.data)
            dashboardScope.loadingMsg = "Please see below the results."
            list = response.data

            dashboardScope.urls = list
//            $state.go('urlList', dashboardScope.urls)

            // Pagination Block
            dashboardScope.totalItems = dashboardScope.urls.length;
            dashboardScope.currentPage = 1;
            dashboardScope.numPerPage = 1;

            dashboardScope.paginate = function(value) {
//                console.log("In Pagination", value)
                var begin, end, index;
                begin = (dashboardScope.currentPage - 1) * dashboardScope.numPerPage;
                end = begin + dashboardScope.numPerPage;
                index = dashboardScope.urls.indexOf(value);
//                console.log(index)
                return (begin <= index && index < end);
            };

        }

        var failure = function(error){
            console.log(error)
            dashboardScope.loadingMsg = "Failed to load."
        }

        dashboardService.crawl(data).then(success, failure)
    }

    return dashboardScope;

})
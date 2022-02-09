function initMap() {
    // ルート検索の条件
    var request = {
        origin: new google.maps.LatLng(document.getElementById('ido1').value, document.getElementById('keido1').value), // 出発地
        destination: new google.maps.LatLng(document.getElementById('ido3').value, document.getElementById('keido3').value), // 目的地
        waypoints: [ // 経由地点(指定なしでも可)
            { location: new google.maps.LatLng(document.getElementById('ido2').value, document.getElementById('keido2').value) },
        ],
        travelMode: google.maps.DirectionsTravelMode.WALKING, // 交通手段(歩行。DRIVINGの場合は車)
    };

    // マップの生成
    var map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(document.getElementById('ido1').value, document.getElementById('keido1').value), // マップの中心
        zoom: 10 // ズームレベル
    });

    var d = new google.maps.DirectionsService(); // ルート検索オブジェクト
    var r = new google.maps.DirectionsRenderer({ // ルート描画オブジェクト
        map: map, // 描画先の地図
        preserveViewport: false, // 描画後に中心点をずらさない
    });
    // ルート検索
    d.route(request, function (result, status) {
        // OKの場合ルート描画
        if (status == google.maps.DirectionsStatus.OK) {
            r.setDirections(result);
        }
    });
}
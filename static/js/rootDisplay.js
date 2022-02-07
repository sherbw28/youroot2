function initMap(){
    var array = [];
    var ido1;
    var keido1;
    var ido2;
    var keido2;
    var ido3;
    var keido3;
    var geocoder = new google.maps.Geocoder();

    var name1 = "佐賀市";
    var name2 = "久留米市";
    var name3 = "大分市";
    
    for(var i = 0; i < 3; i++){
        if (i == 0){
            geocoder.geocode(
                {
                    'address': name1,
                    'region': 'jp'
                },
                function(results, status){
                    if(status==google.maps.GeocoderStatus.OK){
                        //処理
                        ido1 = results[0].geometry.location.lat();
                        keido1 = results[0].geometry.location.lng();
                        array.push(ido1);
                        array.push(keido1);
                    }
                }
                );
            }else if(i == 1){
                geocoder.geocode(
                    {
                        'address': name2,
                        'region': 'jp'
                    },
                    function(results, status){
                        if(status==google.maps.GeocoderStatus.OK){
                            //処理
                            ido2 = results[0].geometry.location.lat();
                            keido2 = results[0].geometry.location.lng();
                            array.push(ido2);
                            array.push(keido2);
                        }
                    }
                    );
                }else if(i == 2){
                    geocoder.geocode(
                        {
                            'address': name3,
                            'region': 'jp'
                        },
                        function(results, status){
                            if(status==google.maps.GeocoderStatus.OK){
                                //処理
                                ido3 = results[0].geometry.location.lat();
                                keido3 = results[0].geometry.location.lng();
                                array.push(ido3);
                                array.push(keido3);
                    }
                    console.log(array[0])

                    var request = {
                        origin: new google.maps.LatLng(array[0],array[1]), // 出発地
                        destination: new google.maps.LatLng(array[2], array[3]), // 目的地
                        waypoints: [ // 経由地点(指定なしでも可)
                            { location: new google.maps.LatLng(array[4],array[5]) },
                        ],
                        travelMode: google.maps.DirectionsTravelMode.DRIVING, // 交通手段(歩行。DRIVINGの場合は車)
                    };

                    // マップの生成
                    var map = new google.maps.Map(document.getElementById("map"), {
                        center: new google.maps.LatLng(array[0],array[1]), // マップの中心
                        zoom: 13 // ズームレベル
                    });

                    var d = new google.maps.DirectionsService(); // ルート検索オブジェクト
                    var r = new google.maps.DirectionsRenderer({ // ルート描画オブジェクト
                        map: map, // 描画先の地図
                        preserveViewport: true, // 描画後に中心点をずらさない
                    });
                    // ルート検索
                    d.route(request, function(result, status){
                        // OKの場合ルート描画
                        if (status == google.maps.DirectionsStatus.OK) {
                            r.setDirections(result);
                        }
                    });

                }
            );
        }
    }
    // console.log(array);
    // console.log(array[0]);
    // console.log(array.length)
    // geocoder.geocode(
    //   {
    //     'address': name,
    //     'region': 'jp'
    //   },
    //   function(results, status){
    //     if(status==google.maps.GeocoderStatus.OK){
    //         //処理
    //         let ido = results[0].geometry.location.lat();
    //         const keido = results[0].geometry.location.lng();
    //         console.log(ido);
    //         console.log(keido);
    //     }
    //   }
    // );
}

// function initMap() {
//     // ルート検索の条件

//     var request = {
//         origin: new google.maps.LatLng(33.260577521897815,130.29129588713124), // 出発地
//         destination: new google.maps.LatLng(33.578750723161974, 130.39576972815505), // 目的地
//         waypoints: [ // 経由地点(指定なしでも可)
//             { location: new google.maps.LatLng(33.259277331707665,130.26563515318378) },
//         ],
//         travelMode: google.maps.DirectionsTravelMode.DRIVING, // 交通手段(歩行。DRIVINGの場合は車)
//     };

//     // マップの生成
//     var map = new google.maps.Map(document.getElementById("map"), {
//         center: new google.maps.LatLng(33.260577521897815,130.29129588713124), // マップの中心
//         zoom: 13 // ズームレベル
//     });

//     var d = new google.maps.DirectionsService(); // ルート検索オブジェクト
//     var r = new google.maps.DirectionsRenderer({ // ルート描画オブジェクト
//         map: map, // 描画先の地図
//         preserveViewport: true, // 描画後に中心点をずらさない
//     });
//     // ルート検索
//     d.route(request, function(result, status){
//         // OKの場合ルート描画
//         if (status == google.maps.DirectionsStatus.OK) {
//             r.setDirections(result);
//         }
//     });
// }

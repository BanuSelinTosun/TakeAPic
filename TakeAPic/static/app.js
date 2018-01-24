function updatePic(name){
    src="//www.google.com/maps/embed/v1/place?"+
    "zoom=12&key=AIzaSyA6QG8IoU0eQulNezQScWTgtH7zdf-6MU0&q="+name
    map=$("iframe#map")
    map.attr("src",src)
    $("table#zchart tr.highlight").each(function () {
        $(this).removeClass('highlight');
    })
    $("tr"+"#z"+name).addClass('highlight');
}

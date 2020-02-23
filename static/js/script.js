$("document").ready(function(){
    setTimeout(function(){
        $("div.alert").remove();
    }, 4000 ); // 4 secs

});

$('.carousel').carousel({
    interval: 4000,
    pause: "hover"
})
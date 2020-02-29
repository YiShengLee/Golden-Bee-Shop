// Hide Button Section
let honey = document.querySelector("#empty");
let checkout = document.querySelector("#checkout");

if (honey){
    checkout.style.display = "none";
}

$("document").ready(function(){
    setTimeout(function(){
        $("div.alert").remove();
    }, 4000 ); // 4 secs

});

// Carousel Interval Speed
$('.carousel').carousel({
    interval: 4000,
    pause: "hover"
})


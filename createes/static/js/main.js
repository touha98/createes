const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$(document).ready(function(){
    setTimeout(function() {
        $('#message').fadeOut('slow')
    }, 4000)
    function contacts() {
        var width = $(window).width();
        if(width < 768){
            $('#top-bar').hide();
            $('#bottom-bar').show();
            $('.break').hide();
        }
        else{
            $('#top-bar').show();
            $('#bottom-bar').hide();
            $('.break').show();
        }
    }
    contacts();
    $(window).resize(function(){
        contacts()
    })
})
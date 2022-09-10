// Navbar code 
$(document).ready(function() {

    $('.first-button').on('click', function() {

        $('.animated-icon1').toggleClass('open');
    });
    $('.second-button').on('click', function() {

        $('.animated-icon2').toggleClass('open');
    });
    $('.third-button').on('click', function() {

        $('.animated-icon3').toggleClass('open');
    });
    // A function to close navbar while clicking anywhere in document - issue- doesnt change shape when clicked outside navbar
    $(function() {
        $(document).click(function(event) {
            $('.navbar-collapse').collapse('hide');
        });
    });
});

$(function() {
    $('.card_switch').on('click', function() {

        $($(this).parents('.l-wrapper_01')).toggleClass('is-surface').toggleClass('is-reverse');
    });
});

$(function() {
    $('.card_switch_back').on('click', function() {

        $($(this).parents('.l-wrapper_01')).toggleClass('is-surface').toggleClass('is-reverse');
    });
});
/*
$(function() {
    $('#card_switch').on('click', function() {
        $('.l-wrapper_01').toggleClass('is-surface').toggleClass('is-reverse');
    });
});*/
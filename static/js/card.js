
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
$(function() {
    $('.card_switch_03').on('click', function() {

        $($(this).parents('.l-wrapper_01')).toggleClass('is-surface_03').toggleClass('is-reverse_03');
    });
});

$(function() {
    $('.card_switch_03_back').on('click', function() {

        $($(this).parents('.l-wrapper_01')).toggleClass('is-surface_03').toggleClass('is-reverse_03');
    });
});

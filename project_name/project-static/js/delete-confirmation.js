var delete_confirmation_handler = function(event){

    event.preventDefault();

    var url = $(this).attr('href'),
        confirm_message = $(this).attr('data-confirm-message');

    if (!confirm_message) confirm_message = "Do you want to delete this record?";
 
    if ( confirm(confirm_message) ){
        window.location.replace(url);
    }
}

var confirm_delete = function() {    
    $('.delete-link').unbind('click',delete_confirmation_handler);
    $('.delete-link').bind('click',delete_confirmation_handler);
};


$(function() {
    confirm_delete();
});
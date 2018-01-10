/*
* 
* Tabs
*
* By Ramkishore Manorahan - @furalyon
* 
*
* To use:
* 1. Include this script
* 2. Use the markup format as shown in the example with the inline-editing classes and the data-attib db hooks
* 3. Style the classes, as needed
*
* usage eg:
    <ul class="page-tab__menu">
        <li><span class='page-tab__button' href="#categories">Categories</span></li>
        <li><span class='page-tab__button' href="#stock-records">Stock Record</span></li>
        <li><span class='page-tab__button' href="#purchases">Purchases</span></li>
    </ul>
    <div class = "page-tab__tab" id='categories'>
        c
    </div>
    <div class = "page-tab__tab" id='stock-records'>
        s
    </div>
    <div class = "page-tab__tab" id='purchases'>
        p
    </div>
*
* Note: Assumes a page has only one tab menu
*
*/


$(function() {
    var $tab_buttons = $('.page-tab__button'),
        $tabs = $('.page-tab__tab'),

        hide_all_tabs = function() {
            $tabs.each(function() {
                $(this).addClass('visuallyhidden');
            });
            $tab_buttons.each(function() {
                $(this).removeClass('active');
            });
        }

        initiate = function() {
            hide_all_tabs();
            var hash = window.location.hash;
            if (!hash) {
                hash = $tab_buttons.first().attr('href');
            }
            $(hash).removeClass('visuallyhidden');
            $tab_buttons.filter(function(index) {
                return $(this).attr('href') === hash;
            }).addClass('active');
        };

    if ($(window).width() > 400){
        $tab_buttons.click(function(event) {
            event.preventDefault();
            hide_all_tabs();
            $(this).addClass('active');
            var tab_id = $(this).attr('href');
            $(tab_id).removeClass('visuallyhidden');
        })

        initiate();    
    }
});
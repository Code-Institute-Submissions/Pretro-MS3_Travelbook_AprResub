/*jshint esversion: 6 */

$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $('input, textarea').characterCounter();
    $('.carousel').carousel({
        duration: 150,
        dist: -80,
        shift: 5,
        padding: 5,
        numVisible: 10,
        indicators: true,
        noWrap: false

    });
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 10,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

    $('.add_comment').click(function(event){
        const inputId = '#' + $(this).attr('data-comment-id');
        const ulId = '#comments' + $(this).attr('data-comment-id');
        const comment = $(inputId).val();
        const url = "/add_adventure_comment/" + $(this).attr('data-comment-id');
        $.post( url, {"comment": comment}).done(function( data ) {
            $(inputId).val("");
            $(ulId).append('<li class="collection-item avatar"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/OOjs_UI_icon_userAvatar-constructive.svg/1024px-OOjs_UI_icon_userAvatar-constructive.svg.png" alt="" class="circle"> <p>'+ data +'</p></li>');
        }); 
    });
    
    $('.delete_comment').click(function(event){
        const commentId = $(this).attr('id');
        const travelId = $(this).attr('data-travel-id');
        const url = "/remove_adventure_comment/" + travelId;
        const comment = $(this);
        $.post(url, {"comment": commentId}).done(function( data ) {
            console.log('response', data);
            comment.parent().remove();
        }); 
    });
});



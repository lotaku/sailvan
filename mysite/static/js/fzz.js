/*##################################################|*/
$(function() {

//    $("div .cms_dragarea-3").addClass('fzz_menu_1','fzz_cms_dragarea-3');
//    $("div .cms_dragarea-3").addClass('fzz_menu_1')
//    $("div .cms_dragarea-78").addClass('fzz_menu_1','fzz_cms_dragarea-78');
    $("div .cms_dragarea-103").addClass('fzz_cms_dragarea-103');
    $("div .cms_dragarea-99").addClass('fzz_cms_dragarea-99');
    $("div .cms_dragarea-7").addClass('fzz_cms_dragarea-7');
    $("div .cms_dragarea-88").addClass('fzz_cms_dragarea-88');
    $("div .cms_dragarea-95").addClass('fzz_cms_dragarea-95');
    $("div .cms_dragarea-105").addClass('fzz_cms_dragarea-105');
    $("div .cms_dragarea-107").addClass('fzz_cms_dragarea-107');
    $("div .cms_dragarea-109").addClass('fzz_cms_dragarea-109');
    $("div .cms_dragarea-111").addClass('fzz_cms_dragarea-111');
    $("div .cms_dragarea-113").addClass('fzz_cms_dragarea-113');
    $("div .cms_dragarea-115").addClass('fzz_cms_dragarea-115');
    $("div .cms_dragarea-117").addClass('fzz_cms_dragarea-117');
    $("div .cms_dragarea-101").addClass('fzz_cms_dragarea-101');
//    footer
    $("div .cms_dragarea-8").addClass('fzz_cms_dragarea-8');
    $("div .cms_dragarea-12").addClass('fzz_cms_dragarea-12');
    $("div .cms_dragarea-16").addClass('fzz_cms_dragarea-16');
    $("div .cms_dragarea-6").addClass('fzz_cms_dragarea-6');
    $("div .cms_dragarea-76").addClass('fzz_cms_dragarea-76');
    $("div .cms_dragarea-45").addClass('fzz_cms_dragarea-45');

    $("div").filter(function() {
        if($(this).text() === "Rb"){
            $(this).parent().parent().addClass('fzz_cms_dragarea-45')
        }
        if($(this).text() === "Info Banner"){
            $(this).parent().parent().addClass('fzz_cms_dragarea-76')
        }
    });
});


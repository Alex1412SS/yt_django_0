$(function(){
    $('.set_menu').hide()
$(".open_set").click(function(){

    $('.set_menu').show(200)
})
$(".set_menu").mouseleave(function(){
    $('.set_menu').slideUp(200)
    $(".open_set").addClass('open_set text-[#ECECEC] px-6 p-2 rounded-full duration-200 hover:text-black hover:bg-green-500 mr-12')
})
});


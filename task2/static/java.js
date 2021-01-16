$(document).ready(function(){
    $('.er').click(function()
    {
        $("#people").prop("disabled",true);
        if($(this).attr('id') == 'group')
        {
            $("#people").prop("disabled",false);
        }
    })
});
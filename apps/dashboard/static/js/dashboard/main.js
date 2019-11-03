$(document).ready(function (){
    $(document).on("submit", ".ajax_post",function(event){
        event.preventDefault();
        console.log('prevented default');
        
        insert = $(this).attr('insert');
        data = $(this).serialize();
        $(this).trigger("reset")        
        $.ajax({
            type: 'POST',
            url: $(this).attr('endpoint'),
            data: data,
            success: function (serverResponse) {               
                console.log(insert)
                console.log(serverResponse) 
                $(insert).html(serverResponse)
                
            }        
        })
    })
    $(document).on("click", ".ajax_click", function(event){
        event.preventDefault();
        console.log("I'm working sort of")
        insert = $(this).attr('insert')
        console.log(insert)
        $.ajax({
            type: 'GET',
            url: $(this).attr('endpoint'),
            success: function (serverResponse) {
                $(insert).html(serverResponse)

            }
        })        
    })
    $(document).on("keyup", ".search", function(event){
        
        console.log($(this).serialize())
        
    
    })
    


})